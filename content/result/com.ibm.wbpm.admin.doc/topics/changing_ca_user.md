# Changing the cell admin user

## Before you begin

Log in to the WebSphere administrative console as the
administrative user that corresponds to the IBM® Business Automation Workflow CellAdmin security
role that was specified as the default administrative account during
installation.

## Procedure

1. Create a new WebSphere® Application
Server user from the WebSphere Application
Server admin console.
2. In the Server Admin area of the Process Admin Console,
click User Management > User
synchronization > Add and
enter the new user ID. Click Synchronize. You
must do this for all deployment environments, if you have multiple
deployment environments.
3. Assign the new user to the WebSphere Application
Server operator, deployer,
and administrator roles.  See Authorizing access to administrative roles in
the WebSphere Application
Server documentation.
4. Add the new user to the bus connector role. See Adding users and groups in the bus connector role.
5. Change the alias that is mapped to the cellAdminAlias to
use the new user. See Modifying authentication aliases.
6. Add the new user to the tw\_admins group
and tw\_authors group. See Creating and managing groups. You must do this for all deployment
environments, if you have multiple deployment environments. Make
sure that the new user ID has the proper access to the WebSphere Application
Server admin console and IBM Business Automation Workflow operations.
You can also verify that the setup was successful by checking the
output file DE\_nameproperties file. This can be
done by using the command BPMConfig -export -profile dmgrProfile -outputDir export\_dir