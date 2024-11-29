<!-- image -->

# EJB import bindings

- Creating EJB import using the external service wizardYou can
use the external service wizard in Integration Designer to build
an EJB import based on an existing implementation. The external service
wizard creates services based on criteria that you provide. It then
generates business objects, interfaces, and import files based on
the services discovered.
- Creating EJB import using the assembly editorYou can create
an EJB import within an assembly diagram using the Integration Designer assembly
editor. From the palette, you can use either an Import or use a Java™ class to create the EJB binding.

The generated import has data bindings that make
the Java-WSDL connection instead of requiring a Java bridge component.
You can directly wire a component with a Web Services Description
Language (WSDL) reference to the EJB import that communicates to an
EJB-based service using a Java interface.

The EJB import can interact with Java EE business logic using either
the EJB 2.1 programming model or the EJB 3.0 programming model.

- Local invocation is used when you want to call Java EE business
logic that resides on the same server as the import.Figure 1. Local invocation of an EJB (EJB
3.0 only)
- Remote invocation is used when you want to call Java EE business
logic that does not reside on the same server as the import. For
example, in the following figure, an EJB import uses the Remote Method
Invocation over Internet InterORB Protocol (RMI/IIOP) to invoke an
EJB method on another server.Figure 2. Remote invocation
of an EJB

When it configures the EJB binding, Integration Designer uses the
JNDI name to determine the EJB programming model level and the type
of invocation (local or remote).

- JAX-WS data handler
- EJB fault selector
- EJB import function selector

If your user scenario is not based on the JAX-WS mapping, you might
need a custom data handler, function selector, and fault selector
to perform the tasks otherwise completed by the components that are
part of the EJB import bindings. This includes the mapping normally
completed by the custom mapping algorithm.