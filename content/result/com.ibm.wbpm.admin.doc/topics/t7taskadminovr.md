<!-- image -->

# Managing the lifecycle of human tasks and task instances

- Lifecycle of human tasks

Human tasks support people when they interact with web services or BPEL processes. The interactions that can take place over the lifetime of a task depend on whether the task is a to-do task, a collaboration task, an invocation task, or an administration task. Certain interactions are possible only in certain task states, and these interactions, in turn, influence the state of the human task.
- Creating and starting a task instance

You can create and start a task instance from any of the task templates that you are authorized to use.
- Working on your tasks

To work on a task, you must claim the task and then perform the actions that are needed to complete it.
- Suspending and resuming task instances using Business Process Choreographer Explorer

You can suspend task instances using Business Process Choreographer Explorer. You might want to do this, for example, to fix a problem that is causing the task instance to fail. When the prerequisites for the task are met, you can resume running the task instance.
- Restarting task instances using Business Process Choreographer Explorer

You can restart task instances using Business Process Choreographer Explorer. You might want to do this, for example, for a human task that is already running but not progressing as expected, or for a task that has reached an unexpected or undesired end state, such as failed or expired.
- Rescheduling task instances

You can reschedule task instances using new date and time data in Business Process Choreographer Explorer.
- Managing priorities of human tasks in Business Process Choreographer Explorer

You can use the priorities of human tasks to filter for tasks, and to sort your list of tasks.
- Lifecycle of subtasks

Subtasks support people when they need to delegate parts of their assigned work to other people, but want to keep control over the overall result. They can also be used to invoke supporting services to help people accomplish the tasks that they are working on.
- Lifecycle of follow-on tasks

Follow-on tasks support people when they want to delegate parts of their assigned work to other people, and the control over the completion of the work.
- Lifecycle of escalations

An escalation is an alert that is raised automatically when a human task is not actioned in the specified amount of time. For example, if tasks are not claimed or are not completed within a defined time limit. You can specify one, or more, escalations for a task. These escalations can be started either in parallel, or as a chain of escalations.
- Modification of task instance properties at run time

At run time, the properties of a task instance, such as its name, who can work on the task, and its duration settings are copied from its template. Typically, a task instance keeps the predefined values of these properties throughout its lifecycle. However, sometimes you might need to override these predefined values at run time in response to your business needs.

<!-- image -->