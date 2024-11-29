# Adding support to Case Package for non-English locales for Containers

## About this task

1. Copy the appropriate fonts necessary to support the particular locale.
2. Update the casepackage\_font.properties file to include the locale information

## Procedure

To customize case package creation when you use the Create Package button action in
case client:

1. Copy the updated casepackage-font.properties and font
files to
<custom\_plugins\_navigator\_persistent\_volume>/casePackage-customisations-bawClient.

To configure case package creation when you use the FileNet P8 workflow component
step ICM\_Operations createPackage operation:

1. Copy the updated casepackage-font.properties
<custom\_plugins\_navigator\_persistent\_volume>/casePackage-customisations-fileNet-workflow
.
2 Copy the font files to<icm\_rules\_CPE\_persistant\_volume> . Important: Before re-running the case-init job perform following operation:
    - These files might be changed in future releases. therefore, do not use the old modified files
when you upgrade, Instead edit the files provided in the upgrade with your changes. the provided
files you can find after upgrade at
custom\_plugins\_navigator\_persistent\_volume/casePackage/casePackage.zip
    - There is no needs to modify userConfig.xml, this file will gets updated
through case-initialization job.
    - To apply customization you needs to re-run case-init job or update the modified
files in appropriate location before case-init job run.
    1. Log in to the Administration Console for Content Platform Engine.
    2. Open your target object store and then expand Browse > Root Folder >
CodeModules.
    3. Open CmAcmCaseOperations. On the Properties tab, scroll down to Deployment
Version Number and set the value to an earlier build number. For example, if the existing build
number is icmapi22.0.001.183, change to icmapi22.0.001.180.
    4. Repeat steps b and c for each target object store in which customization are needed.

## Related concepts

- Case Toolbar widget

## Related information

- Create Package