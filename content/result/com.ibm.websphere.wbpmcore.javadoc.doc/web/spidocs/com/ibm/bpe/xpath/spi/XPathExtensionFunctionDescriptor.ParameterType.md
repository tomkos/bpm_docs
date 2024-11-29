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

## Enum XPathExtensionFunctionDescriptor.ParameterType

- java.lang.Object
    - java.lang.Enum<XPathExtensionFunctionDescriptor.ParameterType>
        - com.ibm.bpe.xpath.spi.XPathExtensionFunctionDescriptor.ParameterType

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<XPathExtensionFunctionDescriptor.ParameterType>

Enclosing class:
XPathExtensionFunctionDescriptor

public static enum XPathExtensionFunctionDescriptor.ParameterType
extends java.lang.Enum<XPathExtensionFunctionDescriptor.ParameterType>
Enumeration to specify parameter and return types of a function.
 The table shows how the defined parameter types map to XPath and Java types:
 

Parameter Type
XPath Type
Java Type

Object
Node
commonj.sdo.DataObject

NODE\_SET
node-set
java.util.List

BOOLEAN
boolean
java.lang.Boolean or boolean

STRING
string
java.lang.String

NUMBER
number
java.lang.Number including any sub-classes, such as: Integer or int.

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

BOOLEAN
Specifies that a parameter or return type is a boolean.

NODE\_SET
Specifies that a parameter or return type is a node-set.

NUMBER
Specifies that a parameter or return type is a number.

OBJECT
Specifies that a parameter or return type is a complex object.

STRING
Specifies that a parameter or return type is a string.
    - Method Summary Methods Modifier and Type Method and Description static XPathExtensionFunctionDescriptor.ParameterType valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static XPathExtensionFunctionDescriptor.ParameterType [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type                                       | Method and Description                                                                                |
|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| static XPathExtensionFunctionDescriptor.ParameterType   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.        |
| static XPathExtensionFunctionDescriptor.ParameterType[] | values() Returns an array containing the constants of this enum type, in the order they are declared. |

    - Methods inherited from class java.lang.Enum
clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait