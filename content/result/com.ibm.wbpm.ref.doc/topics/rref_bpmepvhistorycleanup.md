# BPMEPVHistoryCleanup command

The BPMEPVHistoryCleanup command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- You can run the command from any cluster member in a network deployment
environment. However, you must first establish the wsadmin session
to the SOAP port of the cluster member from where you are running
the command.
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

Start the command from the install\_root/bin directory.

## Syntax

```
BPMEPVHistoryCleanup
[-containerAcronym process\_application\_acronym]
[-containerSnapshotAcronym process\_application\_snapshot\_acronym]
[-transactionSlice number\_of\_EPV\_values\_to\_delete\_in\_a\_transaction]
[-displayEPVCleanUpStatus true | false]
```

## Parameters

## Examples

- Deleting the complete EPV history of all snapshots of all process
applications.wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMEPVHistoryCleanup()
- Deleting the complete EPV history of a particular snapshots of
 a specific process application using the default transaction slice
of 1000.wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMEPVHistoryCleanup('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1]')
- Deleting the EPV history of all snapshots of a particular process
application and using a transaction slice of 10000.wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMEPVHistoryCleanup('[-containerAcronym BILLDISP -transactionSlice 10000]')