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

## Interface EndpointLookupContextType

- public interface EndpointLookupContextType A representation of the model object 'Endpoint Lookup Context Type '. The following features are supported:

```
public interface EndpointLookupContextType
```

The following features are supported:
 
Endpoint Reference
Registry Annotations

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

com.ibm.wsspi.sca.addressing.EndpointReferenceType
getEndpointReference()
Returns the value of the 'Endpoint Reference' containment reference.

RegistryAnnotationsType
getRegistryAnnotations()
Returns the value of the 'Registry Annotations' containment reference.

void
setEndpointReference(com.ibm.wsspi.sca.addressing.EndpointReferenceType value)
Sets the value of the 'Endpoint Reference' containment reference.

void
setRegistryAnnotations(RegistryAnnotationsType value)
Sets the value of the 'Registry Annotations' containment reference.

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

    - getEndpointReference
com.ibm.wsspi.sca.addressing.EndpointReferenceType getEndpointReference()
Returns the value of the 'Endpoint Reference' containment reference.
Returns:the value of the 'Endpoint Reference' containment reference.See Also:setEndpointReference(EndpointReferenceType)
    - setEndpointReference
void setEndpointReference(com.ibm.wsspi.sca.addressing.EndpointReferenceType value)
Sets the value of the 'Endpoint Reference' containment reference.
Parameters:value - the new value of the 'Endpoint Reference' containment reference.See Also:getEndpointReference()
    - getRegistryAnnotations
RegistryAnnotationsType getRegistryAnnotations()
Returns the value of the 'Registry Annotations' containment reference.
Returns:the value of the 'Registry Annotations' containment reference.See Also:setRegistryAnnotations(RegistryAnnotationsType)
    - setRegistryAnnotations
void setRegistryAnnotations(RegistryAnnotationsType value)
Sets the value of the 'Registry Annotations' containment reference.
Parameters:value - the new value of the 'Registry Annotations' containment reference.See Also:getRegistryAnnotations()