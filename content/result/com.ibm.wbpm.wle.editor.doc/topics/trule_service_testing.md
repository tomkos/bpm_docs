# Testing a Decision service (deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

## Procedure

To test a Decision service, complete these steps:

1. Open the desktop Process Designer (deprecated).
2. Open a process application that contains a business process definition (BPD) with a Decision
service you want to test.
3. Open the BPD and click to select the activity or decision gateway in the business process that
has the Decision service associated with it.
4. Set a breakpoint in the activity. Set breakpoints
at specific locations in the process where you want the process flow
to pause during testing so that you can determine the status of the
process, and identify any errors that might have occurred.
5. Click the Decision service name to open the rules in the
rule editor.
6. Click the Run service icon  in the banner above the rule editor.
7. When Process Designer prompts
you to change to the Inspector interface, click Yes.
The Inspector displays red tokens both in the BPD diagram and
the execution step tree, which provides a hierarchical view of the
execution state, showing the step that is currently running in the
active process instance.

- Debugging a Decision service (deprecated)

 Traditional: 
Debug a rule component in a Decision service using the Inspector perspective and the debugging feature in Process Designer. Use these testing functions to can examine how the Decision service operates in each step of the process execution, which provides a more detailed inspection than simply stepping through the process.
- Exception messages in Decision service testing (deprecated)

 Traditional: 
You can review exception messages that result from Decision service testing. The exceptions provide information that is helpful when you are troubleshooting Decision service execution errors.