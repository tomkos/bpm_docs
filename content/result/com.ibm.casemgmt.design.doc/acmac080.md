# Creating and enabling a Case Analyzer store by using the
command line

## About this task

You must specify a case management target object store to associate with the Case Analyzer store.

In addition, you must specify the name of the schema to use for the Case Analyzer store. This schema must be present in the database that the
Case Analyzer store will use before you create and enable the
store.

You can specify a database connection. If you do not specify a database connection, the database
connection for the target object store is used.

## Procedure

To create and enable a Case Analyzer
store:

1 Prepare the database for the Case Analyzer store. For more information, see Database administrator installation tasks .
    1. Create JDBC data sources. Run the Configure JDBC Data Sources task by using the IBM®
FileNet® P8 Configuration Manager.
For more information, see Editing the Configure JDBC Data Sources tasks and Configuration Manager reference.
    2. Create a database connection.
For more information, see Creating a database connection. Based on performance
considerations, you might want to share data sources. For more information, see Sharing data sources. You enter the database schema name when
you configure and enable the Case Analyzer store by using the Case administration client.
2. Change the current directory to the
install\_root/CaseManagement/configure directory, where
install\_root is the location where Business Automation Workflow is
installed.
3 Create and enable a Case Analyzer store by running thefollowing command. Do not enter any line breaks when you enter the command. configmgr\_cl createCaseAnalyzerStore -profile myprofile -cmtos target\_object\_store -schemaName schema\_name -dbConnName database\_connection -eventPruneSchedule pruning\_time -publishInterval update\_interval [-silent][-force][-help] -profile myprofile Specifies the profile to use. The myprofile value can be one of the following items: -cmtos target\_object\_store Specifies the display name for a case management target object store. -schemaName schema\_name Specifies the name of the schema to use for the Case Analyzer store. -dbConnName database\_connection Specifies the display name of the database connection. You can view and define databaseconnections by using the Administration Console for Content PlatformEngine . -eventPruneSchedule pruning\_time Specifies the time each day when unneeded data is to be pruned from the database. Enter the timein the following format: HH:MM:SS If you do not specify a time, pruning isdisabled. -publishInterval update\_interval Specifies the interval in minutes when the IBM Case Monitor Dashboard data is to be updated. Ifyou do not specify an interval, the data is updated every 5 minutes. -silent Optional: When you specify the -silent parameter, no prompts orinformational messages are shown in the console, but the errors are written to the log. Failuremessages and validation error messages are shown as needed, such as messages about missing passwordsor invalid port numbers. If you run the execute command to run all the activitiesin a profile and you specify the -silent parameter, you must also specify the-force parameter. -force Optional and applies only when the -silent parameter is used. When youspecify the -force parameter, the activity is run without pausing for requiredresponses to validation error messages, such as messages about missing passwords or invalid portnumbers. -help Optional: Shows a brief message on the command syntax instead of running the command.

```
configmgr\_cl createCaseAnalyzerStore
 -profile myprofile
 -cmtos target\_object\_store
 -schemaName schema\_name
 -dbConnName database\_connection
 -eventPruneSchedule pruning\_time
 -publishInterval update\_interval
 [-silent][-force][-help]
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

If you do not specify a time, pruning is
disabled.