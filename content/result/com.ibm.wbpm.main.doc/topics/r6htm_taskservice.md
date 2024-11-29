<!-- image -->

# HumanTaskManagerService interface

The methods that can be called depend on the state of
the task and the authorization of the person that uses the application
containing the method. The main methods for manipulating task objects
are listed here. For more information about these methods and the
other methods that are available in the HumanTaskManagerService interface,
see the Javadoc in the com.ibm.task.api package.

## Task templates

The following methods are
available to work with task templates.

| Method                      | Description                                                                                                               |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------|
| getTaskTemplate             | Retrieves the specified task template.                                                                                    |
| createTask                  | Creates a task instance from the specified task template.                                                                 |
| createAndCallTask           | Creates and runs a task instance from the specified task template and waits synchronously for the result.                 |
| createAndStartTask          | Creates and starts a task instance from the specified task template.                                                      |
| createAndStartTaskAsSubtask | Creates and starts a task instance as a subtask of the specified task.                                                    |
| createInputMessage          | Creates an input message for the specified task template. For example, create a message that can be used to start a task. |
| queryTaskTemplates          | Retrieves task templates that are stored in the database.                                                                 |

## Task instances

The following methods are
available to work with task instances.

| Method                   | Description                                                                                                                    |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| getTask                  | Retrieves a task instance; the task instance can be in any state.                                                              |
| callTask                 | Starts an invocation task synchronously.                                                                                       |
| startTask                | Starts a task that has already been created.                                                                                   |
| startTaskAsSubtask       | Starts a task as a subtask of the task instance.                                                                               |
| suspend                  | Suspends the collaboration or to-do task.                                                                                      |
| resume                   | Resumes the collaboration or to-do task.                                                                                       |
| restart                  | Restarts the task instance.                                                                                                    |
| terminate                | Terminates the specified task instance. If an invocation task is terminated, this action has no impact on the invoked service. |
| delete                   | Deletes the specified task instance.                                                                                           |
| claim                    | Claims the task for processing.                                                                                                |
| update                   | Updates the task instance.                                                                                                     |
| complete                 | Completes the task instance.                                                                                                   |
| completeWithFollowOnTask | Completes the task instance and starts a follow-on task.                                                                       |
| cancelClaim              | Releases a claimed task instance so that it can be worked on by another potential owner.                                       |
| createWorkItem           | Creates a work item for the task instance.                                                                                     |
| transferWorkItem         | Transfers the work item to a specified owner.                                                                                  |
| deleteWorkItem           | Deletes the work item.                                                                                                         |

## Escalations

The following methods are available
to work with escalations.

| Method            | Description                                  |
|-------------------|----------------------------------------------|
| getEscalation     | Retrieves the specified escalation instance. |
| triggerEscalation | Manually triggers an escalation.             |

## Custom properties

Tasks, task templates,
and escalations can all have custom properties. The interface provides
a get and a set method to retrieve and set values for custom properties.
You can also associate named properties with, and retrieve named properties
from task instances. Custom property names and values must be of the
java.lang.String type. The following methods are valid for tasks,
task templates, and escalations.

| Method                 | Description                                                         |
|------------------------|---------------------------------------------------------------------|
| getCustomProperty      | Retrieves the named custom property of the specified task instance. |
| getCustomProperties    | Retrieves the custom properties of the specified task instance.     |
| getCustomPropertyNames | Retrieves the names of the custom properties for the task instance. |
| setCustomProperty      | Stores custom-specific values for the specified task instance.      |