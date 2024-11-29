- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Enum Constants |
- Field |
- Method

- Detail:
- Enum Constants |
- Field |
- Method

## Enum IntegrationType

- java.lang.Object
    - java.lang.Enum<IntegrationType>
        - com.ibm.casemgmt.api.constants.IntegrationType

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<IntegrationType>

public enum IntegrationType
extends java.lang.Enum<IntegrationType>
Represents the integration type of an object store. An object store can be
 configured for integration with an external host to store the content related to
 the case.
 
 Each value in the enum is associated with an integer and a string representation
 of that value.

ID status:
ID review by David Newhall

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

CM8
Indicates integration with CM8.

P8
Indicates native P8 integration only.
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description static IntegrationType fromIntValue (int value) Gets the enum value that corresponds to the specified integer value. static IntegrationType fromStringValue (java.lang.String strValue) Gets the enum value that corresponds to the specified string value. int intValue () Returns the integer value associated with this enum value. java.lang.String stringValue () Returns the string value associated with this enum value. static IntegrationType valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static IntegrationType [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type        | Method and Description                                                                                         |
|--------------------------|----------------------------------------------------------------------------------------------------------------|
| static IntegrationType   | fromIntValue(int value) Gets the enum value that corresponds to the specified integer value.                   |
| static IntegrationType   | fromStringValue(java.lang.String strValue) Gets the enum value that corresponds to the specified string value. |
| int                      | intValue() Returns the integer value associated with this enum value.                                          |
| java.lang.String         | stringValue() Returns the string value associated with this enum value.                                        |
| static IntegrationType   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.                 |
| static IntegrationType[] | values() Returns an array containing the constants of this enum type, in the order they are declared.          |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait