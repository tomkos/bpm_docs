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

## Interface Ticket

- All Superinterfaces:
java.io.Serializable

public interface Ticket
extends java.io.Serializable
Represents a correlation object that ties an SCA asynchronous request and response together.
 A ticket is long lived, can be persisted and re-used across threads and processes. A ticket also
 implements the equals and hashCode methods, which allow it to be used a a key.

- =========== FIELD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT

- ============ FIELD DETAIL ===========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values