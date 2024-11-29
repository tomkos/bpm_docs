# Configuring security in Content Platform Engine

- Permissions for IBM Business Automation Workflow objects

Each Content Platform Engine object such as a folder or document has an Access Control List (ACL) containing the permissions for the object. An ACL is a collection of Access Control Entries (ACEs), where each ACE grants or denies a set of permissions to a user or group.
- Setting permissions for the solution folder

In the Security settings for the solution folder, you can specify which users have rights to the solution folder. Only users who have permission to view the solution folder can work with the solution in Case Client.
- Setting permissions for a case type class

In the Security settings for a case type class, you can specify which users have permission to create a case. You can also specify which creators can retain control over the case.
- Setting permissions for a case type folder

You use the Security settings in the Properties dialog to configure permissions for specific groups. You can add the groups and specify general permission levels and custom settings.
- Setting permissions for discretionary activity classes

For discretionary activity class permissions, you can specify whether all logged-in users can create discretionary activities. You can also specify whether users who create discretionary activities can also have permission to modify those activities.
- Setting permissions for custom activity classes

For custom activity class permissions, you can specify whether all logged-in users can create activities. You can also specify whether users who create custom activities can also have permission to modify those activities.
- Setting permissions for case comments

The permission to create a case comment is granted by default to #AUTHENTICATED\_USERS, meaning that anyone who can log in and has File in Folder / Annotate permissions on the case type instance can create a case comment. You can change this setting to match the requirements of your environment.
- Setting permissions for case relationships

The permission to create a case relationship is granted by default to #AUTHENTICATED\_USERS, meaning that anyone who can log in can create a case relationship. To create a relationship between two cases, a user must have view rights on both cases. The permission to delete a case relationship is granted by default only to the administrator. You can change these settings to match the requirements of your environment.