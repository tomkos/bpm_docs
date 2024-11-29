# Maintaining and monitoring IBM Business Automation Workflow Event
Manager

The Event Manager is the component of the Workflow Server that handles
event scheduling and queuing. For example, when an event is received
by Workflow Server,
that event is translated to a job in the Event Manager. Each job in
the Event Manager is routed through a Scheduler, which schedules and
tracks the execution of its assigned jobs.

| For...                                                                                          | Event Manager...                                                                                                              |
|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Incoming message events from external applications                                              | Queues incoming messages and then kicks off the appropriate UCA.                                                              |
| Schedules set in UCAs                                                                           | Looks to find the next UCA to run, calculates the time until the next UCA is due to run, and is dormant for the time between. |
| Incoming subscription events from external ECM systems (through the RESTFul API send ECM event) | Queues an asynchronous message and initiates the appropriate event subscription and attached service.                         |

<!-- image -->

The scheduling and driving of the work is accomplished with Event
Manager tasks. When an exception occurs, such as a queue-full condition
of the monitor event queue, a re-execution of the particular tasks
is triggered, which attempts to overcome the exception. The re-execute-limit
property that is specified in the Event Manager configuration settings
determines the number of times to try again (set to 5 by default).
After that limit is reached for an Event Manager task, it is not tried
again. Event Manager tasks that fail and reach the re-execute-limit
are put on hold. The tasks are retained in the database, but they
are flagged to be on hold and are only rescheduled when the BPMReplayOnHoldEMTasks command
is run. If an Event Manager task is put on hold, the failure indicates
a possible infrastructure problem. Either a resource is temporarily
unavailable or the system configuration has an issue (for example,
not enough connections). If an Event Manager task is put on hold,
the process instance might stop responding.

- Monitoring the Event Manager

The Event Manager monitor in the Process Admin Console displays information about the Scheduler for the Event Manager on your Workflow Center server or Workflow Server and about the various jobs being tracked by that Scheduler.
- Creating and maintaining blackout periods

Administrators should establish blackout periods to specify times when events cannot be scheduled, for example, due to a public holiday or when regular system maintenance is scheduled. The Event Manager takes blackout periods into account when scheduling and queuing events, event subscriptions, and undercover agents (UCAs).
- Creating and maintaining execution queues

Event Manager jobs are scheduled to be processed by an execution queue. (If you look at the job listing in the Event Manager monitor, you can see that each job is assigned to a job queue.)
- Event Manager configuration settings

To understand how the IBM Business Automation Workflow Event Manager works, review the configuration properties.
- Managing on-hold Event Manager tasks

You can list, replay, and delete on-hold Event Manager tasks by using either REST API calls or administrative commands.
- Tuning databases for the Event Manager

If the IBM Business Automation Workflow Event Manager has poor performance, you can tune the databases by updating optimizer statistics, reorganizing the tables and indexes, providing your database system with a better index, or, on Oracle databases, reducing the contention.