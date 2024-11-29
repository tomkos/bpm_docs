<!-- image -->

# Importing process applications and toolkits from the Workflow Center repository

## Before you begin

When
you import a process application or toolkit from the Workflow Center,
an administrative connection to the Workflow Center server
is created. If the Workflow Center is
running on a network deployment environment, then the administrative
connection is created for the Business Automation Workflow deployment
manager. If the user name and password for the Workflow Center is
the same as for the administrative connection for the deployment manager,
then a Process Center server is automatically created in the Servers
view. Otherwise, a New Server dialog box opens and prompts you to
specify the user ID and password for the deployment manager. If you
do not know the user name and password and you cannot obtain them
from your system administrator, open the Integration Designer Preferences
window and expand Business Integration, then
select Process Center and clear the Automatically
create a Process Center server when needed check box.
This will prevent you from being continually prompted to specify the
user name and password whenever Integration Designer attempts
to automatically create a Workflow Center server,
such as when you import a process application into the workspace.

IBM® Integration
Designer attempts
to automatically create a Workflow Center server
in the Servers view. Workflow Center server
is automatically created in the Servers view.

## Procedure

To import artifacts from the Workflow Center repository
into your workspace, complete the following steps:

1. From the Workflow Center repository,
select a process application or toolkit.

Note:  Traditional:  Only process apps and toolkits
targeted to the Traditional installation environment are shown because Integration Designer contributions are not supported in the
Traditional or Container environment.
2. Click Open in workspace. The process
application or toolkit is imported into your workspace, and you can
view it in the Business Integration perspective.
If you experience difficulty when importing a process application
or toolkit, check that you have Write and Administrator authority
on them. If you have difficulty updating a process application or
toolkit, check that you have Configurator, Operator and Deployer administrative
security roles. If you are not currently assigned to all of these
roles, click Users and Groups in the WebSphere
administrative console and modify the user or group roles.
3. If a New Server dialog box opens and prompts you to specify
the administrative user ID and password for a new Workflow Center server,
but you do not know the user name and password and you cannot obtain
them from your system administrator, select the Do not
automatically create a Process Center server check box
and click Finish. This will prevent you from
being continually prompted to specify the user name and password when Integration Designer attempts
to automatically create a Workflow Center server.