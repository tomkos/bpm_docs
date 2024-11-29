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

## Enum TaskLaunchMode

- java.lang.Object
    - java.lang.Enum<TaskLaunchMode>
        - com.ibm.casemgmt.api.constants.TaskLaunchMode

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<TaskLaunchMode>

public enum TaskLaunchMode
extends java.lang.Enum<TaskLaunchMode>
Represents the launch mode of a task. The values of this enum represent
 values of the choice list CmAcmLaunchModeChoiceList.
 
 Each value in the enum is associated with an integer value from the choice list.

ID status:
ID review by David Newhall

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

SYSTEM\_AUTOMATIC
Indicates that a task is a system managed task that is started automatically.

SYSTEM\_AUTOMATIC\_REPEATABLE
Indicates that a task is a system-managed task that is started automatically.

SYSTEM\_MANUAL
Indicates that a task is a system managed task that is started manually.

SYSTEM\_MANUAL\_REPEATABLE
Indicates that a task is a system-managed task that is started manually.

USER\_AUTOMATIC
Indicates that a task is created by a user.
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description static TaskLaunchMode fromIntValue (int intValue) Gets the enum value that corresponds to the specified integer value. int intValue () Returns the integer value associated with this enum value. static TaskLaunchMode valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static TaskLaunchMode [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type       | Method and Description                                                                                |
|-------------------------|-------------------------------------------------------------------------------------------------------|
| static TaskLaunchMode   | fromIntValue(int intValue) Gets the enum value that corresponds to the specified integer value.       |
| int                     | intValue() Returns the integer value associated with this enum value.                                 |
| static TaskLaunchMode   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.        |
| static TaskLaunchMode[] | values() Returns an array containing the constants of this enum type, in the order they are declared. |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait