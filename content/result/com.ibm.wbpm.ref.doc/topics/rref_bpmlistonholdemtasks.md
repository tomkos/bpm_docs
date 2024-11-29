# BPMListOnHoldEMTasks command

The
Event Manager schedules and drives the execution of work in the Workflow Server and Workflow Center. The
work includes invocation of undercover agents (UCAs), execution of
Business Process Definitions (BPDs), invocation of BPD system task
implementations, and invocation of BPD timer events. The scheduling
and driving of the work is accomplished with Event Manager tasks.
When an exception occurs, such as a queue-full condition of the monitor
event queue, re-execution of the tasks starts, which attempts to overcome
the exception. The re-execute-limit property that is specified in
the Event Manager configuration settings determines the number of
times to try again (set to 5 by default). After that limit is reached
for an Event Manager task, it is not tried again. To prevent a situation
where reaching the limit result in a BPD instance that is not continuing
its navigation anymore, and it stops responding, Event Manager tasks
that fail and reach the re-execute-limit  are put on hold. The tasks
are retained in the database, but they are flagged to be on hold and
rescheduled to be run in the future by using the BPMReplayOnHoldEMTasks command
is run or deleted by using the BPMDeleteOnHoldEMTasks command.

For
information about replaying and deleting on-hold Event Manager tasks,
see BPMReplayOnHoldEMTasks command and BPMDeleteOnHoldEMTasks command.

## Prerequisites

- In a network deployment environment, you must run this command
on the node that contains the application cluster member that handles
the Workflow Server or Workflow Center applications.
Do not run this command from the deployment manager profile.
- You can run the command from any cluster member in a network deployment
environment. However, you must first establish the wsadmin session
to the SOAP port of the cluster member from where you are running
the command.
- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- To access the wsadmin command or MBean operation,
the ID being used must have a WebSphere® Application
Server operator
role. See Administrative roles for information about
roles.
- To access the wsadmin command or MBean
operation, the ID being used must belong to either the bpmAdminGroup
or (for Workflow Center)
the bpmAuthorGroup. The default name for the bpmAdminGroup is tw\_admins
and the default name for the bpmAuthorGroup is tw\_authors. See IBM Business Automation Workflow default group types for information about groups.Tip: By default, only the DeAdmin user has both the WebSphere Application
Server administrator
role and membership in the bpmAdminGroup.

## Location

Start the command from the profile\_root/bin directory
of the application cluster member to which you want to connect. The
application cluster can be on a Workflow Center or
a Workflow Server node.

Logs
created during processing of the command are in the SystemOut.log file
of the cluster member that you connected to.

## Syntax

```
BPMListOnHoldEMTasks
[-bpdInstanceId instance\_id]
[-offset number\_of\_tasks]
[-size number\_of\_tasks]
```

## Parameters

## Example

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython
wsadmin>print AdminTask.BPMListOnHoldEMTasks ()
Task 17 from the 'Async Queue' queue: 'Run the 'UCA that starts a BPD' UCA, triggered by message event or Invoke UCA step'.
Task 18 from the 'BPD Queue' queue: 'Notify process instance 5 to continue processing'.
```

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython
wsadmin>print AdminTask.BPMListOnHoldEMTasks(['-bpdInstanceId', '5'])
Task 18 from the 'BPD Queue' queue: 'Notify process instance 5 to continue processing'.
```