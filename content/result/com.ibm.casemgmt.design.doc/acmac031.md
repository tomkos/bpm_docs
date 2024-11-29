# Adding solutions to a project area by using the command line

## Before you begin

Be sure to have your completed configuration checklist available.

## About this task

When a business analyst creates a solution in Case Builder, the solution is added
to the project area that the user belongs to. However, you can assign
the solution to a different project area. When you assign a solution
to a project area, the solution is removed from the project area to
which it was previously assigned.

## Procedure

To add solutions to a project area:

1. Change the current directory to the
install\_root/CaseManagement/configure directory, where
install\_root is the location where Business Automation Workflow is
installed.
2 Add one or more solutions by runningthe following command. Do not enter any line breaks when you enterthe command. configmgr\_cl addSolutions -projectAreaName project\_area\_name -profile myprofile -solutions solution\_name [-solutions solution\_name\_n ] [-help] -projectAreaName project\_area\_name Specifies the name of the project area to add solutions to. Thedefault project area is named dev\_env\_connection\_definition. -profile myprofile Specifies the profile to use. The myprofile value can be one of the following items: -solutions solution\_name Specifies the solution name to add to the project area. You canenter multiple -solutions solution\_name optionson the same command line. -help Optional: Shows a brief message on the command syntax insteadof running the command.

```
configmgr\_cl addSolutions -projectAreaName project\_area\_name
 -profile myprofile
 -solutions solution\_name [-solutions solution\_name\_n]
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
3. Repeat the previous step to add more solutions to the project
area.