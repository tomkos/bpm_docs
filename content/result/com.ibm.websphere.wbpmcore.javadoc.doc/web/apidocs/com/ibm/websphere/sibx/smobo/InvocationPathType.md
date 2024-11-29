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

## Interface InvocationPathType

- public interface InvocationPathType A representation of the model object 'Invocation Path Type '. The following features are supported:

```
public interface InvocationPathType
```

The following features are supported:
 
Primitive

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

java.util.List<PrimitiveType>
getPrimitive()
Returns the value of the 'Primitive' containment reference list.

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

    - getPrimitive
java.util.List<PrimitiveType> getPrimitive()
Returns the value of the 'Primitive' containment reference list.
 The list contents are of type PrimitiveType.
 
 This is a list of the primitives involved in processing the message up to (and
 including) the failing primitive.  Each entry will have a triplet consisting of
 an in terminal, a named primitive (named after the primitives' display name) and
 an out terminal.  With the exception that the point of failure will not name an
 out terminal.
 
Returns:the value of the 'Primitive' containment reference list.