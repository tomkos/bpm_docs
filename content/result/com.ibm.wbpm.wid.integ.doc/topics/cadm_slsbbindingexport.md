<!-- image -->

# EJB export bindings

- Creating EJB export bindings using the external service wizardYou
can use the external service wizard in Integration Designer to build
an EJB export service based on an existing implementation. The external
service wizard creates services based on criteria that you provide.
It then generates business objects, interfaces, and export files based
on the services discovered.
- Creating EJB export bindings using the assembly editorYou can
create an EJB export using the Integration Designer assembly
editor.

- When you generate an export for an existing SCA component that
has an existing WSDL interface, the export is assigned a Java interface.
- When you generate an export for a Java interface,you can select either a WSDL or a Java interfacefor the export. Note: A Java interfaceused to create an EJB export has the following limitations with regardto the objects (input and output parameters and exceptions) passedas parameters on a remote call: In addition, the exception must be a checked exception, inheritedfrom java.lang.Exception, and it must be singular (that is, it doesnot support throwing multiple checked exception types). Notealso that the business interface of a Java EnterpriseBeanis a plain Java interface andmust not extend javax.ejb.EJBObject or javax.ejb.EJBLocalObject. Themethods of the business interface should not throw java.rmi.Remote.Exception.
    - They must be of concrete type (instead of an interface or abstract
type).
    - They must conform to the Enterprise JavaBeans specification. They must be serializable
and have the default no-argument constructor, and all properties must
be accessible through getter and setter methods.Refer to the Sun
Microsystems, Inc., web site at http://java.sun.com for information
about the Enterprise JavaBeans specification.

In addition, the exception must be a checked exception, inherited
from java.lang.Exception, and it must be singular (that is, it does
not support throwing multiple checked exception types).

Note
also that the business interface of a Java EnterpriseBean
is a plain Java interface and
must not extend javax.ejb.EJBObject or javax.ejb.EJBLocalObject. The
methods of the business interface should not throw java.rmi.Remote.Exception.

The EJB export bindings can interact with Java EE business logic using either the EJB
2.1 programming model or the EJB 3.0 programming model.

- Local invocation is used when the Java EE business logic calls an SCA component
that resides on the same server as the export.
- Remote invocation is used when the Java EE business logic does not
reside on the same server as the export. For example, in the
following figure, an EJB uses RMI/IIOP to call an SCA component on
a different server.Figure 1. Remote
call from a client to an SCA component by
way of an EJB export

When it configures the EJB binding, Integration Designer uses the
JNDI name to determine the EJB programming model level and the type
of invocation (local or remote).

- JAX-WS data handler
- EJB export function selector

If your user scenario is not based on the JAX-WS mapping, you might
need a custom data handler and function selector to perform the tasks
otherwise completed by the components that are part of the EJB export
bindings. This includes the mapping normally completed by the custom
mapping algorithm.