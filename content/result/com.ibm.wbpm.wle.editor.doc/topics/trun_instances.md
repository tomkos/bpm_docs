# Running and debugging processes

## About this task

You can switch easily between running and debugging your activities as required. You can inspect
your activities, and view data variables and their values.

To run a process, complete the following steps:

## Procedure

To run a process, complete the following steps:

1. Open the process that you want to run.
2. Click Run
 in the upper right of the toolbar. 
Note: Choose the server. Choose the remote workflow server to test this instance on your production
or test environment to ensure it runs correctly in that environment. If you choose the remote
server, you are prompted to log in. 
The Inspector opens showing information about the running process. In the diagram, a marker
 indicates the activity where the process is stopped, waiting for input. You can see the
activity and its data variables and values. You can edit the variable values to test different
scenarios. If the activity is a user task, you see it under the list of tasks and you see the coach
in separate browser window where you can walk through the task.

If the process does not run as expected, you can inspect the process by debugging it,
locate the problem, and fix it. To debug a process:

1. Locate the task or activity in the Inspector, and click
Debug beside it and step into the process.  The Debug pane opens,
showing information about the process. The debugger stops the process at the first activity after
the start event. A marker indicates the activity where the process is stopped.
2. Step into the activity to inspect it, or step over to another activity.
3. Examine the variable values to determine whether they are expected. Expand complex type
variables to reveal their fields. You can change values of simple type variables in fields directly
in the Data section. Click Update all to save your changes in the process
instance.
4. Use the Evaluator section to evaluate JavaScript expressions in the context of a running
process. The result of the expression is displayed in the Result
field.
5. When you're done, or want to edit the process, click  in the status bar.