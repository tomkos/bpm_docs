# BPMActivate command

Use the BPMActivate command in connected
mode to activate a snapshot that has been deactivated, stopped, or
undeployed. Activated snapshots can receive and process requests.

Only
the business process definition (BPD) is activated when you activate
a process application. If the process application uses BPEL processes
and the templates were stopped (as described in Administering BPEL
process and task templates), follow the instructions in that section
to start the templates.

The BPMActivate command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- In a network deployment environment,
an application cluster member runs the Workflow Server and Workflow Center applications.
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
BPMActivate 
-containerAcronym process\_application\_acronym
-containerSnapshotAcronym process\_application\_snapshot\_acronym
[-containerTrackAcronym track\_acronym]
```

## Parameters

If you are not working with a snapshot, use Tip as
the value for this parameter.

## Example

The following example illustrates
how to activate a snapshot of the BillingDispute process application.
The snapshot is part of the Main track. In the example, the user establishes
a SOAP connection to the Workflow Center server.

<!-- image -->

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMActivate('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -containerTrackAcronym Main]')
```