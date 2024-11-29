# BPMShowSnapshot command

Use the BPMShowSnapshot command in
connected mode from either a Workflow Center server
or Workflow Server to
return detailed information about a snapshot or tip, including any
dependencies.

The BPMShowSnapshot command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- In a network deployment environment,
you must run this command on the node containing the application cluster
member that handles Workflow Server or Workflow Center applications.
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
BPMShowSnapshot 
-containerAcronym process\_application\_or\_toolkit\_acronym
-containerSnapshotAcronym snapshot\_acronym
[-containerTrackAcronym track\_acronym]
[-showDependents]
```

## Parameters

## Example

The following example illustrates
how to establish a SOAP connection to the Workflow Center server
and return information about the process application snapshot called
BILLDISPSS02

<!-- image -->

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMShowSnapshot('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -containerTrackAcronym Main]')
```

```
Name: Main - JSActivate
Acronym : MJSA
Created On :2013-09-01 14:05:03.207
Created By :User1
State : State[Archived]
```

```
Depends on snapshot Main - JSActivate:
        Process App Acronym: PA1
        Process App Name: PA1
        Snapshot Name: PA1S1
        Snapshot Acronym: PA1S1
        Created On: 2014-02-26 14:25:31.016
        Created By: User.2
```