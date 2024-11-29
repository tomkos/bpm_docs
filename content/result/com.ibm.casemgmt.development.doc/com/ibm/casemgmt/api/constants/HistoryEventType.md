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

## Enum HistoryEventType

- java.lang.Object
    - java.lang.Enum<HistoryEventType>
        - com.ibm.casemgmt.api.constants.HistoryEventType

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<HistoryEventType>

public enum HistoryEventType
extends java.lang.Enum<HistoryEventType>
Represents a type of case history event. Each event type is associated with a string value which is the symbolic 
 name of a core Content Engine event class or an ICM custom event class.

ID status:
ID review by David Newhall, 5/20/2012.

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

CANCEL\_CHECKOUT
The cancel checkout event type.

CASE\_FILE
The event type for filing into a case.

CASE\_RELATED
The event type for relating a case to another case.

CASE\_UNFILE
The event type for unfiling from a case.

CHANGE\_CLASS
The event type for changing the class of an object.

CHANGE\_STATE
The event type for changing the state of an object, such as a task object.

CHECKIN
The event type for a checkin.

CHECKOUT
The event type for a checkout.

CLASSIFY\_COMPLETE
The event type for when classification completes.

CREATION
The event type for when an object is created.

DELETION
The event type for when an object is deleted.

DEMOTE\_VERSION
The event type for when a version of a document is demoted.

FILE
The event type for when an object is filed into a folder.

FREEZE
The event type for when an object is frozen.

LOCK
The event type for when an object is locked.

MOVE\_CONTENT
The event type for when the content of a document is moved.

PROMOTE\_VERSION
The event type for when a version of a document is promoted.

PUBLISH\_COMPLETE
The event type for when a publish operation completes.

PUBLISH\_REQUEST
The event type for when a publish operation is requested.

TAKE\_FEDERATED\_OWNERSHIP
The event type for when federated ownership is taken.

UNFILE
The event type for when an object is unfiled from a folder.

UNLOCK
The event type for when an object is unlocked.

UPDATE
The event type for when an object is updated.

UPDATE\_SECURITY
The event type for when the security of an object is updated.
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description static HistoryEventType fromStringValue (java.lang.String strValue) Gets the enum value that corresponds to the specified string value. java.lang.String stringValue () Returns the string value associated with this enum value. static HistoryEventType valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static HistoryEventType [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type         | Method and Description                                                                                         |
|---------------------------|----------------------------------------------------------------------------------------------------------------|
| static HistoryEventType   | fromStringValue(java.lang.String strValue) Gets the enum value that corresponds to the specified string value. |
| java.lang.String          | stringValue() Returns the string value associated with this enum value.                                        |
| static HistoryEventType   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.                 |
| static HistoryEventType[] | values() Returns an array containing the constants of this enum type, in the order they are declared.          |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait