#!/usr/bin/env python3
"""ipcdex lists every CoreIPC message in a WebKit and compares two builds.

    ipcdex.py <dyld cache or WebKit> [-o index.json]
    ipcdex.py diff <old.json> <new.json> [--no-logstream]

WebKit's message generator, generate_message_names_header in
Source/WebKit/Scripts/webkit/messages.py, writes one table,
IPC::Detail::messageDescriptions, with a 24-byte entry for each
IPC::MessageName and an "<invalid message name>" entry at the end. ipcdex
finds that last entry in WebKit and walks back to the start of
the table, so it needs no symbols.
"""
import argparse
import collections
import json
import os
import struct
import sys
import uuid

WEBKIT_PATHS = (
    "/System/Library/Frameworks/WebKit.framework/Versions/A/WebKit",  # macOS
    "/System/Library/Frameworks/WebKit.framework/WebKit",  # iOS
)
PLATFORMS = {1: "macOS", 2: "iOS"}
END_NAME = b"<invalid message name>\0"
ENTRY_SIZE = 24
TABLE_SYMBOL = b"__ZN3IPC6Detail19messageDescriptionsE"
# IPC::ProcessName, from PROCESS_NAMES in Source/WebKit/Scripts/webkit/messages.py
# plus Unknown.
# Release builds don't contain the names, so they're pinned here.
PROCESSES = ("UI", "Networking", "GPU", "WebContent", "Model", "Unknown")
SYNC_REPLY_FLAG = 1  # messageAllowedWhenWaitingForSyncReply
UNBOUNDED_FLAG = 2  # messageAllowedWhenWaitingForUnboundedSyncReply
REPLY_FLAG = 4  # isAsyncReply
CPU_ARM64 = 0x0100000C
# Chained fixup pointer formats, from mach-o/fixup-chains.h. The arm64e ones keep 43 bits of target
# and the others 36. Some store the target's address and some its offset from the library's start.
ARM64E_FORMATS = (1, 9, 12)  # DYLD_CHAINED_PTR_ARM64E, _ARM64E_USERLAND, _ARM64E_USERLAND24
VMADDR_FORMATS = (1, 2)  # DYLD_CHAINED_PTR_ARM64E, DYLD_CHAINED_PTR_64
OFFSET_FORMATS = (6, 9, 12)  # DYLD_CHAINED_PTR_64_OFFSET, _ARM64E_USERLAND, _ARM64E_USERLAND24


def uuid_text(raw):
    return str(uuid.UUID(bytes=raw)).upper()


