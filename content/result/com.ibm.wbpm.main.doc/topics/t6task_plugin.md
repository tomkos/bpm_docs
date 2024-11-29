<!-- image -->

# Creating plug-ins to customize human task functionality

## About this task

You can create plug-ins for human task API events and
escalation notification events. You can also create a plug-in that processes
the results that are returned from people resolution. For example, at peak
periods you might want to add users to the result list to help balance the
workload.

Before you can use the plug-ins, you must install and register
them. You can register the plug-in to post process people query results with
the TaskContainer application. The plug-in is then available for all tasks.

- Creating API event handlers for Business Process Choreographer

An API event occurs when an API method manipulates a human task. Use the API event handler plug-in service provider interface (SPI) to create plug-ins to handle the task events sent by the API or the internal events that have equivalent API events.
- Creating notification event handlers for Business Process Choreographer

Notification events are produced when human tasks are escalated. Business Process Choreographer provides functionality for handling escalations, such as creating escalation work items or sending emails. You can create notification event handlers to customize the way in which escalations are handled.
- Installing API event handler and notification event handler plug-ins for human tasks

To use API event handler or notification event handler plug-ins, you must install the plug-in so that it can be accessed by the human task container.
- Registering API event handler and notification event handler plug-ins with task templates, task models, and tasks

You can register plug-ins for API event handlers and notification event handlers with tasks, task templates, and task models at various times: when you create an ad hoc task, update an existing task, create an ad hoc task model, or define a task template.
- Using a plug-in to post-process people query results

People resolution in Business Process Choreographer returns a list of the users that are assigned to a specific role, for example, potential owners of a task. You can create a plug-in that changes the results of people queries that are returned by people resolution. For example, to improve workload balancing, you could remove users from the query result who already have a high workload.