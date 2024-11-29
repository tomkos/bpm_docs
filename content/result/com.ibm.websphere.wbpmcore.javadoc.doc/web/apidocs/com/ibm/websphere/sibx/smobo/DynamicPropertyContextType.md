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

## Interface DynamicPropertyContextType

- public interface DynamicPropertyContextType begin-user-doc A representation of the model object 'Dynamic Property Context Type '. end-user-doc The following features are supported:

```
public interface DynamicPropertyContextType
```

The following features are supported:
 
Property Sets
Is Propagated

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

java.util.List<DynamicPropertySetType>
getPropertySets()
Returns the value of the 'Property Sets' containment reference list.

boolean
isIsPropagated()
Returns the value of the 'Is Propagated' attribute

boolean
isSetIsPropagated()
Returns whether the value of the 'Is Propagated' attribute is set

void
setIsPropagated(boolean value)
Sets the value of the 'Is Propagated' attribute

void
unsetIsPropagated()
Unsets the value of the 'Is Propagated' attribute

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

    - getPropertySets
java.util.List<DynamicPropertySetType> getPropertySets()
Returns the value of the 'Property Sets' containment reference list.
 The list contents are of type DynamicPropertySetType.
 

Returns:the value of the 'Property Sets' containment reference list.
    - isIsPropagated
boolean isIsPropagated()
Returns the value of the 'Is Propagated' attribute.
 

Returns:the value of the 'Is Propagated' attribute.See Also:isSetIsPropagated(), 
unsetIsPropagated(), 
setIsPropagated(boolean)
    - setIsPropagated
void setIsPropagated(boolean value)
Sets the value of the 'Is Propagated' attribute.
 

Parameters:value - the new value of the 'Is Propagated' attribute.See Also:isSetIsPropagated(), 
unsetIsPropagated(), 
isIsPropagated()
    - unsetIsPropagated
void unsetIsPropagated()
Unsets the value of the 'Is Propagated' attribute.
 

See Also:isSetIsPropagated(), 
isIsPropagated(), 
setIsPropagated(boolean)
    - isSetIsPropagated
boolean isSetIsPropagated()
Returns whether the value of the 'Is Propagated' attribute is set.
 

Returns:whether the value of the 'Is Propagated' attribute is set.See Also:unsetIsPropagated(), 
isIsPropagated(), 
setIsPropagated(boolean)