# Changing IBM Case Manager server settings

## About this task

You can configure and change connection information for
IBM Case Manager servers in IBM Process Designer. You can edit the
settings for installed snapshots in the Process Admin Console. Changes
there are applied to the existing instances. You must specify separate
settings for each server that is being used.

## Procedure

1. Log in to the Process Admin Console and
select Installed Apps.  You
see the list of installed snapshots. You will see entries on the Servers
page only if the process application snapshot that you selected has
servers specified.
2. Click the overflow menu of a snapshot and select App Details. Then
click the Servers tab.
3. Select a server from the list. The current
server settings are displayed.
4 You can edit any of the fields.
    - Hostname: The hostname or IP address of
the IBM Case Manager server.
    - Port: The port number of the IBM Case Manager
server.
    - Secure: Select Secure if
you want your service to be secure, that is, if you want to use the
Hypertext Transfer Protocol Secure (HTTPS) protocol. You will need
to configure the security. Setting up HTTPS security is described
in Accessing an IBM Business Automation Workflow server using the Secure Sockets Layer (SSL) (deprecated).
    - Target Object Store: The target object
store name for the IBM Case Manager server. A target object store
is used to store runtime case solutions.
    - Connection User ID: The user ID to connect
to the IBM Case Manager server.
    - Password: The password of the user ID that
you are using to connect to the IBM Case Manager server.
5. Click Apply or Cancel.
The Apply and Cancel options are available as soon as you change
a value in any of the fields.When you click Apply,
the server will check the settings. If any settings are incorrect,
you will receive an error message. If you click Cancel, the settings
revert to what was there before you started editing.