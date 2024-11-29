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

## Class HTTPFunctionSelector

- java.lang.Object
    - com.ibm.websphere.http.selectors.HTTPFunctionSelector

- All Implemented Interfaces:
commonj.connector.runtime.BindingContext, commonj.connector.runtime.FunctionSelector, java.io.Serializable

public abstract class HTTPFunctionSelector
extends java.lang.Object
implements commonj.connector.runtime.FunctionSelector, commonj.connector.runtime.BindingContext
A helper class which makes it easier to write FunctionSelectors for use with HTTP Exports.
 The commonj.connection.runtime.FunctionSelector interface provides a single method which takes an array of arbitrary objects as a solitary argument.
 HTTPFunctionSelector implements this method by calling an abstract method with a more descriptive argument list. 
 
 An implementation of HTTPFunctionSelector will implement the new abstract method with the descriptive argument list.
See Also:Serialized Form

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String COPYRIGHT

### Field Summary

| Modifier and Type       | Field and Description   |
|-------------------------|-------------------------|
| static java.lang.String | COPYRIGHT               |

- Fields inherited from interface commonj.connector.runtime.BindingContext
BINDING\_COMMUNICATION, BINDING\_COMMUNICATION\_INBOUND, BINDING\_COMMUNICATION\_OUTBOUND, BINDING\_CONFIGURATION, BINDING\_INVOCATION, BINDING\_INVOCATION\_FAULT, BINDING\_INVOCATION\_REQUEST, BINDING\_INVOCATION\_RESPONSE, BINDING\_NAME, BINDING\_REGISTRY, BINDING\_TYPE, BINDING\_TYPE\_EIS, BINDING\_TYPE\_HTTP, BINDING\_TYPE\_JMS, EXPECTED\_TYPE, INTERACTION\_SPEC

- Constructor Summary

Constructors 

Constructor and Description

HTTPFunctionSelector()

- Method Summary Methods Modifier and Type Method and Description abstract java.lang.String generateEISFunctionName (HTTPControl cp, HTTPHeaders headers, HTTPInputStream input) A more descriptive HTTP-specific method to extract a native method name using the FunctionSelector interface. java.lang.String generateEISFunctionName (java.lang.Object[] args) Unmarshalls parameters and calls an overloaded generateEISFunctionName() method with a more intuitive argument list: HTTPControl, HTTPHeaders, and HTTPInputStream. void setBindingContext (java.util.Map bindingContext) Set Binding Context on the Data Binding.

### Method Summary

| Modifier and Type         | Method and Description                                                                                                                                                                                                                          |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract java.lang.String | generateEISFunctionName(HTTPControl cp,                        HTTPHeaders headers,                        HTTPInputStream input) A more descriptive HTTP-specific method to extract a native method name using the FunctionSelector interface. |
| java.lang.String          | generateEISFunctionName(java.lang.Object[] args) Unmarshalls parameters and calls an overloaded generateEISFunctionName() method   with a more intuitive argument list: HTTPControl, HTTPHeaders, and HTTPInputStream.                          |
| void                      | setBindingContext(java.util.Map bindingContext) Set Binding Context on the Data Binding.                                                                                                                                                        |

    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait