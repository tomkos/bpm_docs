<!-- image -->

# Human tasks

The IBM® Integration
Designer tools
have been designed so that users can easily compose integrative business
solutions without programming skills. To this end, you can easily
define a human task in an intuitive graphical programming environment
called the human task editor.

- An example of a human task
- Assigning people to the task
- Presenting a task to a staff member
- Escalations
- Collaborating with other staff members in a human task

## An example of a human task

<!-- image -->

- who can do the task (roles/people assignment criteria)
- what needs to be done (name)
- what happens when the task takes too long (escalation)
- how the task will be done (input and output data)

## Assigning people to the task

When
you create a human task an important step is to define which people
can work on this task. You define who is eligible to perform the work
using roles and people assignment criteria.

You specify who can work on a task by assigning
a role to the task and by ensuring that the membership of that role
is set to the right group of people.

## Presenting a task to a staff member

When
a human task is started, the staff member interacts with the task
through a user interface in a client environment.

<!-- image -->

In
this modified example, we see that all interaction between the user
and the task is facilitated by a client. The task is delivered to
the user through the client, and the resolution is returned in similar
means.

So far, both examples have shown what happens when the
task can be completed without a problem. What happens when that is
not possible?

## Escalations

<!-- image -->

In this example, we see that the staff member who
claims the task isn't able to complete it in the specified period
of time, and another staff member is alerted. Presumably, this second
employee has the authority to investigate the reasons behind why the
task wasn't completed and proceed accordingly.

## Collaborating with other staff members
in a human task

Ad hoc tasks and transferred work items
are created on-the-fly in the runtime environment, usually
because the situation that has created the need for a task did not
exist when the application was initially developed. You can create
such tasks either from existing task definitions (collaboration and
invocation tasks) or without any existing definition.

You can
use IBM Integration
Designer to
create two types of ad hoc tasks: the subtask and the follow-on task.
Definitions of these ad hoc tasks and transferred work items are given
below.

## Single and parallel ownership of human
tasks

When you create a human task you can choose between single and parallel ownership.
A parallel ownership task (or simply a parallel task) is one
in which multiple people can work on a task at the same moment. Single
ownership means that only one person can work on a task. The first
potential owner to claim a task becomes solely responsible for that
task.

You can use IBM Integration
Designer to
create single and parallel tasks, or to convert a task from one to
the other. Definitions of these concepts are given below.

- Types of human task

There are four types of human tasks that you can define.
- Inline and stand-alone human tasks

You can implement a human task as part of the logic of a BPEL process, or independently of other processes.
- Task templates

A human task template contains the definition of a deployed task model that was created using Integration Designer, or at run time using the Business Process Choreographer APIs.
- Task instances

A task instance is a runtime occurrence of a task template.
- Human task clients

A human task client is a piece of software that provides an interactive link between a human task and the staff member assigned to work upon the task.
- Human task user interfaces

The user interface of a human task is the means by which a staff member interacts with a human task in the runtime environment.
- Versioning of human tasks

You can create new versions of your human task, so that multiple versions of the same task can co-exist in a runtime environment.
- To-do tasks and collaboration tasks with parallel ownership

Tasks with parallel ownership allow potential owners to work simultaneously on the task. A common example of parallel ownership is when a set of potential owners need to approve a to-do task in a BPEL process. Parallel ownership can be specified for to-do tasks and collaboration tasks.
- Using human tasks in different scenarios in IBM WebSphere® Integration Developer
- Lifecycle of a human task

A human task goes through a number of stages from its start to its finish.
- Setting human task preferences

You can set warnings, change the people directory, and modify assignment criteria settings.
- Improving performance when using human task list widgets

You can improve process performance when you add a federation service layer.