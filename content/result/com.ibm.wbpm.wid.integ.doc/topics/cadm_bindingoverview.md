<!-- image -->

# Export and import binding overview

## Flow of information through an export

Figure 1. Flow of a request through the export to a
component

<!-- image -->

1. For WebSphere® MQ bindings
only, the header data binding transforms the protocol header into
a header data object.
2. The function selector determines the native method name from the
protocol message. The native method name is mapped by the export
configuration to the name of an operation on the interface of the
export.
3. The request data handler or data binding on the method transforms
the request to a request business object.
4 The export invokes the component method with the request businessobject.
    - The HTTP export binding, the web service export binding, and the EJB export binding invoke the SCA component
synchronously.
    - The JMS, Generic JMS, MQ JMS, and WebSphere MQ export bindings invoke the
SCA component asynchronously.

Note that an export can propagate the headers and user
properties it receives over the protocol, if context propagation
is enabled. Components that are wired to the export can then
access these headers and user properties. See the Propagation topic
in the WebSphere Integration
Developer documentation for more information.

Figure 2. Flow of a response back through the export

<!-- image -->

1. If a normal response message is received by the export binding,
the response data handler or data binding on the method transforms
the business object to a response.  If the response is a fault,
the fault data handler or data binding on the method transforms the
fault to a fault response. 
For HTTP export bindings only, if
the response is a runtime exception, the runtime exception data handler,
if configured, is called.
2. For WebSphere MQ bindings
only, the header data binding transforms the header data objects into
protocol headers.
3. The export sends the service response over the transport.

## Flow of information through an import

Figure 3. Flow from a component through
the import to a service

<!-- image -->

- The HTTP import binding, the web service import binding, and the
EJB import binding should be invoked synchronously by the calling
component.
- The JMS, Generic JMS, MQ JMS, and WebSphere MQ import binding should be invoked
asynchronously.

1. The request data handler or data binding on the method transforms
the request business object into a protocol request message.
2. For WebSphere MQ bindings
only, the header data binding on the method sets the header business
object in the protocol header.
3. The import invokes the service with the service request over the
transport.

Figure 4. Flow of a response back through the import

<!-- image -->

1. For WebSphere MQ bindings
only, the header data binding transforms the protocol header into
a header data object.
2 A determination is made about whether the response is a fault.
    - If the response is a fault, the fault selector inspects the fault
to determine which WSDL fault it maps to. The fault data handler on
the method then transforms the fault to a fault response.
    - If the response is a runtime exception, the runtime exception
data handler, if configured, is called.
3. The response data handler or binding on the method transforms
the response to a response business object.
4. The import returns the response business object to the component.