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

## Interface EntityResultSet

- All Superinterfaces:
java.io.Serializable

public interface EntityResultSet
extends java.io.Serializable
Provides the results of an entity-based query against a query table.
 
 The entity result set returns entities which match the filter criteria that have been specified
 in the query table and in the query request.
 The entities are sorted according to the sort criteria specified in the query request.
 If sort criteria are not specified, there is no intrinsic order of entities.
 The number of entities returned is restricted by the threshold and skipCount
 parameters of the query request.
 If a threshold is not specified, all entities are returned.
 
 An entity of the result set is defined through the selected attributes.
 The selected attributes reference query table attributes, such as attributes of tasks or process instances.
 If the query table requires instance-based authorization, work item information can also be referenced.
 
 Attribute values can be retrieved and casted to a type that is compatible with the attribute type.
Since:
7.0

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

java.util.List
getEntities()
Returns the entities that are contained in this result set.

EntityInfo
getEntityInfo()
Returns type information of the entities.

java.lang.String
getEntityTypeName()
Returns the type of entities that are returned as the result of the query.

java.util.Locale
getLocale()
Returns the locale that is calculated for the system variable $LOCALE.

java.lang.String
getQueryTableName()
Returns the name of the query table that is associated with this query result.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getQueryTableName
java.lang.String getQueryTableName()
Returns the name of the query table that is associated with this query result.
Returns:The name of the query table.
    - getEntityTypeName
java.lang.String getEntityTypeName()
Returns the type of entities that are returned as the result of the query.
Returns:The type of the entity.
    - getEntityInfo
EntityInfo getEntityInfo()
Returns type information of the entities.
Returns:The type information of the entity - see EntityInfo.
    - getEntities
java.util.List getEntities()
Returns the entities that are contained in this result set.
 Returns an empty list if there are no entities.
 
Returns:A list of Entity objects that are returned as the result of the query.
    - getLocale
java.util.Locale getLocale()
Returns the locale that is calculated for the system variable $LOCALE.
 
Returns:The locale that is set for $LOCALE.