# BPMDeleteDurableMessages command

- intermediate
- boundary
- start events of event subprocesses

The BPMDeleteDurableMessages command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- You cannot use this command to delete messages for BPEL processes.
- You can run the command from any cluster member
in a network deployment environment. However, you must first establish
the wsadmin session to the SOAP port of the cluster member from where
you are running the command.
- To access the wsadmin command, the ID being
used must have the WebSphere® Application
Server administrator
role. See Administrative roles for information about
roles.
- To access the Business Automation Workflow API used
by this command, the ID being used must belong to either the bpmAdminGroup
or bpmAuthorGroup. The default name for the bpmAdminGroup is tw\_admins
and the default name for the bpmAuthorGroup is tw\_authors. See IBM Business Automation Workflow default group types for information about groups.Tip: By default, only the DeAdmin user has both the WebSphere Application
Server administrator
role and membership in the bpmAdminGroup.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
BPMDeleteDurableMessages 
-olderThan age\_in\_days
[-maximumDuration number\_of\_minutes]
[-transactionSlice number\_of\_messages]
```

## Parameters

## Example

```
wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMDeleteDurableMessages( ['-olderThan', '30', '-maximumDuration', '60', '-transactionSlice', '100' ] )
```