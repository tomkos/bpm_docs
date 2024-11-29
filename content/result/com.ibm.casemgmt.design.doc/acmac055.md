# Applying an audit configuration by using the command line

## Before you begin

## Procedure

To apply an audit configuration:

1. Change the current directory to the
install\_root/CaseManagement/configure directory, where
install\_root is the location where Business Automation Workflow is
installed.
2 Apply the audit configuration by running the followingcommand. Do not enter any line breaks when you enter the command. configmgr\_cl applySolutionAuditManifest -profile myprofile -targetEnvName target\_environment\_name -solutionName solution\_name -manifestName manifest\_name [-help] -profile myprofile Specifies the profile to use. The myprofile value can be one of the following items: -targetEnvName target\_environment\_name Specifies the name of the target environment. This argument is required only on productionenvironments. -solutionName solution\_name Specifies the name of the solution that is associated with the audit configuration. -manifestName manifest\_name Specifies the name of the audit manifest. -help Optional and displays a brief message on the command syntax insteadof running the command.

```
configmgr\_cl applySolutionAuditManifest
 -profile myprofile
 -targetEnvName target\_environment\_name
 -solutionName solution\_name
 -manifestName manifest\_name
  [-help]
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