# Creating and maintaining users for a stand-alone server

## Before you begin

- To create and maintain users, log in as an administrative user,
such as a user in the DeAdmin role. Do not remove the user or group
assigned to the DeAdmin role. Only users and groups assigned to this
role can administer servers and users.
- To create users, you must have permission at the WebSphere Application
Server level.

## About this task

- The default user registry is the WebSphere® Application
Server file registry.
- When you add an administrative user during installation, the new
user is automatically added to the tw\_admins user
group. Users in the tw\_admins group can administer
workflow servers, Performance Data Warehouses, and internal users and
groups.

- WebSphere Application Server Virtual Member Manager (VMM) user
repository security groups
- Lightweight Directory Access Protocol (LDAP) user repository security
groups
- Internal Business Automation Workflow custom
user registries

## Procedure

- To create users: Note: After you create a user in the Process Admin Console,the full name will appear in both the first and last name fields ofthe Manager Users section of WebSphere Application Server console.
    1. Log in to the Process Admin Console as a user assigned
to the DeAdmin role.
    2. In the Server Admin area of the Process Admin Console,
click the indicator next to User Management to
list the available management options.
Note: The User Management section in
the User Management window displays only internal
users, that is, users that exist in the file registry part of VMM.
    3. Click User Management.
    4 In the User Management > Maintain User Settings window,enter a user name, a full name, and a password. Passwordsmust meet the following requirements:
        - Must include at least six characters.
        - Must not be the same as the user name.
        - Must not be the same as the existing password.
        - Must be different from the three most recently used passwords.
5. Enter the password a second time to confirm it.
6. Click Add.
- To update users by changing password or other account settings:

1. In the Server Admin area of the Process Admin Console,
click the indicator next to User Management to
list the available management options.
2. Click User Management.
3. In the User Management > Maintain User Settings window,
enter a complete or partial user name in the Retrieve Profile field.
4. Click Retrieve.
5. Change settings as required and click Update.
- To delete users:

1. In the Server Admin area of the Process Admin Console,
click the indicator next to User Management to
list the available management options.
2. Click User Management.
3. In the User Management > Maintain User Settings window,
enter a complete or partial user name in the Retrieve Profile field.
4. Click Retrieve.
5. Select the account that you want from the Internal Business Automation Workflow Users list.
6. Click Delete.