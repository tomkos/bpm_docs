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

## Class TDurationConstants

- java.lang.Object
    - org.eclipse.emf.common.util.AbstractEnumerator
        - com.ibm.wbit.tel.TDurationConstants

- All Implemented Interfaces:
org.eclipse.emf.common.util.Enumerator

public final class TDurationConstants
extends org.eclipse.emf.common.util.AbstractEnumerator

 A representation of the literals of the enumeration 'TDuration Constants',
 and utility methods for working with them.
 

Since:
6.0.1
See Also:TaskPackage.getTDurationConstants()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
copyright 

static int
DURATIONINFINITE
The 'DURATIONINFINITE' literal value

static TDurationConstants
DURATIONINFINITE\_LITERAL
The 'DURATIONINFINITE' literal object

static int
DURATIONZERO
The 'DURATIONZERO' literal value

static TDurationConstants
DURATIONZERO\_LITERAL
The 'DURATIONZERO' literal object

static java.util.List
VALUES
A public read-only list of all the 'TDuration Constants' enumerators
    - Method Summary Methods Modifier and Type Method and Description static TDurationConstants get (int value) Returns the 'TDuration Constants ' literal with the specified integer value static TDurationConstants get (java.lang.String literal) Returns the 'TDuration Constants ' literal with the specified literal value static TDurationConstants getByName (java.lang.String name) Returns the 'TDuration Constants ' literal with the specified name

### Method Summary

| Modifier and Type         | Method and Description                                                                                   |
|---------------------------|----------------------------------------------------------------------------------------------------------|
| static TDurationConstants | get(int value) Returns the 'TDuration Constants' literal with the specified integer value                |
| static TDurationConstants | get(java.lang.String literal) Returns the 'TDuration Constants' literal with the specified literal value |
| static TDurationConstants | getByName(java.lang.String name) Returns the 'TDuration Constants' literal with the specified name       |

    - Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
getLiteral, getName, getValue, toString
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait