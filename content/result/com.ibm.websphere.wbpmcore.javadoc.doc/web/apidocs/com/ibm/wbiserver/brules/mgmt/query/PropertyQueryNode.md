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

## Interface PropertyQueryNode

- All Superinterfaces: QueryNode , java.io.Serializable public interface PropertyQueryNode extends QueryNode , java.io.Serializable This is an interface for querying properties associated with business rule groups. Each instance of this class contains the following: Here are some examples: // Find business rule groups where the value of property "Department" exactly // matches the string "Marketing". PropertyQueryNode propNode = QueryNodeFactory.createPropertyQueryNode("Department", QueryOperator.EQUAL, "Marketing"); // Find business rule groups where the value of property "Department" is like the // string "%Engineering%". PropertyQueryNode propNode = QueryNodeFactory.createPropertyQueryNode("Department", QueryOperator.LIKE, "%Engineering%"); // Find business rule groups where the value of property "Department" is not like the // string "%Engineering%". PropertyQueryNode propNode = QueryNodeFactory.createPropertyQueryNode("Department", QueryOperator.NOT\_LIKE, "%Engineering%"); A PropertyQueryNode can be used by itself to form a query, if the query is using a single property, or it may be combined with other QueryNode objects using the logical operator nodes AndNode , OrNode , and NotNode to form more complicated queries. Special property names are defined to allow queries to be performed on the target name space, name, and display name of an artifact (for example, a business rule group, ruleset, or decision table). These names are defined as constants in the Property interface: PROPERTY\_NAME\_\_TARGET\_NAME\_SPACE , PROPERTY\_NAME\_\_NAME , and PROPERTY\_NAME\_\_DISPLAY\_NAME . Note that if a particular business rule group does not have the property in question defined, it will not even be considered when the query is performed. This means that it will never be returned by a PropertyQueryNode query that specifies that property. For example, consider three business rule groups and a property named "Department". Two of the business rule groups have a "Department" property defined and the third one does not: BRG1 Department = "Marketing" BRG2 Department = "Engineering" BRG3 No department property If you perform a query for all business rule groups with the "Department" property equal to "Marketing", then you will get BRG1. If you perform a query for all business rule groups with the "Department" property not equal to "Marketing", you will get BRG2 but you will not get BRG3. Since BRG3 does not have the "Department" property defined, it will not even be considered in the query. If you want to perform a query that would also return BRG3, you can use the PropertyIsDefinedQueryNode and the NotNode to query for all business rule groups that do not have the "Department" property defined. Then use an OrNode to combine that query with a query for all business rule groups with the "Department" property not equal to "Marketing".

```
public interface PropertyQueryNode
extends QueryNode, java.io.Serializable
```

    1. Property name - the name of the property whose value is to be queried by this
 node.  Note that wildcards such as '%' and '\_' are not allowed in the property name.
 The property name must be an exact match to the name stored in the business rule group
 artifacts.
 Property value - a string containing the value that is to be matched against.
 If the query operator indicates that a "like" query is being performed, then this string
 can contain the wildcard characters '%' (matches 0 or more characters) and '\_' (matches a
 single character).  These wildcards follow SQL syntax.  If you want to search for a value
 containing the '%' or '\_' characters, you can escape these characters using the '\' 
 (backslash) character.  If the '\' character itself is specified in the value, it must also
 have an escape character in front of it, in other words "\\".  A single '\' character that
 is not followed by a '%', a '\_', or another '\' is not allowed and will cause an exception.  
 Note that, since the '\' character is also the escape character for Java strings, when a 
 query value is specified as a Java string the '\' characters must be doubled.  For example, 
 to specify a literal '%' character in the query value you must specify "\\%" in the Java 
 string. 
 Query operator - the operator to be used in this query.  This can be used to indicate
 whether an exact match is being requested or if a "like" query is being performed using
 wildcards.

Here are some examples:
 
    // Find business rule groups where the value of property "Department" exactly 
    // matches the string "Marketing".
    PropertyQueryNode propNode = QueryNodeFactory.createPropertyQueryNode("Department", QueryOperator.EQUAL, "Marketing");
 

    // Find business rule groups where the value of property "Department" is like the
    // string "%Engineering%".
    PropertyQueryNode propNode = QueryNodeFactory.createPropertyQueryNode("Department", QueryOperator.LIKE, "%Engineering%");
 

    // Find business rule groups where the value of property "Department" is not like the
    // string "%Engineering%".
    PropertyQueryNode propNode = QueryNodeFactory.createPropertyQueryNode("Department", QueryOperator.NOT\_LIKE, "%Engineering%");
 

 A PropertyQueryNode can be used by itself to form a query, if the query is using
 a single property, or it may be combined with other QueryNode objects using
 the logical operator nodes AndNode, OrNode, and NotNode
 to form more complicated queries.
 
 Special property names are defined to allow queries to be performed on the target name
 space, name, and display name of an artifact (for example, a business rule group, ruleset, 
 or decision table).  These names are defined as constants in the Property 
 interface:
 PROPERTY\_NAME\_\_TARGET\_NAME\_SPACE,
 PROPERTY\_NAME\_\_NAME, and
 PROPERTY\_NAME\_\_DISPLAY\_NAME.
 
 Note that if a particular business rule group does not have the
 property in question defined, it will not even be considered when the query is performed.
 This means that it will never be returned by a PropertyQueryNode query that
 specifies that property.  For example, consider three business rule groups and a property
 named "Department".  Two of the business rule groups have a "Department" property defined
 and the third one does not:
 
 
     BRG1        Department = "Marketing"
     BRG2        Department = "Engineering"
     BRG3        No department property
 
 
 If you perform a query for all business rule groups with the "Department" property equal
 to "Marketing", then you will get BRG1.  If you perform a query for all business rule
 groups with the "Department" property not equal to "Marketing", you will get BRG2 but 
 you will not get BRG3.  Since BRG3 does not have the "Department" property defined, it
 will not even be considered in the query.  If you want to perform a query that would
 also return BRG3, you can use the PropertyIsDefinedQueryNode and the
 NotNode to query for all business rule groups that do not have the 
 "Department" property defined.  Then use an OrNode to combine that query
 with a query for all business rule groups with the "Department" property not equal to
 "Marketing".

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
Get the name of the property whose value is to be queried by this node.

java.lang.String
getPropertyValue()
Get the value that is to be queried for for this property.

QueryOperator
getQueryOperator()
Get the operator for this query.

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
Get the name of the property whose value is to be queried by this node.
Returns:The name of the property whose value is to be queried by this node.
    - getQueryOperator
QueryOperator getQueryOperator()
Get the operator for this query.
Returns:The operator for this query.
    - getPropertyValue
java.lang.String getPropertyValue()
Get the value that is to be queried for for this property.
Returns:The value that is to be queried for for this property.