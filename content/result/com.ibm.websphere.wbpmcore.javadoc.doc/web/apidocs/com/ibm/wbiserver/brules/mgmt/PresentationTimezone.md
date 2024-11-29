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
- Enum Constants |
- Field |
- Method

- Detail:
- Enum Constants |
- Field |
- Method

## Enum PresentationTimezone

- java.lang.Object
    - java.lang.Enum<PresentationTimezone>
        - com.ibm.wbiserver.brules.mgmt.PresentationTimezone

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<PresentationTimezone>

public enum PresentationTimezone
extends java.lang.Enum<PresentationTimezone>
Contains the possible values for the presentation time zone field of a business rule group.

- =========== ENUM CONSTANT SUMMARY =========== =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

LOCAL
Indicates that dates and times should be presented to the user in the local time zone.

UTC
Indicates that dates and times should be presented to the user in the UTC time zone.
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description static PresentationTimezone valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static PresentationTimezone [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type             | Method and Description                                                                                |
|-------------------------------|-------------------------------------------------------------------------------------------------------|
| static PresentationTimezone   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.        |
| static PresentationTimezone[] | values() Returns an array containing the constants of this enum type, in the order they are declared. |

    - Methods inherited from class java.lang.Enum
clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait