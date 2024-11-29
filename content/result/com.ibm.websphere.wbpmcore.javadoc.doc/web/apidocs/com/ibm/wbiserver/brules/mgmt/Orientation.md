- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Enum Constants |
- Field |
- Method

- Detail:
- Enum Constants |
- Field |
- Method

## Enum Orientation

- java.lang.Object
    - java.lang.Enum<Orientation>
        - com.ibm.wbiserver.brules.mgmt.Orientation

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<Orientation>

public enum Orientation
extends java.lang.Enum<Orientation>
An enum used to identify the orientation of a tree condition.  The orientation can be either
 "row" or "column".

- =========== ENUM CONSTANT SUMMARY =========== =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

COLUMN
Indicates that the element is to be oriented as a column.

ROW
Indicates that the element is to be oriented as a row.
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description static Orientation valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static Orientation [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type    | Method and Description                                                                                |
|----------------------|-------------------------------------------------------------------------------------------------------|
| static Orientation   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.        |
| static Orientation[] | values() Returns an array containing the constants of this enum type, in the order they are declared. |

    - Methods inherited from class java.lang.Enum
clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait