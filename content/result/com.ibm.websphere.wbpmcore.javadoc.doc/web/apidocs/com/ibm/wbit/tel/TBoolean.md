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

## Class TBoolean

- java.lang.Object
    - org.eclipse.emf.common.util.AbstractEnumerator
        - com.ibm.wbit.tel.TBoolean

- All Implemented Interfaces:
org.eclipse.emf.common.util.Enumerator

public final class TBoolean
extends org.eclipse.emf.common.util.AbstractEnumerator

 A representation of the literals of the enumeration 'TBoolean',
 and utility methods for working with them.
 

Since:
6.0.1
See Also:TaskPackage.getTBoolean()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
NO
The 'No' literal value

static TBoolean
NO\_LITERAL
The 'No' literal object

static java.util.List
VALUES
A public read-only list of all the 'TBoolean' enumerators

static int
YES
The 'Yes' literal value

static TBoolean
YES\_LITERAL
The 'Yes' literal object
    - Method Summary Methods Modifier and Type Method and Description static TBoolean get (int value) Returns the 'TBoolean ' literal with the specified integer value static TBoolean get (java.lang.String literal) Returns the 'TBoolean ' literal with the specified literal value static TBoolean getByName (java.lang.String name) Returns the 'TBoolean ' literal with the specified name

### Method Summary

| Modifier and Type   | Method and Description                                                                        |
|---------------------|-----------------------------------------------------------------------------------------------|
| static TBoolean     | get(int value) Returns the 'TBoolean' literal with the specified integer value                |
| static TBoolean     | get(java.lang.String literal) Returns the 'TBoolean' literal with the specified literal value |
| static TBoolean     | getByName(java.lang.String name) Returns the 'TBoolean' literal with the specified name       |

    - Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
getLiteral, getName, getValue, toString
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait