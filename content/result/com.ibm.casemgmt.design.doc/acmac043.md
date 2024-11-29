# Exporting a case solution package by using the command line

## Before you begin

Ensure that the solution does not contain
locked items. You cannot export a solution that contains locked items.

Be sure to have your completed configuration checklist available.

## About this task

- The solution definition file.
- The connection definition.
- The task steps (stored as one XPDL file per case type).
- The Pages subfolder.
- The default page objects and any custom page objects that you created in the development
environment.
- Any documents, objects, or folders that were in the solution folder at the time of export,
including those added by the user.

## Procedure

To export the solution package:

1. Change the current directory to the
install\_root/CaseManagement/configure directory, where
install\_root is the location where Business Automation Workflow is
installed.
2 Run the following command. Do not enter any line breaks when youenter the command. configmgr\_cl exportSolution -profile myprofile -solutionName solution\_name | -solutionTemplateName template\_name -solutionPackage package\_file [-help] [-silent] [-force] -profile myprofile Specifies the profile to use. The myprofile value can be one of the following items: -solutionName solution\_name Specifies the solution to export. You can omit this option if you are exporting a solutiontemplate. -solutionTemplateName template\_name Specifies the solution template to export. You can omit this option if you are exporting asolution. -solutionPackage package\_file Specifies the full path and file name for the exported solution package ZIP file. If the pathincludes spaces, put the entire path in double quotation marks. For example, enter"C:\Solution Packages\Credit Dispute Solution.zip" . -help Optional and displays a brief message on the command syntax instead of running the command. -silent Optional: When you specify the -silent parameter, no prompts orinformational messages are shown in the console, but the errors are written to the log. Failuremessages and validation error messages are shown as needed, such as messages about missing passwordsor invalid port numbers. If you run the execute command to run all the tasks in aprofile and you specify the -silent parameter, you must also specify the-force parameter. -force Optional and applies only when the -silent parameter is used. When youspecify the -force parameter, the task is run without pausing for requiredresponses to validation error messages, such as messages about missing passwords or invalid portnumbers.

```
configmgr\_cl exportSolution -profile myprofile 
 -solutionName solution\_name | -solutionTemplateName template\_name 
 -solutionPackage package\_file
 [-help] [-silent] [-force]
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

## Results

## What to do next