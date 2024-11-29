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

## Class EventHandlerKind

- java.lang.Object
    - org.eclipse.emf.common.util.AbstractEnumerator
        - com.ibm.wsspi.sca.metadata.bpc.model.EventHandlerKind

- All Implemented Interfaces:
org.eclipse.emf.common.util.Enumerator

public final class EventHandlerKind
extends org.eclipse.emf.common.util.AbstractEnumerator

 A representation of the literals of the enumeration 'Event Handler Kind',
 and utility methods for working with them.
 
See Also:com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getEventHandlerKind()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
ON\_ALARM
The 'On Alarm' literal value

static EventHandlerKind
ON\_ALARM\_LITERAL
The 'On Alarm' literal object

static int
ON\_EVENT
The 'On Event' literal value

static EventHandlerKind
ON\_EVENT\_LITERAL
The 'On Event' literal object

static java.util.List
VALUES
A public read-only list of all the 'Event Handler Kind' enumerators
    - Method Summary Methods Modifier and Type Method and Description static EventHandlerKind get (int value) Returns the 'Event Handler Kind ' literal with the specified integer value static EventHandlerKind get (java.lang.String literal) Returns the 'Event Handler Kind ' literal with the specified literal value static EventHandlerKind getByName (java.lang.String name) Returns the 'Event Handler Kind ' literal with the specified name

### Method Summary

| Modifier and Type       | Method and Description                                                                                  |
|-------------------------|---------------------------------------------------------------------------------------------------------|
| static EventHandlerKind | get(int value) Returns the 'Event Handler Kind' literal with the specified integer value                |
| static EventHandlerKind | get(java.lang.String literal) Returns the 'Event Handler Kind' literal with the specified literal value |
| static EventHandlerKind | getByName(java.lang.String name) Returns the 'Event Handler Kind' literal with the specified name       |

    - Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
getLiteral, getName, getValue, toString
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait