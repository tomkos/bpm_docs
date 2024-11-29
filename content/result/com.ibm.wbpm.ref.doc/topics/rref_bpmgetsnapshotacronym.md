# BPMGetSnapshotAcronym command

Use the BPMGetSnapshotAcronym command
in connected mode from either Workflow Center server
or Workflow Server to
return the acronym of a snapshot of a process application on Workflow Center or Workflow Server.

The BPMGetSnapshotAcronym command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- In a network deployment environment, an application
cluster member runs the Workflow Server and Workflow Center applications.
Therefore, you must run this command on the node that contains that
application cluster member. Do not run the command from the deployment
manager profile.
- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- To access the wsadmin command, the ID being used
must have a WebSphere® Application
Server role
with more privileges than the monitor role. See Administrative roles for information about
roles.
- To access the Business Automation Workflow API used
by this command, the ID being used must belong to either the bpmAdminGroup
or bpmAuthorGroup. The default name for the bpmAdminGroup is tw\_admins
and the default name for the bpmAuthorGroup is tw\_authors. See IBM Business Automation Workflow default group types for information about groups.Tip: By default, only the DeAdmin user has both the WebSphere Application
Server administrator
role and membership in the bpmAdminGroup.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

You can check the status of the command in the server SystemOut.log file.

## Syntax

```
BPMGetSnapshotAcronym 
-containerAcronym process\_application\_acronym
-containerSnapshotName snapshot\_name
```

## Parameters

## Example

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMGetSnapshotAcronym('[-containerAcronym BILLDISP -containerSnapshotName 1.1]')
```