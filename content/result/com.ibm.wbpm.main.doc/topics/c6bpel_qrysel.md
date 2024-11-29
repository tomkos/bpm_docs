<!-- image -->

# Select clause

The select clause describes the query result. It specifies a list
of names that identify the object properties (columns of the result)
to return. Its syntax is similar to the syntax of an SQL SELECT clause;
use commas to separate parts of the clause. Each part of the clause
must specify a column from one of the predefined views. The columns
must be fully specified by view name and column name. The columns
returned in the QueryResultSet object appear in the same order as
the columns specified in the select clause.

The select clause does not support SQL aggregation functions, such
as AVG(), SUM(), MIN(), or MAX().

To select the properties of multiple name-value pairs, such as
custom properties and properties of variables that can be queried,
add a one-digit counter to the view name. This counter can take the
values 1 through 9.

## Examples of select clauses

- WORK\_ITEM.OBJECT\_TYPE, WORK\_ITEM.REASON: Gets the object types of the
associated objects and the assignment reasons for the work items.
- DISTINCT WORK\_ITEM.OBJECT\_ID: Gets all of the IDs of objects, without
duplicates, for which the caller has a work item.
- ACTIVITY.TEMPLATE\_NAME, WORK\_ITEM.REASON: Gets the names of the activities the
caller has work items for and their assignment reasons.
- ACTIVITY.STATE, PROCESS\_INSTANCE.STARTER: Gets the states of the activities and
the starters of their associated process instances.
- DISTINCT TASK.TKIID, TASK.NAME: Gets all of the IDs and names of tasks, without
duplicates, for which the caller has a work item.
- TASK\_CPROP1.STRING\_VALUE, TASK\_CPROP2.STRING\_VALUE: Gets the values of the
custom properties that are specified further in the where clause.
- QUERY\_PROPERTY1.STRING\_VALUE, QUERY\_PROPERTY2.INT\_VALUE: Gets the values of the
properties of variables that can be queried. These parts are specified further in the where
clause.
- COUNT( DISTINCT TASK.TKIID: Counts the number of work items for unique tasks
that satisfy the where clause.