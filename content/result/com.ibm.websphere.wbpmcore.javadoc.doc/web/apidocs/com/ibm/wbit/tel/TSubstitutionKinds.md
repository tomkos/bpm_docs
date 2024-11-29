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

## Class TSubstitutionKinds

- java.lang.Object
    - org.eclipse.emf.common.util.AbstractEnumerator
        - com.ibm.wbit.tel.TSubstitutionKinds

- All Implemented Interfaces:
org.eclipse.emf.common.util.Enumerator

public final class TSubstitutionKinds
extends org.eclipse.emf.common.util.AbstractEnumerator

 A representation of the literals of the enumeration 'TSubstitution Kinds',
 and utility methods for working with them.
 

Since:
6.1
See Also:TaskPackage.getTSubstitutionKinds()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
NO\_SUBSTITUTION
The 'No Substitution' literal value

static TSubstitutionKinds
NO\_SUBSTITUTION\_LITERAL
The 'No Substitution' literal object

static int
SELECT\_USER\_IF\_PRESENT
The 'Select User If Present' literal value

static TSubstitutionKinds
SELECT\_USER\_IF\_PRESENT\_LITERAL
The 'Select User If Present' literal object

static int
SUBSTITUTE\_USER\_IF\_ABSENT
The 'Substitute User If Absent' literal value

static TSubstitutionKinds
SUBSTITUTE\_USER\_IF\_ABSENT\_LITERAL
The 'Substitute User If Absent' literal object

static java.util.List
VALUES
A public read-only list of all the 'TSubstitution Kinds' enumerators
    - Method Summary Methods Modifier and Type Method and Description static TSubstitutionKinds get (int value) Returns the 'TSubstitution Kinds ' literal with the specified integer value static TSubstitutionKinds get (java.lang.String literal) Returns the 'TSubstitution Kinds ' literal with the specified literal value static TSubstitutionKinds getByName (java.lang.String name) Returns the 'TSubstitution Kinds ' literal with the specified name

### Method Summary

| Modifier and Type         | Method and Description                                                                                   |
|---------------------------|----------------------------------------------------------------------------------------------------------|
| static TSubstitutionKinds | get(int value) Returns the 'TSubstitution Kinds' literal with the specified integer value                |
| static TSubstitutionKinds | get(java.lang.String literal) Returns the 'TSubstitution Kinds' literal with the specified literal value |
| static TSubstitutionKinds | getByName(java.lang.String name) Returns the 'TSubstitution Kinds' literal with the specified name       |

    - Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
getLiteral, getName, getValue, toString
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait