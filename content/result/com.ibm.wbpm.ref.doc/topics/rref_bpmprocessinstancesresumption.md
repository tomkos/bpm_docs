# BPMProcessInstancesResumption command

## Prerequisites

- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- You can run the command from any cluster member
in a network deployment environment. However, you must first establish
the wsadmin session to the SOAP port of the cluster member from where
you are running the command.
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

Start the wsadmin scripting client from the install\_root/bin directory.

## Syntax

```
BPMProcessInstancesResumption
-containerAcronym process\_application\_\_or\_toolkit\_acronym
-containerSnapshotAcronym snapshot\_acronym
[-maxNumberOfInstances n]
[-getNumberOfInstances]
```

## Parameters

## Examples

In the following example, you first
establish a SOAP connection to the server and then use the BPMProcessInstancesResumption command
to resume a maximum of 500 suspended BPD instances in a snapshot of
the BillingDispute process application. The snapshot is part of the
Main track.

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython
```

```
wsadmin>AdminTask.BPMProcessInstancesResumption('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -maxNumberOfInstances 500]')
```

```
wsadmin>AdminTask.BPMProcessInstancesResumption('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -getNumberOfInstances]')
```