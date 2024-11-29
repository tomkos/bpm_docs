# Setting permissions for a case type class

## About this task

The default setting for CREATE\_INSTANCE allows any user
who can log in to create a case. If you want to allow only certain
users to create cases, this default setting is not appropriate. You
can change the permissions on the case type class.

The default
setting of  #CREATOR-OWNER allows the creator of a case to retain
full control over the case and remain the owner of record. If you
do not want the creator of a case to retain full control over the
case, then the default value for owner is not appropriate. You can
change the setting to make the owner value blank, or you can assign
ownership to a group.

## Procedure

1. To find the case type class in IBM® Administration Console for
Content Platform Engine, navigate to a deployed
solution within an object store.
Case type classes for
an object store are found in the following Administration Console for Content Platform
Engine path: Object store name > Data
Design > Classes > Folder > Base Case > Case Folder.
2 Click the desired case type class in the list and changethe CREATE\_INSTANCE permission:
    1. Click the Security tab and in
the Name list, select #AUTHENTICATED\_USERS
and click the Edit... button.
    2. Clear the Create instance check
box and make any other changes as desired.
    3. Click Add to add one or more
groups to the list.
    4. Click the appropriate check boxes to add the required
permissions, such as Create instance.
    5. Save your changes.
3 Change the #CREATOR\_OWNER setting to blank, or assign ownershipto a specific group: Option Description Set the owner value to blank Assign ownership to a group

| Option                       | Description                                                                                                                                                                                                                                                                                                                                       |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Set the owner value to blank | On the Default Instance Security tab, click Change Owner. Click the Set Default Owner to NULL radio button. Save your changes.                                                                                                                                                                                                                    |
| Assign ownership to a group  | On the Default Instance Security tab, click Change Owner. Click the Change default owner to: radio button and click the Find button. Search for and then add the name of a group (such as Case administrators) by moving the group from the Available Users and Groups list to the Selected Users and Groups list. Click OK to save your changes. |