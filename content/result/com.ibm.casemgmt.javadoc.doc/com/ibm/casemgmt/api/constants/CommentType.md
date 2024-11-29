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

## Enum CommentType

- java.lang.Object
    - java.lang.Enum<CommentType>
        - com.ibm.casemgmt.api.constants.CommentType

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<CommentType>

public enum CommentType
extends java.lang.Enum<CommentType>
Represents a type of comment applied to a case. Comments are always attached
 to a case, but depending on their type may also apply to another object type
 related to that case.
 
 Each value in the enum is associated with a string representation of that value.

ID status:
ID review by David Newhall

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

CASE
The type of comment applied to a case in general.

DOCUMENT
The type of comment applied to a particular document in a case.

TASK
The type of comment applied to a particular task in a case.

WORKITEM
The type of comment applied to a work item.
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description static CommentType fromStringValue (java.lang.String strValue) Gets the enum value that corresponds to the specified string value. java.lang.String stringValue () Returns the string value associated with this enum value. static CommentType valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static CommentType [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type    | Method and Description                                                                                         |
|----------------------|----------------------------------------------------------------------------------------------------------------|
| static CommentType   | fromStringValue(java.lang.String strValue) Gets the enum value that corresponds to the specified string value. |
| java.lang.String     | stringValue() Returns the string value associated with this enum value.                                        |
| static CommentType   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.                 |
| static CommentType[] | values() Returns an array containing the constants of this enum type, in the order they are declared.          |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait