<!-- image -->

# Task instances

| Column name in TASK\_TEMPL view   | Inherited by task instance   | Comments                                                                                                                                                                                                                                                                                                        |
|----------------------------------|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VALID\_FROM                       | No                           | Not needed by the task instance.                                                                                                                                                                                                                                                                                |
| CONTAINMENT\_CTX\_ID               | No                           | Task instances are deleted according to a different set of rules than their corresponding task templates.                                                                                                                                                                                                       |
| IS\_AD\_HOC                        | No                           | Not needed by the task instance: An ad hoc task template creates a task instance that is not ad hoc. An ad hoc task instance does not have a task template.                                                                                                                                                     |
| IS\_INLINE                        | Usually                      | The property is not inherited in the following situations: A subtask instance cannot be inline, even if its template is defined as inline. A follow-on task instance cannot be inline, even if its template is defined as inline.  A human task activity instance is always related to an inline task instance. |
| STATE                            | No                           | A task template must be in the STATE\_STARTED state  to create and start task instances. The instances are then in the STATE\_READY state.                                                                                                                                                                        |

In addition, all of the custom properties of a task template (TASK\_TEMPL\_CPROP
view) are inherited by the custom property instances of a task instance
(TASK\_CPROP view). The multilingual description of a task template
(TASK\_TEMPL\_DESC view) has a row for each locale. A task instance
(TASK\_DESC view) inherits these rows.

## Related concepts

- Types of human task
- Inline and stand-alone human tasks
- Task templates
- Human task clients
- Human task user interfaces
- Versioning of human tasks
- To-do tasks and collaboration tasks with parallel ownership
- Lifecycle of a human task

## Related tasks

- Setting human task preferences
- Improving performance when using human task list widgets