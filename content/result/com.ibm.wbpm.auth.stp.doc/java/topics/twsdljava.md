<!-- image -->

# Calling WSDL interfaces from Java references

## Before you begin

## About this task

## Procedure

1. Create a component with no implementation type.
2. From the palette, drag a Java component
into your assembly diagram to the left of the first component.
3. Select the untyped component (the one on the right). Click
the Add Interface icon, ,
on the component.
4. In the Add Interface window, select Show
WSDL as the interface type and select an existing interface,
or click New and type a name for the interface
in the Name field.
5. Draw a wire from the Java component
to the component with the WSDL interface. An information message tells
you that a matching reference will be generated on the source. You
are asked if you want to continue. Click OK.
6. Next, you are asked if you want to generate a Java reference compatible with the target WSDL
interface instead of generating a WSDL reference. Click Yes.
By selecting this option, you are able to generate a Java reference on the source. This Java reference allows you to use static methods.
If you use a WSDL-type reference, you must use dynamic invocation
interface (DII) methods to interact with the target service. With
this option, two interfaces are generated - synchronous interfaces
and asynchronous interfaces. (The asynchronous interfaces will be
created after the build run or when you regenerate the implementation.) 
The generated Java reference
on the source will contain the Java interface.
You will be able to open that interface by selecting the reference
and right-clicking to select Open Interface.
When you generate the implementation for the Java component,
it will have a method to locate the referenced service. If you have
already generated the Java implementation
before adding the new reference, you can use the Synchronize > to implementation action to regenerate the implementation and add the
new methods to it.
You should not modify this generated code.
If the WSDL interface is refactored, that is if it is moved or renamed,
the generated interfaces will be refactored accordingly. However,
if the WSDL interface is deleted,  the generated interfaces will still
exist. You will get an error message if the WSDL interfaces have been
changed without refactoring. To fix the error, you can use the Regenerate
Java Interface action on the source reference to regenerate
the Java reference code. 
If you have already
created a WSDL reference on the Java component
to access a component that has a WSDL interface, you can use the Convert
to Java Reference action to change the source WSDL reference
into a Java reference. Right-click the reference to
a Java component to see the pop-up menu, which
contains that option. This action creates a Java interface
on the reference that is equivalent to the WSDL interface and allows
the user to access the target service with static methods.

## Example

## Related concepts

- SCA to Java bridge

## Related tasks

- Creating a Java component
- Calling Java interfaces from WSDL references
- Overriding the generated Service Component Architecture implementation
- Overriding a Service Data Object (SDO) to Java conversion

## Related reference

- Java to XML conversion