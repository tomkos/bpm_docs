# Creating and maintaining execution queues

## Before you begin

## About this task

| Execution queue    | Description                                             |
|--------------------|---------------------------------------------------------|
| Asynchronous queue | Allows jobs to run at the same time.                    |
| Synchronous queue  | Forces one job to finish before the next job can start. |

Event subscriptions can only use asynchronous
queues.

Administrators can create multiple synchronous
execution queues to handle Event Manager jobs. When multiple queues
are available, developers who create events and corresponding undercover
agents (UCAs) can specify the queue in which they want their event
to run. You may want to create separate synchronous queues so that
certain types of events can all be routed to a separate queue and
processed sequentially.

## Procedure

To create, modify, or delete a synchronous queue:

- To create a synchronous queue: The new queue is now included in the Synchronous Queueslist.
    1. In the Server Admin area of the Process Admin Console,
click the indicator next to Event Manager to
list the available management options.
    2. Click the Synchronous Queues option.
    3. Enter a name for the new queue in the Description text
box.
    4. Click the Add button.
- To modify the name of a synchronous queue: Important: When you change the name of a synchronousqueue, be sure to inform developers and other members of your teamwho may be specifying that queue to process their events. The queue is included with the new name in the SynchronousQueues list.

1. In the Server Admin area of the Process Admin Console,
click the indicator next to Event Manager to
list the available management options.
2. Click the Synchronous Queues option.
3. Select the queue that you want to change from the Synchronous
Queues list.
4. Change the name in the Description text
box.
5. Click the Update button.
- To delete a synchronous queue: Important: When you delete a synchronous queue,be sure to inform developers and other members of your team who maybe specifying that queue to process their events. The queue is no longer included in the Synchronous Queueslist.

1. In the Server Admin area of the Process Admin Console,
click the indicator next to Event Manager to
list the available management options.
2. Click the Synchronous Queues option.
3. Select the queue that you want to delete from the Synchronous
Queues list.
4. Click the Delete button.