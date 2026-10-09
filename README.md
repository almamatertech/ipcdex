# ipcdex

`ipcdex` lists every CoreIPC message in a WebKit build and shows what changed between two builds.
CoreIPC is how WebKit's processes talk to each other, such as WebContent, GPU, Networking and the UI
process. `ipcdex` reads the list from the build itself, from a macOS or iOS release's shared cache
or from a WebKit you build yourself, so it's exactly what that build has. For each message it gives
the number the build uses, the sending and receiving process, and whether it's synchronous or a
reply.

## Requirements

- Python 3.9 or later.
- A dyld shared cache, or a WebKit you built yourself. A Mac's own cache is
  `dyld_shared_cache_arm64e` in `/System/Volumes/Preboot/Cryptexes/OS/System/Library/dyld/`. Macs
  with newer chips also have `dyld_shared_cache_arm64e_x1` there, with its own build of WebKit for
  those chips. For any other iOS or macOS release, [ipsw](https://github.com/blacktop/ipsw) can pull
  the cache out of Apple's IPSW without downloading all of it:

  ```
  ipsw download ipsw --device iPhone18,4 --version 27.0.1 --dyld
  ipsw download ipsw --macos --version 27.0.1 --dyld --extract-device Mac18,5
  ```

## Usage

```
ipcdex.py <dyld cache or WebKit> [-o index.json]
ipcdex.py diff <old.json> <new.json> [--no-logstream] [--from PROCESS]
```

The first writes an index of the build's messages. The second prints what changed between two
indexes, as Markdown. `indexes/` has three example indexes, for macOS 27.0.1 (26A434), and iOS
26.5.2 (23F84) and 27.0.1 (24A446) for iPhone18,4.

## Index a build

```
$ ipcdex.py /System/Volumes/Preboot/Cryptexes/OS/System/Library/dyld/dyld_shared_cache_arm64e -o macos-27.0.1.json
macOS WebKit 625.1.29.11.28, 4492 messages from 219 receivers, sync from 4256
checks passed
```

It takes under a second. The checks test rules WebKit always follows when it generates the table,
so a failed check means `ipcdex` read it wrong, and it then writes no index. On iOS it skips the
check against WebKit's symbol for the table, since iOS caches don't have it.

## Bring your own build

For a WebKit you build yourself, pass `WebKitBuild/Release/WebKit.framework/Versions/A/WebKit`.
This example uses one of webkit.org's [build archives](https://webkit.org/build-archives/):

```
$ ipcdex.py Release/WebKit.framework/Versions/A/WebKit -o 323385.json
macOS WebKit 627.1.4.0.0, 4619 messages from 219 receivers, sync from 4377
checks passed
```

It reads the 64-bit ARM part of a universal build.

## Look up messages

Each message is one JSON object:

```
$ jq -c '.messages[3000]' indexes/macos-27.0.1.json
{"number":3000,"name":"WebPageProxy_DidUpdateHistoryTitle","receiver":"WebPageProxy","from":"WebContent","to":"UI","sync":false,"reply":false,"stream":false,"allowed_when_waiting_for_sync_reply":false,"allowed_when_waiting_for_unbounded_sync_reply":false}
```

Numbers change between builds, even between macOS and iOS of the same version:

```
$ jq '.messages[] | select(.name == "WebPage_Close") | .number' indexes/macos-27.0.1.json indexes/ios-27.0.1.json
3272
3288
```

Where the messages WebContent sends on macOS 27.0.1 go, leaving out replies:

```
$ jq -r '.messages[] | select(.from == "WebContent" and (.reply | not)) | .to' indexes/macos-27.0.1.json | sort | uniq -c | sort -rn
 946 UI
 875 GPU
 279 Networking
  23 Model
  15 Unknown
```

## Compare two builds

```
$ ipcdex.py diff indexes/ios-26.5.2.json indexes/ios-27.0.1.json
# CoreIPC changes from ios-26.5.2 to ios-27.0.1
...
- 405 messages added and 315 removed
- 6 messages changed route or flags
- 3260 messages kept their names but changed numbers
- New receivers: `ProxyingNetworkAgent`, `ProxyingPageAgent`, `RemoteMediaResourceLoader`, `RemoteMediaResourceLoaderProxy`, `RemoteMesh`
...
## Added (405)

| Message | Number | Route | Flags |
| --- | --- | --- | --- |
...
| `GPUProcess_PromptForGetDisplayMedia` | 109 | UI -> GPU | async reply |
...
| `RemoteMesh_PaintCurrentFrameToImageBuffer` | 4463 | WebContent -> GPU | sync, stream |
| `RemoteMesh_Play` | 2060 | WebContent -> GPU | stream |
...
```

The [full output](indexes/ios-26.5.2-to-27.0.1_diff.md) lists every added and removed message with
its number, route and flags. A message and its async reply share one row and count as one.
Renumbering is only counted, because adding or removing one message shifts the numbers of all the
messages after it. Over half of these changes are messages WebKit generates for logging
(`LogStream`). `--no-logstream` leaves them out, which brings this diff to 171 added and 129 removed.

## Messages from one process

`--from WebContent` keeps only the messages WebContent sends:

```
$ ipcdex.py diff indexes/ios-26.5.2.json indexes/ios-27.0.1.json --no-logstream --from WebContent
...
Only messages WebContent sends, including its replies. The generated LogStream messages are left out.

- 112 messages added and 105 removed
- 6 messages changed route or flags
...
| `RemoteMesh_Render` | 2063 | WebContent -> GPU | stream, async reply |
| `WebBackForwardList_BackForwardItemAtIndexForWebContent` | 4472 | WebContent -> UI | sync |
| `WebFrame_RequestContainerJSHandleForSearchTexts` | 2734 | UI -> WebContent | async reply |
...
```

A process also writes the replies to the messages it receives, so sync messages and messages with
an async reply sent to it count too, like the last row. `--from GPU` shows what the GPU process can
send.

## IDA

`ida/ipcdex.py` loads an index into IDA 9 (tested with 9.4) as the enum `IPC::MessageName`. Open the
WebKit the index was made from, run the script with File > Script file and pick the index:

```
ipcdex: IPC::MessageName has the 4492 messages of WebKit 625.1.29.11.28
```

Then press M on a message number to see its name. In `GPUConnectionToWebProcess::didReceiveSyncMessage`
on macOS 27.0.1, `MOV W11, #0x10A0` becomes `MOV W11, #GPUConnectionToWebProcess_EnsureAudioSession`.
The script checks the WebKit's UUID and refuses an index made from any other build, because
message numbers change between builds.

## How it works

WebKit generates one table with an entry for every message, holding its name, receiver, flags, and
sending and receiving process. A message's number is its place in the table. `ipcdex` finds the
table by the entry that always ends it, `<invalid message name>`, and reads back from there, so it
needs no symbols. Each entry points to its message's name. In a shared cache those pointers are read
through the cache's slide info, and in a WebKit of its own through its chained fixups. The table
comes from WebKit's
[message generator](https://github.com/WebKit/WebKit/blob/WebKit-7625.1.29.11.27/Source/WebKit/Scripts/webkit/messages.py#L2137).

## Limits

- `ipcdex` understands the message table as WebKit has written it since August 2025. On older
  builds it stops with an error instead of giving wrong results.
- The table names each message but doesn't list its arguments or the build flags it depends on.
  For those, read the message's `.messages.in` file in WebKit's source.
- `--from` reads WebKit's list of messages. It can't tell whether the receiving process acts on a
  message or ignores it, for example when the feature behind it is turned off.
- A macOS cache has a second WebKit, for iPad apps running on the Mac. `ipcdex` indexes only the
  main one, which Safari uses.

Licensed under [MIT](LICENSE).