class DyldCache:
    """Reads addresses from a dyld shared cache and the subcaches next to it."""

    def __init__(self, path):
        self.files = [open(path, "rb")]
        header = self.files[0].read(0x200)
        if not header.startswith(b"dyld_v1"):
            raise SystemExit("ipcdex: %s isn't a dyld shared cache" % path)
        self.uuid = header[0x58:0x68]
        self.platform = struct.unpack_from("<I", header, 0xD8)[0]

        mapping_offset = struct.unpack_from("<I", header, 0x10)[0]
        subcache_offset, subcache_count = struct.unpack_from("<II", header, 0x188)
        entry_size = 56 if mapping_offset > 0x1C8 else 24
        entries = self.read_file(self.files[0], subcache_offset, entry_size * subcache_count)
        for i in range(subcache_count):
            entry = entries[i * entry_size:(i + 1) * entry_size]
            suffix = entry[24:].split(b"\0")[0].decode() if entry_size == 56 else ".%d" % (i + 1)
            subcache = path + suffix
            if not os.path.exists(subcache):
                raise SystemExit("ipcdex: missing subcache %s" % subcache)
            f = open(subcache, "rb")
            if f.read(0x68)[0x58:] != entry[:16]:
                raise SystemExit("ipcdex: %s is from a different cache" % subcache)
            self.files.append(f)

        # Each mapping is (start, end, file, file offset, value_add of its slide info or None).
        self.mappings = []
        for f in self.files:
            header = self.read_file(f, 0, 0x200)
            offset, count = struct.unpack_from("<II", header, 0x138)
            for i in range(count):
                address, size, file_offset, slide_offset, slide_size = struct.unpack_from(
                    "<QQQQQ", self.read_file(f, offset + 56 * i, 40))
                value_add = None
                if slide_size:
                    version, = struct.unpack_from("<I", self.read_file(f, slide_offset, 4))
                    if version == 5:
                        value_add, = struct.unpack_from("<Q", self.read_file(f, slide_offset + 16, 8))
                self.mappings.append((address, address + size, f, file_offset, value_add))

        offset, count = struct.unpack_from("<II", self.read_file(self.files[0], 0x1C0, 8))
        self.images = {}
        for i in range(count):
            address, _, _, path_offset = struct.unpack_from(
                "<QQQI", self.read_file(self.files[0], offset + 32 * i, 28))
            name = self.read_file(self.files[0], path_offset, 1024).split(b"\0")[0].decode()
            self.images[name] = address

    @staticmethod
    def read_file(f, offset, size):
        f.seek(offset)
        return f.read(size)

    def mapping(self, address):
        for mapping in self.mappings:
            if mapping[0] <= address < mapping[1]:
                return mapping
        raise SystemExit("ipcdex: address 0x%x isn't in the cache" % address)

    def read(self, address, size):
        start, end, f, file_offset, _ = self.mapping(address)
        return self.read_file(f, file_offset + address - start, min(size, end - address))

    def pointer(self, raw, address):
        """The target of a plain data pointer stored at address, or None. In slide
        info v5, bit 63 marks a signed pointer, bits 34 to 41 hold the top byte
        and the low 34 bits are an offset from value_add."""
        value_add = self.mapping(address)[4]
        if value_add is None or raw == 0 or raw >> 63:
            return None
        high8 = (raw >> 34) & 0xFF
        return (high8 << 56) | (value_add + (raw & 0x3FFFFFFFF))


