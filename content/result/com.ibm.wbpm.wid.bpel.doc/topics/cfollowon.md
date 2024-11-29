<!-- image -->

# Follow-on tasks

Follow-on tasks can be created from stand-alone task templates
that are stored in the Business Process Choreographer database, from
task templates created at run time, or by providing a new task model
at run time. You can start a follow-on task from a to-do task or a
collaboration task that has the supportsFollowOnTask attribute
set to true. A follow-on task can have follow-on
tasks of its own resulting in a chain of tasks.

The input message type of a follow-on task can be different from
its predecessor task. If the input message type of the follow-on task
is the same as that of the predecessor task, the input message content
of the predecessor task is passed automatically to the follow-on task.
The message content can be overwritten when the follow-on task is
created or started.

For a chain of follow-on tasks, the output and fault message types
of each of the follow-on tasks must be identical to those of the first
task in the chain, because the last follow-on task in the chain returns
the message to the calling component or person (originator). The output
or fault message content of the parent task is always copied to the
output or fault message of the follow-on task. These messages can
be modified in the follow-on task and the changes are copied to the
parent task.

## Authorization considerations

- The readers, editors, originator, potential owners, and owner
of the predecessor task become readers of the follow-on task and its
escalations
- Administrators of the predecessor task become administrators of
the follow-on task and its escalations

- Creating follow-on tasks

In the runtime environment, if a person who claims a task finds that they are not able to complete it, they can assign the remaining work to somebody else in the form of a follow-on task.