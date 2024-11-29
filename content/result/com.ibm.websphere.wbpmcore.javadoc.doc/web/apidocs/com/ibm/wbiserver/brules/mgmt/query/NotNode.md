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

## Interface NotNode

- All Superinterfaces:
LogicalOperatorNode, QueryNode, java.io.Serializable

public interface NotNode
extends LogicalOperatorNode, java.io.Serializable
This interface represents a logical NOT operation for a query.  The logical NOT operation can
 be applied to any of the other query nodes.  The result of calling the 
 performQuery method on a NotNode is the set of all business rule
 groups whose properties do not match the query specified by the sub-node of the 
 NotNode.
 Here is an example:
 
    // Find all business rule groups where the value of property "Region" is not equal to
    // "East".
    PropertyQueryNode propertyNode = QueryNodeFactory.createPropertyQueryNode("Region", QueryOperator.EQUAL, "East");
    NotNode notNode = QueryNodeFactory.createNotNode(propertyNode);
 
 Note that this is the same as doing the following:
 
    PropertyQueryNode propertyNode = QueryNodeFactory.createPropertyQueryNode("Region", QueryOperator.NOT\_EQUAL, "East");

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

### Method Summary

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.query.LogicalOperatorNode
getSubNodes