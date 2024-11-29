# Administrative
security roles

There are eight roles provided as part of the administrative
console.
These roles grant permission to ranges of functionality on the administrative
console. When administrative security is enabled, a user must be mapped
to one of these roles in order to access the administrative console.

The first user to log in to the server after installation is added
to the administrator role.

| Administrative security role   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Monitor                        | A member of the monitor role can view the IBM Business Automation Workflow configuration and the current state of the server.                                                                                                                                                                                                                                                                                                                           |
| Configurator                   | A member of the configurator role can edit the IBM Business Automation Workflow configuration.                                                                                                                                                                                                                                                                                                                                                          |
| Operator                       | A member of the operator role has monitor privileges, plus the ability to modify the runtime state (that is, start and stop the server).                                                                                                                                                                                                                                                                                                                |
| Administrator                  | The administrator role is a combination of configurator and operator roles plus additional privileges granted solely to the administrator role. Examples include:Modifying the server user ID and password Mapping users and groups to the administrator role  The administrator also has the permission required to access sensitive information, such as:Lightweight Third Party Authentication (LTPA) passwords Keys                                 |
| ISC Admins                     | This role is available only for administrative console users and not for wsadmin users. Users who are granted this role have administrator privileges for managing users and groups in the federated repositories. For example, a user of the ISC Admins role can complete the following tasks:Create, update, or delete users in the federated repositories configuration Create, update, or delete groups in the federated repositories configuration |
| Deployer                       | Users who are granted this role can perform both configuration actions and runtime operations on applications.                                                                                                                                                                                                                                                                                                                                          |
| Admin Security Manager         | Only users who are granted this role can map users to administrative roles. Also, when fine-grained administrative security is used, only users who are granted this role can manage authorization groups.                                                                                                                                                                                                                                              |
| Auditor                        | Users who are granted this role can view and modify the configuration settings for the security auditing subsystem. Note: The auditor role includes the monitor role. This allows the auditor to view but not change the rest of the security configuration.                                                                                                                                                                                            |

See Administrative roles in the WebSphere® Application
Server information
center for more information.

The failed event manager can be operated by any user granted either
the administrator or the operator role.

Selectors can be configured
by any user granted either the administrator
or the configurator role

- The AllAuthenticated special-subject
means
that the access check of the administrative role ensures that the
user making the request is at least authenticated.
- The Everyone special-subject
means that
anyone, authenticated or not, can perform the action, as if security
were not enabled.