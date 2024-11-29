# Setting permissions for discretionary activity classes

## About this task

The default setting for CREATE\_INSTANCE allows any user to create a discretionary activity. If
you want to allow only certain users to create discretionary activities, this default setting is not
appropriate. You can change the permissions on the discretionary activity class.

Activities are created by the Content Platform Engine server
when a case is created. Activities inherit permissions from the case that owns them. User-created,
or discretionary activities, are created by users. It is a best practice to set user-added
discretionary activity class permissions to ensure that the #CREATOR-OWNER user who created the
discretionary activity class can change the state or modify the properties.

## Procedure

To set permissions on discretionary activity classes:

1. Navigate
to your discretionary activity class in the following path in Administration Console for Content Platform
Engine: Data Design > Classes > Other Classes > Activity > Case Activity > Name based on case type.
2. Click the desired discretionary activity class in the list.
3. Click the Security tab, and in the Name list,
select #AUTHENTICATED\_USERS and click the Edit button.
4. Clear the Create instance check
box and make any other desired changes to permissions. Click OK.
5. Click Add to add one or more groups
to the list.
6. Add the required permissions, including Create
instance if appropriate, by selecting the check boxes.
Click OK.
7. Click the Default Instance Security tab
and select #CREATOR-OWNER.
8. Click Edit. Select the Modify
all properties check box.
9. Click OK. Under Default Instance
Owner, click Change Owner.
10. Under Change default owner, find
and select #CREATOR\_OWNER and click OK.