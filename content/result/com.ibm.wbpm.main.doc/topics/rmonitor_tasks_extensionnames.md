<!-- image -->

# Extension names for human task events

The extension name contains the string value that is used as the value of the
extensionName attribute of the Common Base Event. This is also the name of the
XML element that provides additional data about the event. The names of event elements are in
uppercase, for example BPC.HTM.BASE, and the names of XML elements are in mixed
case, for example, HTMEventCode. Except where indicated, all data elements are of
the type string.

Raw business events contain the extension name in their
type field, for example

{ "business-events-envelope-version": "1.0.1",
"business-events-extension-version": "bawadv/1.0.0", "id": "3a4dbc3d-3ed0-4218-b88c-81c9270c23e7",
"timestamp": "2019-07-31T19:10:13.321Z", "category": "bawadv:HUMAN\_TASK", "type": "bawadv:
BPC.HTM.TASK.INTERACT"...

For more information, see BPEL raw events formats.

- BPC.HTM.BASE

- BPC.HTM.ESCALATION.BASE
- BPC.HTM.ESCALATION.CUSTOMPROPERTYSET
- BPC.HTM.ESCALATION.STATUS
- BPC.HTM.ESCALATION.UPDATED
- BPC.HTM.ESCALATION.WISTATUS
- BPC.HTM.ESCALATION.WITRANSFER

- BPC.HTM.TASK.BASE
- BPC.HTM.TASK.CUSTOMPROPERTYSET
- BPC.HTM.TASK.FAILURE
- BPC.HTM.TASK.FOLLOW
- BPC.HTM.TASK.INTERACT
- BPC.HTM.TASK.MESSAGE
- BPC.HTM.TASK.STATUS
- BPC.HTM.TASK.UPDATED
- BPC.HTM.TASK.WISTATUS
- BPC.HTM.TASK.WITRANSFER

## BPC.HTM.BASE

BPC.HTM.BASE inherits
the XML elements from WBIMonitoringEvent.

| XML element           | Description                                                                                                                                                                                                                        |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HTMEventCode          | The Business Process Choreographer event code that identifies the number of the event type. Possible event codes are listed in the following tables.                                                                               |
| activityInstanceId    | The ID of the activity instance.                                                                                                                                                                                                   |
| displayName           | The display name of the task instance or escalation instance.                                                                                                                                                                      |
| expirationDate        | The expiration date of the task in Coordinated Universal Time (UTC) ISO 8601 format yyyyMMdd HHmmssZ.                                                                                                                              |
| isAdHoc               | This has the value true if the task was created at run time.                                                                                                                                                                       |
| isEscalated           | This has the value true if the task is escalated.                                                                                                                                                                                  |
| isFollowOn            | This has the value true for a follow-on task.                                                                                                                                                                                      |
| isSubTask             | This has the value true for a subtask.                                                                                                                                                                                             |
| isSuspended           | This has the value true if the task is suspended.                                                                                                                                                                                  |
| isWaitingForSubTask   | This has the value true if the task is waiting for subtask.                                                                                                                                                                        |
| kind                  | This contains one of the following values, which indicate the kind of task:101 for a human task.  105 for a participating task.  106 for an administrative task.                                                                   |
| parentTaskId          | The ID of the parent task. If there is no parent task, this is left empty.                                                                                                                                                         |
| principal             | The name of the user associated with this event.                                                                                                                                                                                   |
| processInstanceId     | The ID of the process instance.                                                                                                                                                                                                    |
| processTemplateId     | The ID of the process template.                                                                                                                                                                                                    |
| state                 | This contains one of the following values, which indicate the current state of the task instance.1 - INACTIVE  2 - READY  3 - RUNNING  5 - FINISHED  6 - FAILED  7 - TERMINATE  8 - CLAIMED  12 - EXPIRED  101 - FORWARDED         |
| taskInstanceId        | The ID of the task instance.                                                                                                                                                                                                       |
| taskTemplateId        | The ID of the template.                                                                                                                                                                                                            |
| taskTemplateName      | The name of the task template, including the namespace. This can differ from the display name. For a subtask of a parallel routing task, this value is the name of the parent task template with the string $Child appended to it. |
| taskTemplateValidFrom | The date and time from when the task template is valid.                                                                                                                                                                            |

## BPC.HTM.ESCALATION.BASE

BPC.HTM.ESCALATION.BASE
inherits the XML elements from BPC.HTM.BASE.

| XML element                   | Description                        |
|-------------------------------|------------------------------------|
| escalationName                | The name of the escalation.        |
| escalationInstanceDescription | The description of the escalation. |
| escalationTemplateId          | The template ID of the escalation. |

## BPC.HTM.ESCALATION.CUSTOMPROPERTYSET

BPC.HTM.ESCALATION.CUSTOMPROPERTYSET
inherits the XML elements from BPC.HTM.ESCALATION.BASE.

| XML element        | Description                                                          |
|--------------------|----------------------------------------------------------------------|
| username           | The name of the user who set the custom property.                    |
| propertyName       | The name of the custom property.                                     |
| propertyValue      | The value of the custom property.                                    |
| associatedObjectID | The ID of the associated object that is the escalation  instance ID. |

## BPC.HTM.ESCALATION.STATUS

BPC.HTM.ESCALATION.STATUS
inherits the XML elements from BPC.HTM.ESCALATION.BASE. No further
specific properties are defined for BPC.HTM.ESCALATION.STATUS beyond
the inherited properties.

## BPC.HTM.ESCALATION.UPDATED

BPC.HTM.ESCALATION.UPDATED
inherits the XML elements from BPC.HTM.ESCALATION.BASE.

| XML element            | Description                                                                                                                        |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| durationUntilEscalated | A calendar-specific duration, after which, the task state is checked and depending on it, the escalation occurs or is superfluous. |
| durationUntilRepeated  | A calendar-specific duration, after which the escalation action is performed again.                                                |
| escalationTime         | The time when this escalation will fire.                                                                                           |
| name                   | Name of the escalation.                                                                                                            |

## BPC.HTM.ESCALATION.WISTATUS

BPC.HTM.ESCALATION.WISTATUS
inherits the XML elements from BPC.HTM.ESCALATION.BASE.

| XML element   | Description                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| username      | The names of the users who have work items that are escalated.                                                                                                                                                                                                                                                                                                                                     |
| reason        | The reason that the work item was assigned to the user. This integer value indicates one of the following meanings:REASON\_NONE (0)  REASON\_POTENTIAL\_OWNER (1)  REASON\_EDITOR (2)  REASON\_READER (3)  REASON\_OWNER (4)  REASON\_POTENTIAL\_STARTER (5)  REASON\_STARTER (6)  REASON\_ADMINISTRATOR (7)  REASON\_ORIGINATOR (9)  REASON\_ESCALATION\_RECEIVER (10)  REASON\_POTENTIAL\_INSTANCE\_CREATOR (11) |

## BPC.HTM.ESCALATION.WITRANSFER

BPC.HTM.ESCALATION.WITRANSFER
inherits the XML elements from BPC.HTM.ESCALATION.BASE.

| XML element   | Description                                                                                                                                                                                                                                                                                                                                                                               |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| current       | The name of the current user. This is the user whose work item was transferred to someone else.                                                                                                                                                                                                                                                                                           |
| target        | The name of the user of the work item receiver.                                                                                                                                                                                                                                                                                                                                           |
| reason        | The reason that the work item was transferred. This integer value indicates one of the following meanings:REASON\_NONE (0)  REASON\_POTENTIAL\_OWNER (1)  REASON\_EDITOR (2)  REASON\_READER (3)  REASON\_OWNER (4)  REASON\_POTENTIAL\_STARTER (5)  REASON\_STARTER (6)  REASON\_ADMINISTRATOR (7)  REASON\_ORIGINATOR (9)  REASON\_ESCALATION\_RECEIVER (10)  REASON\_POTENTIAL\_INSTANCE\_CREATOR (11) |

## BPC.HTM.TASK.BASE

BPC.HTM.TASK.BASE
inherits the XML elements from BPC.HTM.BASE.

| XML element             | Description                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| taskInstanceDescription | The description of the task.                                                                                                                                                                                                                                                                                                                                                    |
| subTaskLevel            | The hierarchy level of a sub-task. The value is 1 for a first level sub-task, 2 for a second level sub-task, and so on.                                                                                                                                                                                                                                                         |
| taskInstanceName        | The name of the task instance.  For inline tasks, it has a prefix consisting of the process template name and the dollar symbol. For a subtask of a parallel routing task, this value is constructed by concatenating the name of the parent task instance with the string $p and an integer that identifies the subtask, for example, parentTaskName$p5 for the fifth subtask. |

## BPC.HTM.TASK.CUSTOMPROPERTYSET

BPC.HTM.TASK.CUSTOMPROPERTYSET
inherits the XML elements from BPC.HTM.TASK.BASE.

| XML element        | Description                                                   |
|--------------------|---------------------------------------------------------------|
| username           | The name of the user who set the custom property.             |
| propertyName       | The name of the custom property.                              |
| propertyValue      | The value of the custom property.                             |
| associatedObjectID | The ID of the associated object that is the task instance ID. |

## BPC.HTM.TASK.FAILURE

BPC.HTM.TASK.FAILURE
inherits the XML elements from BPC.HTM.TASK.BASE.

| XML element         | Description                                                                        |
|---------------------|------------------------------------------------------------------------------------|
| taskFailedException | A string containing the faultNameSpace and faultName separated by a semicolon (;). |
| faultName           | The name of the fault.                                                             |

## BPC.HTM.TASK.FOLLOW

BPC.HTM.TASK.FOLLOW
inherits the XML elements from BPC.HTM.TASK.BASE.

| XML element   | Description                                              |
|---------------|----------------------------------------------------------|
| followTaskId  | The ID of the task that was started as a follow-on task. |

## BPC.HTM.TASK.INTERACT

BPC.HTM.TASK.INTERACT
inherits the XML elements from BPC.HTM.TASK.BASE.

| XML element   | Description                                            |
|---------------|--------------------------------------------------------|
| username      | The name of the user that is associated with the task. |

## BPC.HTM.TASK.MESSAGE

BPC.HTM.TASK.MESSAGE
inherits the XML elements from BPC.HTM.TASK.BASE.

| XML element           | Description                                                                           |
|-----------------------|---------------------------------------------------------------------------------------|
| message or message\_BO | A String or business object representation that contains the input or output message. |

## BPC.HTM.TASK.STATUS

BPC.HTM.TASK.STATUS
inherits the XML elements from BPC.HTM.TASK.BASE. No further
specific properties are defined for BPC.HTM.TASK.STATUS beyond the
inherited properties.

## BPC.HTM.TASK.UPDATED

BPC.HTM.TASK.UPDATED
inherits the XML elements from BPC.HTM.TASK.BASE.

| XML element                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| businessRelevant            | Allows you to distinguish between business relevant and "auxiliary" tasks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| contextAuthorizationOfOwner | Possible values are: 0 = AUTH\_NONE: Indicates that no operations can be performed on the associated context. 3 = AUTH\_READER: Indicates that operations  that require Reader authority can be performed on the associated context object, for example, reading the properties of a process instance.                                                                                                                                                                                                                                            |
| name                        | The name of the task.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| namespace                   | The namespace used to categorize the task.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| description                 | The description of the task.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| displayName                 | The display name of the task instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| priority                    | The priority of the task.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| type                        | The type used to categorize the task.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| eventHandlerName            | A Java object that handles vetoable events sent to the application component.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| durationUntilDeleted        | The time period after the task instance reaches an end state, that the instance will be deleted.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| deletionTime                | Either the scheduled deletion time, or null if no deletion is scheduled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| durationUntilDue            | A calendar-specific duration, for how long this task is expected to take.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| dueTime                     | The time when the task is expected to be finished.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| durationUntilExpires        | A calendar-specific duration, after which the task will expire.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| expirationTime              | The actual date when this task will expire.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| escalated                   | Indicated whether an escalation occurred for this task.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| parentContextID             | The parent context for this task. This is the ID the task is dependant on.  For top-level tasks (either the root of a sub-task tree or the root of a follow-on task chain) this is set by the task that creates the application component at creation time and provides a key to the corresponding context in the calling application component. For example, for Business Flow Manager, this can be the PIID, EIID, SIID or AIID. For sub-tasks this is the ID of the next higher level task instance. For non-inline tasks this is the ACOID. |
| supportsClaimIfSuspended    | Indicates whether suspended tasks can be claimed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| supportsDelegation          | Indicates whether this task can be delegated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| supportsFollowOnTasks       | Indicates whether following tasks are supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| supportsSubTasks            | Indicates whether sub-tasks can be invoked for this task.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## BPC.HTM.TASK.WISTATUS

BPC.HTM.TASK.WISTATUS
inherits the XML elements from BPC.HTM.TASK.BASE.

| XML element   | Description                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| username      | The names of the users who have work items that were created or deleted.                                                                                                                                                                                                                                                                                                                           |
| reason        | The reason that the work item was assigned to the user. This integer value indicates one of the following meanings:REASON\_NONE (0)  REASON\_POTENTIAL\_OWNER (1)  REASON\_EDITOR (2)  REASON\_READER (3)  REASON\_OWNER (4)  REASON\_POTENTIAL\_STARTER (5)  REASON\_STARTER (6)  REASON\_ADMINISTRATOR (7)  REASON\_ORIGINATOR (9)  REASON\_ESCALATION\_RECEIVER (10)  REASON\_POTENTIAL\_INSTANCE\_CREATOR (11) |

## BPC.HTM.TASK.WITRANSFER

BPC.HTM.TASK.WITRANSFER
inherits the XML elements from BPC.HTM.TASK.BASE.

| XML element   | Description                                                                                                                                                                                                                                                                                                                                                                               |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| current       | The name of the current user. This is the user whose work item was transferred to someone else.                                                                                                                                                                                                                                                                                           |
| target        | The name of the user of the work item receiver.                                                                                                                                                                                                                                                                                                                                           |
| reason        | The reason that the work item was transferred. This integer value indicates one of the following meanings:REASON\_NONE (0)  REASON\_POTENTIAL\_OWNER (1)  REASON\_EDITOR (2)  REASON\_READER (3)  REASON\_OWNER (4)  REASON\_POTENTIAL\_STARTER (5)  REASON\_STARTER (6)  REASON\_ADMINISTRATOR (7)  REASON\_ORIGINATOR (9)  REASON\_ESCALATION\_RECEIVER (10)  REASON\_POTENTIAL\_INSTANCE\_CREATOR (11) |