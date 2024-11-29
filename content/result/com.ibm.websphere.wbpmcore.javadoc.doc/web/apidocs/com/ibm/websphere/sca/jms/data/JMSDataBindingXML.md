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

## Interface JMSDataBindingXML

- All Known Implementing Classes:
JMSDataBindingImplXML

public interface JMSDataBindingXML
A DataBinding represents the mapping between a native data
 format and an SDO DataObject, and vice-versa. 
 This interface provides methods to control how doc-literal 
 messages will be treated by the runtime.
 A JMSDataBinding can implement this interface if the native
 data of a doc-literal message can be wrapped.

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

boolean
outputWrappedXML()
Used by the runtime to determine whether a doc-lit wrapped input type
 should be unwrapped before passing it to the data binding, and
 whether to doc-lit wrap the output type.

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

    - outputWrappedXML
boolean outputWrappedXML()
Used by the runtime to determine whether a doc-lit wrapped input type
 should be unwrapped before passing it to the data binding, and
 whether to doc-lit wrap the output type.
Returns:A boolean specifying either wrapped XML or unwrapped XML
                        (false implies unwrapped)