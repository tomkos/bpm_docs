<!-- image -->

# Developing applications for BPEL processes and human tasks

## About this task

- An inline invocation task (also known as an originating
task in the API). You can provide an invocation task for
every receive activity, for each onMessage element of a pick activity,
and for each onEvent element of an event handler. This task then controls
who is authorized to start a process or communicate with a running
process instance.
- An administration task. You can provide an administration task
to specify who is authorized to administer the process or perform
administrative operations on the failed activities of the process.
- A to-do task (also known as a participating task in
the API).A to-do task implements a human task activity. This type
of activity allows you to involve people in the process.

- The business process is the container for all of the activities
that belong to the process, including the human task activities that
are represented by to-do tasks. When a process instance is created,
a unique object ID (PIID) is assigned.
- When a human task activity is activated during the execution ofthe process instance, an activity instance is created, which is identifiedby its unique object ID (AIID). At the same time, an inline to-dotask instance is also created, which is identified by its object ID(TKIID). The relationship of the human task activity to the task instanceis achieved by using the object IDs:
    - The to-do task ID of the activity instance is set to the TKIID
of the associated to-do task.
    - The containment context ID of the task instance is set to the
PIID of the process instance that contains the associated activity
instance.
    - The parent context ID of the task instance is set to the AIID
of the associated activity instance.
- The lifecycles of all inline to-do task instances are managed
by the process instance. When the process instance is deleted, then
the task instances are also deleted. For example, all
of the tasks that have the containment context ID set to the PIID
of the process instance are automatically deleted.

- Determining the BPEL process templates or activities that can be started

A BPEL process can be started by invoking the call, initiate, or sendMessage methods of the Business Flow Manager API. If the process has only one starting activity, you can use the method signature that requires a process template name as a parameter. If the process has more than one starting activity, you must explicitly identify the starting activity.
- Processing a page flow that is started by a to-do task

Some workflows are performed by only one person, for example, ordering books from an online bookstore. This example shows how to use both the Business Flow Manager and the Human Task Manager APIs are to process this type of workflow.