class Library:
    """Reads addresses from a WebKit built outside a shared cache, such as one built from source. It
    reads the 64-bit ARM slice of a universal binary, and pointers stored as chained fixups."""

    def __init__(self, path):
        self.file = open(path, "rb")
        self.start = 0
        magic, = struct.unpack(">I", self.file.read(4))
        if magic in (0xCAFEBABE, 0xCAFEBABF):  # a universal binary, whose header is big-endian
            count, = struct.unpack(">I", self.file.read(4))
            size = 20 if magic == 0xCAFEBABE else 32
            slices = {}
            for i in range(count):
                entry = self.read_file(8 + size * i, size)
                cputype, subtype = struct.unpack_from(">Ii", entry)
                if cputype == CPU_ARM64:
                    slices[subtype & 0xFF] = struct.unpack_from(">I" if size == 20 else ">Q", entry, 8)[0]
            if not slices:
                raise SystemExit("ipcdex: %s has no 64-bit ARM slice" % path)
            self.start = slices.get(2, next(iter(slices.values())))  # arm64e if there is one
        magic, cputype, _, _, ncmds, size = struct.unpack("<IiiIII", self.read_file(0, 24))
        if magic != 0xFEEDFACF or cputype != CPU_ARM64:
            raise SystemExit("ipcdex: %s is neither a dyld shared cache nor a 64-bit ARM library" % path)
        commands = self.read_file(32, size)
        self.uuid = self.platform = name = fixups = None
        self.segments = []  # (address, end, file offset, file size)
        offset = 0
        for _ in range(ncmds):
            cmd, cmdsize = struct.unpack_from("<II", commands, offset)
            if cmd == 0x19:  # LC_SEGMENT_64
                address, size, fileoff, filesize = struct.unpack_from("<QQQQ", commands, offset + 24)
                self.segments.append((address, address + size, fileoff, filesize))
            elif cmd == 0xD:  # LC_ID_DYLIB
                at, = struct.unpack_from("<I", commands, offset + 8)
                name = commands[offset + at:offset + cmdsize].split(b"\0")[0].decode()
            elif cmd == 0x32:  # LC_BUILD_VERSION
                self.platform, = struct.unpack_from("<I", commands, offset + 8)
            elif cmd == 0x80000034:  # LC_DYLD_CHAINED_FIXUPS
                fixups, = struct.unpack_from("<I", commands, offset + 8)
            offset += cmdsize
        self.base = self.segments[0][0]
        self.images = {name: self.base}
        # Each segment's pointer format, from the chained fixups' starts. A library without chained
        # fixups stores plain addresses.
        self.formats = {}
        if fixups is not None:
            starts, = struct.unpack_from("<I", self.read_file(fixups, 8), 4)
            count, = struct.unpack("<I", self.read_file(fixups + starts, 4))
            for i, at in enumerate(struct.unpack("<%dI" % count, self.read_file(fixups + starts + 4, 4 * count))):
                if at:
                    self.formats[i], = struct.unpack_from("<H", self.read_file(fixups + starts + at, 8), 6)

    def read_file(self, offset, size):
        self.file.seek(self.start + offset)
        return self.file.read(size)

    def segment(self, address):
        for i, (start, end, fileoff, filesize) in enumerate(self.segments):
            if start <= address < end:
                return i, start, fileoff, filesize
        raise SystemExit("ipcdex: address 0x%x isn't in the library" % address)

    def read(self, address, size):
        _, start, fileoff, filesize = self.segment(address)
        return self.read_file(fileoff + address - start, max(0, min(size, filesize - (address - start))))

    def pointer(self, raw, address):
        """The target of a plain data pointer stored at address, or None. A chained fixup keeps its
        target in the low bits and the top byte above them. Signed pointers and binds to other
        libraries are left out, as in the cache."""
        fmt = self.formats.get(self.segment(address)[0])
        if fmt is None:
            return raw or None
        if raw == 0 or raw >> 63 or (fmt in ARM64E_FORMATS and raw >> 62 & 1):
            return None
        bits = 43 if fmt in ARM64E_FORMATS else 36
        target, high8 = raw & ((1 << bits) - 1), (raw >> bits) & 0xFF
        if fmt not in VMADDR_FORMATS and fmt not in OFFSET_FORMATS:
            raise SystemExit("ipcdex: the library's pointer format %d isn't one ipcdex reads" % fmt)
        return (high8 << 56) | (target if fmt in VMADDR_FORMATS else self.base + target)


Section = collections.namedtuple("Section", "segment name address size")


class MachO:
    """The load commands of one image in the cache."""

    def __init__(self, cache, address):
        self.cache = cache
        magic, _, _, _, ncmds, size = struct.unpack("<IiiIII", cache.read(address, 24))
        if magic != 0xFEEDFACF:
            raise SystemExit("ipcdex: no Mach-O at 0x%x" % address)
        commands = cache.read(address + 32, size)
        self.sections = []
        self.uuid = self.version = self.symtab = self.linkedit = None
        offset = 0
        for _ in range(ncmds):
            cmd, cmdsize = struct.unpack_from("<II", commands, offset)
            if cmd == 0x19:  # LC_SEGMENT_64
                segment = commands[offset + 8:offset + 24].split(b"\0")[0].decode()
                vmaddr, _, fileoff, _, _, _, nsects, _ = struct.unpack_from("<QQQQiiII", commands, offset + 24)
                if segment == "__LINKEDIT":
                    self.linkedit = (vmaddr, fileoff)
                for s in range(offset + 72, offset + 72 + 80 * nsects, 80):
                    name = commands[s:s + 16].split(b"\0")[0].decode()
                    self.sections.append(Section(segment, name, *struct.unpack_from("<QQ", commands, s + 32)))
            elif cmd == 0x2:  # LC_SYMTAB
                self.symtab = struct.unpack_from("<IIII", commands, offset + 8)
            elif cmd == 0x1B:  # LC_UUID
                self.uuid = commands[offset + 8:offset + 24]
            elif cmd == 0x2A:  # LC_SOURCE_VERSION
                v, = struct.unpack_from("<Q", commands, offset + 8)
                self.version = "%d.%d.%d.%d.%d" % (
                    v >> 40, (v >> 30) & 0x3FF, (v >> 20) & 0x3FF, (v >> 10) & 0x3FF, v & 0x3FF)
            offset += cmdsize

    def section(self, segment, name):
        return next((s for s in self.sections if s.segment == segment and s.name == name), None)

    def symbols_in(self, section):
        """(name, address) of the image's own symbols that point into section.
        macOS caches keep WebKit's local symbols here. iOS caches move them to a
        separate .symbols file, so this finds none there."""
        if not self.symtab or not self.linkedit:
            return []
        symoff, nsyms, stroff, _ = self.symtab
        linkedit = lambda fileoff: self.linkedit[0] + fileoff - self.linkedit[1]
        found = []
        for strx, ntype, _, _, value in struct.iter_unpack("<IBBHQ", self.cache.read(linkedit(symoff), 16 * nsyms)):
            if (ntype & 0x0E) == 0x0E and section.address <= value < section.address + section.size:
                name = self.cache.read(linkedit(stroff) + strx, 256).split(b"\0")[0]
                found.append((name, value))
        return found


def read_table(cache, webkit):
    """The table's address, its entries in order, the IPC::ReceiverName value
    of Invalid and the table's section.

    Each entry is (name, receiver, flags, sender, destination). An entry is a
    pointer to the name, the name's length with its NUL, the IPC::ReceiverName,
    the flag bits, and the IPC::ProcessName of the sender and of the
    destination, padded to 24 bytes."""
    cstring = webkit.section("__TEXT", "__cstring")
    strings = cache.read(cstring.address, cstring.size)
    at = strings.find(b"\0" + END_NAME)
    if at < 0 or strings.find(b"\0" + END_NAME, at + 1) >= 0:
        raise SystemExit("ipcdex: no single %r string in WebKit" % END_NAME[:-1].decode())
    end_name = cstring.address + at + 1

    def entry(data, offset, address):
        raw, length = struct.unpack_from("<QQ", data, offset)
        target = cache.pointer(raw, address)
        if target is None or not cstring.address <= target or not 2 <= length <= 512:
            return None
        name = strings[target - cstring.address:target - cstring.address + length]
        if len(name) != length or name[-1] or 0 in name[:-1] or not name.isascii():
            return None
        receiver, flags, sender, destination = data[offset + 16:offset + 20]
        if flags > 7 or any(data[offset + 20:offset + 24]):
            return None
        return name[:-1].decode(), receiver, flags, sender, destination

    # The end entry is a pointer to the end name followed by its length, 23,
    # in a const data section.
    found = []
    length = struct.pack("<Q", len(END_NAME))
    for section in webkit.sections:
        if section.name != "__const" or section.segment == "__TEXT":
            continue
        data = cache.read(section.address, section.size)
        offset = data.find(length, 8)
        while offset >= 0:
            if offset % 8 == 0 and cache.pointer(struct.unpack_from("<Q", data, offset - 8)[0],
                                                 section.address + offset - 8) == end_name:
                found.append((section, data, offset - 8))
            offset = data.find(length, offset + 1)
    if len(found) != 1:
        raise SystemExit("ipcdex: found %d message tables in WebKit, expected 1" % len(found))
    section, data, end_offset = found[0]
    end = entry(data, end_offset, section.address + end_offset)
    if end is None or end[3:] != (len(PROCESSES) - 1,) * 2:
        raise SystemExit("ipcdex: this message table has a layout ipcdex doesn't read")

    entries = []
    offset = end_offset - ENTRY_SIZE
    while offset >= 0:
        e = entry(data, offset, section.address + offset)
        if e is None or not 1 <= e[1] < end[1]:
            break
        entries.append(e)
        offset -= ENTRY_SIZE
    entries.reverse()
    return section.address + offset + ENTRY_SIZE, entries, end[1], section


def index(path):
    """The meta block and the messages of the WebKit at path, in a dyld shared cache or a library of
    its own, the number of the first sync message, and the results of the checks, which are
    reported but not written to the index."""
    with open(path, "rb") as f:
        in_cache = f.read(7) == b"dyld_v1"
    cache = DyldCache(path) if in_cache else Library(path)
    if in_cache:
        webkit_path = next((p for p in WEBKIT_PATHS if p in cache.images), None)
        if webkit_path is None:
            raise SystemExit("ipcdex: no WebKit in %s" % path)
    else:
        webkit_path = next(iter(cache.images))
    webkit = MachO(cache, cache.images[webkit_path])
    start, entries, invalid, section = read_table(cache, webkit)

    # ReceiverName values are numbered in name order, with IPC last and
    # Invalid after it. IPC's own messages are the ones without a prefix.
    ipc = invalid - 1
    prefixes = collections.defaultdict(collections.Counter)
    for name, receiver, *_ in entries:
        prefixes[receiver][name.split("_", 1)[0] if receiver != ipc else "IPC"] += 1
    receivers = {r: names.most_common(1)[0][0] for r, names in prefixes.items()}

    # Messages are sorted with all async messages first, so the sync ones
    # start after the IPC receiver's async messages.
    first_sync = 0
    while first_sync < len(entries) and entries[first_sync][1] != ipc:
        first_sync += 1
    while first_sync < len(entries) and entries[first_sync][1] == ipc:
        first_sync += 1

    # The generator sets the sync-reply flag on every message of a stream
    # receiver, so a receiver whose async messages all have it is one.
    sync_reply_flags = collections.defaultdict(list)
    for name, receiver, flags, *_ in entries[:first_sync]:
        if not flags & REPLY_FLAG:
            sync_reply_flags[receiver].append(flags & SYNC_REPLY_FLAG)
    stream = {r for r, bits in sync_reply_flags.items() if all(bits)}

    process = lambda p: PROCESSES[p] if p < len(PROCESSES) else str(p)
    messages = []
    for number, (name, receiver, flags, sender, destination) in enumerate(entries):
        messages.append({
            "number": number,
            "name": name,
            "receiver": receivers[receiver],
            "from": process(sender),
            "to": process(destination),
            "sync": number >= first_sync,
            "reply": bool(flags & REPLY_FLAG),
            "stream": receiver in stream,
            "allowed_when_waiting_for_sync_reply": bool(flags & SYNC_REPLY_FLAG),
            "allowed_when_waiting_for_unbounded_sync_reply": bool(flags & UNBOUNDED_FLAG),
        })

    # Each check is something the generator guarantees, so a failure means
    # ipcdex read the table wrong.
    sort_key = lambda m: (m["receiver"] == "IPC", m["name"])
    in_order = lambda part: part == sorted(part, key=sort_key)
    receiver_ids = sorted(r for r in receivers if r != ipc)
    symbols = [address for name, address in webkit.symbols_in(section) if name == TABLE_SYMBOL]
    checks = {
        "one_prefix_per_receiver": all(len(names) == 1 for names in prefixes.values()),
        "names_unique": len({m["name"] for m in messages}) == len(messages),
        "sorted": in_order(messages[:first_sync]) and in_order(messages[first_sync:]),
        "receivers_in_name_order": [receivers[r] for r in receiver_ids] == sorted(receivers[r] for r in receiver_ids),
        "sync_flags": all(m["allowed_when_waiting_for_sync_reply"] and not m["reply"]
                          for m in messages[first_sync:]),
        "reply_names": all(m["name"].endswith("Reply") for m in messages if m["reply"]),
        "known_processes": all(max(e[3:]) < len(PROCESSES) for e in entries),
        "symbol": symbols == [start] if symbols else None,
    }
    # Only the cache's file name, so an index is the same on every machine and holds no local path.
    meta = {
        "platform": PLATFORMS.get(cache.platform, "platform %d" % cache.platform),
        "webkit_version": webkit.version,
        "webkit_uuid": uuid_text(webkit.uuid),
        "webkit": webkit_path,
        "cache": os.path.basename(path) if in_cache else None,
        "cache_uuid": uuid_text(cache.uuid) if in_cache else None,
        "table": "0x%x" % start,
        "messages": len(messages),
        "receivers": len(receivers),
    }
    return meta, messages, first_sync, checks


def write_index(meta, messages, out):
    """JSON with one message per line, so indexes compare well with diff and git."""
    out.write('{\n  "meta": %s,\n  "messages": [\n' % json.dumps(meta, indent=2).replace("\n", "\n  "))
    out.write(",\n".join("    " + json.dumps(m) for m in messages))
    out.write("\n  ]\n}\n")


def load(path, logstream):
    with open(path) as f:
        data = json.load(f)
    messages = {m["name"]: m for m in data["messages"] if logstream or m["receiver"] != "LogStream"}
    # An async reply is a message of its own, named after the one it answers. Fold it into that row.
    replies = {n for n, m in messages.items() if m["reply"] and n[:-5] in messages}
    rows = {n: dict(m, async_reply=n + "Reply" in replies) for n, m in messages.items() if n not in replies}
    return data["meta"], rows


def route(m):
    return "%s -> %s" % (m["from"], m["to"])


def flags(m):
    words = [f for f in ("sync", "reply", "stream") if m[f]]
    if m["async_reply"]:
        words.append("async reply")
    # WebKit's AllowedWhenWaitingForSyncReply and AllowedWhenWaitingForSyncReplyDuringUnboundedIPC.
    # Sync and stream messages always have the first.
    if m["allowed_when_waiting_for_sync_reply"] and not (m["sync"] or m["stream"]):
        words.append("handled during sync waits")
    if m["allowed_when_waiting_for_unbounded_sync_reply"]:
        words.append("handled during unbounded sync waits")
    return ", ".join(words)


def diff(old_path, new_path, logstream=True, sender=None):
    """The changes from one index to another, as Markdown."""
    old_meta, old = load(old_path, logstream)
    new_meta, new = load(new_path, logstream)
    # Each whole build's receivers, so --from doesn't call an existing receiver new.
    old_all, new_all = ({m["receiver"] for m in side.values()} for side in (old, new))
    if sender:
        processes = {m[end] for side in (old, new) for m in side.values() for end in ("from", "to")}
        if sender not in processes:
            raise SystemExit("ipcdex: no process named %s. The indexes have %s" % (sender, ", ".join(sorted(processes))))
        # A process writes the messages it sends and the replies to the ones it receives. A message
        # stays if the process sends it in either build, so one that starts or stops being sent
        # shows as changed.
        sends = lambda m: m["from"] == sender or (m["to"] == sender and (m["sync"] or m["async_reply"]))
        names = {n for side in (old, new) for n, m in side.items() if sends(m)}
        old, new = ({n: m for n, m in side.items() if n in names} for side in (old, new))
    old_label, new_label = (os.path.basename(p).rsplit(".json", 1)[0] for p in (old_path, new_path))
    added = sorted(n for n in new if n not in old)
    removed = sorted(n for n in old if n not in new)
    kept = {n for n in new if n in old}
    unnumbered = lambda m: {k: v for k, v in m.items() if k != "number"}
    changed = sorted(n for n in kept if unnumbered(old[n]) != unnumbered(new[n]))
    renumbered = sum(old[n]["number"] != new[n]["number"] for n in kept)
    old_receivers = {m["receiver"] for m in old.values()}
    new_receivers = {m["receiver"] for m in new.values()}
    messages = lambda n: "%d message%s" % (n, "" if n == 1 else "s")
    listed = lambda items: ", ".join("`%s`" % i for i in sorted(items)) or "none"

    out = ["# CoreIPC changes from %s to %s" % (old_label, new_label), ""]
    out += ["| | %s | %s |" % (old_label, new_label), "| --- | --- | --- |"]
    out.append("| Platform | %s | %s |" % (old_meta["platform"], new_meta["platform"]))
    out.append("| WebKit | %s | %s |" % (old_meta["webkit_version"], new_meta["webkit_version"]))
    out.append("| Messages | %d | %d |" % (len(old), len(new)))
    out += ["| Receivers | %d | %d |" % (len(old_receivers), len(new_receivers)), ""]
    notes = []
    if sender:
        notes.append("Only messages %s sends, including its replies." % sender)
    if not logstream:
        notes.append("The generated LogStream messages are left out.")
    if notes:
        out += [" ".join(notes), ""]
    out += [
        "- %s added and %d removed" % (messages(len(added)), len(removed)),
        "- %s changed route or flags" % messages(len(changed)),
        "- %s kept their names but changed numbers" % messages(renumbered),
        "- New receivers: %s" % listed(new_receivers - old_all),
        "- Removed receivers: %s" % listed(old_receivers - new_all),
        "",
    ]

    counts = collections.defaultdict(lambda: [0, 0])
    for n in added:
        counts[new[n]["receiver"]][0] += 1
    for n in removed:
        counts[old[n]["receiver"]][1] += 1
    if counts:
        out += ["## Changes per receiver", "", "| Receiver | Added | Removed |", "| --- | --- | --- |"]
        for receiver, (a, r) in sorted(counts.items(), key=lambda item: (-sum(item[1]), item[0])):
            out.append("| %s | %d | %d |" % (receiver, a, r))
        out.append("")

    for title, group, side in (("Added", added, new), ("Removed", removed, old)):
        if group:
            out += ["## %s (%d)" % (title, len(group)), ""]
            out += ["| Message | Number | Route | Flags |", "| --- | --- | --- | --- |"]
            for n in group:
                m = side[n]
                out.append("| `%s` | %d | %s | %s |" % (n, m["number"], route(m), flags(m)))
            out.append("")
    if changed:
        out += ["## Changed route or flags (%d)" % len(changed), "", "| Message | Old | New |", "| --- | --- | --- |"]
        for n in changed:
            old_text, new_text = (", ".join(filter(None, (route(m), flags(m)))) for m in (old[n], new[n]))
            out.append("| `%s` | %s | %s |" % (n, old_text, new_text))
        out.append("")
    return "\n".join(out)


