<!-- image -->

# SCA to Java bridge

Data that flows through IBM® Business Automation
Workflow is modeled as XML schemas and processed by the server as service data objects or business objects.  A service data object is a runtime representation of business data that implements the data object interface, as described in the Service Data Objects Version 2 specification.

Types that are modeled as XML and whose runtime representations
are data objects are referred to as WSDL types, where inputs , outputs,
and faults are described as XML schemas. Existing Java and
Java 2 Platform Enterprise Edition applications process data as Java types. Java types include Java primitives,
classes defined by the J2SE API, and user-defined Java classes.

In an integration environment, components that are processing WSDL
types sometimes need to invoke existing Java applications
that expect data as Java types.
An example is a Service Component Architecture (SCA) component that
needs to invoke a session EJB. This invocation requires a conversion
between WSDL types and Java types.
The conversion is accomplished by an SCA to Java bridge
component.

- a Java interface
- a Java class that implements one, and only one,
interface
- a stateless session bean remote interface

- java\_classMapper.component
- java\_classMapper.wsdl
- java\_classMapper.java

You can generate the files and wiring in the IBM Integration
Designer assembly editor (see Calling Java interfaces
from WSDL references, which you can access from the related links below) or you can generate the files from IBM Workflow
Server using the genMapper command. If you generate the files from the genMapper command, import those files into a module in IBM Integration
Designer. You can then use the assembly editor to wire the WSDL reference and the Java interface to the generated component.

- You can use a plain Java or
stateless session bean remote interface.
- The Java class can implement one, and
only one, interface. If the class does not implement one interface
or implements more than one interface, the assembly editor will not
offer you the option to generate the bridge component.
- If your input is a user-defined Java class,
it must adhere to section 5.4 of the JAX-RPC 1.1 conventions. The
JAX-RPC specification has implications for the generated code. For
details of the specific type conversions, see Java to
XML conversion in the related links below.

An interface consists of one or more operations, which in turn
have parameters. When using an SCA-to-Java bridge component, you can
pass these parameters only by value. The system uses the Java class name as the type name for the generated
data object. When you need to pass parameters from the operations
of a target Java interface that is a user-defined
interface, you must override the code and provide a concrete class
that the system can instantiate. If the runtime environment cannot
find the type to create the concrete class, the system generates a
runtime exception.

For some java.util container classes, the
mapper generates complex types that are based on xsd:anyType as
the WSDL type. These container classes include arrays, SortedMap,
AbstractMap, BitSet, Dictionary, IdentityHashMap, LinkedHashMap, and
TreeMap (see Java to XML conversion for more
details). In some cases, you might need to override the generated
code by writing custom conversion code.

Edit the generated code according to the commented instructions
in the file, but do not change the file names. For links to topics
that provide more details about editing that code, see the related
tasks below.

## Related tasks

- Creating a Java component
- Calling WSDL interfaces from Java references
- Calling Java interfaces from WSDL references
- Overriding the generated Service Component Architecture implementation
- Overriding a Service Data Object (SDO) to Java conversion

## Related reference

- Java to XML conversion