<!-- image -->

# Enabling searches for user registries without wildcards

## Before you begin

- Enable application security and administrative security. See Setting up security for the Business Space component and Process Portal.
- Check that your user ID is registered in the user registry for
your product.

## About this task

By default, when a Heritage Process Portal user searches for users or groups by
typing one or more characters, Heritage Process Portal automatically adds wildcard characters.
For example, if the user registry is an LDAP server and the user types smit, Heritage Process Portal converts this into a *smit* query
so that the return includes names like Smith, Smithers,
and Psmith. However, if you do not want
the automatic wildcards because, for example, your user registry does
not permit them, you can disable this functionality.

To
turn off the automatic wildcard searches for your environment, complete
the following steps.

## Procedure

- For a stand-alone server, complete the following steps:
    1. Update the profile\_root\BusinessSpace\node\_name\server\_name\mm.runtime.prof\config\ConfigService.properties configuration
file with com.ibm.mashups.user.stripWildcards=true.
    2. Run the updatePropertyConfig command
in the wsadmin environment of the profile: The following
example uses Jython:  
AdminTask.updatePropertyConfig('[-serverName server\_name -nodeName node\_name -propertyFileName
"profile\_root\BusinessSpace\node\_name\server\_name\mm.runtime.prof\config\ConfigService.properties"
-prefix "Mashups\_"]')
AdminConfig.save()

Important: For Windows, the value for the propertyFileName parameter
must be the full path to the file, and all backslashes must be double,
for example: AdminTask.updatePropertyConfig('[-serverName server\_name -nodeName node\_name -propertyFileName
"profile\_root\\BusinessSpace\\node\_name\\server\_name\\mm.runtime.prof\\config\\ConfigService.properties"
-prefix "Mashups\_"]').

The following example
uses Jacl: 
$AdminTask updatePropertyConfig {-serverName server\_name -nodeName node\_name -propertyFileName
"profile\_root\BusinessSpace\node\_name\server\_name\mm.runtime.prof\config\ConfigService.properties"
-prefix "Mashups\_"}
$AdminConfig save
    3. Restart the server.
- For a cluster, complete the following steps:

1. Update the deployment\_manager\_profile\_root\BusinessSpace\cluster\_name\mm.runtime.prof\config\ConfigService.properties configuration
file with com.ibm.mashups.user.stripWildcards=true.
2. From the deployment manager, run the updatePropertyConfig command
in the wsadmin environment of the profile: The following
example uses Jython:  
AdminTask.updatePropertyConfig('[-clusterName cluster\_name -propertyFileName
"deployment\_manager\_profile\_root\BusinessSpace\cluster\_name\mm.runtime.prof\config\ConfigService.properties"
-prefix "Mashups\_"]')
AdminConfig.save()

The following example uses Jacl: 
$AdminTask
updatePropertyConfig {-clusterName cluster\_name -propertyFileName
"deployment\_manager\_profile\_root\BusinessSpace\cluster\_name\mm.runtime.prof\config\ConfigService.properties"
-prefix "Mashups\_"}
$AdminConfig save
3. Restart the deployment manager.