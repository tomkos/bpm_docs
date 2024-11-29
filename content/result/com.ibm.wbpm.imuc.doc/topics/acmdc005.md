# Setting permissions for a case type folder

## Procedure

To set permissions on the case type folder:

1. To find the case type folder, navigate to the following
path within the object store in IBM® Administration Console for
Content Platform Engine: Browse > Root Folder > IBM Business Automation
Workflow > Solution
Deployments > Solution name > Case Types > Case type name.
2. Click the Security tab and click Add... to
add one or more groups to the list.
3. For each group, specify the appropriate permission level.

Important: For each entry, set the Apply
To: drop-down setting to This object and all
children. This setting ensures that the permissions are
inherited by all objects that have established a security proxy relationship
to the case.

For the sample groups, grant the following
permissions:   

Table 1. Sample groups
and permissions

Group
Permissions

Case Administrators
Full Control

Case Initiators
View Properties, plus Modify Properties, Create
subfolder and File in folder/Annotate rights, Read Permission rights

Case Workers
Modify 

Case Viewers
View Properties

#AUTHENTICATED\_USERS
No access. Delete this entry in the permissions
list.