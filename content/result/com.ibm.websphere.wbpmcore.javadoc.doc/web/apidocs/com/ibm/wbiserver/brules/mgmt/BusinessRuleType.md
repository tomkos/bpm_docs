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

## Enum BusinessRuleType

- java.lang.Object
    - java.lang.Enum<BusinessRuleType>
        - com.ibm.wbiserver.brules.mgmt.BusinessRuleType

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<BusinessRuleType>

public enum BusinessRuleType
extends java.lang.Enum<BusinessRuleType>
An enum used to identify the type of a business rule.

- =========== ENUM CONSTANT SUMMARY =========== =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

DECISION\_TABLE
Indicates that the business rule is a decision table.

RULE\_SET
Indicates that the business rule is a ruleset.
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description static BusinessRuleType valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static BusinessRuleType [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type         | Method and Description                                                                                |
|---------------------------|-------------------------------------------------------------------------------------------------------|
| static BusinessRuleType   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.        |
| static BusinessRuleType[] | values() Returns an array containing the constants of this enum type, in the order they are declared. |

    - Methods inherited from class java.lang.Enum
clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait