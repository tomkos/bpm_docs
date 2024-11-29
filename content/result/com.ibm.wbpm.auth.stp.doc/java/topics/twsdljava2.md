<!-- image -->

# Calling Java interfaces from WSDL references

## About this task

Most components in the assembly diagram use WSDL interfaces
and references. If such a component needs to call a Java component
or a stateless session bean EJB import that has a Java interface,
you will not be able to wire the source component's WSDL reference
directly to the session bean import that has the Java interface.
However, IBM® Integration
Designer allows
you to drag a Java class or a stateless session
bean onto the assembly editor canvas as a component or import. The
editor then provides the option to generate a facade map component
with a Java reference and a WSDL interface to make
it easy for you to complete the wiring.

For
technical information about the generation process and transforms,
see SCA to Java bridge and Java to XML conversion from the related
links below.

Here are the step-by-step instructions:

## Procedure

1. In the Business Integration view, locate the existing Java implementation or stateless session bean
that you want to use.
2. Drag your Java object
into your assembly diagram. A Java class
becomes a component when it is dropped on the canvas. A stateless
session bean becomes an import.
3. You are prompted to create a facade map component. Click Yes.
A facade map component with a WSDL interface and an equivalent Java reference is created. This facade map component
automatically converts the incoming event for the WSDL interface to
the equivalent Java outgoing event sent to the
service wired to its reference. The following detail from the assembly
diagram shows a facade map component, Bridge, that is wired to a stateless
session bean import, SLSBImport:
4. Draw a wire from the business process component to the
WSDL interface of the bridge component in the assembly. The
editor creates a matching WSDL reference on the BusinessProcess component
to complete the bridge. The facade map component does not contain
any business logic; it just enables a connection between the Java interface and the WSDL reference. The following
assembly diagram shows that the BusinessProcess component is wired
through the Bridge component to the SLSBImport Java import:

## Results

## Related concepts

- SCA to Java bridge

## Related tasks

- Creating a Java component
- Calling WSDL interfaces from Java references
- Overriding the generated Service Component Architecture implementation
- Overriding a Service Data Object (SDO) to Java conversion

## Related reference

- Java to XML conversion