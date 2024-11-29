- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Class TaskType

- java.lang.Object
    - com.ibm.casemgmt.api.tasks.TaskType

- public final class TaskType
extends java.lang.Object
Represents a task type deployed as part of a solution in IBM Case Manager. TaskType instances are exposed 
 only for discretionary task types. Instances of TaskType are obtained by calling the 
 getDiscretionaryTaskTypes() method or the getDiscretionaryTaskType() method of CaseType.
 
 To create a task instance for a particular discretionary task type, call the createPendingInstance() 
 factory method of the Task class and then call additional methods on the Task object to configure
 and save the new task.

ID status:
ID review by David Newhall, 5/16/2012.

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description java.lang.String getDefaultView () Returns the default view the task type. java.lang.String getDescription () Returns the textual description of the task type. java.lang.String getDisplayName () Returns the display name of the task type. com.filenet.api.util.Id getId () Returns the Id of the task type. java.lang.String getName () Returns the name of the task type. boolean hasInstanceCreationRights () Indicates whether the current authenticated user has the rights to create tasks that are of this discretionary task type. boolean isContainer () Indicates whether this task type represents a container task. boolean isHidden () Indicates whether this task type should be hidden in a user interface. boolean isLaunchInfoRequired () Indicates whether launch information is required to create an instance of this discretionary task type. boolean isToDo () Indicates whether this task type represents a ToDo task.

### Method Summary

| Modifier and Type       | Method and Description                                                                                                                                  |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String        | getDefaultView() Returns the default view the task type.                                                                                                |
| java.lang.String        | getDescription() Returns the textual description of the task type.                                                                                      |
| java.lang.String        | getDisplayName() Returns the display name of the task type.                                                                                             |
| com.filenet.api.util.Id | getId() Returns the Id of the task type.                                                                                                                |
| java.lang.String        | getName() Returns the name of the task type.                                                                                                            |
| boolean                 | hasInstanceCreationRights() Indicates whether the current authenticated user has the rights to create tasks that are of this discretionary   task type. |
| boolean                 | isContainer() Indicates whether this task type represents a container task.                                                                             |
| boolean                 | isHidden() Indicates whether this task type should be hidden in a user interface.                                                                       |
| boolean                 | isLaunchInfoRequired() Indicates whether launch information is required to create an instance of this discretionary task type.                          |
| boolean                 | isToDo() Indicates whether this task type represents a ToDo task.                                                                                       |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait