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

## Interface ESBTerminalType

- All Superinterfaces: TerminalType public interface ESBTerminalType extends TerminalType An ESB specific implementation of the TerminalType interface. This interface defines the following pieces of information that define the terminal type: These types refer to type information about the three parts of a Service Message Object.

```
public interface ESBTerminalType
extends TerminalType
```

    - Body type
    - Correlation context type
    - Transient context type

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

javax.xml.namespace.QName
getBodyType()
Returns the type of the SMO body.

javax.xml.namespace.QName
getCorrelationContextType()
Returns the type of the SMO correlation context

javax.xml.namespace.QName
getSharedContextType()
Returns the type of the SMO shared context.

javax.xml.namespace.QName
getTransientContextType()
Returns the type of the SMO transient context.

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

    - getBodyType
javax.xml.namespace.QName getBodyType()
Returns the type of the SMO body.
Returns:the SMO body type
    - getCorrelationContextType
javax.xml.namespace.QName getCorrelationContextType()
Returns the type of the SMO correlation context
Returns:the SMO correlation context type
    - getTransientContextType
javax.xml.namespace.QName getTransientContextType()
Returns the type of the SMO transient context.
Returns:the SMO transient context type
    - getSharedContextType
javax.xml.namespace.QName getSharedContextType()
Returns the type of the SMO shared context.
Returns:the SMO shared context type