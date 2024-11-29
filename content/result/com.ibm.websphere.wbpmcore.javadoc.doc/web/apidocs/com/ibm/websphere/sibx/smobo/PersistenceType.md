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

## Enum PersistenceType

- java.lang.Object
    - java.lang.Enum<PersistenceType>
        - com.ibm.websphere.sibx.smobo.PersistenceType

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<PersistenceType>, org.eclipse.emf.common.util.Enumerator

public enum PersistenceType
extends java.lang.Enum<PersistenceType>
implements org.eclipse.emf.common.util.Enumerator
A representation of the literals of the enumeration 'Persistence Type',
 and utility methods for working with them.
 
 Note that these literals are only of use to the custom mediation writer and cannot
 be used in filter primitive expressions.

- =========== ENUM CONSTANT SUMMARY =========== =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

NON\_PERSISTENT\_LITERAL
The 'Non Persistent' literal object

PERSISTENT\_LITERAL
The 'Persistent' literal object
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT 

static int
NON\_PERSISTENT
The 'Non Persistent' literal value

static int
PERSISTENT
The 'Persistent' literal value

static java.util.List<PersistenceType>
VALUES
A public read-only list of all the 'Persistence Type' enumerators.
    - Method Summary Methods Modifier and Type Method and Description static PersistenceType get (int value) Returns the 'Persistence Type ' literal with the specified value. static PersistenceType get (java.lang.String literal) Returns the 'Persistence Type ' literal with the specified name. static PersistenceType getByName (java.lang.String name) Returns the 'Persistence Type ' literal with the specified name java.lang.String getLiteral () java.lang.String getName () int getValue () java.lang.String toString () Returns the literal value of the enumerator, which is its string representation static PersistenceType valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static PersistenceType [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type        | Method and Description                                                                                |
|--------------------------|-------------------------------------------------------------------------------------------------------|
| static PersistenceType   | get(int value) Returns the 'Persistence Type' literal with the specified value.                       |
| static PersistenceType   | get(java.lang.String literal) Returns the 'Persistence Type' literal with the specified name.         |
| static PersistenceType   | getByName(java.lang.String name) Returns the 'Persistence Type' literal with the specified name       |
| java.lang.String         | getLiteral()                                                                                          |
| java.lang.String         | getName()                                                                                             |
| int                      | getValue()                                                                                            |
| java.lang.String         | toString() Returns the literal value of the enumerator, which is its string representation            |
| static PersistenceType   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.        |
| static PersistenceType[] | values() Returns an array containing the constants of this enum type, in the order they are declared. |

    - Methods inherited from class java.lang.Enum
clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait