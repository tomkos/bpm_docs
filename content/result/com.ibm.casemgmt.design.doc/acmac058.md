# applySolutionSecurityManifest command

## Syntax

```
configmgr\_cl applySolutionSecurityManifest
 -profile myprofile
 -targetEnvName target\_environment\_name
 -solutionName solution\_name
 -manifestName manifest\_name
  [-silent][-force][-help]
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