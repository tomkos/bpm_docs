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

## Interface OperationType

- public interface OperationType
The OperationType interface represents an operation on a service interface. Service interfaces can be described using either the Java or the WSDL
 language. An InterfaceType provides a language independent view of an interface, OperationType provides a language independent view of an operation
 (a Java method or a WSDL operation). OperationType provides methods to get the operation name as well as the SDO type of the input, output, and the
 exceptions that can be thrown by the operation.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static commonj.sdo.Type
MULTIPART\_TYPE
Used to indicate a Multipart type.
    - Method Summary

Methods 

Modifier and Type
Method and Description

commonj.sdo.Type
getExceptionType(java.lang.String uri,
                java.lang.String name)
Returns an SDO type describing the named exception type.

java.util.List
getExceptionTypes()
Returns the list of SDO types describing the exceptions that can be thrown by the operation.

commonj.sdo.Type
getInputType()
Returns the SDO type describing the operation input type.

java.lang.String
getName()
Returns the operation name.

commonj.sdo.Type
getOutputType()
Returns the SDO type describing the operation output type.

boolean
isWrapperType(commonj.sdo.Type type)
Returns true if the given type represents a wrapper for the parameters to the operation.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- MULTIPART\_TYPE
static final commonj.sdo.Type MULTIPART\_TYPE
Used to indicate a Multipart type. Types that extend the Multipart type represent wrappers for multiple WSDL parts or parameters on a java method.

- Method Detail

### Method Detail

    - getName
java.lang.String getName()
Returns the operation name.
Returns:The operation name.
    - getInputType
commonj.sdo.Type getInputType()
Returns the SDO type describing the operation input type.
Returns:The operation input type.
    - getOutputType
commonj.sdo.Type getOutputType()
Returns the SDO type describing the operation output type.
Returns:The operation output type.
    - getExceptionTypes
java.util.List getExceptionTypes()
Returns the list of SDO types describing the exceptions that can be thrown by the operation.
Returns:the List of SDO types describing the exceptions thrown by the operation.
    - getExceptionType
commonj.sdo.Type getExceptionType(java.lang.String uri,
                                java.lang.String name)
Returns an SDO type describing the named exception type.
Parameters:uri - The namespace URI of the exception type.name - The name of the exception type.
Returns:The SDO type describing the exception.
    - isWrapperType
boolean isWrapperType(commonj.sdo.Type type)
Returns true if the given type represents a wrapper for the parameters to the operation.
Parameters:type - The SDO type.
Returns:True if the given type represents a wrapper for multiple parameters.