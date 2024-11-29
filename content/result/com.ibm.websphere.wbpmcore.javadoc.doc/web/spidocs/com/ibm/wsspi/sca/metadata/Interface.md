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

## Interface Interface

- public interface Interface
Interface that represent the interface information from a SCA component.
Since:
7.5.1.0

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

java.util.Collection<Operation>
getOperations()
Method returns the list of Operations of the specified interface.

java.util.Collection<OperationType>
getOperationTypes()
Method returns the list of OperationTypes of the specified interface.

javax.xml.namespace.QName
getPortType()
Method returns the QName of the specified interface.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getPortType
javax.xml.namespace.QName getPortType()
Method returns the QName of the specified interface.
Returns:QName
     QName of the specified interface.
    - getOperations
java.util.Collection<Operation> getOperations()
Method returns the list of Operations of the specified interface.
Returns:Collection
     The list of Operations of the specified interface.
    - getOperationTypes
java.util.Collection<OperationType> getOperationTypes()
Method returns the list of OperationTypes of the specified interface.
Returns:Collection
     The list of OperationTypes of the specified interface.