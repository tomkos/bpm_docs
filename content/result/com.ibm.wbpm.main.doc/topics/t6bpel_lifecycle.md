<!-- image -->

# Managing the lifecycle of a BPEL process

## About this task

Examples are provided that show how you might develop
applications for the following typical lifecycle actions on processes.

- Starting BPEL processes

The way in which a BPEL process is started depends on whether the process is a microflow or a long-running process. The service that starts the process is also important to the way in which a process is started; the process can have either a unique starting service or several starting services.
- Suspending and resuming a BPEL process

You can suspend long-running, top-level process instance while it is running and resume it again to complete it.
- Restarting a BPEL process

You can restart a process instance that is in the finished, terminated, failed, or compensated state.
- Terminating a process instance

Sometimes, a top-level process instance that in an unrecoverable state must be terminated.
- Deleting process instances

Completed process instances are automatically deleted from the Business Process Choreographer database if the corresponding property is set for the process template in the process model. You might want to keep process instances in your database, for example, to query data from process instances that are not written to the audit log. However, stored process instance data does not only impact disk space and performance but also prevents process instances that use the same correlation set values from being created. Therefore, you should regularly delete process instance data from the database.