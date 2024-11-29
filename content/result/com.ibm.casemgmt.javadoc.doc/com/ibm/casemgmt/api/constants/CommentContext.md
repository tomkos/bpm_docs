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

## Enum CommentContext

- java.lang.Object
    - java.lang.Enum<CommentContext>
        - com.ibm.casemgmt.api.constants.CommentContext

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<CommentContext>

public enum CommentContext
extends java.lang.Enum<CommentContext>
Represents the action, such as adding a document
 or case, that was being taken when a comment was created.
 
 Each value in the enum is associated with an integer value from the Content Engine choice list 
 CmAcmActionChoiceList. It is also associated with a string representation of that value.

ID status:
ID review by David Newhall, 5/20/2012.

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

CASE
The context when adding a comment on a case.

CASE\_CREATE
The context when adding a comment and creating a case.

CASE\_UPDATE
The context when updating comment on a case.

DOCUMENT
The context when adding a comment on a document.

DOCUMENT\_ADD
The context when adding a comment and adding a document.

QUICK\_TASK
The context when adding a comment on a quick task.

TASK
The context when adding a comment on a task.

TASK\_CREATE
The context when adding a comment and creating a task.

TASK\_DISABLE
The context when adding a comment and disabling a task.

TASK\_ENABLE
The context when adding a comment and enabling a task.

TASK\_START
The context when adding a comment and starting a task.

WORK\_ITEM
The context when adding a comment on a work item.

WORK\_ITEM\_COMPLETE
The context when adding a comment and completing a work item.
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description static CommentContext fromIntValue (int intValue) Gets the enum value that corresponds to the specified integer value. static CommentContext fromStringValue (java.lang.String strValue) Gets the enum value that corresponds to the specified string value. int intValue () Returns the integer value associated with this enum value. java.lang.String stringValue () Returns the string value associated with this enum value. static CommentContext valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static CommentContext [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type       | Method and Description                                                                                         |
|-------------------------|----------------------------------------------------------------------------------------------------------------|
| static CommentContext   | fromIntValue(int intValue) Gets the enum value that corresponds to the specified integer value.                |
| static CommentContext   | fromStringValue(java.lang.String strValue) Gets the enum value that corresponds to the specified string value. |
| int                     | intValue() Returns the integer value associated with this enum value.                                          |
| java.lang.String        | stringValue() Returns the string value associated with this enum value.                                        |
| static CommentContext   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.                 |
| static CommentContext[] | values() Returns an array containing the constants of this enum type, in the order they are declared.          |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait