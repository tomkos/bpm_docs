# Listing on-hold Event Manager tasks

## Using the Process Admin Console

1. Click Server Admin > IBM
BPM Admin > Health Management.
2. Select the command List Event Manager tasks.
3. Specify values for the command's parameters.
4. Click Submit.
5. If there is an error, you will see the error message.
6. If there is no error, you see the tasks that match the specified
parameters.

## Using a REST API call

Call the
BPM operations REST API GET https://host:port/ops/std/bpm/event\_manager\_tasks.

- To list all on-hold Event Manager tasks:GET https://host:port/ops/std/bpm/event\_manager\_tasks?states=on\_hold
- To list all on-hold Event Manager tasks for the process instance
ID 5:GET https://host:port/ops/std/bpm/event\_manager\_tasks?process\_id=5&states=on\_hold
- To list the first 20 on-hold Event Manager tasks:GET https://host:port/ops/std/bpm/event\_manager\_tasks?size=20&states=on\_hold
- To list the second 20 on-hold Event Manager tasks:GET https://host:port/ops/std/bpm/event\_manager\_tasks?size=20&offset=20&states=on\_hold

## Using a wsadmin command

To
list on-hold Event Manager tasks, see BPMListOnHoldEMTasks command.