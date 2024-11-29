<!-- image -->

# Modification of task instance properties at run time

In addition, the predefined values of some properties can contain
references to other properties: they are then called replacement variable
expressions.

Business Process Choreographer Explorer, Business Space, and the
Business Process Choreographer APIs support the modification of task
instances at run time.

## Properties that can be changed at run time

- Business relevance
- Context authorization of owner
- Deletion time
- Description
- Display name
- Due time
- Escalation state
- Event handler name
- Expiration time
- Name
- Namespace
- Parent context ID
- Priority
- Read
- Supports claim if suspended
- Supports delegation
- Supports follow-on tasks
- Supports subtasks
- Type
- Work basket

- Changes to the expiration, deletion, and due times for tasks at run time

Sometimes a business situation requires that you change the due, expiration, or deletion time that was originally defined for a task. The task state determines which of these times you can reschedule, cancel, and start at run time, and when these actions can be taken. You can use Business Process Choreographer Explorer to change these times, or you can use the update method of the Human Task Manager API to modify the appropriate task property.
- Changes to the timing of an escalation at run time

Sometimes a business situation requires that you change the timing of an escalation that was specified when the escalation was defined. The escalation state determines which of these times you can change, and when these actions can be taken. You can use the update method of the Human Task Manager API to modify the appropriate escalation property. You can also use the Tasks List widget or the Escalations List widget in Business Space to override the scheduled escalation time, and start an escalation immediately.
- Replacement variables in human tasks

Replacement variables are used in the definitions of human tasks to refer to a value of an element that is resolved at run time. These variables represent task and process-related data, such as people assigned to a task or custom properties for the task. This data is available at run time for all or part of the lifecycle of a task instance.

<!-- image -->