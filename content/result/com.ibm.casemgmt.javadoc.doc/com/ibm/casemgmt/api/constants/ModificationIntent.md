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

## Enum ModificationIntent

- java.lang.Object
    - java.lang.Enum<ModificationIntent>
        - com.ibm.casemgmt.api.constants.ModificationIntent

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<ModificationIntent>

public enum ModificationIntent
extends java.lang.Enum<ModificationIntent>
Represents the modification intent when fetching an object such as a case.
 If the intent is not to modify the object, some operations can be optimized
 or deferred until necessary. In particular, the communication with an
 external data service, if configured, can be deferred until necessary.

ID status:
ID review by David Newhall

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

MODIFY
Indicates an intent to modify the object.

NOT\_MODIFY
Indicates an intent not to modify the object.
    - Method Summary All Methods Static Methods Concrete Methods Modifier and Type Method and Description static ModificationIntent valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static ModificationIntent [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type           | Method and Description                                                                                |
|-----------------------------|-------------------------------------------------------------------------------------------------------|
| static ModificationIntent   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.        |
| static ModificationIntent[] | values() Returns an array containing the constants of this enum type, in the order they are declared. |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait