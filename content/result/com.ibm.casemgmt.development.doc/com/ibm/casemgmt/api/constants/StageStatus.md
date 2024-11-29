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

## Enum StageStatus

- java.lang.Object
    - java.lang.Enum<StageStatus>
        - com.ibm.casemgmt.api.constants.StageStatus

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<StageStatus>

public enum StageStatus
extends java.lang.Enum<StageStatus>
Represents the status values of a stage.

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

COMPLETED
Indicates that the stage is completed.

ONHOLD
Indicates that the stage has been placed on hold.

UNKNOWN
Indicates the stage is in an unknown state.

WAITING
Indicates that the stage is waiting for a previous stage to complete.

WORKING
Indicates the stage is currently in progress.
    - Method Summary All Methods Static Methods Concrete Methods Modifier and Type Method and Description static StageStatus valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static StageStatus [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type    | Method and Description                                                                                |
|----------------------|-------------------------------------------------------------------------------------------------------|
| static StageStatus   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.        |
| static StageStatus[] | values() Returns an array containing the constants of this enum type, in the order they are declared. |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait