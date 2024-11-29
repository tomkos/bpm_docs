- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Enum Constants |
- Field |
- Method

- Detail:
- Enum Constants |
- Field |
- Method

## Enum CaseState

- java.lang.Object
    - java.lang.Enum<CaseState>
        - com.ibm.casemgmt.api.constants.CaseState

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<CaseState>

public enum CaseState
extends java.lang.Enum<CaseState>
Represents the possible states of a case. The case state indicates whether
 the case is newly created, currently being initialized, actively being worked on,
 etc.
 
 Each value in the enum is associated with an integer value from the content 
 engine choice list CmAcmCaseStateChoiceList.  It is also associated
 with a string representation of that value.

ID status:
ID review by David Newhall

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

COMPLETE
The state of a case that is complete.

FAILED
The state of a case that has failed.

INITIALIZING
The state of a case that is being initialized.

NEW
The state of a case that is newly created.

WORKING
The state of a case that is actively being worked on.
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description static CaseState fromIntValue (int intValue) Gets the enum value that corresponds to the specified integer value. static CaseState fromStringValue (java.lang.String strValue) Gets the enum value that corresponds to the specified string value. int intValue () Returns the integer value associated with this enum value. java.lang.String stringValue () Returns the string value associated with this enum value. static CaseState valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static CaseState [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type   | Method and Description                                                                                         |
|---------------------|----------------------------------------------------------------------------------------------------------------|
| static CaseState    | fromIntValue(int intValue) Gets the enum value that corresponds to the specified integer value.                |
| static CaseState    | fromStringValue(java.lang.String strValue) Gets the enum value that corresponds to the specified string value. |
| int                 | intValue() Returns the integer value associated with this enum value.                                          |
| java.lang.String    | stringValue() Returns the string value associated with this enum value.                                        |
| static CaseState    | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.                 |
| static CaseState[]  | values() Returns an array containing the constants of this enum type, in the order they are declared.          |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait