<!-- image -->

# State transition diagrams for invocation tasks

The person who creates and starts the invocation task becomes the
task originator. When the task is started, it automatically invokes
the service and waits for its result. When the service result is available,
the invocation task stores it and the originator can retrieve it as
long as the task exists.

<!-- image -->

After creation, the task reaches the inactive state. In this state,
you can update task properties, or set custom properties. To invoke
the service, the task must be started. It can be started by the originator
or one of the potential starters.

- The task can escalate if the service does not return in time.
It is put into the escalated substate, and it stays in this state
for the rest of the task lifecycle.
- The task can expire. This is a state change that ends the task.
- The task can be terminated manually using the terminate action.
This is a state change that ends the task.

The normal task flow is that the service returns with an output
or fault message. The task is then put into the finished state if
an output message is returned, or the failed state if a fault message
is returned. In both cases, the message is available to the task originator
and starter.

The failed, terminated, finished, and expired states are end states.
If the task template specifies automatic deletion, the task is either
deleted after the deletion timer expires, or it is deleted manually.
By default, invocation tasks are not automatically deleted so that
the result of the invoked service can be accessed.

A task in one of the end states can be restarted. The task is put
back into the running state. Escalations associated with the task
are canceled and the deletion timer is also canceled.

- If the BPEL process is started using the Business Flow Manager
API, or an SCA client, the task for the activity that creates the
process instance is created and started implicitly by the BPEL process.
Invocation tasks can also be used by process instances that are already
running. In this case they are created by the process and are associated
with a receive or pick (receive choice) activity, or an on-event event
handler.
- The task is represented in the BPEL process as a receive or pick
(receive choice) activity, or an on-event event handler. If an inline
invocation task is defined for an activity, it also defines the authorization
for this activity.
- If
invocation tasks are created and started by the BPEL process, their
lifecycle is determined by the process, and they are deleted with
the process. If they are started using the Human Task Manager API,
their lifecycle is independent of the process regardless of how they
were created, and their results can be displayed even after the process
is deleted.
- Regardless of how an inline invocation task is started, the due
time for it can be rescheduled.
- Inline
invocation tasks can be modeled with values for both the duration
until expiration and the duration until deletion. These settings are
available only if the tasks are created using the Human Task Manager
API. These durations can be updated before the task starts, and rescheduled
after the task has started.