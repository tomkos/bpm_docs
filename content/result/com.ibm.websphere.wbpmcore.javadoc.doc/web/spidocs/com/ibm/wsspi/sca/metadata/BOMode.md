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

## Enum BOMode

- java.lang.Object
    - java.lang.Enum<BOMode>
        - com.ibm.wsspi.sca.metadata.BOMode

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<BOMode>

public enum BOMode
extends java.lang.Enum<BOMode>
Enum class for the different BO modes available. There are to possible values:
 BO\_LAZY and BO\_EAGER.
Since:
7.5.1
See Also:BO\_EAGER, 
BO\_LAZY

- =========== ENUM CONSTANT SUMMARY =========== =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

BO\_EAGER 

BO\_LAZY
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description static BOMode valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static BOMode [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type   | Method and Description                                                                                |
|---------------------|-------------------------------------------------------------------------------------------------------|
| static BOMode       | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.        |
| static BOMode[]     | values() Returns an array containing the constants of this enum type, in the order they are declared. |

    - Methods inherited from class java.lang.Enum
clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait