<!-- image -->

# Accessing Enterprise JavaBeans (EJB) services

## About this task

The generated import will have data bindings that make the
Java-WSDL connection instead of requiring a Java™ bridge component. This will allow for the
direct wiring of a component with a Web Services Description Language
(WSDL) reference to the EJB import which communicates to an EJB-based
service using a Java interface.

- You have a PI (project interchange) file which was created in Rational® Application
Developer that
has an EJB application.
- You have a EJB client JAR file in the module.
- You have EJB Java classes
that have been copied in a project in the workspace.
- You have an EAR file that contains the EJB application created
outside of IBM Integration
Designer.

External Java EE applications
can invoke an SCA component by way of an EJB export binding. Using
an EJB export lets you expose SCA components so that external Java EE applications can invoke
those components using the EJB programming model.

The EJB export
bindings can interact with Java EE
business logic using either the EJB 2.1 programming model or the EJB
3.0 programming model.

- EJB 2.1 local invocation is not supported for an EJB import.
- An SCA component cannot be exposed through an EJB 2.1 local enterprise
bean by an EJB export.

The following topics describe concepts and step-by-step
instructions for creating EJB imports and EJB exports using IBM Integration
Designer:

- Creating EJB imports

You can use IBM Integration Designer to create EJB imports that invoke remote EJBs.
- Creating EJB exports

You can use IBM Integration Designer to expose SCA components using an export with an EJB binding so that external Java 2 Platform Enterprise Edition applications can invoke those components using the EJB programming model.
- EJB 3.0 and EJB 2.1

EJB 3.0 has some significant differences with EJB 2.1. You should be aware of these differences when developing applications with EJB bindings based on 3.0 or higher.
- JAXB and EJBs

A valid generated XML Schema Definition (XSD) is not necessarily valid in the context of generated Java beans based on it.