def main(args):
    if args[:1] == ["diff"]:
        parser = argparse.ArgumentParser(
            prog="ipcdex.py diff", description="Print the changes between two indexes as Markdown.")
        parser.add_argument("old", help="the older index")
        parser.add_argument("new", help="the newer index")
        parser.add_argument("--no-logstream", action="store_true", help="leave out the generated LogStream messages")
        parser.add_argument("--from", dest="sender", metavar="PROCESS",
                            help="only messages this process sends, including its replies, such as WebContent")
        args = parser.parse_args(args[1:])
        sys.stdout.write(diff(args.old, args.new, logstream=not args.no_logstream, sender=args.sender))
        return 0

    parser = argparse.ArgumentParser(
        prog="ipcdex.py", description="Index the CoreIPC messages in the WebKit of a dyld shared cache.",
        epilog="ipcdex.py diff <old.json> <new.json> compares two indexes.")
    parser.add_argument("cache", help="a dyld shared cache with its subcaches next to it, or a WebKit library outside one")
    parser.add_argument("-o", metavar="index.json", help="write the index here instead of to standard output")
    args = parser.parse_args(args)
    meta, messages, first_sync, checks = index(args.cache)
    failed = [k for k, v in checks.items() if v is False]
    skipped = [k for k, v in checks.items() if v is None]
    print("%s WebKit %s, %d messages from %d receivers, sync from %d" % (
        meta["platform"], meta["webkit_version"], meta["messages"], meta["receivers"], first_sync),
        file=sys.stderr)
    # A failed check means ipcdex misread the table, so nothing is written.
    if failed:
        print("checks failed: %s, so no index was written" % ", ".join(failed), file=sys.stderr)
        return 1
    print("checks passed" + ("" if not skipped else ", skipped %s" % ", ".join(skipped)), file=sys.stderr)
    if args.o:
        with open(args.o, "w") as f:
            write_index(meta, messages, f)
    else:
        write_index(meta, messages, sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
