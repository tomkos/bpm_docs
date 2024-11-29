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

## Interface PropertyIsDefinedQueryNode

- All Superinterfaces:
QueryNode, java.io.Serializable

public interface PropertyIsDefinedQueryNode
extends QueryNode, java.io.Serializable
This is an interface for querying for business rule groups that have a particular
 property defined, regardless of what the value of that property is.
 Here is an example:
 
    // Find business rule groups that have property "Department" defined to be some
    // value.
    PropertyIsDefinedQueryNode node = QueryNodeFactory.createPropertyIsDefinedQueryNode("Department");
 

 A PropertyIsDefinedQueryNode can be used by itself to form a query, if the query 
 is using a single property, or it may be combined with other QueryNode objects 
 using the logical operator nodes AndNode, OrNode, and 
 NotNode to form more complicated queries.
 
 Note that the property name specified for the PropertyIsDefinedQueryNode
 cannot make use of any wildcard characters such as '%' or '\_'.  Only an exact match on the
 property name is allowed.

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
getPropertyName()
Get the name of the property that is to be queried by this node.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getPropertyName
java.lang.String getPropertyName()
Get the name of the property that is to be queried by this node.
Returns:The name of the property that is to be queried by this node.