<!-- image -->

# Invoking a service within a flow

Invoking a service within a mediation flow and not at its end is
achieved through the use of the Service Invoke primitive. The primitive
can be used in both a request and response flow and has properties
similar to the callout node of the request flow.

1. Create a mediation flow. Select Service Invoke from the Service
Invocation category of the palette and drop it on the canvas.
2 Complete the Select Reference Operation windowas follows:
    1. Select the required service reference from the list.
    2. Select an operation on the interface of that reference.
    3. Select the Message Enrichment mode check
box to enable the Message Enrichment mode. In this mode, a section
of the input message, which is received by the in terminal
of the Service Invoke mediation primitive, is used for the service
invocation. The output message that passes through the out terminal
is constructed by merging the response from the service with the original
request message that was passed into the mediation primitive. If
this check box is clear, the default mode is assumed. In this mode,
message enrichment does not occur, and the body and header sections
of the response message from the service invocation are propagated
to the output message.
    4. Click OK.
3 If the reference has not yet been created:

1. Click New in the Select Reference
Operation window.
2. In the Add Reference window, type a name
for the reference, select an interface, and click OK.
The reference is then added to the list along
with the operations in the interface.
4. Select the operation you want to invoke and click OK. Note: The
associated reference and operation names cannot be changed after you
have selected them. You will have to create a new primitive in order
to do that.
In Message Enrichment mode, the message type
of the in and out terminals
must match, but is initially not set. When the in terminal
is wired, its message type is defined implicitly (by the input message)
and is propagated to the out terminals. In
default mode, the in and out terminals
are set to the appropriate message types for the interface and operation
with which the mediation primitive is associated.
5. To view the settings available to you, right-click the primitive,
and click Show In > Properties
View. You are presented with the following
view:
6. Set the properties of the primitive. The following table summarizes
the properties of the primitive. Note: The Parameter
mappings table and the Propagate request headers
to service being invoked and Propagate response
headers from service being invoked check boxes are enabled
only when working in Message Enrichment mode.
For detailed
information, see Service Invoke mediation primitive

| Property                                                                                                            | Description                                                                                                                                                  | Possible values                                                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference name                                                                                                      | The reference of the service that is called by the callout.                                                                                                  |                                                                                                                                                                                                                                                                                                                                       |
| Operation name                                                                                                      | The name of the operation called by the callout.                                                                                                             |                                                                                                                                                                                                                                                                                                                                       |
| Use dynamic endpoint if set in the message header                                                                   | Determines if the TargetAddress header should be used to override the endpoint if present.                                                                   | If set to True and if the TargetAddress header is populated, the message is forwarded. Otherwise, the message proceeds normally. Default: true                                                                                                                                                                                        |
| Async timeout                                                                                                       | Specifies the time to wait for a response when performing an asynchronous deferred response invocation.                                                      | -1 - infinite wait 0 - expects an immediate response 1+ - waits specified number of seconds for a response  If timeout occurs, the fail terminal is fired. This is treated as an unmodeled fault with regard to retry conditions. Default: 5                                                                                          |
| Require mediation flow to wait for service response when the flow component is invoked asynchronously with callback | Determines if the call should be forced to act in a synchronous manner.                                                                                      | Boolean: true or false  Default: false                                                                                                                                                                                                                                                                                                |
| Invocation style                                                                                                    | Determines whether the service is invoked synchronously or asynchronously.                                                                                   | Default, Sync, or Async Default: Default                                                                                                                                                                                                                                                                                              |
| Parameter                                                                                                           | A preconfigured read-only value identifying whether the element to be transformed or updated forms part of the input, output, or fault message.              |                                                                                                                                                                                                                                                                                                                                       |
| Name                                                                                                                | A preconfigured read-only name for the input, output, or fault parameter type.                                                                               |                                                                                                                                                                                                                                                                                                                                       |
| Type                                                                                                                | The type of the element value in the message.                                                                                                                |                                                                                                                                                                                                                                                                                                                                       |
| Value                                                                                                               | Specifies an XPath 1.0 expression that identifies the element to be transformed or updated.                                                                  | Use the XPath Expression Builder to build a custom XPath expression.                                                                                                                                                                                                                                                                  |
| Propagate request headers to service being invoked                                                                  | Determines whether the request message, which is sent to the service, is populated with the header of the input message that is received at the in terminal. |                                                                                                                                                                                                                                                                                                                                       |
| Propagate response headers from service being invoked                                                               | Determines whether the output message is populated with the response message header from the service being invoked.                                          |                                                                                                                                                                                                                                                                                                                                       |
| Retry on                                                                                                            | Determines whether and how fault responses affect retry.                                                                                                     | Never - operation call is never retried, no matter the type of fault Any fault - operation call is retried on both modeled and unmodeled faults Modeled fault - operation call is retried only when a modeled fault is received Unmodeled fault - operation call is retried only when an unmodeled fault is received   Default: Never |
| Retry count                                                                                                         | Number of retry attempts following initial failure before a modeled fault, timeout or fail terminal is fired.                                                | The number must be an integer greater than or equal to 0. Default: 0                                                                                                                                                                                                                                                                  |
| Retry delay                                                                                                         | Sets the delay between retry attempts, in seconds.                                                                                                           | Must be an integer greater than or equal to 0. If 0, there will be no delay between attempts meaning they will run as fast as the server can handle them.  Default: 0                                                                                                                                                                 |
| Try alternate endpoints                                                                                             | Determines if any alternate endpoints should be used on retries.                                                                                             | True - alternate endpoints found in the SMO headers will be used   Otherwise they are not tried    This function is only available if 'Use dynamic endpoint' is also True. Default: True                                                                                                                                              |