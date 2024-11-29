- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Interface InterfaceType

- public interface InterfaceType
The InterfaceType interface represents a service interface. Service interfaces can be described using either the Java or the WSDL
 language. An InterfaceType provides a language independent view of an interface. The interface has a namespace, a name and a
 collection of OperationTypes representing the java methods or WSDL operations declared on the interface.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getName()
Returns the interface name.

OperationType
getOperationType(java.lang.String name)
Returns an OperationType object representing the named operation.

java.util.List
getOperationTypes()
Returns a list of OperationType objects representing the operations on the interface.

java.lang.String
getURI()
Returns the interface namespace URI.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getName
java.lang.String getName()
Returns the interface name.
Returns:The name of the interface.
    - getURI
java.lang.String getURI()
Returns the interface namespace URI.
Returns:The namespace URI of the interface.
    - getOperationTypes
java.util.List getOperationTypes()
Returns a list of OperationType objects representing the operations on the interface.
Returns:The list of OperationType objects representing the operations on the interface.
    - getOperationType
OperationType getOperationType(java.lang.String name)
Returns an OperationType object representing the named operation.
Parameters:name - 
Returns:The OperationType object representing the named operation.