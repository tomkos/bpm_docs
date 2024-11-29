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

## Interface EnumerationConstraint

- All Superinterfaces:
Constraint, java.io.Serializable

public interface EnumerationConstraint
extends Constraint
This interface represents an enumeration constraint.  This is a list of discrete values that are
 the only valid values for a particular parameter.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.util.List<EnumerationItem>
getEnumerationItems()
Get the list of enumeration items for this enumeration constraint.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getEnumerationItems
java.util.List<EnumerationItem> getEnumerationItems()
Get the list of enumeration items for this enumeration constraint.  Each enumeration item
 defines one value that is valid for the parameter.  Together, the list of enumeration
 items defines all valid values.
Returns:A List of EnumerationItems for this enumeration constraint.
 The returned List is unmodifiable.