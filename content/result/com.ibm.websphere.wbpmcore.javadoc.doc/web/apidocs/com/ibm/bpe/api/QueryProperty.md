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

## Interface QueryProperty

- All Superinterfaces:
java.io.Serializable

All Known Subinterfaces:
QueryPropertyExtension

public interface QueryProperty
extends java.io.Serializable
Returns the properties of a variable that can be queried.
 
 Query properties can be declared for process-level variables.
 The type of a query property can be a built-in XML schema simple type or a user-defined
 simple type based on a built-in XML schema type using restrictions.
Since:
6.0.2

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
TYPE\_DECIMAL
Symbolic constant for a floating point type.

static int
TYPE\_GENERIC
Symbolic constant for a type that is not a string, number, decimal, or timestamp.

static int
TYPE\_NUMBER
Symbolic constant for an integer type.

static int
TYPE\_STRING
Symbolic constant for a string type.

static int
TYPE\_TIMESTAMP
Symbolic constant for a timestamp type.
    - Method Summary

Methods 

Modifier and Type
Method and Description

int
getMappedType()
Returns the type that can be used in queries.

java.lang.String
getName()
Returns the name of the property that can be queried.

java.lang.String
getNamespace()
Returns the namespace of the property that can be queried.

java.lang.String
getType()
Returns the QName of the property type.

java.lang.String
getVariableName()
Returns the name of the process-level variable that contains properties
 that can be used in queries.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- TYPE\_GENERIC
static final int TYPE\_GENERIC
Symbolic constant for a type that is not a string, number, decimal, or timestamp.
See Also:Constant Field Values

- TYPE\_STRING
static final int TYPE\_STRING
Symbolic constant for a string type.
See Also:Constant Field Values

- TYPE\_NUMBER
static final int TYPE\_NUMBER
Symbolic constant for an integer type.
See Also:Constant Field Values

- TYPE\_DECIMAL
static final int TYPE\_DECIMAL
Symbolic constant for a floating point type.
See Also:Constant Field Values

- TYPE\_TIMESTAMP
static final int TYPE\_TIMESTAMP
Symbolic constant for a timestamp type.
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getVariableName
java.lang.String getVariableName()
Returns the name of the process-level variable that contains properties
 that can be used in queries.
Returns:The name of the variable.
    - getName
java.lang.String getName()
Returns the name of the property that can be queried.
Returns:The name of the property.
    - getNamespace
java.lang.String getNamespace()
Returns the namespace of the property that can be queried.
 For properties that are defined inline, the namespace is the namespace of the BPEL process.
Returns:The namespace of the property.
    - getMappedType
int getMappedType()
Returns the type that can be used in queries.
 
 Possible values are: TYPE\_GENERIC, TYPE\_STRING, TYPE\_NUMBER, TYPE\_DECIMAL, TYPE\_TIMESTAMP.
Returns:The mapped type.
    - getType
java.lang.String getType()
Returns the QName of the property type.
 It can be an xsd type or a user-defined type.
Returns:The QName of the property type.