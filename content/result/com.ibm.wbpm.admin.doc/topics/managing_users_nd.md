# Creating and maintaining users for a deployment environment

## Before you begin

Authorize users to manage other users. To enable users to add, delete, or modify other users in
WebSphere, assign the user to the WebSphere® Application
Server IdMgrWriter role by
running the following command in the wsadmin scripting client:

```
wsadmin> AdminTask.mapIdMgrUserToRole( [ '-roleName', 'IdMgrWriter', '-userId', 'uid=sample\_user,o=defaultWIMFileBasedRealm' ] )
wsadmin> AdminConfig.save()
```

- Run the command on the deployment manager node. In IBM® Business Automation Workflow
Express, run the command on the
stand-alone server.
- The command must be run in connected mode. Do not specify the wsadmin
-conntype none option.

See the topic Providing security. Refer to the topic IdMgrConfig command group for the AdminTask object for
more information on the WebSphere Application
Server IdMgrWriter
role.

If a user needs to use the Process Admin Console to manage other
users, then add the user to the tw\_admins group
in the Process Admin Console.
See the topic Creating and managing groups.

To create
and maintain users, log in as an administrative user, such as a user
in the DeAdmin role. Do not remove a user or group assigned to the
DeAdmin role. Only users and groups assigned to this role can administer
servers and users.

## About this task

- WebSphere Application
Server Virtual
Member Manager (VMM) user repository security groups
- Lightweight Directory Access Protocol (LDAP) user repository security
groups
- Internal IBM Business Automation Workflow custom
user registries

## Procedure

The procedure for creating and configuring user accounts
varies according to the type of user registry that is configured and
whether you use an external security provider.Note: In
the Server Admin area of the Process Admin Console, the User
Management section in the User Management window
displays only internal users, that is, users that exist in the file
registry part of VMM.

- Use the appropriate method to manage user authentication. 
For example, to configure Microsoft Active
Directory to perform user authentication see Using Microsoft Active Directory for
authentication in the WebSphere Application
Server documentation. To add
users to the Lightweight Directory Access Protocol user registry, see Adding users to the Lightweight Directory Access Protocol user registry in
the WebSphere Application
Server
documentation.
- To configure a user ID for specific access privileges on a Windows system, see Configuring a user ID for proper privileges for local operating system
registries in the WebSphere Application
Server documentation.
- To assign users to specific security roles for application security, see Assigning users and groups to roles in the WebSphere Application
Serverdocumentation.
- To assign users and groups to administrative roles so that the users can perform
administrative functions, see Authorizing access to administrative roles in the WebSphere Application
Serverdocumentation.
- To assign users to internal groups to access the administrative
console, Workflow Center,
and Process Portal applications,
see Business Automation Workflow security roles.
- On containers, manage users in the LDAP server connected
to User Management Service.