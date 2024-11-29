# Importing a solution from a manifest by using the command line

## Before you begin

Run the extract script that you created for the VCS to extract the manifest and related solution
files.

## Procedure

1. Change the current directory to the
install\_root/CaseManagement/configure directory, where
install\_root is the location where Business Automation Workflow is
installed.
2 Import the solution manifest by running the following command. Do not enter any line breakswhen you enter the command. configmgr\_cl importSolutionManifest -profile myprofile -solutionManifest mymanifest -projectAreaName project\_area\_name [-silent] [-force] [-help] -profile myprofile Specifies the profile to use. The myprofile value can be one of the following items: -solutionManifest mymanifest The full path to the solution manifest that you want to import. If the path includes adirectory name with spaces, enclose the path in double quotation marks. For example, enter"C:\Solution Manifests\PREFIX\_Manifest.json" . Any files that are relatedto the solution manifest must be in the same folder as the solution manifest. Important: Do not rename any of the extracted files including the solution manifest file. Donot modify the content of any of the extracted files. -projectAreaName project\_area\_name Specifies the name of the project area for the solution. This option is valid only for importinga solution package to into another development environment. -silent Optional: When you specify the -silent parameter, no prompts orinformational messages are shown in the console, but the errors are written to the log. Failuremessages and validation error messages are shown as needed, such as messages about missing passwordsor invalid port numbers. If you run the execute command to run all the activitiesin a profile and you specify the -silent parameter, you must also specify the-force parameter. -force Optional and applies only when the -silent parameter is used. When youspecify the -force parameter, the activity is run without pausing for requiredresponses to validation error messages, such as messages about missing passwords or invalid portnumbers. -help Optional: Shows a brief message on the command syntax instead of running the command.

```
configmgr\_cl importSolutionManifest -profile myprofile 
 -solutionManifest mymanifest
 -projectAreaName project\_area\_name 
 [-silent] [-force] [-help]
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

If the path includes a
directory name with spaces, enclose the path in double quotation marks. For example, enter
"C:\Solution Manifests\PREFIX\_Manifest.json".

Any files that are related
to the solution manifest must be in the same folder as the solution manifest.