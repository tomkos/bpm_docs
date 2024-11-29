# BPMDeleteOnHoldEMTasks command

The Event Manager schedules and
drives the execution of work in the Workflow Server and Workflow Center. The
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
that fail and reach the re-execute-limit are put on hold. Such tasks
are retained in the database, but they are flagged to be on hold and
rescheduled to be run in the future by using the BPMReplayOnHoldEMTasks command
or deleted by using the BPMDeleteOnHoldEMTasks command.

For
information about listing and replaying on-hold Event Manager tasks,
see BPMListOnHoldEMTasks command and BPMReplayOnHoldEMTasks command.

For example, when
monitoring is enabled and the Workflow Server produces
more monitor events than can be processed fast enough, the queue fills
up and results in a queue full condition. The BPD transactions that
attempt to emit the monitor events fail and are rolled back. Affected
Event Manager tasks are tried again until reaching the re-execute-limit
of the Event Manager and any Event Manager tasks that were tried until
reaching the re-execute-limit are flagged as on hold.

The BPMDeleteOnHoldEMTasks command
is run using the AdminTask object of the wsadmin scripting client.

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
BPMDeleteOnHoldEMTasks
[-all]
[-ids task\_id\_list]
```

## Parameters

You must provide one of the following
parameters:

## Example

```
wsadmin>print AdminTask.BPMDeleteOnHoldEMTasks(['-all'])
```

Example
of output:

The BPMDeleteOnHoldEMTasks command
deleted 11 on-hold Event Manager Tasks.

```
wsadmin>print AdminTask.BPMDeleteOnHoldEMTasks(['-ids', ['9', '8', '7']])
```

Example of output:

```
The BPMDeleteOnHoldEMTasks command deleted 1 on-hold Event Manager Task.
The following Event Manager Task(s) could not be deleted because they do not exist: 8.
The following Event Manager Task(s) could not be deleted because they are not on-hold: 7.
```