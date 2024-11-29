<!-- image -->

# Managing failed WebSphere MQ events

## About this task

| bindingManaged   | Allow binding to manage recovery for failed messages    |
|------------------|---------------------------------------------------------|
| unmanaged        | Rely on transport-specific recovery for failed messages |

- The function selector fails
- The fault selector fails
- The fault selector returns the RuntimeException fault type
- The fault handler fails
- The data binding or data handler fails after another attempt in WebSphere MQ

1. MQExport receives the request message.
2. MQExport starts the SCA component.
3. The SCA component returns a response to MQExport.
4. MQExport sends a response message.

The Recovery service captures the WebSphere MQ
message and stores it in the failed event database. It also captures and stores the module name,
component name, operation name, failure time, exception detail, and WebSphere MQ properties of the failed event. You can use the failed event
manager to manage failed WebSphere MQ events, or you can
use a custom program.

To manage a failed WebSphere MQ event, perform the following steps.

## Procedure

1. Use the failed event manager to locate information about the failed event, taking note of the
exception type.
2 Locate the exception type in Table 1 to determinethe location and possible causes of the error, as well as suggested actions for managing the failedevent. Table 1. Failed WebSphere MQ events Exception type Location of error Possible cause of error Suggested action FaultServiceException Fault handler or fault selector There is malformed data in the WebSphere MQ message. There was an unexpected error in the fault handler or fault selector. ServiceRuntimeException Fault handler The fault selector and runtime exception handler are configured to interpretthe WebSphere MQ message as a runtime exception. This is an expected exception. Look at the exception text to determine the exact cause, and then takeappropriate action. DataBindingException or DataHandlerException Data binding or data handler There is malformed data in the WebSphere MQ message. There was an unexpected error in the data binding or data handler. SelectorException Function selector There is malformed data in the WebSphere MQ message. There was an unexpected error in the function selector.

| Exception type                               | Location of error               | Possible cause of error                                                                                                                                      | Suggested action                                                                                                                                                                   |
|----------------------------------------------|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FaultServiceException                        | Fault handler or fault selector | There is malformed data in the WebSphere MQ message.                                                                                                         | Inspect the message and locate the malformed data. Repair the client that originated the message so it creates correctly formed data. Resend the message. Delete the failed event. |
| FaultServiceException                        | Fault handler or fault selector | There was an unexpected error in the fault handler or fault selector.                                                                                        | Debug the custom fault selector or fault handler, fixing any errors identified. Resubmit the failed event.                                                                         |
| ServiceRuntimeException                      | Fault handler                   | The fault selector and runtime exception handler are configured to interpret the WebSphere MQ message as a runtime exception. This is an expected exception. | Look at the exception text to determine the exact cause, and then take appropriate action.                                                                                         |
| DataBindingException or DataHandlerException | Data binding or data handler    | There is malformed data in the WebSphere MQ message.                                                                                                         | Inspect the message and locate the malformed data. Repair the client that originated the message so it creates correctly formed data. Resend the message. Delete the failed event. |
| DataBindingException or DataHandlerException | Data binding or data handler    | There was an unexpected error in the data binding or data handler.                                                                                           | Debug the custom data binding or data handler, fixing any errors identified. Resend the message. Delete the failed event.                                                          |
| SelectorException                            | Function selector               | There is malformed data in the WebSphere MQ message.                                                                                                         | Inspect the message and locate the malformed data. Repair the client that originated the message so it creates correctly formed data. Resend the message. Delete the failed event. |
| SelectorException                            | Function selector               | There was an unexpected error in the function selector.                                                                                                      | Debug the custom function selector, fixing any errors identified. Resend the message. Delete the failed event.                                                                     |