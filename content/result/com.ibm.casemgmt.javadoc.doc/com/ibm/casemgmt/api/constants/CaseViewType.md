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

## Enum CaseViewType

- java.lang.Object
    - java.lang.Enum<CaseViewType>
        - com.ibm.casemgmt.api.constants.CaseViewType

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<CaseViewType>

public enum CaseViewType
extends java.lang.Enum<CaseViewType>
Represents a type of page view that is assigned to a case type. Page views
 are defined by the solution to control how the case properties
 are displayed in different types of views, such as in 
 a summary view or case data view.
 
 Each value in the enum is associated with a string representation of that value.

ID status:
ID review by David Newhall

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

CASE\_DATA
The type of view used to display general details about a case.

CASE\_PROPERTIES
This new view is used to maintain the order of case properties of a particular case type.

CASE\_SEARCH
The type of view used to search for cases of a particular case type.

CASE\_SUMMARY
The type of view that displays summary information about a case.
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description static CaseViewType fromStringValue (java.lang.String strValue) Gets the enum value that corresponds to the specified string value. java.lang.String stringValue () Returns the string value associated with this enum value. static CaseViewType valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static CaseViewType [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type     | Method and Description                                                                                         |
|-----------------------|----------------------------------------------------------------------------------------------------------------|
| static CaseViewType   | fromStringValue(java.lang.String strValue) Gets the enum value that corresponds to the specified string value. |
| java.lang.String      | stringValue() Returns the string value associated with this enum value.                                        |
| static CaseViewType   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.                 |
| static CaseViewType[] | values() Returns an array containing the constants of this enum type, in the order they are declared.          |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait