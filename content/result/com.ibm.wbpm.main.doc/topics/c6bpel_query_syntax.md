<!-- image -->

# Syntax of the API query method

The syntax of the query depends on the object type. The following
table shows the syntax for each of the different object types.

| Object                                 | Syntax                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Process template                       | ProcessTemplateData[] queryProcessTemplates                         (java.lang.String whereClause,                         java.lang.String orderByClause,                         java.lang.Integer threshold,                         java.util.TimeZone timezone);                                                    |
| Task template                          | TaskTemplate[]        queryTaskTemplates                         (java.lang.String whereClause,                         java.lang.String orderByClause,                         java.lang.Integer threshold,                         java.util.TimeZone timezone);                                                       |
| Business-process and task-related data | QueryResultSet query (java.lang.String selectClause,                       java.lang.String whereClause,                       java.lang.String orderByClause,                       java.lang.Integer skipTuples                       java.lang.Integer threshold,                       java.util.TimeZone timezone); |

- Select clause

The select clause in the query function identifies the object properties that are to be returned by a query.
- Where clause

The where clause in the query function describes the filter criteria to apply to the query domain.
- Order-by clause

The order-by clause in the query function specifies the sort criteria for the query result set.
- Skip-tuples parameter

The skip-tuples parameter specifies the number of query-result-set tuples from the beginning of the query result set that are to be ignored and not to be returned to the caller in the query result set.
- Threshold parameter

The threshold parameter in the query function restricts the number of objects returned from the server to the client in the query result set.
- Timezone parameter

The time-zone parameter in the query function defines the time zone for time-stamp constants in the query.
- Filtering data using variables in queries

A query result returns the objects that match the query criteria. You might want to filter these results on the values of variables.
- Query results

A query result set contains the results of a Business Process Choreographer API query.