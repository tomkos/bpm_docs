# Stepping through a process in the desktop Process Designer (deprecated)

## About this task

When you run a process, you can step through the execution
to ensure that your business process definition works as expected.
You can use this functionality for team playbacks and to help debug
your process.

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## Procedure

1. Open a business process definition in Process Designer.
2. Optional: To view instances running on a different
server or to view instances for a different version of the BPD, select
a different server or snapshot from the drop-down menus in the toolbar.
Important: Remote process servers must be connected
to your Workflow Center to
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
3. Click the Run button in the upper right corner.
4. When you are prompted to change to the Inspector interface,
click Yes. Note: Select the check
box if you want Process Designer to
change interfaces without prompting for approval.
5. In the Process Instances tab, click the new or received
task and then click the Run button. In some cases, you
might need to select a user account or provide a password for a specific
user account in order to run a task. This is controlled by lane assignments
and routing for activities. See Assigning teams to BPDs and lanes and Assigning teams to BPD activities for more information.
6. Complete the task when it runs. For example, if the task
generates a Coach, enter requested values and complete the form. When
the task is complete, you return to the Inspector.
7. Click the Refresh icon in the toolbar. The
Inspector shows the progress by moving the token to the next step
in both the diagram and the navigation tree. Note: If your BPD includes
an attached timer event, you can right-click the timer event token
in the navigation tree and select Fire Timer to
trigger the event.
8. You can expand subprocesses, event subprocesses, and linked
processes as you step through their contents by double-clicking on
the activity in the diagram view. Even if you do not expand a subprocess
activity, you still step through activities contained in the subprocess.
9. To see the variables passed from step to step, click the
process node in the navigation tree.
10. Right-click a variable and then click Show in
Execution Evaluator.  The Inspector opens
the Execution Evaluator tab and shows the values for the parameters
within the selected variable.
You can use the Execution Evaluator
to inspect the variable values as they change through the flow of
the business process definition. Note: You can also manipulate variables
in the Execution Evaluator using JavaScript expressions to validate
your process implementation. To do so, enter the JavaScript expression
and click the Run icon at the top of the Evaluator. The results are
displayed in the bottom pane of the tab.
11. In the Process Instances tab, click the task for the next
step, and then click the Run task icon.
12. Click the Refresh icon in the toolbar. You
can tell that the business process definition is complete when the
final step has a status of Closed and there are no
active tokens in the diagram or navigation tree.