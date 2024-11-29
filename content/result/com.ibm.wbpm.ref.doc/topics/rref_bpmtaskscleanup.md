# BPMTasksCleanup command

Sometimes long running process instances can build up
many completed task instances. The BPMTasksCleanup command
deletes these tasks to improve system performance. Deleting these
tasks also reduces the time that it takes to migrate process instances.

In
general, start by deleting completed system and decision tasks. Consider
deleting completed user tasks only if you need further performance
improvements because deleting user tasks before the process instance
completes could distort duration statistics for users who worked on
those tasks. If the process instance has completed, use the BPMProcessInstancesPurge command instead. The BPMProcessInstancesPurge command
deletes all tasks including user tasks. Another difference between BPMTasksCleanup and BPMProcessInstancesPurge is
that BPMTasksCleanup does not delete tasks from
the Process Portal index.
For information about the Process Portal index,
see Administering the Process Portal index.

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
BPMTasksCleanup 
[-containerAcronym container\_acronym]
[-containerSnapshotAcronym container\_snapshot\_acronym]
-taskStatus task\_status
[-processName process\_name]
[-taskType task\_types]
[-taskID task\_IDs]
[-endedAfterLocal local\_time\_on\_the\_server]
[-endedBeforeLocal local\_time\_on\_the\_server]
[-outputFile file\_path]
[-maximumDuration number\_of\_minutes]
[-transactionSlice number\_of\_tasks\_to\_delete\_in\_a\_transaction]
```

The
tasks that are deleted by this command conform to all of its parameters.
That is, if you provide a set of task IDs and set taskStatus to
CLOSED, the command deletes only the identified tasks if they are
closed. If they have a different status, the command does not delete
them.

## Parameters

- If you set this parameter, then you must also define
-containerSnapshotAcronym.
- If you do not include the taskID parameter, you must define this
parameter.

- If you set this parameter, then you must also define
-containerAcronym.
- If you do not include the taskID parameter, you must define this
parameter.
- If you want the command to operate on the current working version of a process application you
can specify the value Tip instead of specifying a snapshot acronym.

- CLOSED
- SENT
- ACTIONED
- ALERT
- ALL\_COMPLETED - Deletes all closed, sent, and
actioned tasks.

- SYSTEM\_TASK
- USER\_TASK Tip: In some scenarios,
deleting user tasks before the process completes might distort statistics
about the average duration that user worked on such tasks in the past.
- DECISION\_TASKTip: DECISION\_TASK is only applicable
to the decision task that has an implementation of a decision service. For the decision task with
service flow as the implementation, use SYSTEM\_TASK as the
taskType.
- ALL

## Examples

The following examples show how
to use the BPMTasksCleanup command.

- Deleting the closed tasks for all of the processes in snapshot
V1 of the PA435 process application:wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMTasksCleanup('[-containerAcronym PA435 -containerSnapshotAcronym V1 -taskStatus CLOSED -outputFile C:\US58626\log1.txt]')

- Deleting the specified tasks if they are complete:wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMTasksCleanup('[-taskStatus ALL\_COMPLETED -taskID [4 5 1001 1002]]')
- Deleting all tasks with CLOSED status before the specified date on the server in an allotted
time of 60 minutes. The increased transactionSlice helps performance but risks
that the command might run for longer than 60 minutes to complete its final
transaction:wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMTasksCleanup('[-containerAcronym PA435 -containerSnapshotAcronym V1 -taskStatus CLOSED -endedBeforeLocal 2014-01-02T21:37:06 -maximumDuration 60 -transactionSlice 200]')
- Deleting all completed tasks in a specified
process:wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMTasksCleanup('[-containerAcronym PA435 -containerSnapshotAcronym V1 -taskStatus ALL\_COMPLETED -processName billPaymentProcess]')