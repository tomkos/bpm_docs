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
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Class Role

- java.lang.Object
    - org.eclipse.emf.common.util.AbstractEnumerator
        - com.ibm.wsspi.sca.metadata.bpc.model.Role

- All Implemented Interfaces:
org.eclipse.emf.common.util.Enumerator

public final class Role
extends org.eclipse.emf.common.util.AbstractEnumerator

 A representation of the literals of the enumeration 'Role',
 and utility methods for working with them.
 
See Also:com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getRole()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
ADMINISTRATOR
The 'Administrator' literal value

static Role
ADMINISTRATOR\_LITERAL
The 'Administrator' literal object

static java.lang.String
COPYRIGHT 

static int
EDITOR
The 'Editor' literal value

static Role
EDITOR\_LITERAL
The 'Editor' literal object

static int
POTENTIAL\_INSTANCE\_CREATOR
The 'Potential Instance Creator' literal value

static Role
POTENTIAL\_INSTANCE\_CREATOR\_LITERAL
The 'Potential Instance Creator' literal object

static int
POTENTIAL\_OWNER
The 'Potential Owner' literal value

static Role
POTENTIAL\_OWNER\_LITERAL
The 'Potential Owner' literal object

static int
POTENTIAL\_STARTER
The 'Potential Starter' literal value

static Role
POTENTIAL\_STARTER\_LITERAL
The 'Potential Starter' literal object

static int
READER
The 'Reader' literal value

static Role
READER\_LITERAL
The 'Reader' literal object

static java.util.List
VALUES
A public read-only list of all the 'Role' enumerators
    - Method Summary Methods Modifier and Type Method and Description static Role get (int value) Returns the 'Role ' literal with the specified integer value static Role get (java.lang.String literal) Returns the 'Role ' literal with the specified literal value static Role getByName (java.lang.String name) Returns the 'Role ' literal with the specified name

### Method Summary

| Modifier and Type   | Method and Description                                                                    |
|---------------------|-------------------------------------------------------------------------------------------|
| static Role         | get(int value) Returns the 'Role' literal with the specified integer value                |
| static Role         | get(java.lang.String literal) Returns the 'Role' literal with the specified literal value |
| static Role         | getByName(java.lang.String name) Returns the 'Role' literal with the specified name       |

    - Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
getLiteral, getName, getValue, toString
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait