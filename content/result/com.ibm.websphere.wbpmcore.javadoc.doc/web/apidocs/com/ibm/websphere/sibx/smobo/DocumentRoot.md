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

## Interface DocumentRoot

- public interface DocumentRoot A representation of the model object 'Document Root '. The following features are supported:

```
public interface DocumentRoot
```

The following features are supported:
 
Mixed
XMLNS Prefix Map
XSI Schema Location
Smo

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

commonj.sdo.Sequence
getMixed()
Returns the value of the 'Mixed' attribute list.

ServiceMessageObject
getSmo()
Returns the value of the 'Smo' containment reference.

java.util.Map
getXMLNSPrefixMap()
Returns the value of the 'XMLNS Prefix Map' map.

java.util.Map
getXSISchemaLocation()
Returns the value of the 'XSI Schema Location' map.

void
setSmo(ServiceMessageObject value)
Sets the value of the 'Smo' containment reference.

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

    - getMixed
commonj.sdo.Sequence getMixed()
Returns the value of the 'Mixed' attribute list.
Returns:the value of the 'Mixed' attribute list.
    - getXMLNSPrefixMap
java.util.Map getXMLNSPrefixMap()
Returns the value of the 'XMLNS Prefix Map' map.
 The key is of type String,
 and the value is of type String,
Returns:the value of the 'XMLNS Prefix Map' map.
    - getXSISchemaLocation
java.util.Map getXSISchemaLocation()
Returns the value of the 'XSI Schema Location' map.
 The key is of type String,
 and the value is of type String,
Returns:the value of the 'XSI Schema Location' map.
    - getSmo
ServiceMessageObject getSmo()
Returns the value of the 'Smo' containment reference.
Returns:the value of the 'Smo' containment reference.See Also:setSmo(ServiceMessageObject)
    - setSmo
void setSmo(ServiceMessageObject value)
Sets the value of the 'Smo' containment reference.
Parameters:value - the new value of the 'Smo' containment reference.See Also:getSmo()