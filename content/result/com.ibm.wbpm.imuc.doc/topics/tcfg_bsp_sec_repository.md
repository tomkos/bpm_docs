<!-- image -->

# Selecting the user repository for Heritage Process Portal (deprecated) and the Business Space component

## Before you begin

- You must have a user registry configured and application security enabled. For information about
application security, see Setting up security for the Business Space component and Process Portal.
- Check that your user ID is registered in the user registry for
your product.

## About this task

- Based on the type of LDAP configuration that you are using, your
settings can impact your ability to access Business Space correctly.
Make sure that the user filters, the group filters, and mapping settings
are configured properly. For more information, see Configuring Lightweight Directory Access Protocol
search filters in the WebSphere Application Server documentation.
- Based on the type of federated repository configuration that you
are using, your settings can affect your ability to access Business Space correctly.
Make sure that the realms are configured properly. For more information,
see Managing the realm in a federated repository configuration in
the WebSphere Application Server documentation.
- The LDAP security is set up by default to use the login property uid
(user ID) for searching in Business Space. If your LDAP
security is changed to use another unique LDAP field, such as mail (email
address) for the login property, then you must modify the userIdKey property in the
ConfigServices.properties file in order for searching to work in Business Space. Follow step 3 in the procedure.
- Process implementations must use user and group name forms that
match the form of the name being returned from the configured registry.Some
user registry configurations expose user and group names in a long
form. For example, the Lightweight Directory Access Protocol (LDAP)
registry uses the long form ("cn=User1,ou=test,o=ibm,c=us"). Other
configurations expose user and group names in a short form ("User1").
When
users and groups are assigned to teams in a process, either the short
form or the long form is used. If you switch to a different user registry
configuration, your existing process implementations stop working
if the new user registry configuration uses a different form for the
names. A stand-alone LDAP registry returns group names in the long
name format, while a federated repository returns only the short names.
- If you are using a Microsoft SQL
Server database and the Standalone LDAP registry,
make sure that the user distinguished name (user DN) does not exceed
450 characters. If any of the user DN entries exceed 450 characters,
you must designate the Federated repositories option
for the user account repository.
- If you are using Federated repositories,
you have additional capabilities in your widgets and framework, such
as enhanced search capabilities. When searching for users to share
spaces and pages, the search scope includes email, a full user name,
and user ID.

## Procedure

1. On the Global security administrative
console page, under User account repository,
designate either Federated repositories, Local
Operating System, Standalone LDAP registry,
or Standalone custom registry.
2. Restart the server.
3 If you want to change the default user repository fromthe default Federated repositories , modifythe MashupAdminForOOBSpace property in the ConfigServices.properties todesignate the correct user ID (the UID property for your user repository)as the valid administrator ID.
    1. Copy the modified file into an empty folder on your
system.  The ConfigServices.properties file
is located at profile\_root\BusinessSpace\node\_name\server\_name\mm.runtime.prof\config\ConfigService.properties for
a stand-alone server or deployment\_manager\_profile\_root\BusinessSpace\cluster\_name\mm.runtime.prof\config\ConfigService.properties for
a cluster.
    2 Run the updatePropertyConfig commandusing the wsadmin scripting client. Important: ForWindows, the value for the propertyFileName parametermust be the full path to the file, and all backslashes must be double,for example: AdminTask.updatePropertyConfig('[-serverName server\_name -nodeName node\_name -propertyFileName"profile\_root \\BusinessSpace\\node\_name \\server\_name \\mm.runtime.prof\\config\\ConfigService.properties"-prefix "Mashups\_"]') .
        - For a stand-alone server: 
