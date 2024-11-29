# BPMUpdateTheme command

Use the BPMUpdateTheme command to
make a project (process application or toolkit) to look like another
project without redeploying the project. The command generates the
CSS based on the theme definition of a source process application
or toolkit snapshot. While the generated CSS for the two projects
is different, the projects can have a similar look because the definitions
used to generate the CSS are the same.

Use the command in
connected mode from a workflow server.

The BPMUpdateTheme command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- In a network deployment environment, you
must run this command on the node containing the application cluster
member that handles Workflow Server applications.
Do not run this command from the deployment manager profile.
- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- To access the wsadmin command, the ID being used
must have a WebSphere® Application
Server role
with more privileges than the monitor role. See Administrative roles for information about
roles.
- To access the Business Automation Workflow API used
by this command, the ID being used must belong to the bpmAdminGroup.
The default name for the bpmAdminGroup is tw\_admins. See IBM Business Automation Workflow default group types for information about groups.Tip: By default, only the DeAdmin user has both the WebSphere Application
Server administrator
role and membership in the bpmAdminGroup.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

You can check the status of the command in the server SystemOut.log file.

## Syntax

```
BPMUpdateTheme 
-sourceContainerAcronym process\_application\_or\_toolkit\_acronym
-sourceContainerSnapshotAcronym snapshot\_acronym
[-themeName theme]
-targetContainerAcronym process\_application\_or\_toolkit\_acronym
-targetContainerSnapshotAcronym snapshot\_acronym
```

## Parameters

## Example

After you
establish a SOAP connection to Workflow Server, you
can use the following example to apply the BILLPAY snapshot v5.3 theme
definition to the BILLDISP snapshot v2.

```
wsadmin>AdminTask.BPMUpdateTheme('[-sourceContainerAcronym BILLPAY -sourceContainerSnapshotAcronym v5.3 
-themeName billTheme -targetContainerAcronym BILLDISP -targetContainerSnapshotAcronym v2]')
```