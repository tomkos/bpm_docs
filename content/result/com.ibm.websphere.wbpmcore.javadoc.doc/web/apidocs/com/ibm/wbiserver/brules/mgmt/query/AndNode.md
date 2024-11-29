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

## Interface AndNode

- All Superinterfaces:
LogicalOperatorNode, QueryNode, java.io.Serializable

public interface AndNode
extends LogicalOperatorNode, java.io.Serializable
This interface represents a logical AND operation for a query.  The result of performing
 the query represented by an AndNode is be the set of all
 objects whose properties match all of the queries specified by all of the
 sub-nodes of the AndNode.
 Here is an example:
 
    // Find business rule groups where the value of property "Department" is "Marketing" and
    // the value of property "Region" is "Midwest".
    PropertyQueryNode leftNode = QueryNodeFactory.createPropertyQueryNode("Department", QueryOperator.EQUAL, "Marketing");
    PropertyQueryNode rightNode = QueryNodeFactory.createPropertyQueryNode("Region", QueryOperator.EQUAL, "Midwest");
    AndNode rootNode = QueryNodeFactory.createAndNode(leftNode, rightNode);

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