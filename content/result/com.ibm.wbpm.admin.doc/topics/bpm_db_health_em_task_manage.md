# Managing on-hold Event Manager tasks

The Event Manager schedules and drives the
execution of work in Workflow Server and Workflow Center. The
work includes invocation of undercover agents (UCAs), execution of
Business Process Definitions (BPDs), invocation of BPD system task
implementations, and invocation of BPD timer events. The scheduling
and driving of the work is accomplished with Event Manager tasks.

When an exception occurs, such as a queue-full condition of the
monitor event queue, re-execution of the tasks starts, which attempts
to overcome the exception. The re-execute-limit property that is specified
in the Event Manager configuration settings determines the number
of times to try again (set to 5 by default). After that limit is reached
for an Event Manager task, it is not tried again. Event Manager tasks
that fail and reach the re-execute-limit  are put on hold. The tasks
are retained in the database, but they are flagged to be on hold.

- Listing on-hold Event Manager tasks

You can use the a REST API call or a wsadmin command to list Event Manager tasks that are on hold.
- Replaying on-hold Event Manager tasks

You can use the Process Admin Console, a REST API call, or a wsadmin command to replay Event Manager tasks that are on hold.
- Deleting on-hold Event Manager tasks

To delete Event Manager tasks that are on hold, you can use the health management capability of the Process Admin Console, or a REST API call via the Swagger interface, or a wsadmin command.