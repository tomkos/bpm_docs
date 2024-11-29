# Adding users to a project area by using the command line

## Before you begin

Be sure to have your completed configuration checklist available.

## About this task

Each user can belong to only one project area in addition to the default project area. If you
assign a user to a project area, the user is removed from the project area that they originally
belonged to.

You can add groups to the default project area only. You can only add users individually to your
nondefault project areas.

## Procedure

To add users to a project area:

1. Change the current directory to the
install\_root/CaseManagement/configure directory, where
install\_root is the location where Business Automation Workflow is
installed.
2 Optional: List the usersor groups that are already signed to the project area by running thefollowing command. Do not enter any line breaks when you enter thecommand. configmgr\_cl listPrincipals -projectAreaName project\_area\_name -profile myprofile [-silent] [-force][-help] -projectAreaName project\_area\_name The name of the project area. The default project area is nameddev\_env\_connection\_definition . The name can contain up to 255 characters. Ifthe name includes a space, put the name in double quotation marks, for example, "CreditDispute Area" . The name cannot contain any of the following characters: \ /: * ? " <> | -profile myprofile Specifies the profile to use. The myprofile value can be one of the following items: -silent Optional: When you specify the -silent parameter, no prompts orinformational messages are shown in the console, but the errors are written to the log. Failuremessages and validation error messages are shown as needed, such as messages about missing passwordsor invalid port numbers. If you run the execute command to run all the activitiesin a profile and you specify the -silent parameter, you must also specify the-force parameter. -force Optional and applies only when the -silent parameter is used. When youspecify the -force parameter, the activity is run without pausing for requiredresponses to validation error messages, such as messages about missing passwords or invalid portnumbers. -help Optional and displays a brief message on the command syntax insteadof running the command.

```
configmgr\_cl listPrincipals -projectAreaName project\_area\_name
 -profile myprofile
 [-silent] [-force][-help]
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
3 Add users or groups by running the following command. Do not enter any line breaks when youenter the command. configmgr\_cl addPrincipals -projectAreaName project\_area\_name -profile myprofile [-users user\_name ] [-groups group\_name ] [-silent] [-force][-help] -projectAreaName project\_area\_name Specifies the name of the project area to add users to. The default project area is nameddev\_env\_connection\_definition. -profile myprofile Specifies the profile to use. The myprofile value can be one of the following items: -users user\_name Specifies the short name or display name of the user that you want to add. A user can belong tothe default project area and one other project area. If you add a user to a nondefault project area,that user is removed from any other nondefault project area. You can add multiple users at one time by adding more -usersuser\_name entries on the same command. If you are adding only groups, you can omit this option. -groups group\_name Specifies the short name or display name of the group that you want to add. Groups can be addedto the default project area only. You can add multiple groups at one time by adding more -groupsgroup\_name entries on the same command. You can omit this option if you are adding only users. -silent Optional: When you specify the -silent parameter, no prompts orinformational messages are shown in the console, but the errors are written to the log. Failuremessages and validation error messages are shown as needed, such as messages about missing passwordsor invalid port numbers. If you run the execute command to run all the activitiesin a profile and you specify the -silent parameter, you must also specify the-force parameter. -force Optional and applies only when the -silent parameter is used. When youspecify the -force parameter, the activity is run without pausing for requiredresponses to validation error messages, such as messages about missing passwords or invalid portnumbers. -help Optional and displays a brief message on the command syntax instead of running the command.

```
configmgr\_cl addPrincipals -projectAreaName project\_area\_name
 -profile myprofile
 [-users user\_name] [-groups group\_name]
 [-silent] [-force][-help]
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

Specifies the short name or display name of the user that you want to add. A user can belong to
the default project area and one other project area. If you add a user to a nondefault project area,
that user is removed from any other nondefault project area.

You can add multiple users at one time by adding more -users
user\_name entries on the same command.

If you are adding only groups, you can omit this option.

Specifies the short name or display name of the group that you want to add. Groups can be added
to the default project area only.

You can add multiple groups at one time by adding more -groups
group\_name entries on the same command.

You can omit this option if you are adding only users.

4. Repeat the previous step to add more users or groups for
the project area.