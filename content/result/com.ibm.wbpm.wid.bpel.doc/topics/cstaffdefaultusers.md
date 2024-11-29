<!-- image -->

# Default people assignments and inheritance rules

Inheritance rules are applied to automatically assign people to a particular
role, based on the fact that they are already assigned to another role. Inheritance
rules effectively add users to a role in addition to the users that are determined
by people assignment. These rules differ for inline tasks and stand-alone
tasks.

## Inline tasks

| Roles for inline human tasks and their escalations   | If the role is not defined in the task model ...   | If people assignment fails...                |
|------------------------------------------------------|----------------------------------------------------|----------------------------------------------|
| Task administrator                                   | Only inheritance applies                           | Only inheritance applies                     |
| Task potential instance creator                      | Everybody becomes potential instance creator       | Everybody becomes potential instance creator |
| Task potential starter                               | Everybody becomes potential starter                | Everybody becomes potential starter          |
| Task potential owner                                 | Everybody becomes potential owner                  | Administrators become potential owners       |
| Task editor                                          | No editor                                          | No editor                                    |
| Task reader                                          | Only inheritance applies                           | Only inheritance applies                     |
| Escalation receiver                                  | Administrators become escalation receivers         | Administrators become escalation receivers   |

- Process administrators become administrators for all inline tasks, their
subtasks, follow-on tasks, and escalations.
- Process readers become readers for all inline tasks, their subtasks, follow-on
tasks, and escalations.
- Task administrators become administrators for all subtasks, follow-on
tasks, and escalations of all these tasks.
- Task readers become readers for all subtasks, follow-on tasks, and escalations
of all these tasks.
- Members of any task role become readers for this task's escalations, subtasks,
and follow-on tasks.
- Escalation receivers become readers for the escalated task.

## Stand-alone tasks

| Roles for stand-alone human tasks and their escalations   | If the role is not defined in the task model ...   | If people assignment fails...                |
|-----------------------------------------------------------|----------------------------------------------------|----------------------------------------------|
| Task administrator                                        | Originator becomes administrator                   | The task is not started                      |
| Task potential instance creator                           | Everybody becomes potential instance creator       | Everybody becomes potential instance creator |
| Task potential starter                                    | Originator becomes potential starter               | The task is not started                      |
| Potential owner                                           | Everybody becomes potential owner                  | Administrators become potential owners       |
| Editor                                                    | No editor                                          | No editor                                    |
| Reader                                                    | Only inheritance applies                           | Only inheritance applies                     |
| Escalation receiver                                       | Administrators become escalation receivers         | Administrators become escalation receivers   |

- Task administrators become administrators for all subtasks, follow-on
tasks, and escalations of all these tasks.
- Task readers become readers for all subtasks, follow-on tasks, and escalations
of all these tasks.
- Members of any task role become readers for this task's escalations, subtasks,
and follow-on tasks.
- Escalation receivers become readers for the escalated task.

When a method is invoked using the Business Flow Manager API,
members of the BPESystemAdministrator role have administrator
authorization, and members of the BPESystemMonitor role
have reader authorization. When a method is invoked via the Human Task Manager
API, members of the TaskSystemAdministrator role have administrator
authorization, and members of the TaskSystemMonitor role
have reader authorization.