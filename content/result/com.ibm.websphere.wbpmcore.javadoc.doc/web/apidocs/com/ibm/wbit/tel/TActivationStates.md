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

## Class TActivationStates

- java.lang.Object
    - org.eclipse.emf.common.util.AbstractEnumerator
        - com.ibm.wbit.tel.TActivationStates

- All Implemented Interfaces:
org.eclipse.emf.common.util.Enumerator

public final class TActivationStates
extends org.eclipse.emf.common.util.AbstractEnumerator

 A representation of the literals of the enumeration 'TActivation States',
 and utility methods for working with them.
 

Since:
6.0.1
See Also:TaskPackage.getTActivationStates()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
CLAIMED
The 'Claimed' literal value

static TActivationStates
CLAIMED\_LITERAL
The 'Claimed' literal object

static java.lang.String
COPYRIGHT 

static int
READY
The 'Ready' literal value

static TActivationStates
READY\_LITERAL
The 'Ready' literal object

static int
RUNNING
The 'Running' literal value

static TActivationStates
RUNNING\_LITERAL
The 'Running' literal object

static java.util.List
VALUES
A public read-only list of all the 'TActivation States' enumerators

static int
WAITING\_FOR\_SUB\_TASK
The 'Waiting For Sub Task' literal value

static TActivationStates
WAITING\_FOR\_SUB\_TASK\_LITERAL
The 'Waiting For Sub Task' literal object
    - Method Summary Methods Modifier and Type Method and Description static TActivationStates get (int value) Returns the 'TActivation States ' literal with the specified integer value static TActivationStates get (java.lang.String literal) Returns the 'TActivation States ' literal with the specified literal value static TActivationStates getByName (java.lang.String name) Returns the 'TActivation States ' literal with the specified name

### Method Summary

| Modifier and Type        | Method and Description                                                                                  |
|--------------------------|---------------------------------------------------------------------------------------------------------|
| static TActivationStates | get(int value) Returns the 'TActivation States' literal with the specified integer value                |
| static TActivationStates | get(java.lang.String literal) Returns the 'TActivation States' literal with the specified literal value |
| static TActivationStates | getByName(java.lang.String name) Returns the 'TActivation States' literal with the specified name       |

    - Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
getLiteral, getName, getValue, toString
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait