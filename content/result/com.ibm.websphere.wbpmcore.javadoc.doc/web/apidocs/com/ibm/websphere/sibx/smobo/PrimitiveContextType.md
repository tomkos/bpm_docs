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

## Interface PrimitiveContextType

- public interface PrimitiveContextType A representation of the model object 'Primitive Context Type '. The following features are supported:

```
public interface PrimitiveContextType
```

The following features are supported:
 
Endpoint Lookup Context

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.util.List<EndpointLookupContextType>
getEndpointLookupContext()
Returns the value of the 'Endpoint Lookup Context' containment reference list.

FanOutContextType
getFanOutContext()
Returns the value of the 'Fan Out Context' containment reference

WTXContextType
getWTXContext()
Returns the value of the 'WTX Context' containment reference.

void
setFanOutContext(FanOutContextType value)
Sets the value of the 'Fan Out Context' containment reference

void
setWTXContext(WTXContextType value)
Sets the value of the 'WTX Context' containment reference.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- $sccsid
static final java.lang.String $sccsid
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getEndpointLookupContext
java.util.List<EndpointLookupContextType> getEndpointLookupContext()
Returns the value of the 'Endpoint Lookup Context' containment reference list.
 The list contents are of type EndpointLookupContextType.
Returns:the value of the 'Endpoint Lookup Context' containment reference list.
    - getFanOutContext
FanOutContextType getFanOutContext()
Returns the value of the 'Fan Out Context' containment reference.
 

Returns:the value of the 'Fan Out Context' containment reference.See Also:setFanOutContext(FanOutContextType)
    - setFanOutContext
void setFanOutContext(FanOutContextType value)
Sets the value of the 'Fan Out Context' containment reference.
 

Parameters:value - the new value of the 'Fan Out Context' containment reference.See Also:getFanOutContext()
    - getWTXContext
WTXContextType getWTXContext()
Returns the value of the 'WTX Context' containment reference.
Returns:the value of the 'WTX Context' containment reference.See Also:setWTXContext(WTXContextType)
    - setWTXContext
void setWTXContext(WTXContextType value)
Sets the value of the 'WTX Context' containment reference.
Parameters:value - the new value of the 'WTX Context' containment reference.See Also:getWTXContext()