# BPMRemoveProcessApplication command

Use the BPMRemoveProcessApplication command
in connected mode to remove a process application from Workflow Center. You
can run this command only on Workflow Center.

The BPMRemoveProcessApplication command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- In a network deployment environment, you must run
this command on the node containing the application cluster member
that handles Workflow Center applications.
Do not run this command from the deployment manager profile. The 
input file is read from the machine on which the connected server
is running. If you want to access the file from another machine, establish
a remote wsadmin session from the current machine to the server on
the machine where the file is stored.
- The process application must be in an archived state before you
run this command.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
BPMRemoveProcessApplication
-containerAcronym process\_application\_acronym
```

## Parameters

## Example

```
wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMRemoveProcessApplication('[-containerAcronym MYCOAPP]')
```