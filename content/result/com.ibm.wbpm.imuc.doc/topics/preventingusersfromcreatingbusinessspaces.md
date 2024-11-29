<!-- image -->

# Preventing users from creating spaces

## About this task

These superusers (or Heritage Process Portal administrators) can create a space and
transfer ownership to other users. The users who are assigned ownership
of spaces can then administer the spaces as if they had created them.
For example, they can set who can view and edit the space and its
properties and they can add pages. Other than the superuser role,
you cannot define groups or individual users who are allowed to create
spaces.

To limit creating spaces to superusers only, complete
the following steps.

## Procedure

1 Change the com.ibm.mashups.lockeddown settingto true in the configuration file: The default value of false meansthat all users can create spaces. When the value is true ,only superusers can create spaces.
    - For a stand-alone server: profile\_root\BusinessSpace\node\_name\server\_name\mm.runtime.prof\config\ConfigService.properties
    - For a cluster: deployment\_manager\_profile\_root\BusinessSpace\cluster\_name\mm.runtime.prof\config\ConfigService.properties
2 Run the updatePropertyConfig commandin the wsadmin environment of the profile:

- For a stand-alone server: The following example
uses Jython:  
AdminTask.updatePropertyConfig('[-serverName server\_name -nodeName node\_name 
-propertyFileName "profile\_root\BusinessSpace\node\_name\server\_name
\mm.runtime.prof\config\ConfigService.properties" -prefix "Mashups\_"]')
AdminConfig.save()Important: For Windows,
the value for the propertyFileName parameter
must be the full path to the file, and all backslashes must be double,
for example: AdminTask.updatePropertyConfig('[-serverName server\_name -nodeName node\_name -propertyFileName
"profile\_root\\BusinessSpace\\node\_name\\server\_name\\mm.runtime.prof\\config\\ConfigService.properties"
-prefix "Mashups\_"]').

 
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

## Results