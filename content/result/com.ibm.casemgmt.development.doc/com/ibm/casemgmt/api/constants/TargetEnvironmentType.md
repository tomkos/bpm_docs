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

## Enum TargetEnvironmentType

- java.lang.Object
    - java.lang.Enum<TargetEnvironmentType>
        - com.ibm.casemgmt.api.constants.TargetEnvironmentType

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<TargetEnvironmentType>

public enum TargetEnvironmentType
extends java.lang.Enum<TargetEnvironmentType>
Represents an environment type.

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

DEVELOPMENT
Indicates a development environment.

PRODUCTION
Indicates a production environment.
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description static TargetEnvironmentType fromIntValue (int value) Gets the enum value that corresponds to the specified integer value. static TargetEnvironmentType fromStringValue (java.lang.String strValue) Gets the enum value that corresponds to the specified string value. int intValue () Returns the integer value associated with this enum value. java.lang.String stringValue () Returns the string value associated with this enum value. static TargetEnvironmentType valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static TargetEnvironmentType [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type              | Method and Description                                                                                         |
|--------------------------------|----------------------------------------------------------------------------------------------------------------|
| static TargetEnvironmentType   | fromIntValue(int value) Gets the enum value that corresponds to the specified integer value.                   |
| static TargetEnvironmentType   | fromStringValue(java.lang.String strValue) Gets the enum value that corresponds to the specified string value. |
| int                            | intValue() Returns the integer value associated with this enum value.                                          |
| java.lang.String               | stringValue() Returns the string value associated with this enum value.                                        |
| static TargetEnvironmentType   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.                 |
| static TargetEnvironmentType[] | values() Returns an array containing the constants of this enum type, in the order they are declared.          |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait