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

## Class GatewayKind

- java.lang.Object
    - org.eclipse.emf.common.util.AbstractEnumerator
        - com.ibm.wsspi.sca.metadata.bpc.model.GatewayKind

- All Implemented Interfaces:
org.eclipse.emf.common.util.Enumerator

public final class GatewayKind
extends org.eclipse.emf.common.util.AbstractEnumerator

 A representation of the literals of the enumeration 'Gateway Kind',
 and utility methods for working with them.
 
See Also:com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getGatewayKind()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
AND
The 'AND' literal value

static GatewayKind
AND\_LITERAL
The 'AND' literal object

static java.lang.String
COPYRIGHT 

static int
IOR
The 'IOR' literal value

static GatewayKind
IOR\_LITERAL
The 'IOR' literal object

static int
NONE
The 'NONE' literal value

static GatewayKind
NONE\_LITERAL
The 'NONE' literal object

static java.util.List
VALUES
A public read-only list of all the 'Gateway Kind' enumerators

static int
XOR
The 'XOR' literal value

static GatewayKind
XOR\_LITERAL
The 'XOR' literal object
    - Method Summary Methods Modifier and Type Method and Description static GatewayKind get (int value) Returns the 'Gateway Kind ' literal with the specified integer value static GatewayKind get (java.lang.String literal) Returns the 'Gateway Kind ' literal with the specified literal value static GatewayKind getByName (java.lang.String name) Returns the 'Gateway Kind ' literal with the specified name

### Method Summary

| Modifier and Type   | Method and Description                                                                            |
|---------------------|---------------------------------------------------------------------------------------------------|
| static GatewayKind  | get(int value) Returns the 'Gateway Kind' literal with the specified integer value                |
| static GatewayKind  | get(java.lang.String literal) Returns the 'Gateway Kind' literal with the specified literal value |
| static GatewayKind  | getByName(java.lang.String name) Returns the 'Gateway Kind' literal with the specified name       |

    - Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
getLiteral, getName, getValue, toString
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait