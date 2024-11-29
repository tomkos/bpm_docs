# Replaying on-hold Event Manager tasks

## Using the Process Admin Console

1. Click Server Admin > IBM
BPM Admin > Health Management.
2. Select the command Replay Event Manager tasks.
3. Optionally specify values for the command's parameters to limit
which tasks are replayed.
4. Click Submit.
5. If there is an error, you will see the error message.
6. If there is no error, you see the results of the submitting the
replay command.

## Using a REST API call

Call the
BPM operations REST API POST https://host:port/ops/std/bpm/event\_manager\_tasks/replay.

- To replay all on-hold Event Manager tasks:POST https://host:port/ops/std/bpm/event\_manager\_tasks/replay
- To replay up to 100 on-hold Event Manager tasks for process instance
49:POST https://host:port/ops/std/bpm/event\_manager\_tasks/replay?max\_number=100&process\_id=49
- To replay specific on-hold Event Manager tasks :POST https://host:port/ops/std/bpm/event\_manager\_tasks/replay?em\_task\_ids=9,8,7

## Using a wsadmin command

To
replay on-hold Event Manager tasks, see BPMReplayOnHoldEMTasks command.