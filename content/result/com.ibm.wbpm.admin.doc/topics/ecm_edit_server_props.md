# Changing Enterprise Content Management server settings

## About this task

You can configure connection information for Enterprise Content Management (ECM) servers in the
designer. You can edit the settings for installed snapshots in the Process Admin Console. Changes
there are applied to the existing instances. You must specify separate settings for each server that
is being used.

## Procedure

1. Log in to the Process Admin Console and
select Installed Apps.  You
see the list of installed snapshots.
2. Click the overflow menu of a snapshot and select App Details. Then
click the Servers tab. 
 You will see entries on the Servers page only if the process application snapshot that
you selected has servers specified.
3. Select a server from the list. The current
server settings are displayed.
4 You can edit any of the fields.
    - Hostname: The hostname or IP address of
the Enterprise Content Management server.
    - Port: The port number of the Enterprise
Content Management server.
    - Context Path: The path to the application
on the server. This context is different for each product.
    - Secure: Select Secure if you want your service to
be secure, that is, if you want to use the Hypertext Transfer Protocol Secure (HTTPS) protocol. You
will need to configure the security. Setting up HTTPS security is described
in Accessing an Enterprise Content Management server using the Secure Socket Layer (SSL).
    - Repository: The name of your repository.
    - Connection User ID: The user ID to connect
to the Enterprise Content Management server.
    - Password: The password for the ID that
you are using to connect to the Enterprise Content Management server.
    - Always use this connection information: Selected by default. Only this
user ID and password will be used for authentication. Selecting this check box means this user ID
and password overrides any other user information. Remove this option if you have single sign-on
enabled between the workflow server and the ECM server and would like to have the user context
propagated to the ECM server when called from a human service or coach.
5. Click Test Connection to check the
settings. If any settings are incorrect, you receive an error message.
6. Click Apply or Cancel.

## Results