AdminTask.updatePropertyConfig('[-serverName server\_name -nodeName node\_name 
-propertyFileName "profile\_root\BusinessSpace\node\_name\server\_name
\mm.runtime.prof\config\ConfigService.properties" -prefix "Mashups\_"]')
AdminConfig.save()
        - For a cluster:
AdminTask.updatePropertyConfig('[-clusterName cluster\_name -propertyFileName
 "deployment\_manager\_profile\_root\BusinessSpace\cluster\_name\mm.runtime.prof\
config\ConfigService.properties" -prefix "Mashups\_"]')
AdminConfig.save()
3. Log into Heritage Process Portal and reassign the owners of the default
spaces to the new administrator ID.
4 If you are using an LDAP repository with a unique LDAPfield, such as mail (email address) for thelogin property instead of uid (user ID), modifythe userIdKey property in the ConfigServices.properties filein order for searching to work in Business Space .

1. Locate the ConfigServices.properties file
at profile\_root\BusinessSpace\node\_name\server\_name\mm.runtime.prof\config\ConfigService.properties for
a stand-alone server or deployment\_manager\_profile\_root\BusinessSpace\cluster\_name\mm.runtime.prof\config\ConfigService.properties for
a cluster.
2. Change the userIdKey attribute from uid to
match the login property for your LDAP user repository, for example, mail.
3. Copy the modified file into an empty folder on your
system.
4 Run the updatePropertyConfig commandusing the wsadmin scripting client. Important: ForWindows, the value for the propertyFileName parametermust be the full path to the file, and all backslashes must be double,for example: AdminTask.updatePropertyConfig('[-serverName server\_name -nodeName node\_name -propertyFileName"profile\_root \\BusinessSpace\\node\_name \\server\_name \\mm.runtime.prof\\config\\ConfigService.properties"-prefix "Mashups\_"]') .
    - For a stand-alone server: 
AdminTask.updatePropertyConfig('[-serverName server\_name -nodeName node\_name 
-propertyFileName "profile\_root\BusinessSpace\node\_name\server\_name
\mm.runtime.prof\config\ConfigService.properties" -prefix "Mashups\_"]')
AdminConfig.save()
    - For a cluster:
AdminTask.updatePropertyConfig('[-clusterName cluster\_name -propertyFileName
 "deployment\_manager\_profile\_root\BusinessSpace\cluster\_name\mm.runtime.prof\
config\ConfigService.properties" -prefix "Mashups\_"]')
AdminConfig.save()
5 If you want to restrict logging in to Heritage Process Portal to a subset of users and groups, youcan change the mapping of the Business Space Java™ EE security role. Changing the Java EE securityrole mapping does not affect the user/group search function in BusinessSpace.

1. Update the user/group mapping for two
enterprise applications: BSpaceEAR\_node\_server and mm.was\_node\_server (for
a stand-alone server environment) or BSpaceEAR\_cluster and mm.was\_cluster (for
a network deployment environment).
2. Click Applications > Application Types > WebSphere enterprise
applications and select the two applications.
3. Under Detail Properties, select  Security role to user/group mapping.
4. Remap the businessspaceusers and Allauthenticated roles
from the two applications by first removing the special subject.
5. Click Map Special Subjects and
select None.
6. Click Map Users or Map
Groups and assign each role to your selected users or
groups.
6. Restart the server.
7. Log in to Heritage Process Portal and reassign the owners of the default
spaces to the new administrator ID.

## What to do next

- To set authorization to pages and spaces in Heritage Process Portal, you can manage authorization when creating
the pages and spaces.
- To designate who can perform administrator actions in Heritage Process Portal, see Assigning the superuser role.

If you find the following errors in the SystemOut.log file,
you might have extra attributes in your user registry that cannot
be processed:

```
00000046 SystemErr R Caused by: com.ibm.websphere.wim.exception.WIMSystemException: CWWIM1013E  
    The value of the property secretary is not valid for entity uid=xxx,c=us,ou=yyy,o=ibm.com. 
00000046 SystemErr R at com.ibm.ws.wim.adapter.ldap.LdapAdapter.setPropertyValue(LdapAdapter.java:3338)
```

```
com.ibm.mashups.user.userProfile = LIMITED
com.ibm.mashups.user.groupProfile = LIMITED
```

The ConfigServices.properties file
is located at profile\_root\BusinessSpace\node\_name\server\_name\mm.runtime.prof\config\ConfigService.properties for
a stand-alone server or deployment\_manager\_profile\_root\BusinessSpace\cluster\_name\mm.runtime.prof\config\ConfigService.properties for
a cluster. After modifying the ConfigServices.properties file,
run the updatePropertyConfig command using the
wsadmin scripting client by following the instructions in step 4.d.

If
you have Java EE security enabled
in a cluster, consider tightening the entry in the server policy applied
to the Business Space help location.

The Business Space help
location policy is:

grant codeBase     "file:${was.install.root}/profiles/profile\_name/temp/node\_name/-"
{

permission java.security.AllPermission;

};

Tighten
the policy by changing it to:

grant codeBase     "file:${was.install.root}/profiles/profile\_name/temp/node\_name/server\_name/BSpaceHelpEAR\_node\_name\_server\_name/BSpaceHelp.war/-"
{

permission java.security.AllPermission;

};