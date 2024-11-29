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

## Class QueryNodeFactory

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.query.QueryNodeFactory

- public class QueryNodeFactory
extends java.lang.Object
This is a factory class for creating different kinds of query nodes.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static java.lang.String
PROPERTY\_NAME\_\_DISPLAY\_NAME
The name of the system-defined property containing the display name of the object.

static java.lang.String
PROPERTY\_NAME\_\_NAME
The name of the system-defined property containing the name of the object.

static java.lang.String
PROPERTY\_NAME\_\_TARGET\_NAME\_SPACE
The name of the system-defined property containing the target namespace of the object.

static java.lang.String
PROPERTY\_NAME\_\_VERSION
The name of the system-defined property containing the version of the object.
    - Method Summary Methods Modifier and Type Method and Description static AndNode createAndNode (java.util.List<QueryNode > nodes) Construct an AndNode with an arbitrary number of sub-nodes. static AndNode createAndNode (QueryNode [] nodes) Construct an AndNode with an arbitrary number of sub-nodes. static AndNode createAndNode (QueryNode leftNode, QueryNode rightNode) Construct an AndNode with two sub-nodes. static NotNode createNotNode (QueryNode subNode) Construct a NotNode . static OrNode createOrNode (java.util.List<QueryNode > nodes) Construct an OrNode with an arbitrary number of sub-nodes. static OrNode createOrNode (QueryNode [] nodes) Construct an OrNode with an arbitrary number of sub-nodes. static OrNode createOrNode (QueryNode leftNode, QueryNode rightNode) Construct an OrNode with two sub-nodes. static PropertyIsDefinedQueryNode createPropertyIsDefinedQueryNode (java.lang.String propertyName) Create PropertyIsDefinedQueryNode object. static PropertyQueryNode createPropertyQueryNode (java.lang.String propertyName, QueryOperator queryOperator, java.lang.String propertyValue) Create a PropertyQueryNode object.

### Method Summary

| Modifier and Type                 | Method and Description                                                                                                                                                                               |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static AndNode                    | createAndNode(java.util.List<QueryNode> nodes) Construct an AndNode with an arbitrary number of sub-nodes.                                                                                           |
| static AndNode                    | createAndNode(QueryNode[] nodes) Construct an AndNode with an arbitrary number of sub-nodes.                                                                                                         |
| static AndNode                    | createAndNode(QueryNode leftNode,              QueryNode rightNode) Construct an AndNode with two sub-nodes.                                                                                         |
| static NotNode                    | createNotNode(QueryNode subNode) Construct a NotNode.                                                                                                                                                |
| static OrNode                     | createOrNode(java.util.List<QueryNode> nodes) Construct an OrNode with an arbitrary number of sub-nodes.                                                                                             |
| static OrNode                     | createOrNode(QueryNode[] nodes) Construct an OrNode with an arbitrary number of sub-nodes.                                                                                                           |
| static OrNode                     | createOrNode(QueryNode leftNode,             QueryNode rightNode) Construct an OrNode with two sub-nodes.                                                                                            |
| static PropertyIsDefinedQueryNode | createPropertyIsDefinedQueryNode(java.lang.String propertyName) Create PropertyIsDefinedQueryNode object.                                                                                            |
| static PropertyQueryNode          | createPropertyQueryNode(java.lang.String propertyName,                        QueryOperator queryOperator,                        java.lang.String propertyValue) Create a PropertyQueryNode object. |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait