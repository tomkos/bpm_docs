<!-- image -->

# Instance-based authorization roles for human tasks

People are assigned to the following roles at run time by people
assignment based on the user and user group information that is stored
in a people directory: potential creator, potential starter, potential
owner, reader, editor, administrator, and escalation receiver. The
following roles are associated with only one user and are assigned
as the result of a task action: originator, starter, owner.

These roles are authorized to perform the following actions:

| Role                | Authorized actions                                                                                                                                                                                                                                             |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Potential creator   | Members of this role can create an instance of the task. If a potential instance creator is not defined for the task template, then all users are considered to be a member of this role.                                                                      |
| Originator          | The person with this role has administrative rights until the task starts. When the task starts, the originator has the authority of a reader and can perform some administrative actions, such as suspending and resuming tasks, and transferring work items. |
| Potential starter   | Members of this role can start an existing task instance. If a potential starter is not specified for stand-alone tasks, the originator becomes the potential starter. For inline invocation tasks without a potential starter, the default is everybody.      |
| Starter             | The person with this role has the authority of a reader and can perform some administrative actions, such as transferring work items.                                                                                                                          |
| Potential owner     | Members of this role can claim a task. If a potential owner is specified, then all users are considered to be members of this role. If people resolution fails for this role, then the administrators are assigned as the potential owners.                    |
| Owner               | The person with this role works on and completes a task.                                                                                                                                                                                                       |
| Reader              | Members of this role can view the properties of all of the task objects, but cannot work on them.                                                                                                                                                              |
| Editor              | Members of this role can work with the content of a task, but cannot claim or complete it.                                                                                                                                                                     |
| Administrator       | Members of this role can administer tasks, task templates, and escalations.                                                                                                                                                                                    |
| Escalation receiver | Members of this role have the authority of a reader for the escalation and the escalated task.                                                                                                                                                                 |

## Related information

- Predefined people assignment criteria
- Customizing people assignment criteria