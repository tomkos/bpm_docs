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

## Interface BranchTemplateData

- All Superinterfaces:
java.io.Serializable

public interface BranchTemplateData
extends java.io.Serializable
Accesses the properties of a branch that follows a switch activity.
 
Since:
6.2

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

java.lang.String
getCondition()
Returns the XPATH condition that is associated with the branch.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getCondition
java.lang.String getCondition()
Returns the XPATH condition that is associated with the branch.
 For Java conditions, null is returned.