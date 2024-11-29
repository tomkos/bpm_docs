<!-- image -->

# Creating an IBM Workflow
Center server

## Before you begin

There is generally no need to create
a Workflow Center server
manually unless the existing server has been deleted.

Before
a Workflow Center server
can be automatically or manually created, you may need to obtain the
relevant administrative connection information from your system administrator,
including the administrative user name and password. If you cannot
obtain the administrative user name and password, open the Integration Designer Preferences
window and expand Business Integration, then
select Process Center and clear the Automatically
create a Process Center server when needed check box.
This will prevent you from being continually prompted to specify the
user name and password whenever Integration Designer attempts
to automatically create a Workflow Center server,
such as when you import a process application into the workspace.

## About this task

When a process application
is imported into the workspace, an administrative connection to the
Process Center server is created. If the Process Center is running
on a network deployment environment, then the administrative connection
is created for the IBM BPM deployment manager. If the user name and
password for the Process Center is the same as for the administrative
connection for the deployment manager, then the Process Center server
is automatically created in the Servers view. Otherwise, a New Server
dialog box opens and prompts you to specify the administrative user
ID and password. If you do not know the user ID and password and you
cannot obtain them from the system administrator, select the Do
not automatically create a Process Center server check
box and click Finish. This will prevent you
from being continually prompted to specify the user name and password
when Integration Designer attempts
to automatically create a Workflow Center server.

If
you have removed a Workflow Center server
from the Servers view, you can retrieve the server by right-clicking
the process application in the Business Integration view and then
selecting Refresh from Process Center.

If you
are connected to a Workflow Center but
there is no corresponding Workflow Center server
in the Servers view, you can manually create a Workflow Center server
by completing the instructions in the following procedure.

## Procedure

1. Ensure that the Workflow Center is
running.
2. In Integration Designer, click
the Servers tab to open the Servers view.
3. In the Servers view, right-click anywhere in the view and
select New > Server. The New Server wizard
opens to the Define a New Server page.
4 Define the new Workflow Center serverby completing the following steps:
    1. In the Select the server type list
box, select IBM Workflow Center.
    2. In the Server's host name field, ensure that the correct host
name is specified for the Workflow Center server (playback
server) that you want to create.
    3. In the Server name field, accept
the default name or type in another name for the server.
    4. Click Next.
5 Specify the connection settings for the Workflow Center bycompleting the following steps:

1. If you want to set the host name, HTTP port, user ID,
and password with the URI settings for the default Workflow Center,
click Use Default Workflow Center.
(To view or change the Workflow Center URI
settings, select Window > Preferences to open
the Preferences window, then expand Business Integration in
the tree view and select Workflow Center.)
2. If you want to set the host name, HTTP port, user ID,
and password with the URI settings for a different (non-default) Workflow Center,
specify the URI, as well as the user ID and password used to log into
the Workflow Center,
in the Workflow Center URI, User
ID, and Password fields.
3. If you want to attempt to establish a connection to
the Workflow Center to
verify that your connection settings are correct, click Test
Connection.
4. Click Next.
6 Although the correct host name and ports are automaticallydetermined and set for the Workflow Center server,you must specify the remaining connection settings by completing thefollowing steps:

1. Select the Security is enabled on this server check
box if you want to specify that the server has security enabled. (The
check box is selected by default.)
2. In the User ID and Password fields,
specify the administrative user name and password that are used for
your Workflow Center server.
If you do not know the administrative user name and password, contact
your system administrator. (By default, the fields are pre-populated
with the user ID and password that are used to log in to the Workflow Center.)
3. Click Finish.

## Results