<!-- image -->

# Human task events

- Task events
- Escalation events

Inline tasks can emit both human task events and
activity events. For a list of the activity events, see Activity events.

All human task events can be emitted in both the Dynamic Event Framework (DEF) and the audit
trail, with the exception of the task template events. The task template events
TASK\_TEMPLATE\_INSTALLED and TASK\_TEMPLATE\_UNINSTALLED can only be emitted in the audit trail.

## Key to table columns

## Task events

The following table
describes all task events.

|   Code | Event name                    | Description                                                                                                                                        |
|--------|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
|  51001 | TASK\_CREATED                  | Task created                                                                                                                                       |
|  51002 | TASK\_DELETED                  | Task deleted                                                                                                                                       |
|  51003 | TASK\_STARTED                  | Task started                                                                                                                                       |
|  51004 | TASK\_COMPLETED                | Task completed                                                                                                                                     |
|  51005 | TASK\_CLAIM\_ CANCELLED         | Claim canceled                                                                                                                                     |
|  51006 | TASK\_CLAIMED                  | Task claimed                                                                                                                                       |
|  51007 | TASK\_TERMINATED               | Task terminated                                                                                                                                    |
|  51008 | TASK\_FAILED                   | Task failed                                                                                                                                        |
|  51009 | TASK\_EXPIRED                  | Task expired                                                                                                                                       |
|  51010 | TASK\_WAITING\_FOR\_SUBTASK      | Waiting for subtasks                                                                                                                               |
|  51011 | TASK\_SUBTASKS\_COMPLETED       | Subtasks completed                                                                                                                                 |
|  51012 | TASK\_RESTARTED                | Task restarted                                                                                                                                     |
|  51013 | TASK\_SUSPENDED                | Task suspended                                                                                                                                     |
|  51014 | TASK\_RESUMED                  | Task resumed                                                                                                                                       |
|  51015 | TASK\_COMPLETED\_WITH\_FOLLOW\_ON | Task completed and follow-on task started                                                                                                          |
|  51101 | TASK\_UPDATED                  | Task updated                                                                                                                                       |
|  51102 | TASK\_INPUT\_MESSAGE\_UPDATED    | Input message updated. Business object payload is available.                                                                                       |
|  51103 | TASK\_OUTPUT\_MESSAGE\_UPDATED   | Output message updated. Business object payload is available.                                                                                      |
|  51104 | TASK\_FAULT\_MESSAGE\_UPDATED    | Fault message updated. Business object payload is available.                                                                                       |
|  51201 | TASK\_WORKITEM\_DELETED         | Work item deleted                                                                                                                                  |
|  51202 | TASK\_WORKITEM\_CREATED         | Work items created                                                                                                                                 |
|  51204 | TASK\_WORKITEM\_TRANSFERRED     | Work item transferred                                                                                                                              |
|  51205 | TASK\_WORKITEM\_REFRESHED       | Work items refreshed                                                                                                                               |
| 51301  | TASK\_CUSTOMPROPERTY\_SET       | Custom property set. This event is generated when a custom property of a task instance is changed.                                                 |
|  52001 | TASK\_TEMPLATE\_INSTALLED       | These are task template events, which are only emitted in the audit trail. They are not emitted as events, and are included here for completeness. |
|  52002 | TASK\_TEMPLATE\_UNINSTALLED     | These are task template events, which are only emitted in the audit trail. They are not emitted as events, and are included here for completeness. |

## Escalation events

The following
table describes all task escalation events.

|   Code | Event name                      | Description                                                                                               |
|--------|---------------------------------|-----------------------------------------------------------------------------------------------------------|
|  53001 | ESCALATION\_UPDATED              | Escalation updated                                                                                        |
|  53201 | ESCALATION\_WORKITEM\_DELETED     | Work item deleted                                                                                         |
|  53202 | ESCALATION\_WORKITEM\_CREATED     | Work item created                                                                                         |
|  53204 | ESCALATION\_WORKITEM\_TRANSFERRED | Escalation transferred                                                                                    |
|  53205 | ESCALATION\_WORKITEM\_REFRESHED   | Work item refreshed                                                                                       |
|  51302 | ESCALATION\_CUSTOMPROPERTY\_SET   | Custom property set. This event is generated when a custom property of an escalation instance is changed. |