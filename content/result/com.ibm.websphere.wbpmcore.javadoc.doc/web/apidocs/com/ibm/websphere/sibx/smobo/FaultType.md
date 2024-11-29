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

## Interface FaultType

- public interface FaultType begin-user-doc A representation of the model object 'Fault Type '. end-user-doc The following features are supported:

```
public interface FaultType
```

The following features are supported:
 
Code
Reason
Node
Role

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

com.ibm.wsspi.sca.message.FaultCodeElement
getCode()
Returns the value of the 'Code' containment reference.

java.lang.String
getNode()
Returns the value of the 'Node' attribute.

com.ibm.wsspi.sca.message.FaultReasonElement
getReason()
Returns the value of the 'Reason' containment reference.

java.lang.String
getRole()
Returns the value of the 'Role' attribute.

void
setCode(com.ibm.wsspi.sca.message.FaultCodeElement value)
Sets the value of the 'Code' containment reference.

void
setNode(java.lang.String value)
Sets the value of the 'Node' attribute.

void
setReason(com.ibm.wsspi.sca.message.FaultReasonElement value)
Sets the value of the 'Reason' containment reference.

void
setRole(java.lang.String value)
Sets the value of the 'Role' attribute.

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

    - getCode
com.ibm.wsspi.sca.message.FaultCodeElement getCode()
Returns the value of the 'Code' containment reference.
Returns:the value of the 'Code' containment reference.See Also:#setCode(FaultcodeType)
    - setCode
void setCode(com.ibm.wsspi.sca.message.FaultCodeElement value)
Sets the value of the 'Code' containment reference.
Parameters:value - the new value of the 'Code' containment reference.See Also:getCode()
    - getReason
com.ibm.wsspi.sca.message.FaultReasonElement getReason()
Returns the value of the 'Reason' containment reference.
Returns:the value of the 'Reason' containment reference.See Also:#setReason(FaultreasonType)
    - setReason
void setReason(com.ibm.wsspi.sca.message.FaultReasonElement value)
Sets the value of the 'Reason' containment reference.
Parameters:value - the new value of the 'Reason' containment reference.See Also:getReason()
    - getNode
java.lang.String getNode()
Returns the value of the 'Node' attribute.
Returns:the value of the 'Node' attribute.See Also:setNode(String)
    - setNode
void setNode(java.lang.String value)
Sets the value of the 'Node' attribute.
Parameters:value - the new value of the 'Node' attribute.See Also:getNode()
    - getRole
java.lang.String getRole()
Returns the value of the 'Role' attribute.
Returns:the value of the 'Role' attribute.See Also:setRole(String)
    - setRole
void setRole(java.lang.String value)
Sets the value of the 'Role' attribute.
Parameters:value - the new value of the 'Role' attribute.See Also:getRole()