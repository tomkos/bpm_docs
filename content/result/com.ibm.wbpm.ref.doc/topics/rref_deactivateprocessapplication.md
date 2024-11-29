# BPMDeactivate command

The deactivation function prevents any new
requests but allows all existing instances and in-flight requests
to complete processing. Using the optional parameters, you can also
deactivate the default snapshot as well as suspend in-flight instances.

It is possible to deactivate the default snapshot without using the optional
-force parameter. It is, therefore, recommended to check whether the snapshot
is set as the default before deactivating it. When there is only one snapshot for a process
application, deactivating the default snapshot might be intended, but when there is more than one,
it is recommended that you mark another snapshot as the default before deactivating the current
default snapshot.

You might need to deactivate a snapshot if you want
to undeploy it from a Workflow Center server,
or if you want to stop it or undeploy it from a Workflow Server.

- If your process application uses a BPEL process as the main entry
component, you must stop the corresponding BPEL template in the WebSphere
administrative console. See "Administering BPEL process and task templates."
- Additionally, if this BPEL process invokes a BPD, you must allow
any existing instances to complete after you stop the template but
before you deactivate the snapshot. See "Administering BPEL process
and task templates."
- In all cases, you must clean up the associated process instance
data from the Business Process Choreographer database, as described
in "Cleanup procedures for Business Process Choreographer."

The BPMDeactivate command is run using
the AdminTask object of the wsadmin scripting client.

## Prerequisites

- In a network deployment environment, you must
run this command on the node containing the application cluster member
that handles Workflow Server or Workflow Center applications.
Do not run this command from the deployment manager profile.
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
BPMDeactivate 
-containerAcronym process\_application\_or\_toolkit\_acronym
-containerSnapshotAcronym snapshot\_acronym
[-containerTrackAcronym track\_acronym]
[-force]
[-suspendAllBPDInstances]
[-outputFile file\_path]
```

## Parameters

## Example

In the following example, you first
establish a SOAP connection to the Workflow Center server
and then deactivate a snapshot of the BillingDispute process application.
The snapshot is part of the Main track.

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython
```

```
wsadmin>AdminTask.BPMDeactivate('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -containerTrackAcronym Main]')
```