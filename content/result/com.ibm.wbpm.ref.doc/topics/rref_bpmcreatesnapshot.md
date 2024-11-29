# BPMCreateSnapshot command

Use the BPMCreateSnapshot command
in connected mode from Workflow Center to
create snapshots for process applications or toolkits. You can run
this command only on Workflow Center.

The BPMCreateSnapshot command
is run using the AdminTask object of the wsadmin
scripting client.

## Prerequisites

- In a network deployment environment,
an application cluster member runs the Workflow Server and Workflow Center applications.
Therefore, you must run this command on the node that contains that
application cluster member. Do not run the command from the deployment
manager profile.
- You can run the command for only one process application or toolkit
at a time.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
BPMCreateSnapshot 
-containerAcronym process\_application\_or\_toolkit\_acronym
[-containerTrackAcronym track\_acronym]
-snapshotName snapshot\_name
-snapshotDescription snapshot\_description
```

## Parameters

## Example

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMCreateSnapshot("[-containerAcronym TPA -containerSnapshotName SS1 -containerSnapshotDescription '0824snapshot']")
```

<!-- image -->