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

## Enum SolutionDeploymentStatus

- java.lang.Object
    - java.lang.Enum<SolutionDeploymentStatus>
        - com.ibm.casemgmt.api.constants.SolutionDeploymentStatus

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<SolutionDeploymentStatus>

public enum SolutionDeploymentStatus
extends java.lang.Enum<SolutionDeploymentStatus>
Represents the status of a deployed solution.

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

COMPLETE
Indicates a completed status.

COMPLETE\_WITH\_WARNINGS
Indicates a completed with warnings status.

FAILED
Indicates a failed status.

INITIATED
Indicates an initiated status.

UNKNOWN
Indicates an unknown status.
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description static SolutionDeploymentStatus fromIntValue (int value) Gets the enum value that corresponds to the specified integer value. int intValue () Returns the integer value associated with this enum value. java.lang.String stringValue () Returns the string value associated with this enum value. static SolutionDeploymentStatus valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static SolutionDeploymentStatus [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type                 | Method and Description                                                                                |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| static SolutionDeploymentStatus   | fromIntValue(int value) Gets the enum value that corresponds to the specified integer value.          |
| int                               | intValue() Returns the integer value associated with this enum value.                                 |
| java.lang.String                  | stringValue() Returns the string value associated with this enum value.                               |
| static SolutionDeploymentStatus   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.        |
| static SolutionDeploymentStatus[] | values() Returns an array containing the constants of this enum type, in the order they are declared. |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait