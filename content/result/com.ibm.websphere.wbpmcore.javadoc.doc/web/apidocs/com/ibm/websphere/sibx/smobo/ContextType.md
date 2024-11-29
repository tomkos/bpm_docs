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

## Interface ContextType

- All Known Subinterfaces: UserDefinedContextType public interface ContextType A representation of the model object 'Context Type '. The following features are supported:

```
public interface ContextType
```

The following features are supported:
 
Correlation
Transient
Fail Info
Primitive Context

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

java.lang.Object
getCorrelation()
Returns the value of the 'Correlation' containment reference.

DynamicPropertyContextType
getDynamicProperty()
Returns the value of the 'Dynamic Property' containment reference

FailInfoType
getFailInfo()
Returns the value of the 'Fail Info' containment reference.

PrimitiveContextType
getPrimitiveContext()
Returns the value of the 'Primitive Context' containment reference.

java.lang.Object
getShared()
Returns the value of the 'Shared' containment reference

java.lang.Object
getTransient()
Returns the value of the 'Transient' containment reference.

UserContextType
getUserContext()
Returns the value of the 'User Context' containment reference

void
setCorrelation(java.lang.Object value)
Sets the value of the 'Correlation' containment reference.

void
setDynamicProperty(DynamicPropertyContextType value)
Sets the value of the 'Dynamic Property' containment reference

void
setFailInfo(FailInfoType value)
Sets the value of the 'Fail Info' containment reference.

void
setPrimitiveContext(PrimitiveContextType value)
Sets the value of the 'Primitive Context' containment reference.

void
setShared(java.lang.Object value)
Sets the value of the 'Shared' containment reference

void
setTransient(java.lang.Object value)
Sets the value of the 'Transient' containment reference.

void
setUserContext(UserContextType value)
Sets the value of the 'User Context' containment reference

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

    - getCorrelation
java.lang.Object getCorrelation()
Returns the value of the 'Correlation' containment reference.
 
 Returns the Business Object representing the correlation context.
 
Returns:the value of the 'Correlation' containment reference.See Also:setCorrelation(Object)
    - setCorrelation
void setCorrelation(java.lang.Object value)
Sets the value of the 'Correlation' containment reference.
Parameters:value - the new value of the 'Correlation' containment reference. Note that
              this must be a commonj.sdo.DataObject rather than a simple java.lang.Object.See Also:getCorrelation()
    - getTransient
java.lang.Object getTransient()
Returns the value of the 'Transient' containment reference.
 
 Returns the Business Object representing the transient context.
 
Returns:the value of the 'Transient' containment reference.See Also:setTransient(Object)
    - setTransient
void setTransient(java.lang.Object value)
Sets the value of the 'Transient' containment reference.
Parameters:value - the new value of the 'Transient' containment reference. Note that
              this must be a commonj.sdo.DataObject rather than a simple java.lang.Object.See Also:getTransient()
    - getFailInfo
FailInfoType getFailInfo()
Returns the value of the 'Fail Info' containment reference.
 
 Returns the details of a reported exception in a FailInfo element.
 
Returns:the value of the 'Fail Info' containment reference.See Also:setFailInfo(FailInfoType)
    - setFailInfo
void setFailInfo(FailInfoType value)
Sets the value of the 'Fail Info' containment reference.
Parameters:value - the new value of the 'Fail Info' containment reference.See Also:getFailInfo()
    - getPrimitiveContext
PrimitiveContextType getPrimitiveContext()
Returns the value of the 'Primitive Context' containment reference.
 
 Returns the Business Object representing the primitive
 context.
 
Returns:the value of the 'Primitive Context' containment reference.See Also:setPrimitiveContext(PrimitiveContextType)
    - setPrimitiveContext
void setPrimitiveContext(PrimitiveContextType value)
Sets the value of the 'Primitive Context' containment reference.
Parameters:value - the new value of the 'Primitive Context' containment reference.See Also:getPrimitiveContext()
    - getShared
java.lang.Object getShared()
Returns the value of the 'Shared' containment reference.
 

Returns:the value of the 'Shared' containment reference.See Also:setShared(Object)
    - setShared
void setShared(java.lang.Object value)
Sets the value of the 'Shared' containment reference.
 

Parameters:value - the new value of the 'Shared' containment reference.  Note that
              this must be a commonj.sdo.DataObject rather than a simple java.lang.Object.See Also:getShared()
    - getDynamicProperty
DynamicPropertyContextType getDynamicProperty()
Returns the value of the 'Dynamic Property' containment reference.
 

Returns:the value of the 'Dynamic Property' containment reference.See Also:setDynamicProperty(DynamicPropertyContextType)
    - setDynamicProperty
void setDynamicProperty(DynamicPropertyContextType value)
Sets the value of the 'Dynamic Property' containment reference.
 

Parameters:value - the new value of the 'Dynamic Property' containment reference.See Also:getDynamicProperty()
    - getUserContext
UserContextType getUserContext()
Returns the value of the 'User Context' containment reference.
 

Returns:the value of the 'User Context' containment reference.See Also:setUserContext(UserContextType)
    - setUserContext
void setUserContext(UserContextType value)
Sets the value of the 'User Context' containment reference.
 

Parameters:value - the new value of the 'User Context' containment reference.See Also:getUserContext()