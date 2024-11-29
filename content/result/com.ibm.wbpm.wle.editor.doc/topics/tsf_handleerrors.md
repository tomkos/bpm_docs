# Handling errors in service flows

## About this task

- To catch errors in the parent process, service, or client-side human service, use an error
boundary event that is attached to the service flow node and catches errors at that particular
step.
- To catch errors in the service flow, use error boundary events that you can attach to activity
nodes of either service task or linked service flow type.
- To throw specific errors and end the processing of the service flow at a specified step, use
error end events.

| Icon   | Error event                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        | Error boundary event. An intermediate error event that is attached to an activity in the service flow.       | Catches errors and receives error data from the service flow activity to which it is attached. To model where the service flow resumes after it catches an error, you connect each error boundary event to an activity that runs the error handling logic. You can wire an error boundary event to any node.You can attach error boundary events to any service-type activity in your service flow, be that a service task or a linked service flow. You can reposition the error boundary event along the boundary of the activity. You can remove it from the activity or you can move it to another activity. For more information, see Catching errors by using error boundary events. |
|        | Error end event that throws an error and ends the processing of the service flow in which it is implemented. | Throws a specific error and ends the processing of the service flow in which it is implemented. You can connect an error end event to any node in the service flow. You can specify an error code and error data for the error.For more information, see Throwing errors in service flows.                                                                                                                                                                                                                                                                                                                                                                                                 |

- Catching errors by using error boundary events

An error intermediate event that is attached to the boundary of an activity is called an error boundary event. When you attach an error boundary to an activity in a service flow or heritage human service, the event catches errors and receives error data from the activity it is attached to. The error boundary event is triggered while the activity is running and interrupts the execution of the service at that step.
- Throwing errors in service flows

For errors that are thrown from a service flow or heritage human service, you can use error end events to end the processing of the service at a specified step.