# exportSolution command

## Syntax

```
configmgr\_cl exportSolution -profile myprofile 
 -solutionName solution\_name | -solutionTemplateName template\_name 
 -solutionPackage package\_file
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

## Sample commands

```
configmgr\_cl exportSolution -profile myDevelop1 
 -solutionName Solution1 
 -solutionPackage "C:\Program Files (x86)\IBM\CaseManagement\solution\_packages\Solution1.zip"
```

```
configmgr\_cl exportSolution -profile myDevelop1 
 -solutionTemplateName Template1 
 -solutionPackage "C:\Program Files (x86)\IBM\CaseManagement\solution\_packages\Template1.zip"
```

```
configmgr\_cl exportSolution -help
```