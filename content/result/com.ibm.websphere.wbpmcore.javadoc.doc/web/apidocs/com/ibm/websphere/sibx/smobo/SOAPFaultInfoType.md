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

## Interface SOAPFaultInfoType

- public interface SOAPFaultInfoType A representation of the model object 'SOAP Fault Info Type '. This is used to represent SOAP Fault information. Please refer to the SOAP specification version 1.1 or detailed usage information. The following features are supported:

```
public interface SOAPFaultInfoType
```

This is used to represent SOAP Fault information.  Please refer to the SOAP
 specification version 1.1 or detailed usage information.

The following features are supported:
 
Faultcode
Faultstring
Faultactor

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

FaultType
getExtendedFaultInfo()
Returns the value of the 'Extended Fault Info' containment reference.

java.lang.String
getFaultactor()
Returns the value of the 'Faultactor' attribute.

java.lang.Object
getFaultcode()
Returns the value of the 'Faultcode' attribute.

java.lang.String
getFaultstring()
Returns the value of the 'Faultstring' attribute.

void
setExtendedFaultInfo(FaultType value)
Sets the value of the 'Extended Fault Info' containment reference.

void
setFaultactor(java.lang.String value)
Sets the value of the 'Faultactor' attribute.

void
setFaultcode(java.lang.Object value)
Sets the value of the 'Faultcode' attribute.

void
setFaultstring(java.lang.String value)
Sets the value of the 'Faultstring' attribute.

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

    - getFaultcode
java.lang.Object getFaultcode()
Returns the value of the 'Faultcode' attribute.
Returns:the value of the 'Faultcode' attribute.See Also:setFaultcode(Object)
    - setFaultcode
void setFaultcode(java.lang.Object value)
Sets the value of the 'Faultcode' attribute.
Parameters:value - the new value of the 'Faultcode' attribute.See Also:getFaultcode()
    - getFaultstring
java.lang.String getFaultstring()
Returns the value of the 'Faultstring' attribute.
Returns:the value of the 'Faultstring' attribute.See Also:setFaultstring(String)
    - setFaultstring
void setFaultstring(java.lang.String value)
Sets the value of the 'Faultstring' attribute.
Parameters:value - the new value of the 'Faultstring' attribute.See Also:getFaultstring()
    - getFaultactor
java.lang.String getFaultactor()
Returns the value of the 'Faultactor' attribute.
Returns:the value of the 'Faultactor' attribute.See Also:setFaultactor(String)
    - setFaultactor
void setFaultactor(java.lang.String value)
Sets the value of the 'Faultactor' attribute.
Parameters:value - the new value of the 'Faultactor' attribute.See Also:getFaultactor()
    - getExtendedFaultInfo
FaultType getExtendedFaultInfo()
Returns the value of the 'Extended Fault Info' containment reference.
Returns:the value of the 'Extended Fault Info' containment reference.See Also:setExtendedFaultInfo(FaultType)
    - setExtendedFaultInfo
void setExtendedFaultInfo(FaultType value)
Sets the value of the 'Extended Fault Info' containment reference.
Parameters:value - the new value of the 'Extended Fault Info' containment reference.See Also:getExtendedFaultInfo()