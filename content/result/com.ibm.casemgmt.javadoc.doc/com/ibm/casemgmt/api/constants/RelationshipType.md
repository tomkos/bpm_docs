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

## Enum RelationshipType

- java.lang.Object
    - java.lang.Enum<RelationshipType>
        - com.ibm.casemgmt.api.constants.RelationshipType

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<RelationshipType>

public enum RelationshipType
extends java.lang.Enum<RelationshipType>
Represents a type of relationship between two cases. A relationship is represented by an
 instance of a subclass of the Content Engine Link class. The Link class has the properties
 Tail and Head.  The Tail represents the source case
 in the direction of the relationship and Head represents the destination in 
 that direction. 
 
 Each value in the enum is associated with an integer and a string representation of that value.

ID status:
ID review by David Newhall

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

CHILD
Indicates that a case is a child of another case.

MERGE\_SOURCE
Indicates that a case is the source of a merge with another case.

MERGE\_TARGET
Indicates that a case is the target of a merge with another case.

PARENT
Indicates that a case is the parent of another case.

RELATED
Indicates that a case is in general related to another case.

SPLIT\_SOURCE
Indicates that a case is the source of a split to another case.

SPLIT\_TARGET
Indicates that a case is the target of a split from another case.

UNRELATED
Indicates that two cases are unrelated that were previously related.
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description static RelationshipType fromIntValue (int intValue) Gets the enum value that corresponds to the specified integer value. static RelationshipType fromStringValue (java.lang.String strValue) Gets the enum value that corresponds to the specified string value. int intValue () Returns the integer value associated with this enum value. java.lang.String stringValue () Returns the string value associated with this enum value. static RelationshipType valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static RelationshipType [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type         | Method and Description                                                                                         |
|---------------------------|----------------------------------------------------------------------------------------------------------------|
| static RelationshipType   | fromIntValue(int intValue) Gets the enum value that corresponds to the specified integer value.                |
| static RelationshipType   | fromStringValue(java.lang.String strValue) Gets the enum value that corresponds to the specified string value. |
| int                       | intValue() Returns the integer value associated with this enum value.                                          |
| java.lang.String          | stringValue() Returns the string value associated with this enum value.                                        |
| static RelationshipType   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.                 |
| static RelationshipType[] | values() Returns an array containing the constants of this enum type, in the order they are declared.          |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait