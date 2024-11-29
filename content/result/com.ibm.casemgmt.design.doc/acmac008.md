# storePasswords command

## Syntax

```
There are no missing passwords to store.
```

```
configmgr\_cl storePasswords [-task task\_type | -taskfile task\_file\_name]
 -profile myprofile [-help]
```

## Parameters

The -task task\_type parameter
specifies a specific task to encrypt the passwords for. You can omit
the -task task\_type parameter
if you want to store passwords for all the tasks or if you specify
the -taskfile task\_file\_name parameter.

| Password description                          | Property name and XML file name                                                                                                                      |
|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Application server administrator password     | ApplicationServerAdminPassword property in the websphereapplicationserver.xml file.                                                                  |
| IBM® Content Navigator administrator password | NexusPassword property in the contentnavigatorserver.xml file                                                                                        |
| Content Platform Engine domain user password  | CEPassword property in the contentengineserver.xml file                                                                                              |
| Directory service bind user password          | LDAPBindPassword property in the configureldap.xml file                                                                                              |
| Case operations password                      | CaseOperationsPassword property in the registerprojectarea.xml file (development environment) or registertargetenv.xml file (production environment) |
| LTPA key password                             | LTPAKeyPassword property in the importltpakey.xml file                                                                                               |

When you specify a specific task for the storePasswords command, encrypted
passwords are added to the task file, the websphereapplicationserver.xml file,
the contentnavigatorserver.xml file, and the
contentengineserver.xml file. The following table describes the valid
task\_type and task\_file\_name values, the password property
names, and the task configuration XML file names that are affected by the task options.

|  task\_type values      |  task\_file\_name values   | Description                                                                                                                                                                                                                                                                |
|------------------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| No value is specified. | No value is specified.   | Encrypts the passwords for all the tasks in the profile, as listed in Table 1.                                                                                                                                                                                             |
| configbox              | configbox.xml            | Encrypts the password configuring the Box host properties.                                                                                                                                                                                                                 |
| configibmbpm           | configibmbpm.xml         | Encrypts the password configuring the IBM Business Automation Workflow host properties.                                                                                                                                                                                    |
| configrules            | configrules.xml          | Lists the task that configures business rules in your solution.                                                                                                                                                                                                            |
| registerprojectarea    | registerprojectarea.xml  | Encrypts the case operations user password that is stored in CaseOperationsPassword property in the registerprojectarea.xml file and the IBM Content Navigator administrator password that is stored in the NexusPassword property in the contentnavigatorserver.xml file. |
| registertargetenv      | registertargetenv.xml    | Encrypts the case operations user password that is stored in CaseOperationsPassword property in the registertargetenv.xml file and the IBM Content Navigator administrator password that is stored in the NexusPassword property in the contentnavigatorserver.xml file.   |

Specifies the configuration XML file to encrypt the passwords
for. You can omit the -taskfile task\_file\_name parameter
if you want to store passwords for all the tasks or if you specify
the -task task\_type parameter.

If
you omit the -task task\_type parameter
and the -taskfile task\_file\_name parameter,
you are prompted to enter the passwords for each configuration XML
file in the profile. Each password is encrypted before it is added
to the XML file. The passwords that you enter depend on the type of
profile, which is described in Table 1.

See Table 2 for the valid task\_file\_name values
and passwords.

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
configmgr\_cl storePasswords -profile develop1
```

```
configmgr\_cl storePasswords -help
```