<!-- image -->

# Evaluation of task elements and their replacement variables
at run time

1. The variables are initialized before the task element is evaluated
2. The task element is evaluated before the query from the client
application

| Task-related action         | Sequence of evaluation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Create a task               | Task element: People assignment for potential instance creators is evaluated Replacement variable: htm:task.potentialInstanceCreators is initialized   Task element: People assignment for potential starters is evaluated Replacement variable: htm:task.potentialInstanceStarters is initialized Replacement variable: htm:task.instanceID is initialized Replacement variable: htm:task.displayName is initialized Replacement variable: htm:task.property.customPropertyName is initialized   Task element: The task priority is evaluated Replacement variable: htm:task.originator is initialized   Task element: The task description is evaluated Replacement variable: htm:task.description is initialized                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Start a task                | Task element: No elements are evaluated Replacement variable: htm:input.[part|part\XPath|\XPath] is initialized   Task element: The duration until the task is overdue is evaluated Task element: The duration until the task expires is evaluated Task element: People assignment for the administrator role is evaluated Replacement variable: htm:task.administrators is initialized   Task element: People assignment for potential owners is evaluated Replacement variable: htm:task.potentialOwners is initialized   Task element: People assignment for editors is evaluated Replacement variable: htm:task.editors is initialized   Task element: People assignment for readers is evaluated Replacement variable: htm:task.readers is initialized Replacement variable: htm:task.starter is initialized   Task element: The custom properties for the task are evaluated Replacement variable: htm:task.property.customPropertyName is initialized   Task element: The inline custom properties for the task are evaluated Task element: The business category is evaluated Task element: The task priority is evaluated Task element: The task work basket is evaluated Task element: The task description is evaluated Replacement variable: htm:task.description is initialized |
| An escalation is created    | No task elements are evaluated. The following replacement variables are initialized: htm:escalation.instanceID htm:escalation.activationState htm:escalation.expectedTaskState htm:escalation.displayName htm:escalation.description htm:escalation.property.customPropertyName                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| An escalation is activated  | Task element: The escalation duration is evaluated Task element: The escalation properties are evaluated Replacement variable: htm:escalation.property.customPropertyName is initialized   Task element: The escalation description is evaluated Replacement variable: htm:escalation.description is initialized or changed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| An escalation is triggered  | Task element: Escalation receivers are evaluated.  Replacement variable: htm:escalation.receivers is evaluated  Note that the definition can refer to the escalation receivers of another escalation, for example, it can include a variable like htm:escalation(otherEscalationName).receivers. Task element: For email notifications, the email subject and body are evaluated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| A task reaches an end state | Task element: The duration until deletion of the task is evaluated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

- A task element should only include replacement variables thatare initialized before the task element is evaluated:
    - Replacement variables that are initialized due to an earlier task
action are the replacement variables that are located in rows that
precede the row that contains the task element.  For example, the
replacement variable %htm:task.originator% is initialized when a task
is created. Therefore, it can be included in the definition of the
task element People assignment for potential owners that
is evaluated when the task instance is started.
    - Replacement variables that are initialized as part of the same
task action as the task element evaluation, but before the task element
evaluation is done are shown on the same row.  As indicated in the
table, for selected task actions (task creation, task update, escalation
activation, escalation timer expiration) an evaluation order is defined
for both task elements and replacement variables. Based on this sequence,
you can see which of the replacement variables are initialized before
a task element is evaluated. For example, a replacement variable
%htm:input.\param1% is initialized when the task starts, but before
any of the task elements are evaluated. Therefore it can be included
in the definition of the task element People assignment
for potential owners that is also evaluated during the start of
the task instance.
  If an evaluation order is not given in a table
row, no specific evaluation order is guaranteed for that row.
- A task element evaluation can imply the initialization of a correspondingreplacement variable:

- Some task elements have corresponding replacement variables that
can be used by other task elements.  For example, the task element People assignment for potential owners has a corresponding
replacement variable %htm:task.potentialOwners%, that is initialized
after the task element is evaluated. This means that task elements
can be defined in terms of other task elements.

## Related concepts

- Replacement variables: Examples of usage patterns in task elements

## Related reference

- Actions that initialize or change replacement variables for human task elements