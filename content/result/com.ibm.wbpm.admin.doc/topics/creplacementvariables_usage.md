<!-- image -->

# Replacement variables: Examples of usage patterns in task elements

## A task description includes run time-specific information

| Task element         | Definition                                                                                                                                                                                                                                                         |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task custom property | name: 'property1'  value: a default value                                                                                                                                                                                                                          |
| Task description     | "This task instance has   as ID: %htm:task.instanceID%  as originator: %htm:task.originator%  as administrators: %htm:task.administrators%  as owner: %htm:task.owner%  a custom property with the name 'property1'  which is set to %htm:task.property.property1% |

If you use the setCustomProperty method
on a task instance, you can set an individual custom property for
the task instance. When the task starts, the task description is evaluated,
and this value is included in the description that is displayed in
the client application.

## Control the duration of task with a custom property

| Task element           | Definition                               |
|------------------------|------------------------------------------|
| Task calendar          | 'Simple'                                 |
| Task custom property   | name: 'property1'  value: '2days 3hours' |
| Duration until overdue | %htm:task.property.property1%            |

If you use the setCustomProperty method
on a task instance, you can set a custom property for the task instance
in a format that is allowed by the simple calendar. When the task
starts, the duration until overdue is evaluated, and this value is
inserted for the duration.

## Control the people assignment of an inline task

| Task element                                | Definition                                             |
|---------------------------------------------|--------------------------------------------------------|
| People assignment for potential owners role | Users by User IDuserId: %wf:activity(activity1).owner% |

In the replacement variable, activity1 is
a human task activity in a BPEL process that is in the claimed state.
This means that the owner of the task is known. When the second task
is started, the people assignment for the potential owners is evaluated.
The owner of the first task is inserted as the parameter value in
the people assignment expression.

## Expose part of an input message as a custom property

| Task element                | Definition                                           |
|-----------------------------|------------------------------------------------------|
| Task custom property        | name: customerId  value: "%htm:input.\customerId%"   |
| Task inline custom property | name: CUSTOM\_TEXT1  value: "%htm:input.\customerId%" |

For example, a task is started with an input message that contains the customer ID 0815. To sort
the query results to find this task, you can define an inline custom property,
CUSTOM\_TEXT1, and then define sort criteria in the query table for this attribute.

## Related concepts

- Evaluation of task elements and their replacement variables at run time

## Related reference

- Actions that initialize or change replacement variables for human task elements