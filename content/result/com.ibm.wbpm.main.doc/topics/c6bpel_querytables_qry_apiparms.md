<!-- image -->

# Query table API parameters

You use query table API methods to retrieve content when
you run queries against a query table in Business Process Choreographer.

| Parameter             | Optional   | Type and description                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Query table name      | No         | java.lang.String The unique name of the query table.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Filter options        | Yes        | com.ibm.bpe.api.FilterOptions if the Business Flow Manager Enterprise JavaBeans is used, or com.ibm.task.api.FilterOptions if the Human Task Manager Enterprise JavaBeans is used.Options which can be used to define the query. For example, a query threshold is set on this parameter to limit the number of results returned.                                                                                                                                                           |
| Authorization options | Yes        | com.ibm.bpe.api.AuthorizationOptions or com.ibm.bpe.api.AdminAuthorizationOptions if the Business Flow Manager Enterprise JavaBeans is used. com.ibm.task.api.AuthorizationOptions or com.ibm.task.api.AdminAuthorizationOptions if the Human Task Manager Enterprise JavaBeans is used.Authorization can be further constrained if instance-based authorization is used. For query tables which require role-based authorization, an instance of AdminAuthorizationOptions must be passed. |
| Parameters            | Yes        | A java.util.List of com.ibm.bpe.api.Parameter if the Business Flow Manager Enterprise JavaBeans is used or com.ibm.task.api.Parameter if the Human Task Manager Enterprise JavaBeans is used.This parameter is used to pass user parameters, which are specified in a filter or selection criterion on a composite query table.                                                                                                                                                             |

A query is run on one specific query table only. The relationship between multiple query tables
is defined with composite query tables. In terms of the query API (as distinct from the query table
API), this corresponds to database views.

You specify filters and selection criteria in expressions during query table development using
the Query Table Builder. For more information, refer to the documentation topic about composite
query tables and the topic about filter and search criteria of query tables. For information about
the Query Table Builder, see the SupportPacs site. Look for PA71 WebSphere Process Server - Query
Table Builder. To access the link, see the related references section of this topic.p

- Query table name

When you run a query on a query table in Business Process Choreographer, the query table name is passed as an input parameter to the methods of the query table API.
- Filter options for query tables

When you run a query on a query table in Business Process Choreographer, filter options can be passed as input parameters to the methods of the query table API.
- Authorization options for the query table API

When you run a query on a query table in Business Process Choreographer, authorization options can be passed as input parameters to the methods of the query table API.
- Parameters

When you run a query on a query table in Business Process Choreographer, you can pass user parameters as input parameters to the methods of the query table API. In query table definitions, you can specify parameters in filters on the primary query table, on the authorization, and on the query table. Parameters can also be specified in selection criteria on attached query tables.