<!-- image -->

# Connecting to an IBM Workflow
Server on
IBM Workflow
Center

## Before you begin

## About this task

## Procedure

1. In the Servers view, right-click your Workflow Center server and select Connect to a
Process Server. The New Server wizard opens.
2. In the Servers list, select the process server that you want to create
in the workspace for the Workflow Center. The list
can display the names of one or more development, test, staging or production process servers, but
it only displays the names of the process servers that are currently connected to the Workflow Center that you specified on the previous page of
the wizard.
3. Click Next.
4 Although the correct host name and ports are automatically determined and set, you must specifythe remaining connection settings for the IBM WorkflowServer by completing the following steps:
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