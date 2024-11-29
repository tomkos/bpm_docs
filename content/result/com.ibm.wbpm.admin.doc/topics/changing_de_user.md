# Changing the deployment environment administrator

## Before you begin

Log in to the WebSphere administrative console as the administrative user that corresponds to the
IBM® Business Automation Workflow
CellAdmin security role that was specified as the default administrative account during
installation.

## Procedure

1. Create a new WebSphere® Application
Server user if you do
not already have one configured in the user repository. For example, the Lightweight Directory
Access Protocol (LDAP) user repository.
2. In the Server Admin area of the Process Admin Console, click User
Management > User
synchronization > Add and enter the new user ID. Click
Synchronize.
3. Assign the new user to the WebSphere Application
Server
operator, deployer, and administrator roles.  See Authorizing access to administrative roles in the WebSphere Application
Server documentation.
4. Add the user to the bus connector role. See Adding users and groups in the bus connector
role.
5. Change the alias that is mapped to the IBM Business Process Manager DeAdmin
security role to use the new user.  See Business Automation Workflow security roles.
6. Add the user to the administrators group, by default, tw\_admins.
 See Creating and managing groups.
7. Configure the user as a system lane user. See Configuring additional system lane users.
8. Restart the deployment environment.