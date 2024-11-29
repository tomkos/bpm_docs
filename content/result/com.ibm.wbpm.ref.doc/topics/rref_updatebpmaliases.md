# updateBPMAliasesAndRunAsRolesPasswords command

This command provides a command-line method
to synchronize passwords for authentication aliases or application
RunAs roles after a password has been changed for a user defined in
the file registry or external security provider. Before running this
command, you should review the task topic "Changing IBM Business Automation
Workflow passwords
after installation."

The updateBPMAliasesAndRunAsRolesPasswords command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

The following conditions must
be met:

- The command must be run on the deployment manager node.
- If the deployment manager is stopped, use the wsadmin
-conntype none option to run the command in disconnected
mode.
- If the deployment manager is running, you must connect with a
user ID that has WebSphere Application Server configurator privileges.
Do not use the wsadmin -conntype none option.

## Location

Start the wsadmin scripting client
from the deployment\_manager\_profile/bin directory.
The updateBPMAliasesAndRunAsRolesPasswords command
does not write to a log file, but the wsadmin scripting client always
writes a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## Syntax

```
updateBPMAliasesAndRunAsRolesPasswords
-userName user\_name
-password new\_password
-de de\_name
```

## Required parameters

## Examples

The
following Jython example shows how to use the updateBPMAliasesAndRunAsRolesPasswords command:

```
dmgr\_profile\_root/bin>wsadmin -conntype NONE -lang jython

wsadmin>AdminTask.updateBPMAliasesAndRunAsRolesPasswords( [ '-de','de\_name','-userName', 'user\_name', '-password', 'new\_password' ] ) 

You should see the following:

Processing: IBM\_BPM\_PerformanceDW\_SingleCluster
Processing: IBM\_BPM\_Teamworks\_SingleCluster
Processing: BPEContainer\_SingleCluster
Processing: TaskContainer\_SingleCluster

wsadmin>AdminConfig.save()
```