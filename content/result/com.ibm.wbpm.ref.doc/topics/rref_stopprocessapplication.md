<!-- image -->

# BPMStop command

Use the BPMStop command in connected mode to stop a deactivated snapshot on a
workflow server.

The BPMStop command is run using the AdminTask object of the wsadmin scripting
client.

## Prerequisites

- In a network deployment environment, you must run this command on the node
containing the application cluster member that handles Workflow Server applications. Do not
run this command from the deployment manager profile.
- In a network deployment environment, make sure that all the
node agents are active before you stop a BLA. If a node is inactive, the BLA enters the
UNKNOWN state instead of the STOPPED state and fails to stop,
although the stop command runs asynchronously and completes without an error. The failure to stop
along with the UNKNOWN state prevents you from undeploying the BLA.
- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- To access the wsadmin command, the ID being used
must have a WebSphere Application
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
BPMStop 
-containerAcronym process\_application\_acronym
-containerSnapshotAcronym process\_application\_snapshot\_acronym
```

## Parameters

If you are not
working with a snapshot, use Tip as the value for this parameter.

## Example

The following example illustrates how to establish a SOAP connection to the Workflow Center server, and then stop
a BLA of the BillingDispute process application.

```
wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMStop('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1]')
```