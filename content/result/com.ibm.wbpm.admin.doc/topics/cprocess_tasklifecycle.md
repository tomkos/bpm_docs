<!-- image -->

# Lifecycle of stand-alone human tasks that are invoked
by a BPEL process

For reuse, it often makes sense to implement a step of the business
logic as a separate stand-alone task and to invoke this task from
different locations in the main process. When these applications are
deployed, the stand-alone task must be deployed to the same Business
Process Choreographer database.

A stand-alone to-do task can have a peer-to-peer relationship or
a parent-child relationship with the calling process. This relationship
determines how the lifecycle of the invoked task is managed.

- Restarting an invoke activity causes the current task instance
to be deleted, and a new task instance to be created and started.
- Forcing completion of the invoke activity causes the task instance
to be terminated.
- Skipping the invoke activity in the running state causes the task
instance to be terminated.
- Deleting or terminating the invoke activity causes the task instance
to be deleted.

If the autonomy attribute of the task is set to child,
you can still suspend and resume the task instance independently of
the BPEL process.

A parent-child relationship can be established only between
processes and tasks that interact directly. If another SCA component
intercepts this interaction, it might prevent a parent-child relationship
from being established, for example, an interface map component that
is wired between the process and the task.

<!-- image -->