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

## Enum RelationshipType

- java.lang.Object
    - java.lang.Enum<RelationshipType>
        - com.ibm.websphere.wsaddr10.RelationshipType

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<RelationshipType>, org.eclipse.emf.common.util.Enumerator

public enum RelationshipType
extends java.lang.Enum<RelationshipType>
implements org.eclipse.emf.common.util.Enumerator

 A representation of the literals of the enumeration 'Relationship Type',
 and utility methods for working with them.

- =========== ENUM CONSTANT SUMMARY =========== =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

HTTP\_WWW\_W3\_ORG200508\_ADDRESSING\_REPLY\_LITERAL
The 'Http Www W3 Org200508 Addressing Reply' literal object.
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT 

static int
HTTP\_WWW\_W3\_ORG200508\_ADDRESSING\_REPLY
The 'Http Www W3 Org200508 Addressing Reply' literal value.

static java.util.List<RelationshipType>
VALUES
A public read-only list of all the 'Relationship Type' enumerators.
    - Method Summary Methods Modifier and Type Method and Description static RelationshipType get (int value) Returns the 'Relationship Type ' literal with the specified integer value. static RelationshipType get (java.lang.String literal) Returns the 'Relationship Type ' literal with the specified literal value. static RelationshipType getByName (java.lang.String name) Returns the 'Relationship Type ' literal with the specified name. java.lang.String getLiteral () java.lang.String getName () int getValue () java.lang.String toString () Returns the literal value of the enumerator, which is its string representation. static RelationshipType valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static RelationshipType [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type         | Method and Description                                                                                  |
|---------------------------|---------------------------------------------------------------------------------------------------------|
| static RelationshipType   | get(int value) Returns the 'Relationship Type' literal with the specified integer value.                |
| static RelationshipType   | get(java.lang.String literal) Returns the 'Relationship Type' literal with the specified literal value. |
| static RelationshipType   | getByName(java.lang.String name) Returns the 'Relationship Type' literal with the specified name.       |
| java.lang.String          | getLiteral()                                                                                            |
| java.lang.String          | getName()                                                                                               |
| int                       | getValue()                                                                                              |
| java.lang.String          | toString() Returns the literal value of the enumerator, which is its string representation.             |
| static RelationshipType   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.          |
| static RelationshipType[] | values() Returns an array containing the constants of this enum type, in the order they are declared.   |

    - Methods inherited from class java.lang.Enum
clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait