<!-- image -->

# Imports and exports

A module exports its capability when it provides the ability for an external service or module to
invoke an operation on a defined interface. Using exports, a module can be made available over a
number of different transport protocols.

Figure 1. SCA module

<!-- image -->

- SCA (used for SCA module to module)
- Web service
- JMS
- MQ
- HTTP
- Enterprise JavaBeans

Figure 2. Module to module communication using imports and exports

<!-- image -->

Figure 3. Module using different protocols to communicate

<!-- image -->

- Function selectors
- Data handlers
- Fault selector
- Fault handler
- Context propagation
- Exception handling

- Function selector

The function selector determines which operation defined on the associated interface is invoked.
- Data handler

Data handlers are reusable transformation logic in IBM Workflow Server, which can be used by exports and imports. Data handlers can transform native formats into business data and from business data into native formats required by external services.
- Fault handling

You can configure your import and export bindings to handle faults (for example, business exceptions) that occur during processing by specifying fault selectors and fault handlers. The fault selector determines whether the response message is a normal response, a business or runtime fault that is received by an import. A fault handler processes fault data and transforms it into the correct format to be sent by the export or import binding.
- Context propagation

Context propagation allows information associated with an invocation to be carried throughout a request or response.
- Exception handling

Within an import or export, unexpected situations cause exceptions to be raised. The way in which the binding is configured determines how exceptions, raised by data handlers or data bindings, are handled.
- Retry configuration

SCA uses a service integration bus to transport messages between components, imports, and exports. These destinations are created by installation tasks when a module is installed to a IBM Workflow Server server. If the target service component returns a system error, the service integration bus automatically resubmits the message until a threshold on the module destination is reached (the default retry threshold is 4).

<!-- image -->