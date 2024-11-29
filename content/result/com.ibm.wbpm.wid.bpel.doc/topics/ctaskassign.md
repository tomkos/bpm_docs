<!-- image -->

# Authorization and people assignment for human tasks

- Task authorization and work items

Every task role enables users to carry out an exact set of actions on the associated task. A person's authorization is managed using work items. A work item represents the relationship of the assigned person to the task actions implied by the task role.
- Assigning roles to your human task

A role is a set of employees who share the same level of authority. When it comes to working on tasks, the role that the person belongs to defines their authorization.
- People resolution

People resolution retrieves user information from people directories based on a set of parameterized query expressions, known as people assignment criteria.
- People assignment criteria

People assignment criteria are constructs that are used in the task model to identify sets of people that can be assigned to an instance-based authorization role. At run time, the people resolution uses the people assignment criteria to retrieve the user IDs and other user information from the people directory, for example, for composing emails. People assignment criteria are also used during run time when task models are created programmatically.
- Ownership patterns

When you assign potential owners to a human task you can establish a pattern of ownership. This pattern defines whether users can simultaneously interact with the task. Depending on the ownership pattern, you can also define completion conditions, propagation of user roles and aggregation options.
- Substitution for absentees

The substitution feature allows you to specify absence settings either for yourself, or for members of the group that you administer. A substitution policy defines how to deal with tasks and escalations that are assigned to absent users.