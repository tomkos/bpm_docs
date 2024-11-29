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

- public interface DocumentRoot begin-user-doc A representation of the model object 'Document Root '. end-user-doc The following features are supported: See Also: WMQStructuresPackage.getDocumentRoot()

```
public interface DocumentRoot
```

The following features are supported:
 
Mixed
XMLNS Prefix Map
XSI Schema Location
Mq Control
Mq Headers
Mqmd

- ========== METHOD SUMMARY ===========
    - Method Summary

Methods 

Modifier and Type
Method and Description

commonj.sdo.Sequence
getMixed()
Returns the value of the 'Mixed' attribute list

MQControl
getMqControl()
Returns the value of the 'Mq Control' containment reference

MQHeaders
getMqHeaders()
Returns the value of the 'Mq Headers' containment reference

MQMD
getMqmd()
Returns the value of the 'Mqmd' containment reference

java.util.Map
getXMLNSPrefixMap()
Returns the value of the 'XMLNS Prefix Map' map.

java.util.Map
getXSISchemaLocation()
Returns the value of the 'XSI Schema Location' map.

void
setMqControl(MQControl value)
Sets the value of the 'Mq Control' containment reference

void
setMqHeaders(MQHeaders value)
Sets the value of the 'Mq Headers' containment reference

void
setMqmd(MQMD value)
Sets the value of the 'Mqmd' containment reference

- ============ METHOD DETAIL ==========
    - Method Detail

### Method Detail

- getMixed
commonj.sdo.Sequence getMixed()
Returns the value of the 'Mixed' attribute list.
 

 If the meaning of the 'Mixed' attribute list isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Mixed' attribute list.See Also:WMQStructuresPackage.getDocumentRoot\_Mixed()

- getXMLNSPrefixMap
java.util.Map getXMLNSPrefixMap()
Returns the value of the 'XMLNS Prefix Map' map.
 The key is of type String,
 and the value is of type String,
 

 If the meaning of the 'XMLNS Prefix Map' map isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'XMLNS Prefix Map' map.See Also:WMQStructuresPackage.getDocumentRoot\_XMLNSPrefixMap()

- getXSISchemaLocation
java.util.Map getXSISchemaLocation()
Returns the value of the 'XSI Schema Location' map.
 The key is of type String,
 and the value is of type String,
 

 If the meaning of the 'XSI Schema Location' map isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'XSI Schema Location' map.See Also:WMQStructuresPackage.getDocumentRoot\_XSISchemaLocation()

- getMqControl
MQControl getMqControl()
Returns the value of the 'Mq Control' containment reference.
 

 If the meaning of the 'Mq Control' containment reference isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Mq Control' containment reference.See Also:setMqControl(MQControl), 
WMQStructuresPackage.getDocumentRoot\_MqControl()

- setMqControl
void setMqControl(MQControl value)
Sets the value of the 'Mq Control' containment reference.
 

Parameters:value - the new value of the 'Mq Control' containment reference.See Also:getMqControl()

- getMqHeaders
MQHeaders getMqHeaders()
Returns the value of the 'Mq Headers' containment reference.
 

 If the meaning of the 'Mq Headers' containment reference isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Mq Headers' containment reference.See Also:setMqHeaders(MQHeaders), 
WMQStructuresPackage.getDocumentRoot\_MqHeaders()

- setMqHeaders
void setMqHeaders(MQHeaders value)
Sets the value of the 'Mq Headers' containment reference.
 

Parameters:value - the new value of the 'Mq Headers' containment reference.See Also:getMqHeaders()

- getMqmd
MQMD getMqmd()
Returns the value of the 'Mqmd' containment reference.
 

 If the meaning of the 'Mqmd' containment reference isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Mqmd' containment reference.See Also:setMqmd(MQMD), 
WMQStructuresPackage.getDocumentRoot\_Mqmd()

- setMqmd
void setMqmd(MQMD value)
Sets the value of the 'Mqmd' containment reference.
 

Parameters:value - the new value of the 'Mqmd' containment reference.See Also:getMqmd()