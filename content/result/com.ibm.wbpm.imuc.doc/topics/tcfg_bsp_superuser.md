<!-- image -->

# Assigning the superuser role

## Before you begin

- Enable application security and administrative security. See Setting up security for the Business Space component and Process Portal.
- Check that your user ID is registered in the user registry for
your product.

## About this task

Assign the superuser role by using the following application
server security role: Admin. Using this method
gives you flexibility in assigning the role to any number of your
organization's existing groups and users. It doesn't require the creation
of an administrators group in the user registry for the sole purpose
of acting as the focal point for the superuser.

If you already have a Business Space superuser assigned
from an earlier version than V7.5, you can modify the superuser by user group instead. See Assigning the superuser by user group.

## Procedure

- If you are setting up administrators with the superuserrole for the first time, complete the following steps.
    1. Log in to the administrative console for your product.
    2 Click Applications > Application Types > WebSphere enterpriseapplications and select one of the followingapplications:
        - mm.was\_node\_server (for
a stand-alone server environment)
        - mm.was\_cluster (for
a network deployment environment)
3. Click Security role to user/group mappings.
4. Select the row for the Admin role,
and click the Map Users button or the Map
Groups button to map either users or groups to the Admin
role.
5. Click Save.
6. Restart the server.
- If you previously assigned superusers based on user groups,and you want to switch to this simpler way to manage superusers byrole, complete the following steps.

1 Open the configuration file.
    - For a stand-alone server: profile\_root\BusinessSpace\node\_name\server\_name\mm.runtime.prof\config\ConfigService.properties
    - For a cluster: deployment\_manager\_profile\_root\BusinessSpace\cluster\_name\mm.runtime.prof\config\ConfigService.properties
2. Change the following property values in the configuration
file as shown: com.ibm.mashups.adminGroupName
= {com.ibm.mashups.J2EERole.Admin}  
com.ibm.mashups.widget.attributes.configure.groups=
3 Run the updatePropertyConfig commandin the wsadmin environment of the profile. Important: For Windows, the value for the propertyFileName parametermust be the full path to the file, and all backslashes must be double,for example: AdminTask.updatePropertyConfig('[-serverName server\_name -nodeName node\_name -propertyFileName"profile\_root \\BusinessSpace\\node\_name \\server\_name \\mm.runtime.prof\\config\\ConfigService.properties"-prefix "Mashups\_"]') .

- For a stand-alone server: The following example uses Jython:
 
AdminTask.updatePropertyConfig('[-serverName server\_name -nodeName node\_name 
-propertyFileName "profile\_root\BusinessSpace\node\_name\server\_name
\mm.runtime.prof\config\ConfigService.properties" -prefix "Mashups\_"]')
AdminConfig.save()
 
The
following example uses Jacl: 
$AdminTask updatePropertyConfig {-serverName server\_name -nodeName node\_name
 -propertyFileName "profile\_root\BusinessSpace\node\_name\server\_name
\mm.runtime.prof\config\ConfigService.properties" -prefix "Mashups\_"}
$AdminConfig save
- For a cluster:The following example uses Jython:  
AdminTask.updatePropertyConfig('[-clusterName cluster\_name -propertyFileName
 "deployment\_manager\_profile\_root\BusinessSpace\cluster\_name\mm.runtime.prof\
config\ConfigService.properties" -prefix "Mashups\_"]')
AdminConfig.save()
The following example uses Jacl: 
$AdminTask updatePropertyConfig {-clusterName cluster\_name -propertyFileName
 "deployment\_manager\_profile\_root\BusinessSpace\cluster\_name\mm.runtime.prof\
config\ConfigService.properties" -prefix "Mashups\_"}
$AdminConfig save
4. Restart the server.
5. Use the previous procedure to assign users to the Business Space superuser roles.