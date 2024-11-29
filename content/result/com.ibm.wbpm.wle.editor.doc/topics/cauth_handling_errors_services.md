# Handling errors in services

| Service event                                                                       | Description                                                                                                                                                                    |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| error intermediate event  attached to the boundary of a step (error boundary event) | Catches errors from the step.                                                                                                                                                  |
| error intermediate event  as part of the service flow                               | Catches all errors raised by steps of the service flow that are not handled by an error intermediate event at the boundary of a step. This event can have only outbound links. |
| error end event                                                                     | Throws an error and ends the processing of this service. You might, for example, use an error end event when you want a particular result from a coach to end a human service. |

To determine whether to use error events in your services,
consider the following points:

- You must attach error intermediate events to steps in your service.
The attached error event is known as a error boundary event.
- Include error intermediate events in the service flow so that
they can act as global error handlers in the service.
- Determine whether errors can be handled immediately, and normal
processing can be continue, or if another error can be thrown at another
level. Then implement error handling from the bottom up.
- Use an error end event to throw a specific error. You can specify
an error code and error data for the error.
- Consider specifying the error data to catch specific errors. For
example, you could filter on the error code for the types of errors
that are caught and map the error code to a variable after the errors
are caught. When all errors are caught, or if only an error code is
specified, the error data is captured in an XMLElement in
the tw.system.error variable.

## Using error
intermediate events in the service flow

The use of error
intermediate events in a service flow offers several options in error
handling, but it must be done carefully to prevent unexpected behaviour.

An
error intermediate event in the service flow can act as a global error
handler in the service. It catches errors that are not already handled
by boundary error events. The error intermediate event cannot catch
specific errors; it is a catchAll error event. It is meant for handling
errors that can be handled within that very service flow. It is recommended
that you not wire back into the normal flow. Instead, after the error
handling, logic should be concluded with an end event. After the error
handling you might reenter the service and run the normal flow with
corrected data.

To handle validation errors in a save service for shared business objects, catch
the error BPMBOSaveFailedError that is available in the list of specific errors.
This error is only available on nodes that save the execution context, either automatically (for
example, coaches) or explicitly by enabling the Save execution context
option. For more information, see Save services for shared business objects.

To handle errors in a service and wire back to the normal
flow in the same service, use one or more error boundary events with
specific errors and the catchAll options.

```
<server>   <!-- insert if not already present -->
       <execution-context> <!-- insert if not already present -->
            <prevent-intermediate-error-loop  merge="replace">false</prevent-intermediate-error-loop>
        </execution-context> <!-- insert if not already present -->  
</server> <!-- insert if not already present -->
```