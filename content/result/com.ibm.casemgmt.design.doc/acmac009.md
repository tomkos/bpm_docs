# test command

## Syntax

```
configmgr\_cl test -task task\_type | -taskfile task\_file\_name
 -profile myprofile [-silent][-force][-help]
```

## Parameters

| Option              | Configuration file                                                        | Description                                                                                                                                                                                                                                                                                                    |
|---------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| configibmbpm        | configibmbpm.xml                                                          | Tests the connection between the Case configuration tool, the IBM® Business Automation Workflow host server, and the Content Platform Engine server.                                                                                                                                                           |
| deploysolution      | deploysolution.xml deploysolution.n.xml. n is an integer starting with 2. | Opens the role assignment page for you to assign LDAP users to the roles for this solution. You must run the configmgr\_cl execute -taskfile deploysolution.n -profile myprofile before you assign roles. You can also assign users later in Case Client.                                                       |
| registeradmin       | registeradmin.xml                                                         | Test the connection between the Case configuration tool and the IBM Content Navigator server and verifies the ID for the selected plug-in.                                                                                                                                                                     |
| registercpeapplets  | registercpeapplets.xml                                                    | This task registers the plug-in for IBM Content Navigator that contains the IBM FileNet® Process Designer applet.Tip: Run this task only if you want to launch the IBM FileNet Process Designer applet from Case Builder. You do not need to run this task to use the standalone IBM FileNet Process Designer. |
| registerprojectarea | registerprojectarea.xml                                                   | Test the connection between the Case configuration tool and the IBM Content Navigator server and verifies the Case Operations user credentials.                                                                                                                                                                |
| registerservices    | registerservices.xml                                                      | Test the connection between the Case configuration tool and the IBM Content Navigator server and verifies the ID for the selected plug-in.                                                                                                                                                                     |
| registertargetenv   | registertargetenv.xml                                                     | Test the connection between the Case configuration tool and the IBM Content Navigator server and verifies the Case Operations user credentials.                                                                                                                                                                |

- The name of the profile, such as develop1. The profile is located in the
install\_root/CaseManagement/configure/profiles directory.
install\_root is the location where IBM Business Automation
Workflow is installed.
- The full path to the profile directory, such as
"install\_root\CaseManagement\configure\profiles\develop1" or
/install\_root/CaseManagement/configure/profiles/develop1.
- The full path to the profile input file, such as
"install\_root\CaseManagement\configure\profiles\develop1\develop1.cfgp"
or
/install\_root/CaseManagement/configure/profiles/develop1/develop1.cfgp.

## Sample commands

```
configmgr\_cl test -task deploysolution -profile deploy\_one
```

```
configmgr\_cl test -taskfile deploysolution.2.xml
 -profile deploy\_many
```

```
configmgr\_cl test -taskfile deploysolution.2.xml 
-profile  c:\temp\myprofiles\deploy\_many
```

```
configmgr\_cl test -help
```