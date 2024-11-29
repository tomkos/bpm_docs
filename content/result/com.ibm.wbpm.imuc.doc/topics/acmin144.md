# Enabling notification in the Administration Console for Content Platform
Engine

## About this task

## Procedure

To enable email notification:

1. Log in to Administration Console for Content Platform
Engine.
2. Expand Object stores, right-click your target object store,
and click Administrative > Workflow
System..
3. Click the Language Packs tab, and
click New.
4 Add your language pack.
    1. Select your locale from the dropdown menu.
The
locale selection will auto fill the date time mask.
    2. Enter the Content Platform Engine template
path.
By default, the email template directory is set to
the English language directory, which is <install\_path>/IBM/FileNet/ContentEngine/tools/PE/msg/en.
5. Save your changes.
6 Configure the Remote Servers settings:

1. Click the Remote Servers tab.
2. Check the Enable email notification check
box.
3. Enter the host name and port values for your SMTP server.
4. Enter an email ID as the sender of your notifications.
5. Enter the email login ID and password for the system
user that logs into the server and sends the notification.
6. Save your changes.
7. Click the Advanced tab.
8. In the server list, change the value for the CacheSyncFixupEmail setting
to false.
The default value for
this setting is true.
9. Save your changes.