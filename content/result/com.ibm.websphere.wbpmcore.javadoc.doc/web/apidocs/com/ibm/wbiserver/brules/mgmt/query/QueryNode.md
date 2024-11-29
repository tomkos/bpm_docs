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

## Interface QueryNode

- All Superinterfaces: java.io.Serializable All Known Subinterfaces: AndNode , LogicalOperatorNode , NotNode , OrNode , PropertyIsDefinedQueryNode , PropertyQueryNode public interface QueryNode extends java.io.Serializable This interface represents part of a query based on properties. There are two types of objects in the business rule management API that have properties: business rule groups and business rules. QueryNodes can be combined into a tree to specify a query based on properties. This query will be scoped to either business rule groups or business rules depending on the method that is used to process the query. There are several types of query nodes: To perform a query, the user builds up a tree of QueryNode objects that represent the query to be performed. This tree is then passed to method getBRGsByProperties on class BusinessRuleManager . This method will search for business rule groups installed on the server that match the query specified in the given QueryNode and its sub-nodes. Subclasses of the QueryNode interface are provided to perform queries on individual properties associated with the business rule groups as well as to logically combine (AND, OR, NOT) individual property queries. There is a factory class, QueryNodeFactory , that can be used to create query nodes. Here are some examples. To find all business rule groups where the value of property "Property1" is "ValueA", do the following: // Find business rule groups where the value of property "Property1" is "ValueA". PropertyQueryNode propertyNode = QueryNodeFactory.createPropertyQueryNode("Property1", QueryOperator.EQUAL, "ValueA"); List<BusinessRuleGroup> result = BusinessRuleManager.getBRGsByProperties(propertyNode, 0, 0); To find all business rule groups where the value of property "Department" is "Marketing" and the value of property "Region" is "Midwest", do the following: // Find business rule groups where the value of property "Department" is "Marketing" and // the value of property "Region" is "Midwest". PropertyQueryNode leftNode = QueryNodeFactory.createPropertyQueryNode("Department", QueryOperator.EQUAL, "Marketing"); PropertyQueryNode rightNode = QueryNodeFactory.createPropertyQueryNode("Region", QueryOperator.EQUAL, "Midwest"); AndNode rootNode = QueryNodeFactory.createAndNode(leftNode, rightNode); List<BusinessRuleGroup> result = BusinessRuleManager.getBRGsByProperties(rootNode, 0, 0); To find all business rule groups where the value of property "Department" is like "%Engineering%" or the value of property "Region" is not "Midwest", do the following: // Find business rule groups where the value of property "Department" is like // "%Engineering%" or the value of property "Region" is not "Midwest". PropertyQueryNode leftNode = QueryNodeFactory.createPropertyQueryNode("Department", QueryOperator.LIKE, "%Engineering%"); PropertyQueryNode rightNode = QueryNodeFactory.createPropertyQueryNode("Region", QueryOperator.NOT\_EQUAL, "Midwest"); OrNode rootNode = QueryNodeFactory.createOrNode(leftNode, rightNode); List<BusinessRuleGroup> result = BusinessRuleManager.getBRGsByProperties(rootNode, 0, 0);

```
public interface QueryNode
extends java.io.Serializable
```

There are several types of query nodes:
 
A comparison, such as Property1 = 'isEligible'.
 Checking for the existence of a property with a given name.  For example, all objects
 that have Property1 defined.
 A logical operation: AND, OR, and NOT.
 

 To perform a query, the user builds up a tree of QueryNode objects that
 represent the query to be performed.  This tree is then passed to method
 getBRGsByProperties 
 on class
 BusinessRuleManager.  This method will search for business
 rule groups installed on the server that match the query specified in the given 
 QueryNode and its sub-nodes.  Subclasses of the QueryNode interface 
 are provided to perform queries on individual properties associated with the business rule
 groups as well as to logically combine (AND, OR, NOT) individual property queries.  There is
 a factory class, QueryNodeFactory, that can be 
 used to create query nodes.
 
 Here are some examples.  To find all business rule groups where the value of property 
 "Property1" is "ValueA", do the following:
 
    // Find business rule groups where the value of property "Property1" is "ValueA".
    PropertyQueryNode propertyNode = QueryNodeFactory.createPropertyQueryNode("Property1", QueryOperator.EQUAL, "ValueA");
    List<BusinessRuleGroup> result = BusinessRuleManager.getBRGsByProperties(propertyNode, 0, 0);
 

 To find all business rule groups where the value of property "Department" is "Marketing" and
 the value of property "Region" is "Midwest", do the following:
 
    // Find business rule groups where the value of property "Department" is "Marketing" and
    // the value of property "Region" is "Midwest".
    PropertyQueryNode leftNode = QueryNodeFactory.createPropertyQueryNode("Department", QueryOperator.EQUAL, "Marketing");
    PropertyQueryNode rightNode = QueryNodeFactory.createPropertyQueryNode("Region", QueryOperator.EQUAL, "Midwest");
    AndNode rootNode = QueryNodeFactory.createAndNode(leftNode, rightNode);
    List<BusinessRuleGroup> result = BusinessRuleManager.getBRGsByProperties(rootNode, 0, 0);
 
 
 To find all business rule groups where the value of property "Department" is like
 "%Engineering%" or the value of property "Region" is not "Midwest", do the following:
 
    // Find business rule groups where the value of property "Department" is like
    // "%Engineering%" or the value of property "Region" is not "Midwest".
    PropertyQueryNode leftNode = QueryNodeFactory.createPropertyQueryNode("Department", QueryOperator.LIKE, "%Engineering%");
    PropertyQueryNode rightNode = QueryNodeFactory.createPropertyQueryNode("Region", QueryOperator.NOT\_EQUAL, "Midwest");
    OrNode rootNode = QueryNodeFactory.createOrNode(leftNode, rightNode);
    List<BusinessRuleGroup> result = BusinessRuleManager.getBRGsByProperties(rootNode, 0, 0);

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