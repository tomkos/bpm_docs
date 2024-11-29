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

## Class ProcessMode

- java.lang.Object
    - org.eclipse.emf.common.util.AbstractEnumerator
        - com.ibm.wsspi.sca.metadata.bpc.model.ProcessMode

- All Implemented Interfaces:
org.eclipse.emf.common.util.Enumerator

public final class ProcessMode
extends org.eclipse.emf.common.util.AbstractEnumerator

 A representation of the literals of the enumeration 'Process Mode',
 and utility methods for working with them.
 
See Also:com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getProcessMode()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
LONG\_RUNNING
The 'Long Running' literal value

static ProcessMode
LONG\_RUNNING\_LITERAL
The 'Long Running' literal object

static int
MICROFLOW
The 'Microflow' literal value

static ProcessMode
MICROFLOW\_LITERAL
The 'Microflow' literal object

static java.util.List
VALUES
A public read-only list of all the 'Process Mode' enumerators
    - Method Summary Methods Modifier and Type Method and Description static ProcessMode get (int value) Returns the 'Process Mode ' literal with the specified integer value static ProcessMode get (java.lang.String literal) Returns the 'Process Mode ' literal with the specified literal value static ProcessMode getByName (java.lang.String name) Returns the 'Process Mode ' literal with the specified name

### Method Summary

| Modifier and Type   | Method and Description                                                                            |
|---------------------|---------------------------------------------------------------------------------------------------|
| static ProcessMode  | get(int value) Returns the 'Process Mode' literal with the specified integer value                |
| static ProcessMode  | get(java.lang.String literal) Returns the 'Process Mode' literal with the specified literal value |
| static ProcessMode  | getByName(java.lang.String name) Returns the 'Process Mode' literal with the specified name       |

    - Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
getLiteral, getName, getValue, toString
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait