<!-- image -->

# Developing applications for human tasks

## About this task

For more information on the Human Task Manager
API, see the Javadoc in the com.ibm.task.api package.

- Starting an invocation task that invokes a synchronous interface

An invocation task is associated with a Service Component Architecture (SCA) component. When the task is started, it invokes the SCA component. Start an invocation task synchronously only if the associated SCA component can be called synchronously.
- Starting an invocation task that invokes an asynchronous interface

An invocation task is associated with a Service Component Architecture (SCA) component. When the task is started, it invokes the SCA component. Start an invocation task asynchronously only if the associated SCA component can be called asynchronously.
- Creating and starting a task instance

This scenario shows how to create an instance of a task template that defines a collaboration task (also known as a human task in the API) and start the task instance.
- Processing to-do tasks or collaboration tasks

To-do tasks (also known as participating tasks in the API) or collaboration tasks (also known as human tasks in the API) are assigned to various people in your organization through work items. To-do tasks and their associated work items are created, for example, when a process navigates to a human task activity.
- Suspending and resuming a task instance

You can suspend collaboration task instances (also known as human tasks in the API) or to-do task instances (also known as participating tasks in the API).
- Analyzing the results of a task

A to-do task (also known as a participating task in the API) or a collaboration task (also known as a human task in the API) runs asynchronously. If a reply handler is specified when the task starts, the output message is automatically returned when the task completes. If a reply handler is not specified, the message must be retrieved explicitly.
- Terminating a task instance

Sometimes it is necessary for someone with administrator rights to terminate a task instance that is known to be in an unrecoverable state. Because the task instance is terminated immediately, you should terminate a task instance only in exceptional situations.
- Deleting task instances

Task instances are only automatically deleted when they complete if this is specified in the associated task template from which the instances are derived. This example shows how to delete all of the task instances that are finished and are not automatically deleted.
- Releasing a claimed task

When a potential owner claims a task, this person is responsible for completing the task. However, sometimes the claimed task must be released so that another potential owner can claim it.
- Managing work items

During the lifetime of an activity instance or a task instance, the set of people associated with the object can change, for example, because a person is on vacation, new people are hired, or the workload needs to be distributed differently. To allow for these changes, you can develop applications to create, delete, or transfer work items.
- Creating task templates and task instances at run time

You normally use a modeling tool, such as IBM® Integration Designer to build task templates. You then install the task templates in IBM Business Automation Workflow and create instances from these templates, for example, using Business Process Choreographer Explorer. However, you can also create human or participating task instances or templates at run time.
- HumanTaskManagerService interface

The HumanTaskManagerService interface exposes task-related functions that can be called by a local or a remote client.