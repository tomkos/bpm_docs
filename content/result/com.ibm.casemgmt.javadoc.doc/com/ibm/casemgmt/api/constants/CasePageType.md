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

## Enum CasePageType

- java.lang.Object
    - java.lang.Enum<CasePageType>
        - com.ibm.casemgmt.api.constants.CasePageType

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<CasePageType>

public enum CasePageType
extends java.lang.Enum<CasePageType>
Represents the available case page types. When a solution is deployed,
 a particular mashup page can be assigned to various page types for each
 case type.  For the CASE\_PAGE type, the particular page
 can be different for each role. 
 
 Each value in the enumeration is associated with a string representation of
 that value.

ID status:
ID review by David Newhall

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

CASE\_CREATION\_PAGE
The type of page used to create a case.

CASE\_PAGE
The type of page that displays details about a case.

CASE\_SPLIT\_PAGE
The type of page used to split a case, creating a new case.

DYNAMIC\_TASK\_STEP\_PAGE
The type of page that display details for dynamic task step.
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description static CasePageType fromStringValue (java.lang.String strValue) Gets the enum value that corresponds to the specified string value. java.lang.String stringValue () Returns the string value associated with this enum value. static CasePageType valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static CasePageType [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type     | Method and Description                                                                                         |
|-----------------------|----------------------------------------------------------------------------------------------------------------|
| static CasePageType   | fromStringValue(java.lang.String strValue) Gets the enum value that corresponds to the specified string value. |
| java.lang.String      | stringValue() Returns the string value associated with this enum value.                                        |
| static CasePageType   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.                 |
| static CasePageType[] | values() Returns an array containing the constants of this enum type, in the order they are declared.          |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait