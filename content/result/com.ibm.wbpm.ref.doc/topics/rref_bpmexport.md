# BPMExport command

Use the BPMExport command to exchange
a process application or toolkit between Workflow Center servers.
You must run the command in connected mode from a Workflow Center server.

The BPMExport command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- In a network deployment environment, you must
run this command on the node containing the application cluster member
that handles Workflow Center applications.
Do not run this command from the deployment manager profile. The generated
file is saved on the machine where the connected server is running.
To save the generated file on another machine, establish a remote
wsadmin session from the current machine to the server on the machine
where you want to save the file.
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
BPMExport 
-containerAcronym process\_application\_acronym
-containerSnapshotAcronym process\_application\_snapshot\_acronym
[-containerTrackAcronym track\_acronym]
-outputFile file\_path
```

## Parameters

## Example

The following example illustrates
how to export a snapshot of the BillingDispute process application.
In the example, the user establishes a SOAP connection to the Workflow Center server.

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMExport('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -containerTrackAcronym Main -outputFile C:\processApps\BILLDISP201.twx]')
```