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

## Class AttributeType

- java.lang.Object
    - com.ibm.task.api.AttributeType

- All Implemented Interfaces:
java.io.Serializable

public final class AttributeType
extends java.lang.Object
implements java.io.Serializable
This enumeration class defines symbolic constants for attribute types.
 These values are to be used when attribute type information is retrieved.
Since:
7.0
See Also:Serialized Form

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static AttributeType
BINARY
Symbolic constant for attribute type BINARY

static AttributeType
BOOLEAN
Symbolic constant for attribute type BOOLEAN

static java.lang.String
COPYRIGHT 

static AttributeType
DECIMAL
Symbolic constant for attribute type DECIMAL

static AttributeType
ID
Symbolic constant for attribute type object ID

static AttributeType
NUMBER
Symbolic constant for attribute type NUMBER

static AttributeType
STRING
Symbolic constant for attribute type String

static AttributeType
TIMESTAMP
Symbolic constant for attribute type TIMESTAMP
    - Method Summary Methods Modifier and Type Method and Description static AttributeType newAttributeType (java.lang.String typeString) Factory method to create an attribute type by its string representation. java.lang.String toString () Returns a string representation of the attribute type.

### Method Summary

| Modifier and Type    | Method and Description                                                                                                 |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| static AttributeType | newAttributeType(java.lang.String typeString) Factory method to create an attribute type by its string representation. |
| java.lang.String     | toString() Returns a string representation of the attribute type.                                                      |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait