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

## Class HumanTaskKind

- java.lang.Object
    - org.eclipse.emf.common.util.AbstractEnumerator
        - com.ibm.wsspi.sca.metadata.bpc.model.HumanTaskKind

- All Implemented Interfaces:
org.eclipse.emf.common.util.Enumerator

public final class HumanTaskKind
extends org.eclipse.emf.common.util.AbstractEnumerator

 A representation of the literals of the enumeration 'Human Task Kind',
 and utility methods for working with them.
 
See Also:com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getHumanTaskKind()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
ADMINISTRATION
The 'Administration' literal value

static HumanTaskKind
ADMINISTRATION\_LITERAL
The 'Administration' literal object

static int
COLLABORATION
The 'Collaboration' literal value

static HumanTaskKind
COLLABORATION\_LITERAL
The 'Collaboration' literal object

static java.lang.String
COPYRIGHT 

static int
INVOCATION
The 'Invocation' literal value

static HumanTaskKind
INVOCATION\_LITERAL
The 'Invocation' literal object

static int
TO\_DO
The 'To Do' literal value

static HumanTaskKind
TO\_DO\_LITERAL
The 'To Do' literal object

static java.util.List
VALUES
A public read-only list of all the 'Human Task Kind' enumerators
    - Method Summary Methods Modifier and Type Method and Description static HumanTaskKind get (int value) Returns the 'Human Task Kind ' literal with the specified integer value static HumanTaskKind get (java.lang.String literal) Returns the 'Human Task Kind ' literal with the specified literal value static HumanTaskKind getByName (java.lang.String name) Returns the 'Human Task Kind ' literal with the specified name

### Method Summary

| Modifier and Type    | Method and Description                                                                               |
|----------------------|------------------------------------------------------------------------------------------------------|
| static HumanTaskKind | get(int value) Returns the 'Human Task Kind' literal with the specified integer value                |
| static HumanTaskKind | get(java.lang.String literal) Returns the 'Human Task Kind' literal with the specified literal value |
| static HumanTaskKind | getByName(java.lang.String name) Returns the 'Human Task Kind' literal with the specified name       |

    - Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
getLiteral, getName, getValue, toString
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait