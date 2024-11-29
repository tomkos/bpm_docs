# exportSolutionSecurityManifest command

## Syntax

```
configmgr\_cl exportSolutionSecurityManifest -profile myprofile 
 -manifestNames manifest\_names -manifestPackage manifest\_package\_file 
 -solutionName solution\_name [-silent] [-force] [-help]
```

## Parameters

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
configmgr\_cl exportSolutionSecurityManifest -profile myDevelop1 
 -manifestNames Security1 
 -manifestPackage "C:\Program Files (x86)\IBM\CaseManagement\solution\_packages\Security1.zip"
 -solutionName MySolution
```

```
configmgr\_cl exportSolutionSecurityManifest -help
```