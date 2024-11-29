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

## Enum QueryOperator

- java.lang.Object
    - java.lang.Enum<QueryOperator>
        - com.ibm.wbiserver.brules.mgmt.query.QueryOperator

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<QueryOperator>

public enum QueryOperator
extends java.lang.Enum<QueryOperator>
An enum used to identify the query operator to be used for a particular query.

- =========== ENUM CONSTANT SUMMARY =========== =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

EQUAL
Indicates that the value of a property must match the specified string exactly.

LIKE
Indicates that the query should look for business rule groups where a property value
 is like the specified string.

NOT\_EQUAL
Indicates that the value of a property must not match the specified string.

NOT\_LIKE
Indicates that the query should look for business rule groups where a property value is
 not like the specified string.
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description static QueryOperator valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static QueryOperator [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type      | Method and Description                                                                                |
|------------------------|-------------------------------------------------------------------------------------------------------|
| static QueryOperator   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.        |
| static QueryOperator[] | values() Returns an array containing the constants of this enum type, in the order they are declared. |

    - Methods inherited from class java.lang.Enum
clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait