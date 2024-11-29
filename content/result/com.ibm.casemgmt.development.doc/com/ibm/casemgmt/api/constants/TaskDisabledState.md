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

## Enum TaskDisabledState

- java.lang.Object
    - java.lang.Enum<TaskDisabledState>
        - com.ibm.casemgmt.api.constants.TaskDisabledState

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<TaskDisabledState>

public enum TaskDisabledState
extends java.lang.Enum<TaskDisabledState>
Represents the disabled state of a task. The values of this enum represent
 values of the choice list CmAcmDisabledStateChoiceList.
 
 Each value in the enum is associated with an integer value from the choice list.

ID status:
ID review by David Newhall

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

DISABLED\_ABORTED
Indicates that a task has been disabled because it has been aborted.

DISABLED\_BY\_EXCLUSIVE
Indicates that a task has been disabled because it is a non-running task in an exclusive
 set of tasks.

DISABLED\_BY\_USER
Indicates that a task has been disabled by a user.

ENABLED
Indicates that a task is enabled.
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description static TaskDisabledState fromIntValue (int intValue) Gets the enum value that corresponds to the specified integer value. int intValue () Returns the integer value associated with this enum value. static TaskDisabledState valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static TaskDisabledState [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type          | Method and Description                                                                                |
|----------------------------|-------------------------------------------------------------------------------------------------------|
| static TaskDisabledState   | fromIntValue(int intValue) Gets the enum value that corresponds to the specified integer value.       |
| int                        | intValue() Returns the integer value associated with this enum value.                                 |
| static TaskDisabledState   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.        |
| static TaskDisabledState[] | values() Returns an array containing the constants of this enum type, in the order they are declared. |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait