# Adding users to the default project area by using the command
line

## Before you begin

Be sure to have your completed configuration checklist available.

## About this task

A project area groups solutions within the design object
store to limit the effects of resetting the test environment. When
you reset the test environment from Case Builder, only a single project
area is reset. Each development environment has a default project
area, and you can create more project areas as needed to provide isolated
work areas for developing and testing solutions in Case Builder. The default project
area is named dev\_env\_connection\_definition.

Before you add
users to the project area, add them to the master group that you configured
for access to your object store.

You can assign specific solutions
and users to each project area. Each user can belong only to one project
area and the default project area. If you assigned a user to another
project area who is already assigned to any nondefault project area,
that user is automatically removed from the original nondefault project
area. You can add groups to the default project area only.

Adding
a user to a project area gives the user access to the solutions in
the project area in the design object store. If the user is not an
administrator for the target object store, then you must set the security
for the user.

By default, all new solutions
are created in the default project area unless you define additional
project areas.

## Procedure

To add users to the default project area:

1. Change the current directory to the
install\_root/CaseManagement/configure directory, where
install\_root is the location where Business Automation Workflow is
installed.
2 Add a single user or group by runningthe following command. Do not enter any line breaks when you enterthe command. configmgr\_cl addPrincipals -projectAreaName dev\_env\_connection\_definition -profile myprofile -user user\_name -groups group\_name [-help] -projectAreaName dev\_env\_connection\_definition The name of the project area to modify. The default project area is nameddev\_env\_connection\_definitition. -profile myprofile Specifies the profile to use. The myprofile value can be one of the following items: -user user\_name Specifies the short name or display name of the user to add. A user can belong to the defaultproject area and one other project area. -groups group\_name Specifies the short name or display name of the group to add. Groups can be added to the defaultproject area only. -help Optional and displays a brief message on the command syntax instead of running the command.

```
configmgr\_cl addPrincipals -projectAreaName dev\_env\_connection\_definition
 -profile myprofile
 -user user\_name -groups group\_name
 [-help]
```

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
3. Repeat 2 as
needed to add all the users or groups for the default project area.
You will assign solutions to the default project area later,
after you create the solutions. You also can create additional project
areas and assign users and solutions later.