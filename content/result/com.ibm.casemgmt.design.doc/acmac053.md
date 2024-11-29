# Creating and enabling a case history store by using the command
line

## Before you begin

## About this task

No code necessary.

You must specify a case management target object store
to associate with the case history store. You must also specify the
schema name for the case history store database, and a database connection.
If a database connection is not specified, the database connection
for the target object store is used.

https://ibmid.acrolinx.cloud
https://ibmid.acrolinx.cloud
https://ibmid.acrolinx.cloud

## Procedure

To create and enable a case history store:

1. Change the current directory to the
install\_root/CaseManagement/configure directory, where
install\_root is the location where Business Automation Workflow is
installed.
2 Create and enable a case history store by running the followingcommand. Do not enter any line breaks when you enter the command. configmgr\_cl createCaseHistoryStore -profile myprofile -cmtos target\_object\_store -schemaName schema\_name -dbConnName database\_connection [-help] -profile myprofile Specifies the profile to use. The myprofile value can be one of the following items: -cmtos target\_object\_store Specifies the display name for a case management target object store. -schemaName schema\_name Specifies the name of the schema to use for the case history store. -dbConnName database\_connection Specifies the display name of the database connection. You can view and define databaseconnections by using the Administration Console for Content PlatformEngine . -help Optional and displays a brief message on the command syntax insteadof running the command.

```
configmgr\_cl createCaseHistoryStore
 -profile myprofile
 -cmtos target\_object\_store
 -schemaName schema\_name
 -dbConnName database\_connection
  [-help]
```

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