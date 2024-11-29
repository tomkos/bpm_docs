# Exporting a security configuration by using the command line

## About this task

The exportSolutionSecurityManifest command exports a list of security
configurations that are associated with a solution to prepare for importing the security
configurations to another IBM® Business Automation
Workflow environment.
Security configuration settings are stored in a security manifest file. You must specify a
development environment or production environment profile with this command to provide information
about the Content Platform Engine server that contains the
security configuration. You can specify the path for the security configuration package or omit the
value to use the default name and path.

## Procedure

To export the security configuration:

1. Change the current directory to the
install\_root/CaseManagement/configure directory, where
install\_root is the location where Business Automation Workflow is
installed.
2 Run the following command. Do not enter any line breaks when you enter the command. configmgr\_cl exportSolutionSecurityManifest -profile myprofile -manifestNames manifest\_names -manifestPackage manifest\_package\_file -solutionName solution\_name [-silent] [-force] [-help] -profile myprofile Specifies the profile to use. The myprofile value can be one of the following items: -manifestNames manifest\_names Specifies the name of the security manifest. To specify more than one manifest at a time, enter multiple -manifestNames options with the command. -manifestPackage manifest\_package\_file Specifies the exported security package ZIP file. You can specify the full path and file name for the exported security package ZIP file. If the path includes spaces, put the entire path in double quotation marks. For example, enter "C:\Security Packages\Security1.zip" . If you specify only the file name, the security package is exported to the ICM\_Home /CaseManagement/configure directory. If you do not specify an option for -manifestPackage , the security package is exported to ICM\_Home /CaseManagement/solution\_packages/SolutionName \_securityManifest.zip . -solutionName solution\_name Specifies the name of the solution that is associated with the security configuration. -silent Optional: When you specify the -silent parameter, no prompts orinformational messages are shown in the console, but the errors are written to the log. Failuremessages and validation error messages are shown as needed, such as messages about missing passwordsor invalid port numbers. If you run the execute command to run all the activitiesin a profile and you specify the -silent parameter, you must also specify the-force parameter. -force Optional and applies only when the -silent parameter is used. When youspecify the -force parameter, the activity is run without pausing for requiredresponses to validation error messages, such as messages about missing passwords or invalid portnumbers. -help Optional: Shows a brief message on the command syntax instead of running the command.

```
configmgr\_cl exportSolutionSecurityManifest -profile myprofile 
 -manifestNames manifest\_names -manifestPackage manifest\_package\_file 
 -solutionName solution\_name [-silent] [-force] [-help]
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

## Results

## What to do next