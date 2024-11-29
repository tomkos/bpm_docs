# Running and debugging service flows

## Before you begin

## Running service flows

### About this task

### Procedure

To run the service flow, complete the following steps:

1. Open the service flow that you want to run.
2. Click Run
 in the
toolbar.

### Results

## Debugging service flows

### About this task

Using the
Inspector, you can step through the service flow activities to observe how the service flow behaves
as it runs. The Inspector pauses the execution of the service flow before each step and displays the
variable values at each point. If an error occurs, the debugging capability helps you to identify
which step is at fault. The error message is displayed in the playback window and on the sidebar in
the Inspector.

### Procedure

To debug the service flow, complete the following steps:

1. Open the service flow.
2. Click Debug
 in the toolbar. The Inspector opens in the browser window, pausing on the
first step after the Start event.
3. Examine the variable values at that point. When you are ready to move on to the next
activity in the service flow, click Step Over
.  As the execution progresses, indicators mark the progress of the
service flow execution in the diagram.
4. If the service flow includes a linked service, when the service flow execution stops at
the linked service node, you can click Step Into
 to
step into the linked service and debug it. When the linked service flow completes
successfully, the execution moves to the next step in the parent service flow.Tip: If
you are interested in the execution state at a particular step and don't want to follow the progress
of the execution up to that step, you can use breakpoints. This saves you from pressing
Step into or Step over several times. See Debugging flows by using breakpoints.
5. Repeat steps 2 - 4 until you complete the service flow. Or, you can click Run and stop
on breakpoint to continue the debugging session until an enabled breakpoint is encountered or
the service flow terminates. You can also click Terminate to cancel the debugging session
before the service flow reaches the end.
6. When you're done, or you want to edit the service, click  in the status bar.