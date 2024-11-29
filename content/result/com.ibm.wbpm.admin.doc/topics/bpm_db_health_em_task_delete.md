# Deleting on-hold Event Manager tasks

To delete Event Manager tasks that are on hold, you can use the health management
capability of the Process Admin Console, or a REST API call via the Swagger interface, or a wsadmin
command.

## Using the Process Admin Console

1. Click Server Admin > IBM
BPM Admin > Health Management.
2. Select the command Delete Event Manager tasks.
3. Either specify to delete all tasks or a list of IDs of tasks to
delete.
4. Click Submit.
5. If there is an error, you will see the error message.
6. If there is no error, you see the results of the deletion.

## Using a REST API call

Call the
BPM operations REST API DELETE https://host:port/ops/std/bpm/event\_manager\_tasks.

- To delete all on-hold Event Manager tasks:DELETE https://host:port/ops/std/bpm/event\_manager\_tasks?all=true
- To delete specific on-hold Event Manager tasks :DELETE https://host:port/ops/std/bpm/event\_manager\_tasks?em\_task\_ids=9,8,7

## Using a wsadmin command

To
delete on-hold Event Manager tasks, see BPMDeleteOnHoldEMTasks command.