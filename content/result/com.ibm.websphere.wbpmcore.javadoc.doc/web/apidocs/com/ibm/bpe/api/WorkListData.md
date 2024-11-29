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

## Interface WorkListData

- All Superinterfaces:
java.io.Serializable

Deprecated. 
As of version 6.0, replaced by the StoredQueryData object. The WorkList has been renamed to better
 express its meaning.
 

public interface WorkListData
extends java.io.Serializable
Accesses the properties of a worklist.
 
 A worklist is a query persistently stored on the database.
 It represents a set of items which have the same characteristics. These
 characteristics are specified by a filter. Additionally, sort criteria can be defined
 that are applied on the server, and a threshold to restrict the number of items
 transferred from the server to the client.
 
 Although work-list definitions are stored persistently, items contained in the worklist
 are assembled dynamically when they are queried. All worklists are publicly
 accessible.
Since:
5.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
Deprecated.
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getName()
Deprecated. 
Returns the name of the worklist.

java.lang.String
getOrderByClause()
Deprecated. 
Returns the sort criteria specified for the work-list definition.

java.lang.String
getSelectClause()
Deprecated. 
Returns the select clause specified for the work-list definition.

java.lang.Integer
getThreshold()
Deprecated. 
Returns the threshold specified for the work-list definition.

java.lang.String
getWhereClause()
Deprecated. 
Returns the filter specified for the work-list definition.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
Deprecated. 
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getName
java.lang.String getName()
Deprecated. 
Returns the name of the worklist.
    - getSelectClause
java.lang.String getSelectClause()
Deprecated. 
Returns the select clause specified for the work-list definition.
    - getWhereClause
java.lang.String getWhereClause()
Deprecated. 
Returns the filter specified for the work-list definition. If there is no filter,
 a null string is returned.
    - getOrderByClause
java.lang.String getOrderByClause()
Deprecated. 
Returns the sort criteria specified for the work-list definition. If there are no
 sort criteria, a null string is returned.
    - getThreshold
java.lang.Integer getThreshold()
Deprecated. 
Returns the threshold specified for the work-list definition. If there is no
 threshold defined, a null string is returned.