# importSolution command

## Syntax

```
configmgr\_cl importSolution -profile myprofile 
 -solutionPackage package\_file
 -projectAreaName project\_area\_name 
 -serviceDataMap service\_data\_map\_name
 -objectStoreDataMap object\_store\_data\_map\_name
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
configmgr\_cl importSolution -profile myDevelop1 
 -solutionPackage "C:\solution packages\Solution1.zip"
 -projectArea "Credit Dispute"
```

```
configmgr\_cl importSolution -profile myDevelop1 
 -solutionPackage "C:\solution packages\Solution1.zip"
 -projectArea "Credit Dispute" 
 -serviceDataMap "C:\solution packages\sevice\_data\_map.xml"
```

```
configmgr\_cl importSolution -help
```