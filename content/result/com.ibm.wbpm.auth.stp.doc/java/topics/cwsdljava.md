<!-- image -->

# Using Java in the assembly editor

- You can create a Java component.
- You can add a Java reference to a Java component or stand-alone references
to invoke a target service that has a matching WSDL interface. To help you
with this action, you can convert a WSDL reference on a Java component
or on stand-alone references to a Java reference.
- You can drag a Java class onto the assembly editor canvas
as a component or drag an EJB (stateless session bean) as an import. The assembly
editor can generate a map component that allows you to invoke the Java component
or import from a WSDL component.

- When you wire a mediation flow component to a Java component, the service message object
is not propagated through the Java component. As a result, an import invoked
via the Java component will not have any transport headers that
are set inside the mediation flow component.
- You cannot wire a Java component's reference to the interface
of a mediation flow component.

The topics listed below provide information about these processes.

- Creating a Java component

Although most components use Service Component Architecture (SCA) and WSDL interfaces, you can also create Java components and use them with SCA components and Java interfaces.
- SCA to Java bridge

You cannot directly wire a component with a Web Services Definition Language (WSDL) type of reference to another component that has a Java interface, but there is a utility that helps you create a bridge component to make a WSDL to Java connection. The component is generated, so you do not have to write conversion code.
- Calling WSDL interfaces from Java references

In top-down development, if you want a Java component or stand-alone references to invoke a component that has a WSDL interface, you do not need to create the Java reference manually. You can wire a Java component to a component with a WSDL interface. The assembly editor automatically adds a reference to the Java component. You can then choose to generate a Java interface for that reference that matches the WSDL interface on the other component. Otherwise, a WSDL interface will be generated for the reference.
- Calling Java interfaces from WSDL references

Occasions might arise when you want to access a service with Java interfaces from a component that can only support WSDL references. However, you cannot directly draw a wire from a WSDL-typed reference to a Java component or a stateless session bean EJB import that has a Java interface. As well, most component implementations do not allow Java-typed references. The assembly editor provides an easy way of overcoming this difficulty.
- Overriding the generated Service Component Architecture implementation

Sometimes, the conversion the system creates between a Java code and a Service Data Object (SDO) may not meet your needs. Use this procedure to replace the default Service Component Architecture (SCA) class implementation with your own.
- Overriding a Service Data Object (SDO) to Java conversion

Sometimes, the conversion the system creates between a Service Data Object (SDO) and a Java type object may not meet your needs. Use this procedure to replace the default implementation with your own.
- Java to XML conversion

The system generates XML based on Java types using predefined rules.