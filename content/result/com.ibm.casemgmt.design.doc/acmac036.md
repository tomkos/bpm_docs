# addPrincipals command

## Syntax

```
configmgr\_cl addPrincipals -projectAreaName project\_area\_name
 -profile myprofile
 [-users user\_name] [-groups group\_name]
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

Specifies the short name or display name of the user that you
want to add. A user can belong to the default project area and one
other project area. If you add a user to a nondefault project area,
that user is removed from any other nondefault project area.

You
can add multiple users at one time by adding additional -users user\_name entries
on the same command.

You can omit this option if you are adding
only groups.

Specifies the short name or display name of the group that
you want to add. You can add groups only to the default project area.

You
can add multiple groups at one time by adding additional -groups group\_name entries
on the same command.

You can omit this option if you are adding
only users.

## Sample commands

```
configmgr\_cl addPrincipals -projectAreaName MyProjectArea
 -profile MyDevelop1
 -users MariaG
```

```
configmgr\_cl addPrincipals -projectAreaName dev\_env\_connection\_definition
 -profile MyDevelop1
 -groups CaseDevelopers
```

```
configmgr\_cl addPrincipals -projectAreaName MyProjectArea
 -profile MyDevelop1
 -users MariaG -users BarneyF -users JoseP
```

```
configmgr\_cl addPrincipals -projectAreaName dev\_env\_connection\_definition
 -profile MyDevelop1
 -users MariaG -users BarneyF -users JoseP
 -groups CaseDevelopers
```

```
configmgr\_cl addPrincipals -help
```