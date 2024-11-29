<!-- image -->

# Inline tasks

Inline tasks have access to the process context, such as process
variables, custom properties, and activity data. This can be useful
for tasks that involve the separation of duties. Inline to-do tasks
can emit their CEI and audit log events as business process activity
events and human task events. Their subtasks and follow-on tasks emit
events as human task events.

- You need information from the process logic to run human interaction.
Although information from the process can also be modeled into the
input for a human task, the main reason to use an inline human tasks
is because they can have direct access to the process context without
the need to explicitly model the required information into the input
message. Configure this on the Details tab of the Properties view.
- You want to define authorization rights on specific activities

- To-do tasks are human task activities in a process. They share
the same state, but the human task activity does not reflect the forwarded
state or the task substates.
- Invocation tasks are associated with receive or pick (receive
choice) activities, or on-event event handlers.
- Administration tasks are attached either to the process, or to
an activity in the process.
- The lifecycle is usually determined by the process.
    - To-do tasks and administration tasks are created by the BPEL process,
and deleted with the process.
    - Inline to-do tasks do not have their own expiration, the expiration
is defined on the corresponding human task activity. When the human
task activity expires, the to-do task is terminated. Updating or rescheduling
of inline to-do tasks is supported by both the Human Task Manager
and Business Flow Manager APIs. If the Human Task Manager API is used,
the request is forwarded to the human task activity.
    - If
invocation tasks are created and started by the BPEL process, their
lifecycle is determined by the process, and they are deleted with
the process. If they are started using the Human Task Manager API,
their lifecycle is independent of the process regardless of how they
were created, and their results can be displayed even after the process
is deleted.
    - Instances of inline human tasks can be migrated with the process
instance they are related to.
- Inline
invocation tasks can be modeled with values for both the duration
until expiration and the duration until deletion. These settings are
available only if the tasks are created using the Human Task Manager
API. These durations can be updated before the task starts, and rescheduled
after the task has started.
- The update action on inline tasks supports only a subset of task
properties. Only task properties that have no representation in the
process or activity can be updated. For more information on the update method,
see the Javadoc API documentation for the HumanTaskManager interface
in the com.ibm.task.api package, and the information
on which roles are authorized to make specific update actions on tasks.

- The roles reader, administrator, potential owner, owner, and editor
of a to-do task are identical to the corresponding roles of the human
task activity in the process.
- The potential starter role of an inline invocation task determines
who is allowed to invoke and send messages to the corresponding receive
or pick (receive choice) activity, or on-event event handler. Note
that the potential starter and potential instance creator roles have
identical people assignments. If an inline invocation task is not
defined, everybody is authorized to start the activity or event handler.
- The administrator and reader roles for a process administration
task determine who is the process administrator or the process reader.
The process administrator can, for example, force terminate the process
instance.
- The administrator role for an activity administration task determines
who is allowed to administer the corresponding activity. The activity
administrator and the process administrator can, for example, force
retry the activity.
- The process reader and process administrator authorization are
inherited by every process activity or inline human task.
- The scope reader and the scope administrator authorization is
inherited by all of the activities in the scope.