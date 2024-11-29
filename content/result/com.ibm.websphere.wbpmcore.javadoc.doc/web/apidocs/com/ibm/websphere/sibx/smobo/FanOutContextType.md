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

## Interface FanOutContextType

- public interface FanOutContextType begin-user-doc A representation of the model object 'Fan Out Context Type '. end-user-doc The following features are supported:

```
public interface FanOutContextType
```

The following features are supported:
 
Iteration
Occurrence

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

java.math.BigInteger
getIteration()
Returns the value of the 'Iteration' attribute

java.lang.Object
getOccurrence()
Returns the value of the 'Occurrence' containment reference

void
setIteration(java.math.BigInteger value)
Sets the value of the 'Iteration' attribute

void
setOccurrence(java.lang.Object value)
Sets the value of the 'Occurrence' containment reference

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

    - getIteration
java.math.BigInteger getIteration()
Returns the value of the 'Iteration' attribute.
 

Returns:the value of the 'Iteration' attribute.See Also:setIteration(BigInteger)
    - setIteration
void setIteration(java.math.BigInteger value)
Sets the value of the 'Iteration' attribute.
 

Parameters:value - the new value of the 'Iteration' attribute.See Also:getIteration()
    - getOccurrence
java.lang.Object getOccurrence()
Returns the value of the 'Occurrence' containment reference.
 

Returns:the value of the 'Occurrence' containment reference.See Also:setOccurrence(Object)
    - setOccurrence
void setOccurrence(java.lang.Object value)
Sets the value of the 'Occurrence' containment reference.
 

Parameters:value - the new value of the 'Occurrence' containment reference.  Note that
              this must be a commonj.sdo.DataObject rather than a simple java.lang.Object.See Also:getOccurrence()