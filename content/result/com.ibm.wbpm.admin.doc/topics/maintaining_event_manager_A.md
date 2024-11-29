# Monitoring the Event Manager

## Before you begin

You must log in to the Process Admin Console.

## About this task

When you access the Event Manager monitor, you can see
the status for each scheduled job. In a clustered environment, the
monitor displays all Schedulers in the cluster and the jobs for all
Schedulers in the cluster.

## Procedure

To use the Event Manager monitor:

1. In the Server Admin area of the Process Admin Console,
click the indicator next to Event Manager to
list the available management options.
2. Click the Monitor option.
The monitor displays the ID and status for each Scheduler
and also displays all currently scheduled jobs.
3. Click Pause or Pause
All to pause a selected Scheduler or all Schedulers.
If you pause a Scheduler, any executing jobs are completed before
processing is halted.
4. Click Resume or Resume
All to resume processing of the selected Scheduler or
all Schedulers.
5. Examine the list of jobs to determine which events are
scheduled and when they should run. This list can help
you troubleshoot issues with your processes. For
example, if an undercover agent (UCA) is supposed to start a process
automatically at a certain time and you notice that the process is
not running, you can examine the list of jobs to determine if the
UCA was scheduled. If not, you know there could be an issue with the Workflow Server receiving the
event. If the UCA is scheduled, but never runs, you can check the
implementation of the UCA in the Designer to understand why it fails
to run.
6. Click the Refresh button to ensure
you are viewing the most recent data available.

## What to do next

The Event Manager monitor does not show historical information
about UCAs that were successfully run, but you can capture this type
of information in the SystemOut.log file as long
as the log details level for the WLE.wle\_uca exception
component is set to the following default value:

*=info

## Related information

- Log and trace settings