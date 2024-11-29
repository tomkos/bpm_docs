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

## Interface ExecutableQuery

- public interface ExecutableQuery
Interface for customizable queries.
 
 This interface supports implementations that use pre-defined queries. In contrast
 to stored queries, the queries can be customized before calling the query() method.
 
 The get methods of this interface are called by the HumanTaskManagerDelegate when the query
 is set up.
 The setQueryResultSet() method of this interface is called to store the result of the query.
Since:
5.1

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
getOrderByClause()
Retrieves the orderBy-clause of the query to be executed.

java.lang.String
getSelectClause()
Retrieves the select-clause of the query to be executed.

java.lang.Integer
getThreshold()
Retrieves the threshold of the query to be executed.

java.util.TimeZone
getTimezone()
Retrieves the timezone that is to be used for time values in the where-clause
 and in the query result set.

java.lang.String
getWhereClause()
Retrieves the where-clause of the query to be executed.

void
setQueryResultSet(QueryResultSet queryResultSet)
Sets the result of the query.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getSelectClause
java.lang.String getSelectClause()
Retrieves the select-clause of the query to be executed.
 
Returns:String
    The select-clause; must not be null.
    - getWhereClause
java.lang.String getWhereClause()
Retrieves the where-clause of the query to be executed.
 
Returns:String
    The where-clause. Must return null if there is no where-clause.
    - getOrderByClause
java.lang.String getOrderByClause()
Retrieves the orderBy-clause of the query to be executed.
 
Returns:String
    The orderBy-clause. Must return null if there is no orderBy-clause.
    - getThreshold
java.lang.Integer getThreshold()
Retrieves the threshold of the query to be executed.
 
Returns:Integer
    The threshold. Must return null if there is no threshold.
    - getTimezone
java.util.TimeZone getTimezone()
Retrieves the timezone that is to be used for time values in the where-clause
 and in the query result set.
 
Returns:TimeZone
    The time zone. Must return null if there are no time values or if time values are
    provided in UTC.
    - setQueryResultSet
void setQueryResultSet(QueryResultSet queryResultSet)
Sets the result of the query.
 
Parameters:queryResultSet - The result of the query as provided by the Human Task Manager API.