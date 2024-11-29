<!-- image -->

# showSCAModule command

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
showSCAModule
-moduleName moduleName
[-applicationName applicationName]
```

## Required parameters

## Optional parameters

## Example

```
AdminTask.showSCAModule('-moduleName PAORDER-6.0S-SCAM1')
```

```
name:PAORDER-6.0DS-SCAM1
description:null
scaRuntimeVersion:7
businessObjectParsingMode:Lazy
processApp:PAORDER
processAppAcronym:PAORDER
processAppTrack:Main
processAppTrackAcronym:Main
"processAppSnapshot:6.0 Snapshot"
processAppSnapshotAcronym:6.0S
processAppSnapshotGUID:b17ee0ca-d0f8-4a71-a34d-310139a3037a
```