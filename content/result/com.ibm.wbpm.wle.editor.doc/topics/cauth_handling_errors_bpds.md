# Handling errors in processes

| Event                                                                           | Description                                                                                                                                                                                     |
|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| error intermediate event  at the boundary of an activity (error boundary event) | Catches specified errors or all errors Provides error handling logic for errors raised by the activity that it is attached to                                                                   |
| error event subprocess that starts with an error start event                    | Catches specified or all errors Provides error handling logic for errors raised by activities of the process, subprocess, or event subprocess that directly contains the error event subprocess |
| error end event                                                                 | Throws an error                                                                                                                                                                                 |

## Catching errors using error intermediate events

For processes, you can attach an error intermediate event to an activity and connect that event
to an error handling flow or activity. The attached error event is known as a error boundary
event.

To determine
whether to use error immediate events, consider the following points:

- If an error occurs while a process is running an activity with
an attached error event at the boundary, the process flows along the
sequence line that is attached to the error event. Errors are handled
in the flow and then proceed with the normal processing.
- Error intermediate events must be attached to an activity.
- You can have multiple error events for an activity, but only one
catches the error.
- Consider specifying the error data to catch specific errors, filtering
on the error code for the types of errors that are caught, and mapping
to a variable after the errors are caught. When all errors are caught,
or if only an error code is specified, the error data is captured
in an XMLElement in the tw.system.step.error variable.
- To handle validation errors in a save service for shared business objects, catch
the error BPMBOSaveFailedError that is available in the list of specific errors.
This error is only available on nodes that save the execution context, either automatically (for
example, coaches) or explicitly by enabling the Save execution context
option. For more information, see Save services for shared business objects.

## Catching errors using error event subprocesses

An event subprocess is a specialized type of subprocess that is not part of the normal sequence
flow of its parent process. An error event subprocess is an event subprocess that contains an error
start event. The event subprocess is not connected by sequence flow and runs only if the start event
in the event subprocess is triggered. You can use error event subprocesses to handle errors in your
process.

- Define a readable process by locating the error event in the event
subprocess instead of defining it in the process.
- To reuse the error-handling flow for multiple tasks in your process,
use event subprocesses. To reuse an error-handling flow using attached
events, you must attach an intermediate event for each of the tasks
and then connect those events to the error-handling flow.
- Define data objects that you can access only from within the event
subprocess. You can define only those data objects that belong to
a subprocess. The parent process is not cluttered with unnecessary
variables.

For more information about event subprocesses, see Modeling event subprocesses.

## Example of exception handling at the process level

You can use the read-only system variable tw.system.step.error to access the
information stored about an exception that occurred in a process.

The variable exists in the scope of a step and not in a process. It cannot be retrieved on the
next step. Instead, you have to access it in the post-assignments section of the boundary
intermediate exception event.

An example of how to model an exception and handle it is shown in the following image:

1. Declare a private variable of type XMLElement, for example, tw.local.error.
Assign a value to it, for example, new tw.object.XMLElement("abc").
2. Create a post-assignment for the attached intermediate exception event, and assign the system
variable to the variable created in step 1, for example, tw.local.error =
tw.system.step.error.You can use the value in the local variable in the next steps of
your process.

## Throwing errors

You can use an error end event in your process to specify an error code and map to an error type
on errors thrown from the flow of a process or a service.

When working
with either error events or event subprocesses, think about whether
errors can be handled immediately, and normal processing can continue,
or if another error can be thrown at another level. Then implement
error handling from the bottom up. In other cases, it might be more
efficient and readable if subprocess can be reused. Build each linked
process and service so that errors can be captured and corrected.
If a correction is not possible at the lowest level of the implementation,
you can allow the error to move up a level by not including an error
event or include an error event to rethrow the error to the calling
service or process, as shown in the following section.

For example, to ensure that any errors that might occur during process run time are captured, you
can create a high-level process that includes an activity to call the main process as a linked
process and then one additional activity with an underlying service to implement error handling as
shown in the following image:

This type of design ensures that errors thrown from
underlying processes and services are propagated up and handled appropriately.