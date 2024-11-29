# Catching errors by using error event handlers

## About this task

<!-- image -->

<!-- image -->

<!-- image -->

## Procedure

To add an error event handler to the client-side human service:

1. Open the client-side human service that you want to work with.
2. In the Diagram view, add an event handler .
An error event trigger is assigned and the handler changes to an Error event handler.
3 By default, the error event is set to catch all errors. To catch a specific error:
    1. In the Implementation > Behavior properties, select Catch specific errors.
    2. Click the Error code picker to select the error code for the error to be
caught.
 For example, to catch a task-ownership specific error, select the error code
BPMTaskOwnerError.
    3. Click the Error mapping picker to map the error data to an error mapping
variable that was previously defined in the Variables view.
4 Double-click the error event handler, and then implement your error handling logic.

- You can declare additional private variables in the error event handler that are visible
only to the event handler.
- You can use a coach to display the error to the user.
5. Optional: 
To define multiple error event handlers that can have different error
handling logic for different errors, iterate through steps 3 - 5. For each error event handler, use
different error codes or error data to differentiate between the different kinds of errors.
6. Click Save or Finish Editing.