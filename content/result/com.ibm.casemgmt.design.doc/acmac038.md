# listSolutions command

## Syntax

```
configmgr\_cl listSolutions -projectAreaName project\_area\_name
 -profile myprofile
 [-help]
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
configmgr\_cl listSolutions -projectAreaName MyProjectArea
 -profile MyDevelop1
```

```
configmgr\_cl listSolutions
 -projectAreaName dev\_env\_connection\_definition
 -profile MyDevelop1
```

```
configmgr\_cl listSolutions -help
```