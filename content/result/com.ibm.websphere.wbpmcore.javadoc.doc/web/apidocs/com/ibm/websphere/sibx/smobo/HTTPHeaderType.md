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

## Interface HTTPHeaderType

- public interface HTTPHeaderType begin-user-doc A representation of the model object 'HTTP Header Type '. end-user-doc The following features are supported:

```
public interface HTTPHeaderType
```

The following features are supported:
 
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

HTTPControl
getControl()
Returns the value of the 'Control' containment reference

java.util.List<HTTPHeader>
getHeader()
Returns the value of the 'Header' containment reference list.

void
setControl(HTTPControl value)
Sets the value of the 'Control' containment reference

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

    - getControl
HTTPControl getControl()
Returns the value of the 'Control' containment reference.
 

Returns:the value of the 'Control' containment reference.See Also:setControl(HTTPControl)
    - setControl
void setControl(HTTPControl value)
Sets the value of the 'Control' containment reference.
 

Parameters:value - the new value of the 'Control' containment reference.See Also:getControl()
    - getHeader
java.util.List<HTTPHeader> getHeader()
Returns the value of the 'Header' containment reference list.
 The list contents are of type HTTPHeader.
 

Returns:the value of the 'Header' containment reference list.