<!-- image -->

# Undeploying a snapshot on a Workflow Center server

## Before you begin

1. Deactivate the snapshot before you undeploy it. For more information, see Deactivating snapshots on a Workflow Center server.
2. When you use the classic Workflow Center to undeploy a project, it first stops and
then undeploys the BLA.
In a network deployment environment, make sure that all the
node agents are active before you stop a BLA. If a node is inactive, the BLA enters the
UNKNOWN state instead of the STOPPED state and fails to stop,
although the stop command runs asynchronously and completes without an error. The failure to stop
along with the UNKNOWN state prevents you from undeploying the BLA.

## About this task

When you activate a snapshot on the on a Workflow Center server, it is considered deployed on that
server. In order to remove the advanced content artifacts and the associated business-level
application (BLA) from the Workflow Center server,
you must undeploy the snapshot.  A BLA is a WebSphere® Application
Server configuration artifact
that is created only for a snapshot that has advanced content generated in IBM Integration
Designer.

If the
process application uses BPEL processes, the associated process instance
data is cleaned up from the Business Process Choreographer database
before the snapshot is undeployed.

## Procedure

1. From Workflow Center,
select the process application, then click the Snapshots tab.
2. Find the snapshot you want to undeploy, and then click Undeploy from its pop-up menu ().
3. Click OK.

## What to do next