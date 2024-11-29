# Defining a project area by using the command line

## Before you begin

Be sure to have your completed configuration checklist available.

## About this task

You can assign specific solutions and users to each project area. Each user can belong only to
one project area and the default project area. Users can define and modify solutions only in the
project area that they are assigned to. Users who are not assigned to a project area cannot log in
to Case Builder.

When you define a project area, you are prompted to select a connection point for use with the
target object store for the new project area. After you define the project area, you can reuse a
target object store and its associated connection point when you define another project area. Do not
reuse a target object store and connection point.

## Procedure

To define a project area:

1. Change the current directory to the
install\_root/CaseManagement/configure directory, where
install\_root is the location where Business Automation Workflow is
installed.
2 Run the following command. Do not enterany line breaks when you enter the command. configmgr\_cl defineProjectArea -profile myprofile -projectAreaName project\_area\_name -projectAreaDesc project\_area\_description -peConnPt connection\_point\_name [-help] -profile myprofile Specifies the development profile that is associated with the project area. The object store andContent Platform Engine properties from theprofile are used to create the project area. The myprofile value can be one ofthe following items: -projectAreaName project\_area\_name The name of the project area. The default project area is nameddev\_env\_connection\_definition . The name can contain up to 255 characters. Ifthe name includes a space, put the name in double quotation marks, for example, "CreditDispute Area" . The name cannot contain any of the following characters: \ /: * ? " <> | -projectAreaDesc project\_area\_description The description can contain up to 255 characters. If the description includes a space, put thedescription in double quotation marks, for example, "Solutions for credit carddisputes" . -peConnPt connection\_point\_name The connection point to use with this project area. -help Optional and displays a brief message on the command syntax insteadof running the command.

```
configmgr\_cl defineProjectArea 
 -profile myprofile
 -projectAreaName project\_area\_name
 -projectAreaDesc project\_area\_description
 -peConnPt connection\_point\_name
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

## What to do next