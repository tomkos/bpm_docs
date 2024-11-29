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

## Enum XPathExtensionFunctionDescriptor.ExpressionType

- java.lang.Object
    - java.lang.Enum<XPathExtensionFunctionDescriptor.ExpressionType>
        - com.ibm.bpe.xpath.spi.XPathExtensionFunctionDescriptor.ExpressionType

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<XPathExtensionFunctionDescriptor.ExpressionType>

Enclosing class:
XPathExtensionFunctionDescriptor

public static enum XPathExtensionFunctionDescriptor.ExpressionType
extends java.lang.Enum<XPathExtensionFunctionDescriptor.ExpressionType>
Used to express in what type of expressions and conditions this function is available.
 For example, there might be functions that are required in the join condition of a BPEL process
 but not in a link condition.

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

EXIT\_CONDITION
To indicate the function is available in a BPEL exit condition.

FOR\_EACH\_COUNTER
To indicate the function is available in an BPEL for-each counter expression.

GENERAL\_EXPRESSION
To indicate the function is available in a BPEL general expression, for example, in a to or from expression of an assignment.

JOIN\_CONDITION
To indicate the function is available in a BPEL join condition.

TIMEOUT\_EXPRESSION
To indicate the function is available in a BPEL timeout expression.

TRANSITION\_CONDITION
To indicate the function is available in a BPEL  link condition
    - Method Summary Methods Modifier and Type Method and Description static XPathExtensionFunctionDescriptor.ExpressionType valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static XPathExtensionFunctionDescriptor.ExpressionType [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type                                        | Method and Description                                                                                |
|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| static XPathExtensionFunctionDescriptor.ExpressionType   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.        |
| static XPathExtensionFunctionDescriptor.ExpressionType[] | values() Returns an array containing the constants of this enum type, in the order they are declared. |

    - Methods inherited from class java.lang.Enum
clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait