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

## Class ActivityKind

- java.lang.Object
    - org.eclipse.emf.common.util.AbstractEnumerator
        - com.ibm.wsspi.sca.metadata.bpc.model.ActivityKind

- All Implemented Interfaces:
org.eclipse.emf.common.util.Enumerator

public final class ActivityKind
extends org.eclipse.emf.common.util.AbstractEnumerator

 A representation of the literals of the enumeration 'Activity Kind',
 and utility methods for working with them.
 
See Also:com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getActivityKind()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
ASSIGN
The 'ASSIGN' literal value

static ActivityKind
ASSIGN\_LITERAL
The 'ASSIGN' literal object

static int
COMPENSATE
The 'COMPENSATE' literal value

static ActivityKind
COMPENSATE\_LITERAL
The 'COMPENSATE' literal object

static int
COMPENSATESCOPE
The 'COMPENSATESCOPE' literal value

static ActivityKind
COMPENSATESCOPE\_LITERAL
The 'COMPENSATESCOPE' literal object

static java.lang.String
COPYRIGHT 

static int
CUSTOM
The 'CUSTOM' literal value

static ActivityKind
CUSTOM\_LITERAL
The 'CUSTOM' literal object

static int
EMPTY
The 'EMPTY' literal value

static ActivityKind
EMPTY\_LITERAL
The 'EMPTY' literal object

static int
FLOW
The 'FLOW' literal value

static ActivityKind
FLOW\_LITERAL
The 'FLOW' literal object

static int
FOREACHPARALLEL
The 'FOREACHPARALLEL' literal value

static ActivityKind
FOREACHPARALLEL\_LITERAL
The 'FOREACHPARALLEL' literal object

static int
FOREACHSERIAL
The 'FOREACHSERIAL' literal value

static ActivityKind
FOREACHSERIAL\_LITERAL
The 'FOREACHSERIAL' literal object

static int
INVOKE
The 'INVOKE' literal value

static ActivityKind
INVOKE\_LITERAL
The 'INVOKE' literal object

static int
IORINGATEWAY
The 'IORINGATEWAY' literal value

static ActivityKind
IORINGATEWAY\_LITERAL
The 'IORINGATEWAY' literal object

static int
PICK
The 'PICK' literal value

static ActivityKind
PICK\_LITERAL
The 'PICK' literal object

static int
RECEIVE
The 'RECEIVE' literal value

static ActivityKind
RECEIVE\_LITERAL
The 'RECEIVE' literal object

static int
REPEATUNTIL
The 'REPEATUNTIL' literal value

static ActivityKind
REPEATUNTIL\_LITERAL
The 'REPEATUNTIL' literal object

static int
REPLY
The 'REPLY' literal value

static ActivityKind
REPLY\_LITERAL
The 'REPLY' literal object

static int
RETHROW
The 'RETHROW' literal value

static ActivityKind
RETHROW\_LITERAL
The 'RETHROW' literal object

static int
SCOPE
The 'SCOPE' literal value

static ActivityKind
SCOPE\_LITERAL
The 'SCOPE' literal object

static int
SCRIPT
The 'SCRIPT' literal value

static ActivityKind
SCRIPT\_LITERAL
The 'SCRIPT' literal object

static int
SEQUENCE
The 'SEQUENCE' literal value

static ActivityKind
SEQUENCE\_LITERAL
The 'SEQUENCE' literal object

static int
STAFF
The 'STAFF' literal value

static ActivityKind
STAFF\_LITERAL
The 'STAFF' literal object

static int
SWITCH
The 'SWITCH' literal value

static ActivityKind
SWITCH\_LITERAL
The 'SWITCH' literal object

static int
TERMINATE
The 'TERMINATE' literal value

static ActivityKind
TERMINATE\_LITERAL
The 'TERMINATE' literal object

static int
THROW
The 'THROW' literal value

static ActivityKind
THROW\_LITERAL
The 'THROW' literal object

static int
UNKNOWN
The 'UNKNOWN' literal value

static ActivityKind
UNKNOWN\_LITERAL
The 'UNKNOWN' literal object

static java.util.List
VALUES
A public read-only list of all the 'Activity Kind' enumerators

static int
WAIT
The 'WAIT' literal value

static ActivityKind
WAIT\_LITERAL
The 'WAIT' literal object

static int
WHILE
The 'WHILE' literal value

static ActivityKind
WHILE\_LITERAL
The 'WHILE' literal object
    - Method Summary Methods Modifier and Type Method and Description static ActivityKind get (int value) Returns the 'Activity Kind ' literal with the specified integer value static ActivityKind get (java.lang.String literal) Returns the 'Activity Kind ' literal with the specified literal value static ActivityKind getByName (java.lang.String name) Returns the 'Activity Kind ' literal with the specified name

### Method Summary

| Modifier and Type   | Method and Description                                                                             |
|---------------------|----------------------------------------------------------------------------------------------------|
| static ActivityKind | get(int value) Returns the 'Activity Kind' literal with the specified integer value                |
| static ActivityKind | get(java.lang.String literal) Returns the 'Activity Kind' literal with the specified literal value |
| static ActivityKind | getByName(java.lang.String name) Returns the 'Activity Kind' literal with the specified name       |

    - Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
getLiteral, getName, getValue, toString
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait