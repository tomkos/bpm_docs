# Handling errors in client-side human services

- An error boundary event catches errors that are thrown from the service it is attached to. It
can be attached either to a called service node or to a nested client-side human service node.
- An error handler catches errors that are thrown from the client-side human service and all its
nested services.

You can configure boundary events and error event handlers to catch all errors or specific
errors. At run time, boundary events take precedence over error event handlers and specific errors
take precedence over catch-all errors.

- The error event information is captured in the tw.error.code and
tw.error.data  variables. For more information, see JavaScript API for client-side human service development.
- By mapping the error event to a variable, events with incompatible data types are filtered out
and the data is captured in a local variable.

- BPMBOSaveFailedError: Catches errors from a shared business object save
service
- BPMTaskOwnerError: Catches errors that occur when the ownership of a task is
withdrawn from the current user

| Icon   | Error event                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------|--------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        | Error boundary event. An intermediate error event that is attached to a service node in a client-side human service      | Catches errors and receives error data from the service to which it is attached. To model where the client-side human service resumes after it catches an error, you connect each error boundary event to an activity that runs the error handling logic. You can wire an error boundary event to any node.You can attach error boundary events either to a called service node or to a nested client-side human service node. You can reposition the error boundary event along the service boundary. You can remove it from the service or you can move it to another service.  Shortcut key: B For more information, see Catching errors by using error intermediate events.                                                                          |
|        | Global error event handler that catches errors in the client-side human service and runs error handling logic            | Catches all errors or specific errors. It can be used as a stand-alone event handler outside a service. You implement the error handling logic in the error handler.You can use multiple error event handlers in a client-side human service. For example, you can configure an error event handler to catch a specific error code and an error event handler that catches all other errors. You can then implement different logic to handle specific errors and logic to handle all other errors. An error event handler that is used in a nested client-side human service catches errors from the service in which it is defined and from all the nested services below it. For more information, see Catching errors by using error event handlers. |
|        | Error end event that throws an error and ends the processing of the client-side human service in which it is implemented | Throws a specific error and ends the processing of the client-side human service in which it is implemented. You can connect an error end event to any node in a client-side human service. You can specify an error code and error data for the error.For more information, see Throwing errors by using error end events.                                                                                                                                                                                                                                                                                                                                                                                                                              |

- Catching errors by using error intermediate events

When you attach it to a service node, the intermediate event becomes an error boundary event that catches errors and receives error data from the service to which it is attached. The error boundary event is triggered while the service is running and interrupts its execution.
- Catching errors by using error event handlers

Use error event handlers to catch errors at any point in a client-side human service and to implement error handling logic for these errors. To catch a specific error, you can set the implementation error properties in the error event handler by specifying the error code and mapping the error data to a specified variable.
- Throwing errors by using error end events

For errors that are thrown from the flow of a client-side human service, you can use error end events to end the processing of the service at a specified step.