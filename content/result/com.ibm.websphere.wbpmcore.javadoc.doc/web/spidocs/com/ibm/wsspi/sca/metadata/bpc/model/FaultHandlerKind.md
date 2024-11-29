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

## Class FaultHandlerKind

- java.lang.Object
    - org.eclipse.emf.common.util.AbstractEnumerator
        - com.ibm.wsspi.sca.metadata.bpc.model.FaultHandlerKind

- All Implemented Interfaces:
org.eclipse.emf.common.util.Enumerator

public final class FaultHandlerKind
extends org.eclipse.emf.common.util.AbstractEnumerator

 A representation of the literals of the enumeration 'Fault Handler Kind',
 and utility methods for working with them.
 
See Also:com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getFaultHandlerKind()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
CATCH
The 'Catch' literal value

static int
CATCH\_ALL
The 'Catch All' literal value

static FaultHandlerKind
CATCH\_ALL\_LITERAL
The 'Catch All' literal object

static FaultHandlerKind
CATCH\_LITERAL
The 'Catch' literal object

static java.lang.String
COPYRIGHT 

static java.util.List
VALUES
A public read-only list of all the 'Fault Handler Kind' enumerators
    - Method Summary Methods Modifier and Type Method and Description static FaultHandlerKind get (int value) Returns the 'Fault Handler Kind ' literal with the specified integer value static FaultHandlerKind get (java.lang.String literal) Returns the 'Fault Handler Kind ' literal with the specified literal value static FaultHandlerKind getByName (java.lang.String name) Returns the 'Fault Handler Kind ' literal with the specified name

### Method Summary

| Modifier and Type       | Method and Description                                                                                  |
|-------------------------|---------------------------------------------------------------------------------------------------------|
| static FaultHandlerKind | get(int value) Returns the 'Fault Handler Kind' literal with the specified integer value                |
| static FaultHandlerKind | get(java.lang.String literal) Returns the 'Fault Handler Kind' literal with the specified literal value |
| static FaultHandlerKind | getByName(java.lang.String name) Returns the 'Fault Handler Kind' literal with the specified name       |

    - Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
getLiteral, getName, getValue, toString
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait