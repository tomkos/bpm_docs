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

## Interface AuthorizationInfo

- All Superinterfaces:
java.io.Serializable

public interface AuthorizationInfo
extends java.io.Serializable
Provides authorizations specifications of a query table.
Since:
7.0

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

boolean
areGroupsUsed()
Returns whether group work items are considered.

boolean
areIndividualsUsed()
Returns whether individual work items are considered.

boolean
areInheritedWorkItemsUsed()
Returns whether inherited work items are considered.

AuthorizationType
getType()
Returns the authorization type that is used.

boolean
isEverybodyUsed()
Returns whether everybody work items are considered.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - isEverybodyUsed
boolean isEverybodyUsed()
Returns whether everybody work items are considered.
Returns:Specifies whether everybody work items are to be used for a query.
    - areIndividualsUsed
boolean areIndividualsUsed()
Returns whether individual work items are considered.
Returns:Specifies whether individual work items are to be used for a query.
    - areGroupsUsed
boolean areGroupsUsed()
Returns whether group work items are considered.
Returns:Specifies whether group work items are to be used for a query.
    - areInheritedWorkItemsUsed
boolean areInheritedWorkItemsUsed()
Returns whether inherited work items are considered.
Returns:Specifies whether inherited work items are to be used for a query.
    - getType
AuthorizationType getType()
Returns the authorization type that is used.
Returns:The authorization type that is used when a query is run.