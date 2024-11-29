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

## Interface SOAPHeaderType

- public interface SOAPHeaderType A representation of the model object 'SOAP Header Type '. Each SOAP header in the SOAP headers list has this format. The namespace, name, prefix and value of each SOAP header is accessible via this interface. The following features are supported:

```
public interface SOAPHeaderType
```

The following features are supported:
 
Name Space
Name
Prefix
Value

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

java.lang.String
getName()
Returns the value of the 'Name' attribute.

java.lang.String
getNameSpace()
Returns the value of the 'Name Space' attribute.

java.lang.String
getPrefix()
Returns the value of the 'Prefix' attribute.

java.lang.Object
getValue()
Returns the value of the 'Value' containment reference.

void
setName(java.lang.String value)
Sets the value of the 'Name' attribute.

void
setNameSpace(java.lang.String value)
Sets the value of the 'Name Space' attribute.

void
setPrefix(java.lang.String value)
Sets the value of the 'Prefix' attribute.

void
setValue(java.lang.Object value)
Sets the value of the 'Value' containment reference.

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

    - getNameSpace
java.lang.String getNameSpace()
Returns the value of the 'Name Space' attribute.
Returns:the value of the 'Name Space' attribute.See Also:setNameSpace(String)
    - setNameSpace
void setNameSpace(java.lang.String value)
Sets the value of the 'Name Space' attribute.
Parameters:value - the new value of the 'Name Space' attribute.See Also:getNameSpace()
    - getName
java.lang.String getName()
Returns the value of the 'Name' attribute.
Returns:the value of the 'Name' attribute.See Also:setName(String)
    - setName
void setName(java.lang.String value)
Sets the value of the 'Name' attribute.
Parameters:value - the new value of the 'Name' attribute.See Also:getName()
    - getPrefix
java.lang.String getPrefix()
Returns the value of the 'Prefix' attribute.
Returns:the value of the 'Prefix' attribute.See Also:setPrefix(String)
    - setPrefix
void setPrefix(java.lang.String value)
Sets the value of the 'Prefix' attribute.
Parameters:value - the new value of the 'Prefix' attribute.See Also:getPrefix()
    - getValue
java.lang.Object getValue()
Returns the value of the 'Value' containment reference.
Returns:the value of the 'Value' containment reference.See Also:setValue(Object)
    - setValue
void setValue(java.lang.Object value)
Sets the value of the 'Value' containment reference.
Parameters:value - the new value of the 'Value' containment reference. Note that
              this must be a commonj.sdo.DataObject rather than a simple java.lang.Object.See Also:getValue()