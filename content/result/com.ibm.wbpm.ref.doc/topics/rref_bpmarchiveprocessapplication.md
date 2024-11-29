# BPMArchiveProcessApplication command

Use the BPMArchiveProcessApplication command
in connected mode to archive a process application from Workflow Center. You
can run this command only on Workflow Center.

The BPMArchiveProcessApplication command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- In a network deployment environment, you must run this command
on the node containing the application cluster member that handles Workflow Center applications.
Do not run this command from the deployment manager profile. The input
file is read from the machine on which the connected server is running.
If you want to access the file from another machine, establish a remote
wsadmin session from the current machine to the server on the machine
where the file is stored.
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
BPMArchiveProcessApplication
-containerAcronym process\_application\_acronym
```

## Parameters

## Example

```
wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMArchiveProcessApplication('[-containerAcronym MYCOAPP]')
```