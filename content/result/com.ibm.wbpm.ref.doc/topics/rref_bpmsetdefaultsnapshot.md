# BPMSetDefaultSnapshot command

On Workflow Server, the
first snapshot you install is considered the default version. The
items within that snapshot run when an event or other trigger that
applies to more than one version of a process or service is received.
When you install subsequent snapshots, you can use the Make
Default Version option in Process Admin Console to ensure
the snapshot you want to run is the default.

On  Workflow Center, the
default snapshot is always the tip of the default branch. You cannot
set the default snapshot.

The BPMSetDefaultSnapshot command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- In a network deployment environment, an application
cluster member runs the Workflow Server applications.
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
BPMSetDefaultSnapshot 
-containerAcronym process\_application\_acronym
-containerSnapshotAcronym process\_application\_snapshot\_acronym
```

## Parameters

## Example

The following example illustrates
how to set a snapshot of the BillingDispute process application as
the default snapshot. In the example, the user establishes a SOAP
connection to the Workflow Server.

```
wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMSetDefaultSnapshot('[-containerAcronym BILLDISP -containerSnapshotAcronym SS8.5.5]')
```