# modifyProjectArea command

## Syntax

```
configmgr\_cl modifyProjectArea 
 -profile myprofile
 -projectAreaName project\_area\_name
 -projectAreaDesc project\_area\_description
 -peConnPt connection\_point\_name
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
configmgr\_cl modifyProjectArea 
 -profile myDevelop1
 -projectAreaName CreditDisputeProject 
 -projectAreaDescription "Credit Dispute project area"
  [-silent] [-force]
```

```
configmgr\_cl modifyProjectArea 
 -profile myDevelop1
 -projectAreaName CreditDisputeProject
 -peConnPt P8connpoint
  [-silent] [-force]
```

```
configmgr\_cl modifyProjectArea -help
```