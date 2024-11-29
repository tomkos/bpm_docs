# Setting permissions for custom activity classes

## About this task

The default setting for CREATE\_INSTANCE allows any user to create a custom activity. If you want
to allow only certain users to create custom activities, this default setting is not appropriate.
You can change the permissions on the custom activity class.

Custom activities are created by users. When a custom activity is created, it inherits the
security from the case to which it belongs. It is a best practice to set user-added activity class
permissions to ensure that the #CREATOR-OWNER user who created the activity class can change the
state or modify the properties.

## Procedure

To set permissions on custom activity classes:

1. Navigate to your custom activity class in the following path in Administration Console for Content Platform
Engine: Data Design > Classes > Other Classes > Activity > Case Activity > Dynamic Activity.
2. Click the desired custom activity class in the list.
3. Click the Security tab, and in the Name list,
select #AUTHENTICATED\_USERS or the master group and click the Edit button.
4. Clear the Create instance check
box and make any other changes to permissions. Click OK.
5. Click Add to add one or more groups
to the list.
6. Add the required permissions, including Create
instance if appropriate, by selecting the check boxes.
Click OK.