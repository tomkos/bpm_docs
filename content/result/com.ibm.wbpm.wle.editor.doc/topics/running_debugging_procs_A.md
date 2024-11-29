# Managing process instances in the desktop Process Designer (deprecated)

## About this task

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## Procedure

1. Open a business process definition in Process Designer.
2. Click the Run button in the upper right corner.
3. When IBM Business Automation Workflow prompts
you to change to the Inspector interface, click Yes.
Note: Click the check box if you want Process Designer to
change interfaces without prompting for approval. 

In the Process Instances tab, you can see all currently
active and completed process instances.
The Inspector shows
the running and completed instances on the Workflow Center server
for all snapshots (versions) of the current BPD.
4. To view instances running on a different server or to view
instances for a different version of the BPD, select a different server
or snapshot from the drop-down menus in the toolbar. Important: Remote process servers must be connected to your Workflow Center to
be available. To learn how to connect to a remote process server,
see Customizing the Workflow Server settings used to connect to Workflow Center and Using the administrative console to customize the Workflow Server settings used to connect to Workflow Center. To run a process on a different
server using the Inspector, you must first deploy the process application
snapshot that contains the process that you want to run as described
in Installing snapshots on a connected workflow server. If you
click the Run icon while All versions is selected
from the list of snapshots, the Inspector runs the most recent snapshot
of the BPD on the Workflow Center server.
For remote process servers, the snapshots available are limited to
the snapshots that are deployed on that server.
5. To control instances, select an instance from the list
and then click the toolbar option that you want.  For
example, if you want to stop an instance that you started earlier,
click the instance and then click the Terminate Button to terminate
the instance.Tip: You can also filter
the list of instances shown by providing a name in the Instance
Name field and using the Status drop-down
menu.