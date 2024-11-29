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

## Interface ComplexPropertyType

- public interface ComplexPropertyType begin-user-doc A representation of the model object 'Complex Property Type '. end-user-doc The following features are supported:

```
public interface ComplexPropertyType
```

The following features are supported:
 
Name
Value
Type

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
Returns the value of the 'Name' attribute

java.lang.String
getPropertyType()
Returns the value of the 'Type' attribute

java.lang.Object
getValue()
Returns the value of the 'Value' containment reference

void
setName(java.lang.String value)
Sets the value of the 'Name' attribute

void
setPropertyType(java.lang.String value)
Sets the value of the 'Type' attribute

void
setValue(java.lang.Object value)
Sets the value of the 'Value' containment reference

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

    - getName
java.lang.String getName()
Returns the value of the 'Name' attribute.
 

Returns:the value of the 'Name' attribute.See Also:setName(String)
    - setName
void setName(java.lang.String value)
Sets the value of the 'Name' attribute.
 

Parameters:value - the new value of the 'Name' attribute.See Also:getName()
    - getValue
java.lang.Object getValue()
Returns the value of the 'Value' containment reference.
 

Returns:the value of the 'Value' containment reference.See Also:setValue(Object)
    - setValue
void setValue(java.lang.Object value)
Sets the value of the 'Value' containment reference.
 

Parameters:value - the new value of the 'Value' containment reference. Note that
              this must be a commonj.sdo.DataObject rather than a simple java.lang.Object.See Also:getValue()
    - getPropertyType
java.lang.String getPropertyType()
Returns the value of the 'Type' attribute.
 

Returns:the value of the 'Type' attribute.See Also:setPropertyType(String)
    - setPropertyType
void setPropertyType(java.lang.String value)
Sets the value of the 'Type' attribute.
 

Parameters:value - the new value of the 'Type' attribute.See Also:getPropertyType()