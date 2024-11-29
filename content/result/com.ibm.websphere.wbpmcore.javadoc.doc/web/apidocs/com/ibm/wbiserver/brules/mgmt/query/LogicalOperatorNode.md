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

## Interface LogicalOperatorNode

- All Superinterfaces:
QueryNode, java.io.Serializable

All Known Subinterfaces:
AndNode, NotNode, OrNode

public interface LogicalOperatorNode
extends QueryNode, java.io.Serializable
This interface represents a logical operator (AND, OR, or NOT) in a query.

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

java.util.List<QueryNode>
getSubNodes()
Get the list of sub-nodes of this logical operator node.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getSubNodes
java.util.List<QueryNode> getSubNodes()
Get the list of sub-nodes of this logical operator node.  There may be one or more sub-nodes
 in the list.
Returns:The list of sub-nodes of this logical operator node.  The returned List
 object is unmodifiable.