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

## Enum VCSStatus

- java.lang.Object
    - java.lang.Enum<VCSStatus>
        - com.ibm.casemgmt.api.constants.VCSStatus

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<VCSStatus>

public enum VCSStatus
extends java.lang.Enum<VCSStatus>
Represents the status of a VCS operation (commit or deliver)

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

FAILED
Indicates a failed status.

IN\_PROGRESS
Indicates a VCS operation is in progress

NONE
Indicates no status or an unknown status.

SUCCESS
Indicates a successfully completed status.
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description static VCSStatus fromIntValue (int value) Gets the enum value that corresponds to the specified integer value. int intValue () Returns the integer value associated with this enum value. java.lang.String stringValue () Returns the string value associated with this enum value. static VCSStatus valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static VCSStatus [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type   | Method and Description                                                                                |
|---------------------|-------------------------------------------------------------------------------------------------------|
| static VCSStatus    | fromIntValue(int value) Gets the enum value that corresponds to the specified integer value.          |
| int                 | intValue() Returns the integer value associated with this enum value.                                 |
| java.lang.String    | stringValue() Returns the string value associated with this enum value.                               |
| static VCSStatus    | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.        |
| static VCSStatus[]  | values() Returns an array containing the constants of this enum type, in the order they are declared. |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait