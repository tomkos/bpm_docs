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

## Enum HistoryObjectType

- java.lang.Object
    - java.lang.Enum<HistoryObjectType>
        - com.ibm.casemgmt.api.constants.HistoryObjectType

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<HistoryObjectType>

public enum HistoryObjectType
extends java.lang.Enum<HistoryObjectType>
Represents a type of object that a history event is associated with.
 Each object type is associated with a string value which is the symbolic name
 of a Content Engine class.

ID status:
ID review by David Newhall

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

CASE\_COMMENTS
The object type that history events are associated with that are related to case comments.

CASE\_FOLDER
The object type that history events are associated with related to the case folder.

CASE\_SUBFOLDER
The object type that history events are associated with related to a subfolder in a case.

CASE\_TASK
The object type that history events are associated with related to tasks.

DOCUMENT
The object type that history events are associated with related to documents.

QUICK\_TASK
The object type that history events are associated with related to quick tasks.

STAGE
The object type that history events are associated with related to quick tasks.

TASK\_COMMENTS
The object type that history events are associated with related to comments about tasks.

VERSION\_SERIES\_COMMENTS
The object type that history events are associated with related to comments about documents.

WORK\_ITEM\_COMMENTS
The object type that history events are associated with related to comments about work items.
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description static HistoryObjectType fromStringValue (java.lang.String strValue) Gets the enum value that corresponds to the specified string value. java.lang.String stringValue () Returns the string value associated with this enum value. static HistoryObjectType valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static HistoryObjectType [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type          | Method and Description                                                                                         |
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| static HistoryObjectType   | fromStringValue(java.lang.String strValue) Gets the enum value that corresponds to the specified string value. |
| java.lang.String           | stringValue() Returns the string value associated with this enum value.                                        |
| static HistoryObjectType   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.                 |
| static HistoryObjectType[] | values() Returns an array containing the constants of this enum type, in the order they are declared.          |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait