<!-- image -->

# Queries on BPEL process and task data

The EJB query interfaces, query API, and query table API, are available
with Business Process Choreographer.

Depending on the clients that access process or task related data, one or more of the interfaces
can be the appropriate choice. REST and web services APIs are available in Business Process
Choreographer for querying task and process list data. However, for high volume process list and
task list queries, use the Business Process Choreographer EJB query table API or REST query table
API for performance reasons.

- Comparison of the programming interfaces for retrieving process and task data

Business Process Choreographer provides a query table API and a query API for retrieving process and task data. Each of these interfaces has different characteristics.
- Query tables in Business Process Choreographer

Query tables support task and process list queries on data that is contained in the Business Process Choreographer database schema. This includes human task data and BPEL process data that is managed by Business Process Choreographer, and external business data. Query tables provide an abstraction on the data of Business Process Choreographer that can be used by client applications. In this way, client applications become independent of the actual implementation of the query table. Query table definitions are deployed on Business Process Choreographer containers, and are accessible using the query table API.
- Business Process Choreographer EJB query API

You can use the query method or the queryAll method of the service API to retrieve stored information about BPEL processes and tasks. However, it is generally preferable to use the query table API instead.