<!-- image -->

# How faults are handled in export bindings

You configure the export binding using IBM® Integration
Designer.

Figure 1. How fault information is sent from the component
through the export binding to the client

<!-- image -->

You can create a custom data handler or data binding to handle
faults.

## Business faults

Business faults are business
errors or exceptions that occur during processing.

Figure 2. Interface with
two faults

<!-- image -->

In this example, if a client sends a request to create
a customer (to this SCA component) and that customer already exists,
the component throws a CustomerAlreadyExists fault to the export.
The export needs to propagate this business fault back to the calling
client. To do so, it uses the fault data handler that is set up on
the export binding.

1. The binding determines which fault data handler to invoke for
handling the fault. If the service business exception contains the
fault name, the data handler that is set up on the fault is called.
If the service business exception does not contain the name of the
fault, the fault name is derived by matching the fault types.
2. The binding calls the fault data handler with the data object
from the service business exception.
3. The fault data handler transforms the fault data object to a response
message and returns it to the export binding.
4. The export returns the response message to the client.

## Runtime exceptions

A runtime exception is
an exception that occurs in the SCA application during the processing
of a request that does not correspond to a business fault. Unlike
business faults, runtime exceptions are not defined on the interface.

In
certain scenarios, you might want to propagate these runtime exceptions
to the client application so that the client application can take
the appropriate action.

1. The export binding calls the appropriate data handler with the
service runtime exception.
2. The data handler transforms the fault data object to a response
message and returns it to the export binding.
3. The export returns the response message to the client.

Fault handling and runtime exception handling are optional.
If you do not want to propagate faults or runtime exceptions to the
calling client, do not configure the fault data handler or runtime
exception data handler.