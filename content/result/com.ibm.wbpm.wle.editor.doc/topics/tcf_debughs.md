# Running and debugging client-side human services in the Inspector

## About this task

While the client-side human service runs, a
playback window shows the running client-side human service. For coaches, the playback window shows
the rendering of the coach so that you can complete the coach and move to the next step in the
flow.

Using the Inspector, you can incrementally step through the activities in your
client-side human service so that you can observe how the client-side human service behaves as it
runs. The Inspector pauses the execution of the service before each step and displays the variable
values at each point.

## Procedure

1. Open the client-side human service that you want to run.
2. Click Run
 in the upper right
of the toolbar.  The playback window opens, showing the running client-side human
service.
3. If the running activity is a coach, the playback window shows the coach. Complete the
coach and trigger the boundary event to transition out of the coach and move to the next step in the
flow.
If the client-side human service completed successfully, you see a message in the playback
window.

## Debugging client-side human services

### About this task

### Procedure

To debug a client-side human service, follow these steps:

1. Click Debug
 in the upper right of the toolbar. The Inspector opens in the browser
window, pausing on the first step after the Start event.
2. Examine the variable values to determine whether they are expected. When you are ready to
move on to the next activity in the client-side human service, click Step
Over
.
3. If this activity is a coach, the playback window shows the rendering of the coach.
Complete the coach and trigger the boundary event to transition out of the coach. The Inspector
moves to the next step in the flow.  As the execution progresses, the followed path is
highlighted and color-coded indicators are added to the client-side human service diagram to mark
the progress in the execution.
4 If errors occur while running the coach, use the Step into action todebug the coach: When the coach completes successfully, the execution moves to the next step in theflow.
    1. Ensure that the playback window is open. Click Show window

to open it if it is not already open.
    2. Click Step into
 to
pause the execution flow before the coach is run.  
Tip: If you are interested in the execution state at a particular step and don't want to
follow the progress of the execution up to that step, you can use breakpoints. This saves you from
pressing Step into or Step over several times. See
Debugging flows by using breakpoints.
    3. Go step by step through the code to observe how it behaves and identify any
errors.
5. Repeat steps 2 - 4 until you complete the client-side human service.  You can click
Run and stop on breakpoint to continue the debugging session until an enabled breakpoint is
encountered or the service terminates. Alternatively, you can click Terminate
 to cancel the debugging session before the client-side human service reaches the
end.
6. When you're done, or you want to edit the client-side human service, click  in the status bar.