# Throwing errors by using error end events

## About this task

- It ends the flow of the nested service, but the execution can continue in the parent service if
it catches the error that is thrown.
- If the client-side human service is used in a root process, the
error end event propagates the error data all the way to the process. An error intermediate event
that is set up at the process level can catch the error that is thrown by the error end event that
is defined at the human service level.

## Procedure

To add an error end event to the client-side human service:

1. Open the client-side human service that you want to work with.
2. In the Diagram view, add an end event  to the diagram.
3. Select the end event and, in its Implementation properties, under
Event Type, select Error End Event.
The end event changes into an error end event .
4. In the Implementation properties, under Event
Properties, click the Error code picker to select a local
variable and specify the error code for the error to be thrown.
The error code expression must evaluate to a string value at run time. If the error code is
defined as a string literal (for example, "ErrorCode1"), the code is included in
the list of defined errors that can be caught when you create an error intermediate event to catch
the error in a root process.
Click the Error mapping picker to map the error data to an error
mapping variable that was previously defined in the Variables view.
5. Optional: To define multiple error end events that can have different error
handling logic for different errors, iterate through steps 3 - 5. For each error end event, use
different error codes or error data to differentiate between the different kinds of
errors.
6. In the diagram, connect each error end event to the logic you want to run when the error
occurs. If you have multiple error end events, connect each one to the error handling logic that
applies.
7. Click Save or Finish Editing.