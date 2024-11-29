# importSolutionManifest command

## Syntax

```
configmgr\_cl importSolutionManifest -profile myprofile 
 -solutionManifest mymanifest
 -projectAreaName project\_area\_name 
 [-silent] [-force] [-help]
```

## Parameters

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

If the path includes a
directory name with spaces, enclose the path in double quotation marks. For example, enter
"C:\Solution Manifests\SOL1\_Manifest.json".

Any files that are related
to the solution manifest must be in the same folder as the solution manifest.

## Sample commands

```
configmgr\_cl importSolutionManifest -profile myDevelop1 
 -solutionManifest "C:\Solution Manifests\SOL1\_Manifest.json"
 -projectArea "Credit Dispute"
```

```
configmgr\_cl importSolutionManifest -help
```