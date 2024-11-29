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

## Enum DisplayMode

- java.lang.Object
    - java.lang.Enum<DisplayMode>
        - com.ibm.casemgmt.api.constants.DisplayMode

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<DisplayMode>

public enum DisplayMode
extends java.lang.Enum<DisplayMode>
Represents the display mode of a property. If external data integration is configured, 
 an external data service may predetermine a value for that property and in addition
 specify that the property should not be editable in a UI. The settability of the property
 takes precedence regardless of whether the display mode indicates that the property value
 can be edited or not.

ID status:
ID review by David Newhall

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

READ\_ONLY
Indicates that a field to edit a property value should be rendered read only, regardless
 of the settability of the property.

READ\_WRITE
Indicates that a field to edit a property value can be edited normally but is still
 subject to the settability of the property, which takes precedence.
    - Method Summary All Methods Static Methods Concrete Methods Modifier and Type Method and Description static DisplayMode valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static DisplayMode [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type    | Method and Description                                                                                |
|----------------------|-------------------------------------------------------------------------------------------------------|
| static DisplayMode   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.        |
| static DisplayMode[] | values() Returns an array containing the constants of this enum type, in the order they are declared. |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait