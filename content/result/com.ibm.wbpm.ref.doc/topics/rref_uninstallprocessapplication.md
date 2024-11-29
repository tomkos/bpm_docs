<!-- image -->

# BPMUndeploy command

Traditional: 
This command undeploys a process
application snapshot from a server. It is available only if the snapshot
contains advanced content generated in IBM® Integration
Designer and
has a corresponding business-level application (BLA) deployed on the
server.

A BLA is a WebSphere® Application
Server configuration artifact
that is created only for a snapshot that has advanced content generated in IBM Integration
Designer.

Use the BPMUndeploy command in connected
mode to undeploy a process application snapshot from Workflow Center or Workflow Server.

Undeploying the snapshot removes any Service Component
Architecture (SCA) modules, monitor models, and BLAs associated with
the snapshot. If your process application contains BPEL processes,
see the "Deactivating and stopping process applications" link at the
end of this topic.

The BPMUndeploy command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- In a network deployment environment, you must run
this command on the node containing the application cluster member
that handles Workflow Server applications.
Do not run this command from the deployment manager profile.
- The BLA associated with the snapshot must be
in the STOPPED state. For more information, see BPMStop command.
- To run this command, you must have one of these permissions: write or administrative access to
the process application or toolkit, or administrative access to the Workflow Center repository.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
BPMUndeploy 
-containerAcronym process\_application\_acronym
-containerSnapshotAcronym process\_application\_snapshot\_acronym
[-containerTrackAcronym track\_acronym]
```

## Parameters

If you are not working with a snapshot, use Tip as
the value for this parameter. If advanced content is used in the process
application, the Tip value triggers the deployment
and start of the tip version of the BPEL application.

## Example

The following example illustrates
how to establish a SOAP connection to the Workflow Center server,
and then undeploy a snapshot of the BillingDispute process application.

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMUndeploy('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1]')
```