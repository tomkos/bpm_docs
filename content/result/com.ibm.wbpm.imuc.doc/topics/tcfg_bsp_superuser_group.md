<!-- image -->

# Assigning the superuser by user group

## Before you begin

- Enable application security and administrative security. See Setting up security for the Business Space component and Process Portal.
- Check that your user ID is registered in the user registry for
your product.

A
superuser can view, edit, and delete all spaces and pages, can manage
and create templates, and can change ownership of a space by changing
the owner ID.

- Users belonging to the special user group, administrators,
have a superuser role by default. As a result, the superuser role
assignment is handled by user group membership.
- In a single-server environment, the IBM Business Automation Workflow server
creates the administrators user group in the
default user registry. The administrator ID provided during configuration
is automatically added as member of this group.
- In a network deployment environment, the administrators user
group is not created automatically. Use the createSuperUser.py script
to create the user group and add members to that group in the default
user registry.
- If
another user registry (for example, LDAP) is used instead of the default
user registry, or if the default user registry is used but you do
not want to use the administrators user group,
you must identify  the user group that you are using for the Heritage Process Portal superusers. Make sure that the value
that you provide can  be understood by the user registry. For example,
for LDAP, you might provide a name like  cn=administrators,dc=company,dc=com.
For more information about identifying this user group, see the instructions
for changing the administrators group in the What to do next section.
- For widgets in WebSphere Portal, the default group wpsadmins is
also used for the superuser role. Members of this group are granted
the superuser role.Note: Security must be enabled if you want to use
widgets in WebSphere Portal.

If administrative security is not enabled when you configure IBM Business Automation Workflow, only
the special user ID BPMAdministrator has the
superuser role.

- Make sure the default administrators group
name is not changed on the administrative console.
- Use the default file-based user repository for the user registry.
- Start the server or the deployment manager for your IBM Business Automation Workflow environment
for the profile where Heritage Process Portal is installed.

## Procedure

1. Locate the script install\_root\BusinessSpace\scripts\createSuperUser.py for
assigning the superuser role to a user.
2. Open a command prompt, and change directories to the following
directory: profile\_root\bin,
where profile\_root represents the directory for
the profile where IBM Business Automation Workflow is
installed.
3. Type the following command: wsadmin -lang jython
 -f install\_root\BusinessSpace\scripts\createSuperUser.py user\_short\_name password
where user\_short\_name is the unique identifier
for a user in Virtual Member Manager (VMM), and password is
the VMM password for that user. If that user exists in VMM, the user
is added to the administrator group. Note: When the path contains
a space, for example, if install\_root is My
install dir, you must enclose the path names in quotation
marks. For example, type the following command: wsadmin
-lang jython -f "\My install dir\BusinessSpace\scripts\createSuperUser.py" user\_short\_name\_in\_VMM.

## What to do next

To open the Business Space component,
use the following URL: http://host:port/BusinessSpace,
where host is the name of the host where your server
is running and port is the port number for your
server.

You can change the default special user group named adminstrators.
Perform the following steps to check the current group name or change
it to other name.

- profile\_root\BusinessSpace\node\_name\server\_name\mm.runtime.prof\config\ConfigService.properties on
a stand-alone server, or
- deployment\_manager\_profile\_root\BusinessSpace\cluster\_name\mm.runtime.prof\config\ConfigService.properties on
a cluster.

1. Make sure that the group exists in the user repository.
2. Modify the metric com.ibm.mashups.adminGroupName in
the configuration file profile\_root\BusinessSpace\node\_name\server\_name\mm.runtime.prof\config\ConfigService.properties.
3. Run the command updatePropertyConfig in the wsadmin environment
of the profile:$AdminTask updatePropertyConfig {-serverName server\_name -nodeName node\_name -propertyFileName
"profile\_root\BusinessSpace\node\_name\server\_name\mm.runtime.prof\config\ConfigService.properties"
-prefix "Mashups\_"}  and run $AdminConfig save.
4. Restart the server.

1. Make sure that the group exists in the user repository.
2. Modify the metric com.ibm.mashups.adminGroupName in
the configuration file deployment\_manager\_profile\_root\BusinessSpace\cluster\_name\mm.runtime.prof\config\ConfigService.properties.
3. Run the command updatePropertyConfig in the wsadmin environment
of the deployment environment profile:$AdminTask updatePropertyConfig
{-clusterName cluster\_name -propertyFileName "deployment\_manager\_profile\_root\BusinessSpace\cluster\_name\mm.runtime.prof\config\ConfigService.properties"
-prefix "Mashups\_"}  and run $AdminConfig save.
4. Restart the deployment manager.

1. Modify the metric noSecurityAdminInternalUserOnly in
the configuration file profile\_root\BusinessSpace\node\_name\server\_name\mm.runtime.prof\config\ConfigService.properties.
2. Run the command updatePropertyConfig in the wsadmin environment
of the profile:$AdminTask updatePropertyConfig {-serverName server\_name -nodeName node\_name -propertyFileName
"profile\_root\BusinessSpace\node\_name\server\_name\mm.runtime.prof\config\ConfigService.properties"
-prefix "Mashups\_"}  and run $AdminConfig save.
3. Restart the server.

1. Modify the metric noSecurityAdminInternalUserOnly in
the configuration file deployment\_manager\_profile\_root\BusinessSpace\cluster\_name\mm.runtime.prof\config\ConfigService.properties.
2. Run the command updatePropertyConfig in the wsadmin environment
of the deployment environment profile:$AdminTask updatePropertyConfig
{-clusterName cluster\_name -propertyFileName "deployment\_manager\_profile\_root\BusinessSpace\cluster\_name\mm.runtime.prof\config\ConfigService.properties"
-prefix "Mashups\_"}  and run $AdminConfig save.
3. Restart the deployment manager.