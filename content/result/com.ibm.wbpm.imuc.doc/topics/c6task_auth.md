<!-- image -->

# Authorization roles for human
tasks

- Java EE authorization roles for human tasks

System-level Java EE roles are set up when Human Task Manager is configured.
- Instance-based authorization roles for human tasks

A task instance or an escalation instance is not assigned directly to a person, instead it is associated with predefined roles to which people are assigned. Anyone that is assigned to an instance-based role can perform the actions for that role. The association of users to instance-based roles is determined either by people assignment, or as the result of task actions.
- Instance-based authorization roles for work baskets and business categories

A work basket instance or business category instance is not assigned directly to a person, instead it is associated with predefined roles to which people are assigned. Anyone that is assigned to an instance-based role can perform the actions for that role. The association of users to instance-based roles is determined by people assignment.
- Task kinds and instance-based authorization roles

Instance-based authorization roles are associated with human tasks and escalations when the task is modeled. The task kind determines whether a specific authorization role is available for a task.

<!-- image -->