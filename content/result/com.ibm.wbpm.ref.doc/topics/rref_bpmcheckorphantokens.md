# BPMCheckOrphanTokens command

- Delete the token if it is no longer required in the new snapshot.
(Default action)
- Move the token to another step in the process.
- Suspend the process so process instance data can be manipulated
using Process Inspector.

The BPMCheckOrphanTokens command
checks activities only. These include user tasks, system tasks, decision
tasks, subprocesses, event subprocesses, linked processes, and nodes.

## Prerequisites

- In a network deployment environment, you must
run this command on the node containing the application cluster member
that handles Workflow Server applications.
Do not run this command from the deployment manager profile.
- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- To access the wsadmin command, the ID being used
must have the WebSphere® Application
Server deployer
role. See Administrative roles for information about
roles.

## Location

Start the wsadmin scripting client from the install\_root/bin directory.

## Syntax

```
BPMCheckOrphanTokens 
-processAppAcronym process\_application\_acronym
-sourceSnapshotName snapshot\_name | -sourceSnapshotAcronym snapshot\_acronym
-targetSnapshotName snapshot\_name | -targetSnapshotAcronym snapshot\_acronym
-outputFile file\_path
[-overwrite]
```

## Parameters

## Examples

The following example illustrates
how to establish a SOAP connection to the IBM® Workflow
Center server
and then generate an orphaned token policy file for a process application
with acronym OTA.

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com 
-user admin ID -password administrator password -lang jython

wsadmin>AdminTask.BPMCheckOrphanTokens('[-processAppAcronym OTA -sourceSnapshotName 
"Version A" -targetSnapshotName "Version B" -outputFile C:\TokenPolicyFile\_OTA.xml]')
```

The
following example uses  -sourceSnapshotAcronym and -targetSnapshotAcronym.

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com 
-user admin ID -password administrator password -lang jython

wsadmin>AdminTask.BPMCheckOrphanTokens('[-processAppAcronym OTA -sourceSnapshotAcronym
"Version A" -targetSnapshotAcronym "Version B" -outputFile C:\TokenPolicyFile\_OTA.xml]')
```

The
following example uses  -sourceSnapshotAcronym and -targetSnapshotName.

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com 
-user admin ID -password administrator password -lang jython

wsadmin>AdminTask.BPMCheckOrphanTokens('[-processAppAcronym OTA -sourceSnapshotAcronym
"Version A" -targetSnapshotName "Version B" -outputFile C:\TokenPolicyFile\_OTA.xml]')
```