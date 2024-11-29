<!-- image -->

# Fault handling

- For an export binding, the fault data handler transforms the exception
business object sent from the component to a response message that
can be used by the client application.
- For an import binding, the fault data handler transforms the fault
data or response message sent from a service into an exception business
object that can be used by the SCA component.

For import bindings, the binding calls the fault selector,
which determines whether the response message is a normal response,
a business fault, or a runtime exception.

- If the fault data handler is set at all three levels, the data
handler associated with a particular fault is called.
- If fault data handlers are set at the operation and binding levels,
the data handler associated with the operation is called.

Two editors are used in IBM® Integration
Designer to
specify fault handling. The interface editor is used to indicate whether
there will be a fault on an operation. After a binding is generated
with this interface, the editor in the properties view lets you configure
how the fault will be handled. For more information, see the Fault
selectors topic in the IBM Integration
Designer information
center.

- How faults are handled in export bindings

When a fault occurs during the processing of the request from a client application, the export binding can return the fault information to the client. You configure the export binding to specify how the fault should be processed and returned to the client.
- How faults are handled in import bindings

A component uses an import to send a request to a service outside the module. When a fault occurs during the processing of the request, the service returns the fault to the import binding. You can configure the import binding to specify how the fault should be processed and returned to the component.