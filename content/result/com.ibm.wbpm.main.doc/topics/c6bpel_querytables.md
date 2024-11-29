<!-- image -->

# Query tables in Business Process Choreographer

Query tables support task and process list queries on data
that is contained in the Business Process Choreographer database schema.
This includes human task data and BPEL process data that is managed
by Business Process Choreographer, and external business data. Query
tables provide an abstraction on the data of Business Process Choreographer
that can be used by client applications. In this way, client applications
become independent of the actual implementation of the query table.
Query table definitions are deployed on Business Process Choreographer
containers, and are accessible using the query table API.

- Predefined query tables
- Supplemental query tables
- Composite query tables

Figure 1. Query tables in Business Process Choreographer

<!-- image -->

Query tables are represented using similar models in the query table runtime, and you can use the
query table API to query them. While predefined and supplemental query tables point directly to
tables or views in the database, composite query tables compose parts of this data, which is
represented in a single query table.

- Are optimized for running process and task list queries, using performance optimized access
patterns.
- Simplify and consolidate access to the information needed.
- Allow for the fine-grained configuration of authorization and filter options.

You can customize the query tables, for example, you can configure a query table so that it
contains only those tasks or process instances that are relevant in a particular scenario. It is
also recommended that you use query tables where performance is important, such as with high volume
process list and task list queries.

- Develop composite and supplemental query tables
- Import and export query table definitions in XML format

You can download the Query Table Builder on the SupportPacs site. Look for PA71 WebSphere Process
Server - Query Table Builder. To access the link, see the related references section of this
topic.

- Predefined query tables

Predefined query tables provide access to the data in the Business Process Choreographer database. They are the query table representation of the corresponding predefined Business Process Choreographer database views, such as the TASK view or the PROCESS\_INSTANCE view. These predefined query tables enhance the functionality and performance of the predefined database views because they are optimized for running process and task list queries.
- Supplemental query tables

Supplemental query tables in Business Process Choreographer expose to the query table API business data that is not managed by Business Process Choreographer. With supplemental query tables, this external data can be used with data from the predefined query tables when retrieving BPEL process instance information or human task information.
- Composite query tables

Composite query tables in Business Process Choreographer do not have a specific representation of data in the database; they comprise of a combination of data from related predefined and supplemental query tables. Use a composite query table to retrieve the information for a process instance list or task list, such as My To Dos.
- Query table development

Supplemental and composite query tables in Business Process Choreographer are developed during application development using the Query Table Builder. Predefined query tables cannot be developed or deployed. They are available when Business Process Choreographer is installed and provide a simple view on the artifacts in the Business Process Choreographer database schema.
- Filters and selection criteria of query tables

Filters and selection criteria are defined during query table development using the Query Table Builder, which uses a syntax similar to SQL WHERE clauses. Use these clearly defined filters and selection criteria to specify conditions that are based on attributes of query tables.%;
- Authorization for query tables

You can use instance-based authorization, role-based authorization, or no authorization when you run queries on query tables.
- Attribute types for query tables

Attribute types are needed in Business Process Choreographer when query tables are defined, when literal values are used in queries, and when values of a query result are accessed. Rules and mappings are available for each of the attribute types.
- Query table queries

Queries are run on query tables in Business Process Choreographer using the query table API, which is available on the Business Flow Manager EJB and the REST API.
- Query table queries for meta data retrieval

Queries are run on query tables in Business Process Choreographer using the query table API. Methods are available to retrieve meta data from query tables.
- Internationalization for query table meta data

Internationalization is supported for query table meta data.
- Query tables and query performance

Query tables introduce a clean programming model for developing client applications that retrieve lists of human tasks and BPEL processes in Business Process Choreographer. Using query tables improves the performance. Information is provided about the query table API parameters and other factors that affect the performance.
- Creating query tables for Business Process Choreographer Explorer

You can use query tables instead of the EJB query API to improve the performance of Business Process Choreographer Explorer. To create the query tables, use the Query Table Builder.