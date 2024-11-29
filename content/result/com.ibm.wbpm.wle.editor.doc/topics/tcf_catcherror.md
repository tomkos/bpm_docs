# Catching errors by using error intermediate events

## About this task

Shortcut key:
B

In a client-side human diagram, the service node to which
the error boundary event can be attached is either a called service
or a nested client-side human service.

## Procedure

To add an error boundary event to a service in a client-side human
service:

1. Open the client-side human service that you want to work
with.
2. In the Diagram view, add an intermediate event  to the service node.
The intermediate event changes into an error boundary event  that is attached to the boundary of the service.
3. Select the error boundary event and, in its Implementation properties,
under Event Properties, select Catch all errors or
Catch specific errors to specify what type of errors you want the error event
to catch.
4. If you selected Catch specific errors,
click the pickers next to Error code and Error
mapping to filter on the error code for the specific errors
that can be caught and map the error data to a local variable.
5. Connect the error boundary event to the logic you want
to run when the error occurs. For example, you can connect it to a
coach that displays an error message to a user.
6. Click Save or Finish Editing.