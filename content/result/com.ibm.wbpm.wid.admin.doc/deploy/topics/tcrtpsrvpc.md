<!-- image -->

# Creating an IBM Workflow
Server on IBM Workflow
Center

## Before you begin

## About this task

## Procedure

1. In IBM Integration Designer, click the Servers tab
to open the Servers view.
2. Ensure that the IBM Workflow
Server is
running.
3. In the Servers view, right-click anywhere in the view and
select New > Server. The New Server wizard
opens to the Define a New Server page.
4 Define the new Workflow Server on Workflow Center by completing the following steps:
    1. In the Select the server type list box, select IBM Workflow
Server on Workflow Center.
    2. In the Server's host name field, ensure that the correct host name is
selected for the new Workflow Server on Workflow Center that you want to
create.
    3. In the Server name field, accept the default name or type in another
name for the server.
    4. Click Next.
5 Specify the connection settings for the Workflow Center by completing the following steps:

1. If you want to set the host name, HTTP port, user ID, and password with the URI settings for
the default Workflow Center, click Use
Default Workflow Center. (To view or
change the Workflow Center URI settings, select
Window > Preferences to open the Preferences window, then expand
Business Integration in the tree view and select Workflow Center.)
2. If you want to set the host name, HTTP port, user ID, and password with the URI settings for a
different (non-default) Workflow Center, specify the
URI, as well as the user ID and password used to log into the Workflow Center, in the Workflow Center URI, User
ID, and Password fields.
3. If you want to attempt to establish a connection to the Workflow Center to verify that your connection settings are
correct, click Test Connection.
4. Click Next to select the kind of Workflow Server on Workflow Center that you want to create.
6. In the Servers list, select the process server that you want to create
in the workspace for the Workflow Center. The list
can display the names of one or more development, test, staging, or production process servers, but
it only displays the names of the process servers that are currently connected to the Workflow Center that you specified on the previous page of
the wizard.
7. Click Next.
8 Although the correct host name and ports are automatically determined and set, you must specifythe remaining connection settings for the IBM WorkflowServer by completing the following steps:

1. Select the Security is enabled on this server check box if you want to
specify that the server has security enabled. (The check box is selected by default.)
2. In the User ID and Password fields, specify the
administrative user name and password that are used for your IBM Workflow
Server. (By default, the fields are
pre-populated with the user ID and password that are used to log into the IBM Workflow
Server.)
3. Click Finish.

## Results

Unlike a Workflow Center
server, publishing is not available to a Workflow Server on Workflow Center because the snapshot must be installed on a
Workflow Server using the Workflow Center. Also, you cannot make changes to a snapshot,
which means that there is never a need to publish.