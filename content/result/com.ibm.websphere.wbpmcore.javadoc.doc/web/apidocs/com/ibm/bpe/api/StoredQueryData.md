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

## Interface StoredQueryData

- All Superinterfaces:
java.io.Serializable

public interface StoredQueryData
extends java.io.Serializable
Accesses the properties of a query stored persistently. The stored query can be
 public, that is, be available for everybody's usage or private, that is, be available
 for the owner of the stored query only.
 
 A stored query represents a set of items which have the same characteristics. These
 characteristics are specified by a filter.
 To allow for the re-use of stored queries, parameters can be specified in the where-clause
 so that, for example, the owner of an activity or task can be specified when the stored query is executed.
 
 Additionally, sort criteria can be defined that are applied on the server,
 and a threshold to restrict the number of items transferred from the server to the client.
 
 Although these definitions are stored persistently, qualifying items
 are assembled dynamically when they are queried.
 
Since:
6.0.2 - introduced in 6.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
KIND\_PRIVATE
States that the stored query is private.

static int
KIND\_PUBLIC
States that the stored query is public.
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getClientType()
Returns a user-defined client type that names the creator of the stored
 query.

java.lang.String
getCreator()
Returns the ID of the user that created the stored query.

int
getKind()
States whether the stored query is a public query available to everybody or
 a private query available only to its owner.

java.lang.String
getName()
Returns the name of the stored query.

java.lang.String
getOrderByClause()
Returns the sort criteria specified for the stored query definition.

java.lang.String
getOwner()
Returns the owner of the stored query when the stored query is for private
 usage.

java.lang.String
getSelectClause()
Returns the select clause specified for the stored query definition.

java.util.List
getStoredQueryProperties()
Returns a list of user-defined properties for the stored query definition - refer
 to StoredQueryProperty.

java.lang.Integer
getThreshold()
Returns the threshold specified for the stored query definition.

java.lang.String
getWhereClause()
Returns the filter specified for the stored query definition.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- KIND\_PRIVATE
static final int KIND\_PRIVATE
States that the stored query is private.
See Also:Constant Field Values

- KIND\_PUBLIC
static final int KIND\_PUBLIC
States that the stored query is public.
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getName
java.lang.String getName()
Returns the name of the stored query.
    - getSelectClause
java.lang.String getSelectClause()
Returns the select clause specified for the stored query definition.
    - getWhereClause
java.lang.String getWhereClause()
Returns the filter specified for the stored query definition. If there is no filter,
 a null string is returned.
    - getOrderByClause
java.lang.String getOrderByClause()
Returns the sort criteria specified for the stored query definition. If there are no
 sort criteria, a null string is returned.
    - getThreshold
java.lang.Integer getThreshold()
Returns the threshold specified for the stored query definition. If there is no
 threshold defined, a null string is returned.
    - getStoredQueryProperties
java.util.List getStoredQueryProperties()
                                        throws WorkItemManagerException
Returns a list of user-defined properties for the stored query definition - refer
 to StoredQueryProperty. If there are
 no properties, an empty list is returned.
Throws:
WorkItemManagerException
    - getClientType
java.lang.String getClientType()
Returns a user-defined client type that names the creator of the stored
 query. If there is no client type, a null string is returned.
    - getKind
int getKind()
States whether the stored query is a public query available to everybody or
 a private query available only to its owner.
 
 Returns either KIND\_PUBLIC or KIND\_PRIVATE.
    - getOwner
java.lang.String getOwner()
Returns the owner of the stored query when the stored query is for private
 usage. Returns null when the stored query is available for public usage.
    - getCreator
java.lang.String getCreator()
Returns the ID of the user that created the stored query. If the creator is unknown,
 null is returned.