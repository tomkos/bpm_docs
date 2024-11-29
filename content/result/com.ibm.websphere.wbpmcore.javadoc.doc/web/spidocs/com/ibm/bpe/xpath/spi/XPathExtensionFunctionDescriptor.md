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
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Class XPathExtensionFunctionDescriptor

- java.lang.Object
    - com.ibm.bpe.xpath.spi.XPathExtensionFunctionDescriptor

- public class XPathExtensionFunctionDescriptor
extends java.lang.Object
This class describes a single XPath extension function that can be used in XPath
 expressions and conditions in a BPEL process. It provides all necessary information for the runtime environment 
 to register and call the custom XPath function. 
 The extension function can be exposed to the process runtime environment by implementing the XPathExtensionFunctionPlugin interface 
 and providing a service configuration file.
 

Since:
8.5

- ======== NESTED CLASS SUMMARY ======== =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Nested Class Summary

Nested Classes 

Modifier and Type
Class and Description

static class 
XPathExtensionFunctionDescriptor.ExpressionType
Used to express in what type of expressions and conditions this function is available.

static class 
XPathExtensionFunctionDescriptor.ParameterType
Enumeration to specify parameter and return types of a function.
    - Field Summary

Fields 

Modifier and Type
Field and Description

static XPathExtensionFunctionDescriptor.ExpressionType[]
ALL\_EXPRESSION\_TYPES
Constant containing all expression and condition types.

static java.lang.String
COPYRIGHT
    - Constructor Summary

Constructors 

Constructor and Description

XPathExtensionFunctionDescriptor(java.lang.String name,
                                java.lang.String namespace,
                                java.lang.String prefix,
                                java.lang.String className,
                                XPathExtensionFunctionDescriptor.ParameterType[] parameterTypes,
                                XPathExtensionFunctionDescriptor.ParameterType returnType,
                                XPathExtensionFunctionDescriptor.ExpressionType[] expressionTypes)
Constructor setting all members.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getClassName () The Java class name that contains the implementation of this function. XPathExtensionFunctionDescriptor.ExpressionType [] getExpressionTypes () Specifies in what type of expressions and conditions this function will be available. java.lang.String getName () The name of the XPath function. java.lang.String getNamespace () The namespace of the XPath function. XPathExtensionFunctionDescriptor.ParameterType [] getParameterTypes () The parameter types of the XPath function. java.lang.String getPrefix () The namespace prefix used in the XPath expression or condition. XPathExtensionFunctionDescriptor.ParameterType getReturnType () The return type of the XPath function. void setClassName (java.lang.String className) Sets the class name of the Java implementation. void setExpressionTypes (XPathExtensionFunctionDescriptor.ExpressionType [] expressionTypes) Sets the expression types of the function. void setName (java.lang.String name) Sets the name of the XPath function. void setNamespace (java.lang.String namespace) Sets the XML namespace for the function. void setParameterTypes (XPathExtensionFunctionDescriptor.ParameterType [] parameterTypes) Sets the parameter types of the function. void setPrefix (java.lang.String prefix) Sets the XML prefix of the function. void setReturnType (XPathExtensionFunctionDescriptor.ParameterType returnType) Sets the return type of the function. java.lang.String toString ()

### Method Summary

| Modifier and Type                                 | Method and Description                                                                                                           |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String                                  | getClassName() The Java class name that contains the implementation of this function.                                            |
| XPathExtensionFunctionDescriptor.ExpressionType[] | getExpressionTypes() Specifies in what type of expressions and conditions this function will be available.                       |
| java.lang.String                                  | getName() The name of the XPath function.                                                                                        |
| java.lang.String                                  | getNamespace() The namespace of the XPath function.                                                                              |
| XPathExtensionFunctionDescriptor.ParameterType[]  | getParameterTypes() The parameter types of the XPath function.                                                                   |
| java.lang.String                                  | getPrefix() The namespace prefix used in the XPath expression or condition.                                                      |
| XPathExtensionFunctionDescriptor.ParameterType    | getReturnType() The return type of the XPath function.                                                                           |
| void                                              | setClassName(java.lang.String className) Sets the class name of the Java implementation.                                         |
| void                                              | setExpressionTypes(XPathExtensionFunctionDescriptor.ExpressionType[] expressionTypes) Sets the expression types of the function. |
| void                                              | setName(java.lang.String name) Sets the name of the XPath function.                                                              |
| void                                              | setNamespace(java.lang.String namespace) Sets the XML namespace for the function.                                                |
| void                                              | setParameterTypes(XPathExtensionFunctionDescriptor.ParameterType[] parameterTypes) Sets the parameter types of the function.     |
| void                                              | setPrefix(java.lang.String prefix) Sets the XML prefix of the function.                                                          |
| void                                              | setReturnType(XPathExtensionFunctionDescriptor.ParameterType returnType) Sets the return type of the function.                   |
| java.lang.String                                  | toString()                                                                                                                       |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait