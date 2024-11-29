# defineProjectArea command

## Syntax

```
configmgr\_cl defineProjectArea 
 -profile myprofile
 -projectAreaName project\_area\_name
 -projectAreaDesc project\_area\_description
 -peConnPt connection\_point\_name
  [-silent] [-force] [-help]
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
configmgr\_cl defineProjectArea 
 -profile myDevelop1
 -projectAreaName dev\_env\_connection\_definition
 -projectAreaDesc "Default project area for myDevelop1"
 -peConnPt connpoint1
  [-silent] [-force]
```

```
configmgr\_cl defineProjectArea 
 -profile myDevelop1
 -projectAreaName CreditDisputeArea
 -projectAreaDesc "Credit card dispute project area for myDevelop1"
 -peConnPt connpoint1
  [-silent] [-force]
```

```
configmgr\_cl defineProjectArea -help
```