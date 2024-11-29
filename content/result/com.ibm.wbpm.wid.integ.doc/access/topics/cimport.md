<!-- image -->

# Imports

Imports are used in an application in exactly the same way as local
components. This consistency provides a uniform assembly model for
all functions, regardless of their locations or implementations.

Imports have interfaces that are the same as, or a subset of, the
interfaces of the remote service that they are associated with so
that those remote services can be called. To share the interfaces
between modules, put the interfaces into a library. Then, for both
modules, add a dependency on the library to use its resources.

Imports and exports require binding information, which specifies
the means of transporting the data from the modules. An import
binding describes the specific way that an external service is
bound to an import component. For an import that is generated from
an export, the binding type of the import is automatically specified.
Imports can use the following bindings: SCA, web service, HTTP, messaging
(JMS, MQ JMS, generic JMS, MQ), stateless session Enterprise JavaBean
(EJB), and EIS. Available function (or business logic) implemented
in remote systems (such as web services, EIS functions, EJBs, or remote
SCA components) is modeled as an imported service.

If you use the palette in the assembly editor to create the import,
you must specify a binding type for the external service in order
to test it.