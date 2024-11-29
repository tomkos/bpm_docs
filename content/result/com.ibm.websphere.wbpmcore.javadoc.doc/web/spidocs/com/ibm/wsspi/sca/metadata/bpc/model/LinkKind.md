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

## Class LinkKind

- java.lang.Object
    - org.eclipse.emf.common.util.AbstractEnumerator
        - com.ibm.wsspi.sca.metadata.bpc.model.LinkKind

- All Implemented Interfaces:
org.eclipse.emf.common.util.Enumerator

public final class LinkKind
extends org.eclipse.emf.common.util.AbstractEnumerator

 A representation of the literals of the enumeration 'Link Kind',
 and utility methods for working with them.
 
See Also:com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getLinkKind()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
FAULT\_CATCH
The 'Fault Catch' literal value

static int
FAULT\_CATCH\_ALL
The 'Fault Catch All' literal value

static LinkKind
FAULT\_CATCH\_ALL\_LITERAL
The 'Fault Catch All' literal object

static LinkKind
FAULT\_CATCH\_LITERAL
The 'Fault Catch' literal object

static int
STANDARD
The 'Standard' literal value

static LinkKind
STANDARD\_LITERAL
The 'Standard' literal object

static java.util.List
VALUES
A public read-only list of all the 'Link Kind' enumerators
    - Method Summary Methods Modifier and Type Method and Description static LinkKind get (int value) Returns the 'Link Kind ' literal with the specified integer value static LinkKind get (java.lang.String literal) Returns the 'Link Kind ' literal with the specified literal value static LinkKind getByName (java.lang.String name) Returns the 'Link Kind ' literal with the specified name

### Method Summary

| Modifier and Type   | Method and Description                                                                         |
|---------------------|------------------------------------------------------------------------------------------------|
| static LinkKind     | get(int value) Returns the 'Link Kind' literal with the specified integer value                |
| static LinkKind     | get(java.lang.String literal) Returns the 'Link Kind' literal with the specified literal value |
| static LinkKind     | getByName(java.lang.String name) Returns the 'Link Kind' literal with the specified name       |

    - Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
getLiteral, getName, getValue, toString
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait