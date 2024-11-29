# Augmenting deployment manager profiles using the manageprofiles
command-line utility

## Before you begin

Remember to
shut down any servers associated with a profile you plan to augment.

```
runas /env /user:MyAdminName "manageprofiles.bat"
```

## Procedure

1. Use the augment parameter to make changes
to an existing profile with an augmentation template.  The augment parameter causes the manageprofiles command-line
utility to update or augment the profile identified in the -profileName parameter
using the template in the -templatePath parameter.
The file path for -templatePath need not be fully
qualified; install\_root/profileTemplates is
automatically added as a prefix. Note: Do not manually modify the files that are
located in the install\_root/profileTemplates/BPM directory.
2. Run the file from the command line.
The user name specified for the -adminUserName parameter
must already exist and it must have administrative privileges. The -adminAliasName parameter
is optional. Do not supply a -profilePath parameter.
For example:manageprofiles -augment -profileName profileName -templatePath BPM/BpmDmgr -adminAliasName CellAdminAlias -adminUserName adminUserName -adminPassword adminPassword
The status is written to the console window
when the command completes running.

## What to do next

- Add managed-node profiles to be managed by the deployment manager,
and then configure the deployment environment.

## Related reference

- Error running bootstrap command or creating profiles with SQL Server databases

## Related information

- manageprofiles parameters
- Removing a managed node profile from a deployment environment
- Creating or augmenting managed-node profiles on Windows
- DB2 log file error: SQL1092N "USERID does not have the authority to perform the requested command or operation."