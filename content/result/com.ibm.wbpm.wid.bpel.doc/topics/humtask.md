<!-- image -->

# Building human tasks

Use the human task editor to configure human tasks that can be
wired to other components within the IBM® Integration
Designer family
of tools.

Click any of the links shown below to learn more about that topic.

- Relationship between human tasks and BPEL processes

Inline tasks know the process they are related to, and the process knows about its inline tasks. With stand-alone to-do tasks this relationship can be defined with child autonomy. A child task that is directly instantiated by an invoke activity of a BPEL process, participates in the lifecycle of that BPEL process. That is, lifecycle operations, such as termination or deletion, are propagated from the BPEL process to its child tasks. When the activity expires, the to-do task is terminated.
- Human tasks

A human task is, quite simply, a unit of work that involves a human. Quite often, this task requires that the human interact with other services, and thus becomes a task within a larger business goal.
- Creating human tasks

To create a new human task, follow these instructions.
- Scenarios for invoking tasks

Tasks can be invoked in various ways.
- Authorization and people assignment for human tasks

Authorization is the mechanism by which certain people are enabled to perform selected actions on task templates, task instances, and escalations. Authorization roles are used to define sets of actions available to specific roles. People can be assigned to system-level roles using Java EE mechanisms, or to task instance roles using people assignment criteria.
- Setting duration values for your human task

You can set a duration value for your human task to specify how long the task will hold before it is either due, set to expire, or set to be deleted.
- Creating an escalation for your human task

An escalation is a notification that is sent out when an expected result from a task has not been achieved within a set period of time. For example, an escalation could be used to alert a manager when a staff member is unable to complete a task by the deadline.
- Selecting a calendar type for your escalation

Change the calendar type for an escalation by modifying the duration properties of the human task.
- Details tab: business state machine editor

This topic includes a description of each of the field on the Details tab of the Properties view.
- Duration tab: Human Task editor

This topic includes a description of each of the fields on the Duration tab of the Properties view. This tab is available when you select the task itself.
- Defining timer-driven behavior in a BPEL process

You can set timer values in a number of places in the business process editor, and for several different activities or elements. Timer values can be configured to trigger processing or expiration after a specific period of time has either elapsed or been reached.
- Using business calendars within human tasks

When it comes to modeling duration values for time-sensitive aspects of your human task, you can use a business calendar to account for such variables as regular working hours, weekends, and holidays.
- Notifying an event handler of an escalation

You can use customized notification event handlers within your application environment to deal with escalations in your human task model.
- Using custom properties for human tasks

Custom properties are used to categorize a task, and can be useful for querying, sorting, and filtering tasks.
- Escalations

An escalation is a course of action that is implemented when an expected result from a task has not been achieved within a set period of time.
- Creating subtasks

In the runtime environment, if a person who claims a task finds that they are not able to complete it by themselves, they can delegate portions of that original task to other people in the form of subtasks.
- Ad hoc collaboration

When you create or modify a task in the user interface of the runtime environment, you can dynamically define a task either as a subtask or a follow-on task.
- Transferring work items

In the runtime environment, if a person who has claimed a task finds that they are not able to complete it, they can transfer the work item to another person or group.
- Locked tasks

When a human task is imported from IBM WebSphere® Business Modeler some of the items in the editor will be locked. This locking is designed to ensure interoperability between IBM WebSphere Business Modeler and IBM Integration Designer. If you unlock and modify any of the locked items then your human task might no longer be synchronizable with IBM WebSphere Business Modeler exports. It is, therefore, recommended that you do not unlock items.
- Setting up a user interface for your human task

The human task editor provides various client types that you can use to customize a user interface through which users can interact with the tasks in the runtime environment.
- Testing human tasks

You can test several aspects of a human task before you deploy the task to the test environment or production server.
- Task tags

Use task tags in your project to make sure that important tasks are completed.
- Sticky notes

Sticky notes identify areas that serve as a reminder for a software task or human task in your project.
- Extending human tasks using plug-ins

Business Process Choreographer provides an event handling infrastructure for events that occur during the processing of human tasks. Plug-in points are also provided so that you can adapt the functionality to your needs. You can use the service provider interfaces (SPIs) to create customized plug-ins for handling events and the processing of staff queries.
- Limitations for human tasks

There are current limitations that you should be aware of when using the human task editor, or when working with human tasks.