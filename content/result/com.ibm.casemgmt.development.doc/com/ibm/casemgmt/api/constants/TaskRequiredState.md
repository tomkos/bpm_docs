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

## Enum TaskRequiredState

- java.lang.Object
    - java.lang.Enum<TaskRequiredState>
        - com.ibm.casemgmt.api.constants.TaskRequiredState

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<TaskRequiredState>

public enum TaskRequiredState
extends java.lang.Enum<TaskRequiredState>
Represents the required state of a task. The values of this enum represent
 values of the choice list CmAcmRequiredStateChoiceList.
 
 Each value in the enum is associated with an integer value from the choice list.

ID status:
ID review by David Newhall

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

NOT\_REQUIRED
Deprecated. 
This value is not used.

OPTIONAL
Indicates that a task is optional.

REQUIRED\_BY\_INCLUSIVE
Indicates that a task is required because it is in an inclusive set of tasks.

REQUIRED\_BY\_USER
Indicates a task was marked required by a user.
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description static TaskRequiredState fromIntValue (int intValue) Gets the enum value that corresponds to the specified integer value. int intValue () Returns the integer value associated with this enum value. static TaskRequiredState valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static TaskRequiredState [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type          | Method and Description                                                                                |
|----------------------------|-------------------------------------------------------------------------------------------------------|
| static TaskRequiredState   | fromIntValue(int intValue) Gets the enum value that corresponds to the specified integer value.       |
| int                        | intValue() Returns the integer value associated with this enum value.                                 |
| static TaskRequiredState   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.        |
| static TaskRequiredState[] | values() Returns an array containing the constants of this enum type, in the order they are declared. |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait