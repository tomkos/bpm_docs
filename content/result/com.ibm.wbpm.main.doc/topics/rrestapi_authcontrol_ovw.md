# Authorization control for runtime REST API calls

- Authorization roles

Authorization roles are used to define privileges for users and groups for actions that can be applied to entities including users, groups, tasks, and processes.
- REST API authorization for task actions

For each task action, the implemented authorization is determined by a set of associated authorization roles and action policies. You can enable users to perform actions by assigning them to the roles or policies.
- REST API authorization for user, group, and team actions

Two authorization modes are provided for the REST APIs granting access to user, group, 		and team information. A default mode provides limited authorization control while an 		enhanced mode is available to extend authorization control to all concerned 		APIs.
- REST API authorization for accessing repository assets at run time

The ability to access process models, process applications, and environment variables in the repository at run time is determined by a set of associated authorization roles and action policies. You can enable users to access these assets by assigning them to the roles or policies.
- REST API authorization for process instances

The authorization roles and action policies that are associated with each process instance determine the implemented authorization roles and action policies. You can enable users to take actions by assigning them to the roles or policies.
- Removing the assignedToRole column

Because the Execute Query REST API has an auto column called             assignedToRole, the API always returns a value for the auto column             taskAssignedTo. A task can be assigned to a user or a team. To show the         team assignment of a task, the taskAssignedTo column returns the assigned         user or team. However, if your application requires the query to return the             taskAssignedTo column only for tasks assigned to a specific user, you         can remove the assignedToRole column by specifying a configuration option         in the appropriate 100Custom.xml file in your topology.