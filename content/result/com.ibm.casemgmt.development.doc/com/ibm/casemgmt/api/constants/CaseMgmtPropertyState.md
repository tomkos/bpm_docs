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

## Enum CaseMgmtPropertyState

- java.lang.Object
    - java.lang.Enum<CaseMgmtPropertyState>
        - com.ibm.casemgmt.api.constants.CaseMgmtPropertyState

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<CaseMgmtPropertyState>

public enum CaseMgmtPropertyState
extends java.lang.Enum<CaseMgmtPropertyState>
Indicates the type of value held by a CaseMgmtProperty object.
 A CaseMgmtProperty object can hold a value that represents either
 the actual current value for the persisted Content Engine
 object or a working value before the Content Engine object
 is persisted.
 
 The state of this value indicates whether the property holds an
 actual value or whether the value is null. For an object-valued property,
 the state can indicate that the property holds a reference to the
 object rather than the object itself.
 
 A CaseMgmtProperty object can hold an Original Value. 
 The original value can be interesting information if, for example,
 external data integration is involved. The value returned after
 fetching an object could be different than the actual value persisted
 with that object if an External Data Service modified the value before
 returning it to the client. The original value always indicates the
 actual persisted value in that case. The original value is optional,
 depending on the context. The state of the original value may indicate
 that it is unspecified if not applicable to the context.

ID status:
ID review by David Newhall

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

NO\_VALUE
Indicates that the value held by the CaseMgmtProperty object
 is either null (if it has single cardinality) or refers to
 an empty collection (if it has list cardinality).

REFERENCE
Indicates that the value held by the CaseMgmtProperty object
 is a reference to a Content Engine object.

UNSPECIFIED
Indicates that the value held by the CaseMgmtProperty object
 is unspecified.

VALUE
Indicates that the CaseMgmtProperty object holds a value.
    - Method Summary All Methods Static Methods Concrete Methods Modifier and Type Method and Description static CaseMgmtPropertyState valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static CaseMgmtPropertyState [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type              | Method and Description                                                                                |
|--------------------------------|-------------------------------------------------------------------------------------------------------|
| static CaseMgmtPropertyState   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.        |
| static CaseMgmtPropertyState[] | values() Returns an array containing the constants of this enum type, in the order they are declared. |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait