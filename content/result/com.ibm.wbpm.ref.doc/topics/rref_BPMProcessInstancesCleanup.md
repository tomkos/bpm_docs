# BPMProcessInstancesCleanup command (deprecated)

Using this command deletes the BPD instance and its associated
tasks and documents for the instances that are specified by the command
parameters. It also logs data to a standard SystemOut.log file
to track which process applications were selected for deleting instance
data and associated documents.

## Prerequisites

- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- You cannot use this command to delete messages for
BPEL processes.
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
BPMProcessInstancesCleanup 
-containerAcronym process\_application\_acronym
-containerSnapshotAcronym process\_application\_snapshot\_acronym
-instanceStatus instance\_status 
[-endedAfterLocal local\_time\_on\_the\_server]
[-endedBeforeLocal local\_time\_on\_the\_server]
[-instanceID instance\_IDs]
[-maximumDuration number\_of\_minutes]
[-outputFile file\_path]
[-transactionSlice number\_of\_instances\_to\_delete\_in\_a\_transaction]
```

## Parameters

- COMPLETED - Removes all completed process instances
- FAILED - Removes all failed process instances
- CANCELED - Removes all terminated process instances
- ALL - Removes all completed, failed, and canceled process instances

You should check the SystemOut.log file
for exceptions if the cleanup service adjusted your transactionSlice.
Adjusting the number of instances to be deleted in a transaction can
improve the cleanup operation time.

## Examples

The following examples show how
to use the BPMProcessInstancesCleanup command.

- Deleting the BPD instance and its associated tasks for the instances
wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMProcessInstancesCleanup('[-containerAcronym PA435 -containerSnapshotAcronym V1 -instanceStatus FAILED -outputFile C:\US58626\log1.txt]')

- Deleting instances based that are based on instance IDs wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMProcessInstancesCleanup('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -instanceStatus ALL -instanceID [4 5 1001 1002]]')
- Deleting instances that occur during a time range that falls within
a specific rangewsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMProcessInstancesCleanup('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -instanceStatus ALL -endedAfterLocal 2012-01-01T00:00:00 -endedBeforeLocal 2012-02-31T21:37:06]')
- Deleting instances that occur before the specified local time
on the server 
wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMProcessInstancesCleanup('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -instanceStatus ALL -endedBeforeLocal 2012-01-02T21:37:06]') 

wsadmin>AdminTask.BPMProcessInstancesCleanup('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -instanceStatus ALL -endedBeforeLocal 2012-05-02]')
- Deleting instances that occur after the specified local time on
the server
wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMProcessInstancesCleanup('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -instanceStatus ALL -endedAfterLocal 2012-05-31T21:38:00]') 

wsadmin>AdminTask.BPMProcessInstancesCleanup('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -instanceStatus ALL -endedAfterLocal 2012-07-31]')
- Deleting specific instances that occur on a specific time range
and are based on instance IDswsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMProcessInstancesCleanup('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -instanceStatus ALL -endedAfterLocal 2012-01-01T00:00:00 -endedBeforeLocal 2012-02-31T21:37:06 -instanceID [53 54 55]]')
- Deleting instances that occur before and after the specified local
time on the server and are based on instance IDs wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMProcessInstancesCleanup('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -instanceStatus ALL -endedAfterLocal 2012-05-20T00:00:00 -instanceID [53 54 55 56 57 58]]') 

wsadmin>AdminTask.BPMProcessInstancesCleanup('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -instanceStatus ALL -endedBeforeLocal 2012-05-31T21:37:06 -instanceID [53 54 55 56 57 58]]')