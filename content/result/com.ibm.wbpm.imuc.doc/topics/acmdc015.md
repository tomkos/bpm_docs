# Queue permissions

For each role in a solution, one work queue is created. In addition
to work queues, there is an Inbox queue which holds work items assigned
to users. Case Client users
see in-baskets that represent a view into the queue. In-baskets do
not need an additional security setting, as only the queues behind
the in-baskets are configured for security.

| Permission   | Access rights                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Query        | View work items. If no user or group is assigned, any user can view items in the queue.                                                                                                                                                                                                                                                                                                                      |
| Process      | Lock, modify, save, and complete work items. If no user or group is assigned, any user can process items in the queue. Process permission applies to the queue in which the work item is locked, rather than to the destination queue. The destination queue is the queue to which the work item is dispatched upon completion of the step. The destination queue is under system control, not user control. |

In addition to case workers, any user who must assign or reassign
work must also be given Query and Process rights.

The Inbox queue does not usually need extra security because all
users access the queue, but the system will filter and return only
the work items for the current user automatically. You can also limit
access to the Inbox queue to only case workers who process work items
for the solution.