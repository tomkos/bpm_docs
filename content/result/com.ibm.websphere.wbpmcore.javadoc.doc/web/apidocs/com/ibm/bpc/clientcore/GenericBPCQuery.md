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

## Class GenericBPCQuery

- java.lang.Object
    - com.ibm.bpc.clientcore.GenericBPCQuery

- All Implemented Interfaces:
Query

public abstract class GenericBPCQuery
extends java.lang.Object
implements Query
GenericBPCQuery is an abstract base class used to issue queries against 
 the Business Flow Manager and the Human Task Manager.
 

 The class allows you to dynamically set the SELECT, WHERE and ORDER BY clauses as well
 as the Threshold.
 
 In addition, it provides static methods for common conversions that may be required to generate SQL queries.

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

protected java.lang.String
orderClause 

protected java.lang.String
selectClause 

protected java.lang.Integer
threshold 

protected java.lang.String
type 

protected java.lang.String
whereClause
    - Constructor Summary

Constructors 

Constructor and Description

GenericBPCQuery()
    - Method Summary Methods Modifier and Type Method and Description abstract java.util.List execute () Retrieves a list of application objects. java.lang.String getOrderClause () Returns the ORDER BY clause stored for the query. java.lang.String getSelectClause () Returns the SELECT clause stored for the query. java.lang.Integer getThreshold () Returns the Threshold value stored for the query. java.lang.String getType () Returns a type that identifies the objects returned by the Query.execute method. java.lang.String getWhereClause () Returns the WHERE clause stored for the query. void resetWhereClause () Resets the WHERE clause for the query. void setOrderClause (java.lang.String string) Sets the ORDER BY clause for the query. void setSelectClause (java.lang.String string) Sets the SELECT clause for the query. void setThreshold (int integer) Sets the Threshold value for the query. void setThreshold (java.lang.Integer integer) Sets the Threshold value for the query. void setType (java.lang.String value) Sets a type that identifies the objects returned by the Query.execute method. void setWhereClause (java.lang.String string) Sets the WHERE clause for the query.

### Method Summary

| Modifier and Type       | Method and Description                                                                                        |
|-------------------------|---------------------------------------------------------------------------------------------------------------|
| abstract java.util.List | execute() Retrieves a list of application objects.                                                            |
| java.lang.String        | getOrderClause() Returns the ORDER BY clause stored for the query.                                            |
| java.lang.String        | getSelectClause() Returns the SELECT clause stored for the query.                                             |
| java.lang.Integer       | getThreshold() Returns the Threshold value stored for the query.                                              |
| java.lang.String        | getType() Returns a type that identifies the objects returned by the Query.execute method.                    |
| java.lang.String        | getWhereClause() Returns the WHERE clause stored for the query.                                               |
| void                    | resetWhereClause() Resets the WHERE clause for the query.                                                     |
| void                    | setOrderClause(java.lang.String string) Sets the ORDER BY clause for the query.                               |
| void                    | setSelectClause(java.lang.String string) Sets the SELECT clause for the query.                                |
| void                    | setThreshold(int integer) Sets the Threshold value for the query.                                             |
| void                    | setThreshold(java.lang.Integer integer) Sets the Threshold value for the query.                               |
| void                    | setType(java.lang.String value) Sets a type that identifies the objects returned by the Query.execute method. |
| void                    | setWhereClause(java.lang.String string) Sets the WHERE clause for the query.                                  |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait