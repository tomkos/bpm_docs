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

## Enum StageDurationType

- java.lang.Object
    - java.lang.Enum<StageDurationType>
        - com.ibm.casemgmt.api.constants.StageDurationType

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<StageDurationType>

public enum StageDurationType
extends java.lang.Enum<StageDurationType>
Represents the type of units in which a stage duration is specified.  Each value in the enum
 is associated with an integer value from the content engine choice list CmAcmExpectedDurationUnitTypeChoiceList.
 It is also associated with a string representation of that value.

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

DAYS
Indicates that the duration is specified in units of days.

HOURS
Indicates that the duraction is specified in units of hours.

NONE
Indicates that no duration has been specified.

WEEKS
Indicates that the duration is specified in units of weeks.
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description static StageDurationType fromIntValue (int intValue) Gets the enum value that corresponds to the specified integer value. static StageDurationType fromStringValue (java.lang.String strValue) Gets the enum value that corresponds to the specified string value. int intValue () Returns the integer value associated with this enum value. java.lang.String stringValue () Returns the string value associated with this enum value. static StageDurationType valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static StageDurationType [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type          | Method and Description                                                                                         |
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| static StageDurationType   | fromIntValue(int intValue) Gets the enum value that corresponds to the specified integer value.                |
| static StageDurationType   | fromStringValue(java.lang.String strValue) Gets the enum value that corresponds to the specified string value. |
| int                        | intValue() Returns the integer value associated with this enum value.                                          |
| java.lang.String           | stringValue() Returns the string value associated with this enum value.                                        |
| static StageDurationType   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.                 |
| static StageDurationType[] | values() Returns an array containing the constants of this enum type, in the order they are declared.          |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait