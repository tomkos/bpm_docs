# Debugging a process in the desktop Process Designer
(deprecated)

## About this task

The Inspector executes a debugging session in a
browser window. As you step through an underlying process or service
in the debug session in your browser, the Inspector interface shows
the same progress in its diagram view and navigation tree.

You
can use the information from the debugging process to help identify
the point at which a process instance is not functioning as expected.

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## Procedure

1. Open a business process definition (BPD) in IBM Process
Designer.
2. Click Run.
3. When IBM Business Automation Workflow prompts
you to change to the Inspector view, click Yes.
Note: Select the check box if you want IBM Process
Designer to
change interfaces without prompting for approval.
4 In the Process Instances tab,click the new task, and then click Debug task .Depending on the task implementation, complete the steps in one ofthe following procedures:
    - If the task that you are debuggingis implemented as a client-side human service, the client-side humanservice Inspector opens in a browser window, pausing on the firststep after the Start event. Complete the following steps to debugthe client-side human service:
        1. When prompted, select the user that you want to debug the client-side
human service as. You can choose to debug the service as the user
that claimed the task or as a different user. For a different user,
the user name that you select must belong to a user group that has
read access to the corresponding process application. You are logged
in to the web browser using the selected user name.
        2. Use the actions on the sidebar to proceed with the debugging of
the client-side human service. See Debugging client-side human services.
        3. Before running each step in the service flow, examine the variable
values that are displayed on the sidebar at each point to determine
whether they are expected.
        4. To move to the next activity in the service flow, click Step
Over .
        5. If this activity is a coach, complete the coach and trigger the
boundary event to transition out of the coach. The Inspector moves
to the next step in the service flow.
        6. (Optional) To view the progress of the service execution, you
can click the Designer tab in the upper-left
corner of the browser window. On the client-side human service diagram,
the followed path is highlighted and a color-coded token marks the
current position in the service flow.
        7. Complete the debugging of the client-side human service in the
Inspector browser window.
        8. When the debugging of the client-side human service is complete,
go back to the BPD Inspector window and click Refresh  to update the task status accordingly. The Inspector moves
to the next step in the process flow. At the same time, the Inspector
shows progress through the service, using tokens in the diagram and
navigation tree.
- If the task that you are debugging is not implemented as aclient-side human service, complete the following steps to debug theservice: The BPD Inspector opens a debugging session in a browser window.At the same time, the Inspector opens the currently executing servicein the Services in Debug tab and shows progressthrough the service, using tokens in the diagram and navigation tree.
    1. If the service does not require user input, click Run to
run all code and logic and then view the end values.
    2. If the service requires user input, use the Step button
and complete the fields for any associated coaches to step through
each part of the service.
5. To continue through the rest of your BPD, click the Process
Instances tab in the Inspector, and then repeat the actions
in step 4. In the debugger session in your browser,
you can see data that you enter into any displayed coaches and the
values that cause the underlying logic in the services and BPD to
proceed along the available paths. This insight can be extremely helpful
when issues are identified and you need to find the point at which
a process instance is not functioning as you expected.