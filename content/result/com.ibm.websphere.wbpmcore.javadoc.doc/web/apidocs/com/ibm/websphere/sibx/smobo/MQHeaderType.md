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

## Interface MQHeaderType

- public interface MQHeaderType A representation of the model object 'MQ Header Type '. The following features are supported:

```
public interface MQHeaderType
```

The following features are supported:
 
Md
Control
Header

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

MQControl
getControl()
Returns the value of the 'Control' containment reference.

java.util.List<MQChainedHeaderType>
getHeader()
Returns the value of the 'Header' containment reference list.

MQMD
getMd()
Returns the value of the 'Md' containment reference.

void
setControl(MQControl value)
Sets the value of the 'Control' containment reference.

void
setMd(MQMD value)
Sets the value of the 'Md' containment reference.

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

    - getMd
MQMD getMd()
Returns the value of the 'Md' containment reference.
Returns:the value of the 'Md' containment reference.See Also:setMd(MQMD)
    - setMd
void setMd(MQMD value)
Sets the value of the 'Md' containment reference.
Parameters:value - the new value of the 'Md' containment reference.See Also:getMd()
    - getControl
MQControl getControl()
Returns the value of the 'Control' containment reference.
Returns:the value of the 'Control' containment reference.See Also:setControl(MQControl)
    - setControl
void setControl(MQControl value)
Sets the value of the 'Control' containment reference.
Parameters:value - the new value of the 'Control' containment reference.See Also:getControl()
    - getHeader
java.util.List<MQChainedHeaderType> getHeader()
Returns the value of the 'Header' containment reference list.
 The list contents are of type MQChainedHeaderType.
Returns:the value of the 'Header' containment reference list.