# Debugging flows by using breakpoints

## About this task

You can set a breakpoint on an activity, event, or gateway to stop the flow when it
reaches that step. You can also set JavaScript expressions as conditions on breakpoints so that the
breakpoint is triggered only when the condition evaluates to true.

The breakpoints view lists all the breakpoints in a process application and
its dependent toolkits and other information about them such as their location. You can easily edit
breakpoint conditions and delete breakpoints. When an activity, event, or gateway that has a
breakpoint is deleted, the breakpoint still appears in the list, but it is disabled. The breakpoint
remains available in other snapshots where the deleted activity, event, or gateway still exists. If
you don't want a breakpoint to remain in any of the snapshots, you can delete it in the list of
breakpoints.

## Procedure

To stop the flow at a breakpoint, follow these steps:

1. Open the flow.
2. In the diagram, right-click an activity, event, or gateway and click Add
breakpoint. 
A breakpoint icon appears on the activity, event, or gateway. .
3. To enable the breakpoint only when a certain condition occurs, add a breakpoint
condition. Right-click the activity, event, or gateway and click Edit breakpoint
condition. Enter a  JavaScript expression that evaluates to true. 
Tip: You can add conditional breakpoints at various points in your flow so that they are
available when you need to trigger them. To skip a breakpoint, enter false in the
first line of the JavaScript expression. When you want to always trigger a breakpoint, change the
expression into a comment.
4. Run the flow in debug mode by clicking the Debug icon in the
toolbar . The flow stops at the first activity and the Inspector
view opens.
5. Click Run and stop on breakpoint.  You might need to
complete activities until the flow reaches a point where it encounters the breakpoint. Open user
tasks in the playback window, complete the coach to progress to the next activity. For other
activities, you might need to enter data in the Data section to progress the
flow.When the flow stops at the breakpoint, you can inspect it to locate the problem.Tip: You can also add breakpoints after you start the service in debug mode. Right-click an
activity, event, or gateway in the diagram and click Add breakpoint.
6. When you're done, or you want to edit the flow, click  in the status bar.