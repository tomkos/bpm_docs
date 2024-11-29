<!-- image -->

# Managing work authorizations and assignments

## About this task

A work item is the assignment
of a business entity, such as a task or a process instance, to a person
or a group of people for a particular reason. The assignment reason
allows a person to play various roles in the business process scenario,
for example, potential owner, editor, or administrator.

A task
instance or a process instance can have several work items associated
with it because different people can have different roles. For example,
John, Sarah, and Mike are all potential owners of a task instance
and Anne is the administrator; work items are generated for all four
people. John, Sarah, and Mike see only their own work items as tasks
on their list of tasks. Because Anne is the administrator, she gets
her own work item for the task and she can manage the work items generated
for John, Sarah, and Mike.

Sometimes, you might need to change
a task or process instance assignment after they are started, for
example, to transfer a work item from the original owner to someone
else. You might want to specify absence settings for the time you
are away. You might also need to create additional work items or delete
work items that are not needed anymore.

- Creating work items for BPEL processes using Business Process Choreographer Explorer

Work items of a process instance are used to manage administrator or reader authorization for the process instance. You might want to create process work items for new administrators, for example, when a user claims the ownership of a process instance because the user ID of the starter of the process instance will be deleted.
- Transferring BPEL process work items if you are the administrator of the process

You might need to change a work item assignment associated with a BPEL process. For example, you might want to transfer a process work item to another user because the ownership of the process instance needs to be claimed by another person. This might happen, for example, in a long-running process if the organization has changed since the process started.
- Claiming the ownership of BPEL process instances using Business Process Choreographer Explorer

You can transfer the ownership of a BPEL process instance by having a person with process administrator authorization take ownership of the process instance. You might want to do this, for example, in situations where the process starter is no longer with the company.
- Deleting work items for BPEL process using Business Process Choreographer Explorer

You might want to delete work items associated with a BPEL process, for example, if you created work items in error, or if they were generated for someone who no longer works for the company.
- Transferring tasks that you own

If you are the owner of a task, you might need to transfer the task to another user, for example, if someone else needs to provide information to complete the task.
- Transferring task work items if you are the starter, originator, or administrator of the task

You might need to change a task work assignment after work begins on the task. For example, you might want to transfer a task work item to another user if the task owner is on vacation and the task must be completed before this person returns. The way in which you can transfer a work item depends on the role that you have, the state of the task, and the role the new owners or groups have.
- Creating task work items

You might want to create task work items for new potential owners, for example, when none of the current potential owners can accept any additional work. You might also want to create task work items if the query against the people directory does not return any potential owners. This might happen, for example, in a long-running process if the organization has changed since the process started.
- Deleting task work items

You might want to delete task work items, for example, if you created task work items in error or if task work items are generated for someone who no longer works for the company.
- Specifying absence settings

If you intend to be away from the office for a certain time, specify a substitute for your tasks.
- Specifying absence settings for users

If users are prevented from working on their tasks, for example, if they are on sick leave, specify a substitute for the user's tasks.
- Shared people assignments

For a specific task role, the same people assignment criteria are used in all instances of a task template. This is because all of the task instances are instantiated from the same task template. To avoid rerunning people queries, the result of a query is shared across task instances of a task template.
- Optimizing people assignments for work baskets

If you have many tasks within a work basket and often update the people assignments for those tasks, you might get a runtime exception: WorkItem update in progress at the time of updating the assignments. You can avoid these runtime exceptions by enabling the optimized work item model.

<!-- image -->