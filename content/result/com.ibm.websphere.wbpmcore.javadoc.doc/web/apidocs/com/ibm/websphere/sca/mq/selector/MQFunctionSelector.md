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

## Class MQFunctionSelector

- java.lang.Object
    - com.ibm.websphere.sca.mq.selector.MQFunctionSelector

- All Implemented Interfaces:
commonj.connector.runtime.FunctionSelector

public abstract class MQFunctionSelector
extends java.lang.Object
implements commonj.connector.runtime.FunctionSelector
A helper class which makes it easier to write
 FunctionSelectors for use with WMQ Exports. 
 The commonj.connection.runtime.FunctionSelector interface
 provides a single method which takes an array of arbitrary
 objects as a solitary argument. 
 MQFunctionSelector implements this method by calling an
 abstract method with a more descriptive argument list. An
 implementation of MQFunctionSelector will implement the new
 abstract method with the descriptive argument list.
See Also:FunctionSelector

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Constructor Summary

Constructors 

Constructor and Description

MQFunctionSelector()
    - Method Summary Methods Modifier and Type Method and Description abstract java.lang.String generateEISFunctionName (MQMD md, java.lang.String bodyFormat, java.util.List headers, MQDataInputStream input) A more descriptive WMQ-specific method to extract a native method name using the FunctionSelector interface. java.lang.String generateEISFunctionName (java.lang.Object[] arg) Given an array of arguments, returns the selected native method name.

### Method Summary

| Modifier and Type         | Method and Description                                                                                                                                                                                                                                                                            |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract java.lang.String | generateEISFunctionName(MQMD md,                        java.lang.String bodyFormat,                        java.util.List headers,                        MQDataInputStream input) A more descriptive WMQ-specific method to extract a native  method name using the FunctionSelector interface. |
| java.lang.String          | generateEISFunctionName(java.lang.Object[] arg) Given an array of arguments, returns the selected native  method name.                                                                                                                                                                            |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait