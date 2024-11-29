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

## Interface OrNode

- All Superinterfaces:
LogicalOperatorNode, QueryNode, java.io.Serializable

public interface OrNode
extends LogicalOperatorNode, java.io.Serializable
This interface represents a logical OR operation for a query.  The result of performing the
 query represented by an OrNode is be the set of all
 business rule groups whose properties match at least one of the queries specified by the
 sub-nodes of the OrNode.
 Here is an example:
 
    // Find business rule groups where the value of property "Department" is like
    // "%Engineering%" or the value of property "Region" is not "Midwest".
    PropertyQueryNode leftNode = QueryNodeFactory.createPropertyQueryNode("Department", QueryOperator.LIKE, "%Engineering%");
    PropertyQueryNode rightNode = QueryNodeFactory.createPropertyQueryNode("Region", QueryOperator.NOT\_EQUAL, "Midwest");
    OrNode rootNode = QueryNodeFactory.createOrNode(leftNode, rightNode);

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