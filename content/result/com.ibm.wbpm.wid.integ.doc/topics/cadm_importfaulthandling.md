<!-- image -->

# How faults are handled in import bindings

You configure the import binding using IBM® Integration
Designer. You
can specify a fault data handler (or data binding), and you also specify
a fault selector.

## Fault data handlers

The service that processes
the request sends, to the import binding, fault information in the
form of an exception or a response message that contains the fault
data.

Figure 1. How fault information is
sent from the service through the import to the component

<!-- image -->

You can create a custom data handler or data binding
to handle faults.

## Fault selectors

When you configure an import
binding, you can specify a fault selector. The fault selector determines
whether the import response is an actual response, a business exception,
or a runtime fault. It also determines, from the response body or
header, the native fault name, which is mapped by the binding
configuration to the name of a fault in the associated interface.

| Fault selector type   | Description                                                                                                                                                |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header-based          | Determines whether a response message is a business fault, a runtime exception, or a normal message based on the headers in the incoming response message. |
| SOAP                  | Determines whether the response SOAP message is a normal response, business fault, or runtime exception.                                                   |

- Header-based fault selectorIf an application wants to indicate
that the incoming message is a business fault, there must be two headers
in the incoming message for business faults, which is shown as follows: Header name = FaultType, Header value = Business
Header name = FaultName, Header value = <user defined native fault name>
If
an application wants to indicate that the incoming response message
is a runtime exception, then there must be one header in the incoming
message, which is shown as follows:  Header name = FaultType, Header value = Runtime
- SOAP fault selectorA business fault can be sent as part of
the SOAP message with the following custom SOAP header. "CustomerAlreadyExists"
is the name of the fault in this case. <ibmSoap:BusinessFaultName 
xmlns:ibmSoap="http://www.ibm.com/soap">CustomerAlreadyExists
<ibmSoap:BusinessFaultName>

The fault selector is optional. If you do not specify
a fault selector, the import binding cannot determine the type
of response. The binding therefore treats it as a business response
and calls the response data handler or data binding.

You
can create a custom fault selector. The steps for creating a custom
fault selector are provided in the Developing a custom fault selector topic
of the IBM Integration
Designer information
center.

## Business faults

A business fault can occur
when there is an error in the processing of a request. For example,
if you send a request to create a customer and that customer already
exists, the service sends a business exception to the import binding.

- If no fault selector was set up, the binding calls the response
data handler or data binding.
- If a fault selector was set up, the following processing occurs:
    1. The import binding calls the fault selector to determine whether
the response is business fault, business response, or runtime fault.
    2. If the response is a business fault, the import binding calls
the fault selector to provide the native fault name.
    3. The import binding determines the WSDL fault corresponding to
the native fault name returned by the fault selector.
    4. The import binding determines the fault data handler that is configured
for this WSDL fault.
    5. The import binding calls this fault data handler with the fault
data.
    6. The fault data handler transforms the fault data to a data object
and returns it to the import binding.
    7. The import binding constructs a service business exception object
with the data object and the fault name.
    8. The import returns the service business exception object to the
component.

## Runtime exceptions

1. The import binding calls the appropriate runtime exception data
handler with the exception data.
2. The runtime exception data handler transforms the exception data
to a service runtime exception object and returns it to the
import binding.
3. The import returns the service runtime exception object to the
component.