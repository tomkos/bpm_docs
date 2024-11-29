# Importing a security configuration by using the command line

## Before you begin

The solution that the security configurations are associated with must already be in the
    design object store.

## About this task

## Procedure

To import the security configuration package:

1. Change the current directory to the
install\_root/CaseManagement/configure directory, where
install\_root is the location where Business Automation Workflow is
installed.
2 Import the security configuration package by running the following command. Do not enter any line breaks when you enter the command. configmgr\_cl importSolutionSecurityManifest -profile myprofile -manifestPackage manifest\_package\_file [-silent] [-force] [-help] -profile myprofile Specifies the profile to use. The myprofile value can be one of the following items: -manifestPackage manifest\_package\_file Specifies the full path and file name of the security configuration package ZIP file. If the path includes spaces, put the entire path in double quotation marks. For example, enter "C:\Security Packages\Security1.zip" . -silent Optional: When you specify the -silent parameter, no prompts orinformational messages are shown in the console, but the errors are written to the log. Failuremessages and validation error messages are shown as needed, such as messages about missing passwordsor invalid port numbers. If you run the execute command to run all the activitiesin a profile and you specify the -silent parameter, you must also specify the-force parameter. -force Optional and applies only when the -silent parameter is used. When youspecify the -force parameter, the activity is run without pausing for requiredresponses to validation error messages, such as messages about missing passwords or invalid portnumbers. -help Optional: Shows a brief message on the command syntax instead of running the command.

```
configmgr\_cl importSolutionSecurityManifest -profile myprofile 
 -manifestPackage manifest\_package\_file 
 [-silent] [-force] [-help]
```

    - The name of the profile, such as develop1. The profile is located in the
install\_root/CaseManagement/configure/profiles directory.
install\_root is the location where IBM® Business Automation
Workflow is installed.
    - The full path to the profile directory, such as
"install\_root\CaseManagement\configure\profiles\develop1" or
/install\_root/CaseManagement/configure/profiles/develop1.
    - The full path to the profile input file, such as
"install\_root\CaseManagement\configure\profiles\develop1\develop1.cfgp"
or
/install\_root/CaseManagement/configure/profiles/develop1/develop1.cfgp.