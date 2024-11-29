# Deleting tasks from the Process database

## Before you begin

## About this task

The Cleanup Task utility enables administrators to easily
remove the following artifacts from the Process database:

- Tasks that users deleted from their task list
- Tasks that are in the DELETED, SENT, or CLOSED state
- For process instances from Business Automation Workflow releases
earlier than V8.5.5, attachments for deleted or orphaned tasks

As an alternative, you can choose to use the BPMTasksCleanup
command rather than the Cleanup Task utility. The command provides additional flexibility and is
described in the topic BPMTasksCleanup wsadmin command.

## Procedure

To use the Task Cleanup utility:

1. In the Server Admin area of the Process Admin Console,
click the indicator next to Business Automation Workflow Admin to
list the available administrative options.
2. Click the Task Cleanup option.
3. Select the option that you want.

Option
Description

Clean up tasks and their associated data that are marked
as DELETED.
This option removes tasks and attachments. For tasks to
be marked as deleted, the corresponding human service must contain
a modify task step. 

Clean up tasks and their associated data for tasks in the
DELETED, SENT, or CLOSED state.
This option removes tasks and attachments. Tasks are put
into the CLOSED state when either the work on the task or a modify
task step completes.
4. Under Current Counts, note how many
tasks and attachments currently exist in the database for the option
that you choose.
5. Click Cleanup.
6. Under After Cleanup Counts, you
can see how many tasks and attachments were deleted.