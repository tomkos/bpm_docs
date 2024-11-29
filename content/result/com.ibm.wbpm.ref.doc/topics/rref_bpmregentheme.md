# BPMRegenTheme command

Some interim fixes or cumulative fixes (fix packs), contain changes in the CSS theme. To apply
these changes to the snapshots that were created based on the older version of the CSS theme, use
BPMRegenTheme command. The BPMRegenTheme command regenerates
the runtime CSS for a process application or toolkit snapshots.

- The interim fix or fix pack contain any changes in the CSS theme.
- Your process application uses the UI toolkit.

- To update a process application or toolkit tip, you can remove and then add one of your process
application or toolkit dependent toolkits. Removing and adding a dependent toolkit regenerates the
theme. This procedure must be performed in IBM® Process
Designer after you upgrade
or install an interim fix that contains CSS-related changes.
- If you are performing a rolling upgrade, as long as your IBM Workflow
Center is on an earlier
version than your workflow servers, after deploying any snapshots to the workflow servers run the
BPMRegenTheme command to update the CSS theme of the snapshot.

## Prerequisites

- In a network deployment environment, you must run this command on the
node containing the application cluster member that handles
Workflow Center applications.
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

You can check the status of the command in the server SystemOut.log
file.

## Syntax

```
BPMRegenTheme 
-targetContainerAcronym process\_application\_or\_toolkit\_acronym
[-targetContainerSnapshotAcronym snapshot\_acronym]
[-outputFile absolute\_path\_to\_log\_file]
```

## Parameters

An optional parameter that uses an acronym to identify the snapshot that will have its CSS
regenerated based on the currently applied theme definition. If not provided, the theme is
regenerated for all of the named snapshots in the target process application or toolkit, which
includes the tip if you run the command in Process Center.

An optional parameter that contains the absolute path to the log file for logging the results of
the theme regeneration.

Some interim fixes or cumulative fixes (fix packs), contain changes in the CSS theme. To
apply these changes to the snapshots that were created based on the older version of the CSS theme,
use BPMRegenTheme command.

BPMRegenTheme command regenerates the runtime CSS for a process
application or toolkit snapshots.

To determine whether to run the command , check the readme
of the ifix and the post installation documentation for the fixpack. If the iFix or fixpack contain
any changes in the CSS theme and your process application uses UI toolkit , then running
BPMRegenTheme command is required.

The following example illustrates how to
establish a SOAP connection to the Workflow Center server and regenerate
the CSS for the BILLDISP v2 snapshot.

```
wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython

AdminTask.BPMRegenTheme(['-targetContainerAcronym', 'BILLDISP', 
     '-targetContainerSnapshotAcronym', 'v2', '-outputFile', 'c:/regenThemeLog.txt'])
```

```
wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython
AdminTask.BPMRegenTheme(['-targetContainerAcronym', '*'])
```