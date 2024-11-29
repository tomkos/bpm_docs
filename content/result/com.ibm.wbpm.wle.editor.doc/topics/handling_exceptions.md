# Handling errors using error events

- Detect errors.
- Specify how errors are thrown and caught in your runtime environment.
- Recover in a predictable manner.

- Error end events in processes and services that throw errors.
You can assign error codes and error data to errors that are thrown
by the error end events.
- Error intermediate events in processes and services that catch
errors
- Error start events in processes event subprocesses that catch
errors

To catch specific errors using error intermediate events, select an error code from a list of
previously defined errors and map the error data to a variable. The error intermediate events are
boundary events, which means they are attached to the boundary of an activity. Each boundary event
can be triggered only while the activity is running, interrupting the activity. From the process or
service diagram, you can use an error intermediate event that is attached to the boundary of an
activity to catch specific errors and error data from a linked process, a subprocess, or a service.

Another way to catch errors is by using error intermediate events
in services that catch all errors. When you build your service, you
can attach an error intermediate event to the boundary of a step to
catch all errors for that step, and you can  use an error intermediate
event as part of the service to catch all the errors that are raised
by service steps that are not handled by the error intermediate event
at the boundary of the step.

In processes, you also can catch errors by using error event subprocesses.
In the subprocess, you use an error start event that catches errors
if the start event is triggered.

- Catch all errors or specific errors. To catch specific errors, you can select the error code,
map the error data, or both, as described in the following bullets.
- Filter the specific errors that are caught by selecting an error code from a list of all thrown
errors for the linked process, subprocess, or service.
- Map the error data into a variable by selecting an error mapping variable that was previously
defined on the Variables tab. If the error code has changed, make sure to
select the variable again so that it is mapped properly. Note: The error data cannot be mapped to a
variable that is of a list type. If you want to pass information that has the structure of a
sequence as error data, create a business object that contains a parameter that is of a list type
and then use this business object as the variable's type.

If there are multiple error events defined to catch errors for
an error that is thrown in a linked process, subprocess, or service,
the catching event is determined by the precedence rules in the order
that they are listed in the Error event components table.

1. The boundary events catch errors that are raised by the attached
activity, as described in the following table.
2. If there is no error boundary event that handles the error, and
a subprocess is in a process or in an unattached intermediate error
event in a service, errors are caught in the error event subprocesses,
as described in the following table.
3. If there is no error event subprocess that handles the error in
an event subprocess, linked process, or service, errors are propagated
to the next level.

| Specify                                                                        | Errors caught                                                                                                   |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| error code and error data                                                      | Only errors with the same code and data type                                                                    |
| error code                                                                     | Errors with the same code, unless they are already caught by an event, as specified by the preceding rule       |
| error data                                                                     | Errors with the same data type, unless they are already caught by an event, as specified by the preceding rules |
| neither code nor error data or the Catch All Errors option on error properties | All errors that are not already caught by an event, as specified by the preceding rules                         |

Specifying the variable name in the mapping controls the filtering
by error data type. If the type of the variable and the type of the
error data that is displayed on the Properties tab
do not match, the variable type determines the behavior.

- Handling errors in processes

When modeling error handling as part of your process, you can catch errors using error intermediate events or event subprocesses, and you can throw errors using error end events.
- Handling errors in services

For services, you can use error intermediate events to catch errors, and you can use error end events to throw errors.
- Reserved error codes

Reserved error codes are useful for error end events that are used to throw an error and end the processing of a service. The error codes trigger the retry mechanism to retry a task that fails to complete.
- Error events in models from V7.5.x and earlier

If you have Process Designer models from V7.5.x or earlier that use error events, the earlier error handling behavior is still available.