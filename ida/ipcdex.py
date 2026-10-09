"""Load an ipcdex index into IDA 9 as the enum IPC::MessageName.

Open the WebKit the index was made from, run this with File > Script file and
pick the index. Then press M on a message number to see its name. The script
refuses an index whose WebKit UUID matches no image in the database, because
message numbers change with every build.
"""
import json
import struct
import uuid

import ida_bytes
import ida_kernwin
import ida_typeinf
import idautils
import idc


def image_uuids():
    """The LC_UUID of each Mach-O header in the database."""
    found = []
    for header in idautils.Segments():
        if ida_bytes.get_dword(header) != 0xFEEDFACF:
            continue
        command = header + 32
        for _ in range(ida_bytes.get_dword(header + 16)):
            cmd, size = struct.unpack("<II", ida_bytes.get_bytes(command, 8))
            if cmd == 0x1B:  # LC_UUID
                found.append(str(uuid.UUID(bytes=ida_bytes.get_bytes(command + 8, 16))).upper())
            command += size
    return found


def load(path):
    with open(path) as f:
        index = json.load(f)
    webkit = index["meta"]["webkit_uuid"]
    if webkit not in image_uuids():
        ida_kernwin.warning("ipcdex: %s is for WebKit %s, which isn't in this database" % (path, webkit))
        return
    enum = ida_typeinf.enum_type_data_t()
    enum.set_nbytes(2)
    for message in index["messages"]:
        enum.add_constant(message["name"], message["number"])
    tif = ida_typeinf.tinfo_t()
    tif.create_enum(enum)
    error = tif.set_named_type(None, "IPC::MessageName", ida_typeinf.NTF_REPLACE)
    if error != ida_typeinf.TERR_OK:
        ida_kernwin.warning("ipcdex: couldn't save IPC::MessageName, %s" % ida_typeinf.tinfo_errstr(error))
        return
    print("ipcdex: IPC::MessageName has the %d messages of WebKit %s" % (
        len(index["messages"]), index["meta"]["webkit_version"]))


path = idc.ARGV[1] if len(idc.ARGV) > 1 else ida_kernwin.ask_file(False, "*.json", "ipcdex index")
if path:
    load(path)
