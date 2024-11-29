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

## Interface PrimitiveType

- public interface PrimitiveType A representation of the model object 'Primitive Type '. This is used by the invocationPath attribute on the FailInfo Type. The following features are supported:

```
public interface PrimitiveType
```

The following features are supported:
 
In Terminal
Name
Out Terminal

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
getInTerminal()
Returns the value of the 'In Terminal' attribute.

java.lang.String
getName()
Returns the value of the 'Name' attribute.

java.lang.String
getOutTerminal()
Returns the value of the 'Out Terminal' attribute.

void
setInTerminal(java.lang.String value)
Sets the value of the 'In Terminal' attribute.

void
setName(java.lang.String value)
Sets the value of the 'Name' attribute.

void
setOutTerminal(java.lang.String value)
Sets the value of the 'Out Terminal' attribute.

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

    - getInTerminal
java.lang.String getInTerminal()
Returns the value of the 'In Terminal' attribute.
Returns:the value of the 'In Terminal' attribute.See Also:setInTerminal(String)
    - setInTerminal
void setInTerminal(java.lang.String value)
Sets the value of the 'In Terminal' attribute.
Parameters:value - the new value of the 'In Terminal' attribute.See Also:getInTerminal()
    - getName
java.lang.String getName()
Returns the value of the 'Name' attribute.
Returns:the value of the 'Name' attribute.See Also:setName(String)
    - setName
void setName(java.lang.String value)
Sets the value of the 'Name' attribute.
Parameters:value - the new value of the 'Name' attribute.See Also:getName()
    - getOutTerminal
java.lang.String getOutTerminal()
Returns the value of the 'Out Terminal' attribute.
 Note that the last primitive in the chain will have a null for the output terminal.
 
Returns:the value of the 'Out Terminal' attribute.See Also:setOutTerminal(String)
    - setOutTerminal
void setOutTerminal(java.lang.String value)
Sets the value of the 'Out Terminal' attribute.
Parameters:value - the new value of the 'Out Terminal' attribute.See Also:getOutTerminal()