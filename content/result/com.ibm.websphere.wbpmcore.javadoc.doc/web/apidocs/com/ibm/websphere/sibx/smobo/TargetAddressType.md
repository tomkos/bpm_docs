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

## Interface TargetAddressType

- public interface TargetAddressType A representation of the model object 'Target Address Type '. The following features are supported:

```
public interface TargetAddressType
```

The following features are supported:
 
Address

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
getAddress()
Returns the value of the 'Address' attribute.

BindingTypeType
getBindingType()
Returns the value of the 'Binding Type' attribute.

java.lang.String
getImport()
Returns the value of the 'Import' attribute

java.lang.String
getRepositoryMetadata()
Returns the value of the 'Repository Metadata' attribute

boolean
isSetBindingType()
Returns whether the value of the 'Binding Type' attribute is set

void
setAddress(java.lang.String value)
Sets the value of the 'Address' attribute.

void
setBindingType(BindingTypeType value)
Sets the value of the 'Binding Type' attribute

void
setImport(java.lang.String value)
Sets the value of the 'Import' attribute

void
setRepositoryMetadata(java.lang.String value)
Sets the value of the 'Repository Metadata' attribute

void
unsetBindingType()
Unsets the value of the 'Binding Type' attribute

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

    - getAddress
java.lang.String getAddress()
Returns the value of the 'Address' attribute.
Returns:the value of the 'Address' attribute.See Also:setAddress(String)
    - setAddress
void setAddress(java.lang.String value)
Sets the value of the 'Address' attribute.
Parameters:value - the new value of the 'Address' attribute.See Also:getAddress()
    - getBindingType
BindingTypeType getBindingType()
Returns the value of the 'Binding Type' attribute.
 The default value is "NotSet".
 The literals are from the enumeration BindingTypeType.
 

Returns:the value of the 'Binding Type' attribute.See Also:BindingTypeType, 
isSetBindingType(), 
unsetBindingType(), 
setBindingType(BindingTypeType)
    - setBindingType
void setBindingType(BindingTypeType value)
Sets the value of the 'Binding Type' attribute.
 

Parameters:value - the new value of the 'Binding Type' attribute.See Also:BindingTypeType, 
isSetBindingType(), 
unsetBindingType(), 
getBindingType()
    - unsetBindingType
void unsetBindingType()
Unsets the value of the 'Binding Type' attribute.
 

See Also:isSetBindingType(), 
getBindingType(), 
setBindingType(BindingTypeType)
    - isSetBindingType
boolean isSetBindingType()
Returns whether the value of the 'Binding Type' attribute is set.
 

Returns:whether the value of the 'Binding Type' attribute is set.See Also:unsetBindingType(), 
getBindingType(), 
setBindingType(BindingTypeType)
    - getImport
java.lang.String getImport()
Returns the value of the 'Import' attribute.
 

Returns:the value of the 'Import' attribute.See Also:setImport(String)
    - setImport
void setImport(java.lang.String value)
Sets the value of the 'Import' attribute.
 

Parameters:value - the new value of the 'Import' attribute.See Also:getImport()
    - getRepositoryMetadata
java.lang.String getRepositoryMetadata()
Returns the value of the 'Repository Metadata' attribute.
 

Returns:the value of the 'Repository Metadata' attribute.See Also:setRepositoryMetadata(String)
    - setRepositoryMetadata
void setRepositoryMetadata(java.lang.String value)
Sets the value of the 'Repository Metadata' attribute.
 

Parameters:value - the new value of the 'Repository Metadata' attribute.See Also:getRepositoryMetadata()