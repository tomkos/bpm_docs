<!-- image -->

# Versioning of human tasks

An example of early-binding
is an SCA wire. If you wire a stand-alone reference to a human task
component, every invocation of the task using this reference is targeted
to the specific version of the human task component.

- Currently valid tasks. These tasks are used for new task instances.
- Tasks that are no longer valid. These tasks are still used for
running task instances.
- Tasks
that become valid in the future according to their valid-from date.
These tasks apply only to tasks that were deployed using Integration Designer.

Follow-on tasks and subtasks are always invoked using late
binding.

- A human task must not be contained in a toolkit. A toolkit can
be deployed many times as part of different process applications.
If the toolkit contains a human task, this results in different human
tasks with the same name that are not versions of each other. Late
binding chooses the latest deployed version of the target human task
regardless of which process application it belongs to.
- Do not use the same name for a human task that is deployed as
part of a process application, and a human task that is not part of
a process application unless they are versions of each other.
- If a human task is part of a branch other than the main branch,
late binding chooses the latest deployed version of the target human
task regardless of which branch it belongs to.
- The human task names must be unique across all process applications.
If two human tasks in different process applications have the same
name, they are considered to be different versions of the same human
task. In this case, the version of the human task with the latest
timestamp is chosen as the target human task.

## Related concepts

- Types of human task
- Inline and stand-alone human tasks
- Task templates
- Task instances
- Human task clients
- Human task user interfaces
- To-do tasks and collaboration tasks with parallel ownership
- Lifecycle of a human task

## Related tasks

- Setting human task preferences
- Improving performance when using human task list widgets