# Testing the integration

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

After you build and link the input and output of
the required components as instructed in the preceding procedures,
you can test the completed inbound integration using the Inspector
in IBM Process
Designer and
a utility such as soapUI.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application that contains the simple BPD that you created per the instructions
in Adding a message event to a BPD.
3. Open the BPD and click the Run icon in the upper right corner of the BPD diagram. (If you need
detailed instructions for using the Inspector, see Stepping through a process.)
4. When IBM Business Automation Workflow prompts
you to change to the Inspector interface, click Yes. 
Note: Click the check box if you want IBM Process
Designer to
change interfaces without prompting for approval.
5. From the Process Instances tab,
click the received task for Step 1 and then click the run icon (). The coach for
the activity, which is the default Human service, opens in a browser.
6. Click the Done button in the Coach
to complete the first step.
7. Click the refresh icon () in the toolbar.
You can see that the process instance is waiting for the
incoming message event.
8. Using your SOAP utility, such as soapUI, point to the WSDL
URI for the KickTheBPD inbound web service that you
created per the instructions in Creating an inbound web service.
9. In your SOAP utility, initiate a request to the doKick method.
In the someString parameter for the method, provide
the Instance ID for the currently active instance, which you can see
in the Process Instances tab in the Inspector. For example, in the
preceding image, the instance ID of the active instance is 4.
10. Click the Refresh icon in the Inspector toolbar. You should
see that Step 2 has been received, meaning that the message event
was successfully processed and the instance is able to move to the
next step.
11. Click the Step 2 task to select it and then click the Run
task icon. The value is used in the business process definition
correlation mapping that is created in the initial task. If this value
and the value of the BPD mapped variable are equal, the message intermediate
start event runs. If not, the message intermediate start event continues
to wait until a match is found.
12. The Coach for the activity, which is the default Human
service, opens in a browser. Click the Done button
in the Coach to complete the second step.
13. Click the Refresh icon in the Inspector toolbar. You should
see that the task for Step 2 is closed and the process instance has
a status of Complete, indicating that the BPD instance has completed
successfully.