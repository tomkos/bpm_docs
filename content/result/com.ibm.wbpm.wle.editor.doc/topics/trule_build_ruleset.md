# Debugging a Decision service (deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

- Results from running the Decision service are not what you expected.
- Running the Decision service results in an exception and you need
to identify the process step that generates errors.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application in the Designer view.
3. Make sure that you are working in the Decision service
that you want to test and debug.
4. Click the Debug  icon.
5. The Business Automation Workflow Debug
Service opens in a new browser window, as shown in the following diagram:
6. Click Step in the Debug window to
run the Decision service one step at a time, or click Run to
run the complete Decision service.
7. When Process Designer prompts
you to change to the Inspector perspective, click Yes.
Note: The prompt to switch to the Inspector perspective might
be covered up by the Debug window.
8. The Inspector opens the currently running service in the Services
in Debug tab and shows progress through the service, using
a hierarchical tree in the Execution State panel to show the process
step that is running.
9. When you run a Decision service and an exception occurs,
the Inspector clearly identifies the error in the Execution State
panel. The Inspector also tells you where the error happened, and
links directly to the source of the problem. For more information
about using the Inspector to debug errors, see the related topic "Resolving
errors."
10. The Debug service browser window captures error and exception
messages. The first few lines of the exception are displayed at the
top of the browser window. To see the complete message, click Details.
To help you locate the rule that produced the error, some exception
messages refer to specific rules by their order number, such as Rule
1, Rule 2, Rule 3, prefixed by the name of the Decision service step,
as shown in the following example:An error occurred in QuoteLookupRule2 service, at step BalRule1. 
   Detail message: Object stockQ not found at run time during execution. 
   You must make sure that the object has been initialized.