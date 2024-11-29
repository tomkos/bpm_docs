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

## Interface FaultSelector

- All Superinterfaces:
commonj.connector.runtime.BindingContext, java.io.Serializable

public interface FaultSelector
extends commonj.connector.runtime.BindingContext
A Fault Selector that determines if the input data is a business fault,
 runtime fault or a normal response. It also determines the native fault name.

- ======== NESTED CLASS SUMMARY ======== =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Nested Class Summary

Nested Classes 

Modifier and Type
Interface and Description

static class 
FaultSelector.ResponseType
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String COPYRIGHT

### Field Summary

| Modifier and Type       | Field and Description   |
|-------------------------|-------------------------|
| static java.lang.String | COPYRIGHT               |

- Fields inherited from interface commonj.connector.runtime.BindingContext
BINDING\_COMMUNICATION, BINDING\_COMMUNICATION\_INBOUND, BINDING\_COMMUNICATION\_OUTBOUND, BINDING\_CONFIGURATION, BINDING\_INVOCATION, BINDING\_INVOCATION\_FAULT, BINDING\_INVOCATION\_REQUEST, BINDING\_INVOCATION\_RESPONSE, BINDING\_NAME, BINDING\_REGISTRY, BINDING\_TYPE, BINDING\_TYPE\_EIS, BINDING\_TYPE\_HTTP, BINDING\_TYPE\_JMS, EXPECTED\_TYPE, INTERACTION\_SPEC

- Method Summary Methods Modifier and Type Method and Description java.lang.String getFaultName (java.lang.Object source) Gets the native fault name from the headers from the context or from the source Object FaultSelector.ResponseType getResponseType (java.lang.Object source) This method looks at the source object or headers from the context to determine if the response is fault or not.

### Method Summary

| Modifier and Type          | Method and Description                                                                                                                                     |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String           | getFaultName(java.lang.Object source) Gets the native fault name from the headers from the context or from the  source Object                              |
| FaultSelector.ResponseType | getResponseType(java.lang.Object source) This method looks at the source object or headers from the context to  determine if the response is fault or not. |

    - Methods inherited from interface commonj.connector.runtime.BindingContext
setBindingContext