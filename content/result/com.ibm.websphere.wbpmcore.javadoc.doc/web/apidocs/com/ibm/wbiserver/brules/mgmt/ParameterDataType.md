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
- Enum Constants |
- Field |
- Method

- Detail:
- Enum Constants |
- Field |
- Method

## Enum ParameterDataType

- java.lang.Object
    - java.lang.Enum<ParameterDataType>
        - com.ibm.wbiserver.brules.mgmt.ParameterDataType

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<ParameterDataType>

public enum ParameterDataType
extends java.lang.Enum<ParameterDataType>
Enum defining the possible data types for a parameter.

- =========== ENUM CONSTANT SUMMARY =========== =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

BOOLEAN
Data type boolean.

BYTE
Data type byte.

DOUBLE
Data type double.

FLOAT
Data type float.

INT
Data type int.

LONG
Data type long.

SHORT
Data type short.

STRING
Data type string.
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description static ParameterDataType getParameterDataTypeFor (java.lang.String typeName) java.lang.String getTypeName () Get the name of this data type. static ParameterDataType valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static ParameterDataType [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type          | Method and Description                                                                                |
|----------------------------|-------------------------------------------------------------------------------------------------------|
| static ParameterDataType   | getParameterDataTypeFor(java.lang.String typeName)                                                    |
| java.lang.String           | getTypeName() Get the name of this data type.                                                         |
| static ParameterDataType   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.        |
| static ParameterDataType[] | values() Returns an array containing the constants of this enum type, in the order they are declared. |

    - Methods inherited from class java.lang.Enum
clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait