<!-- image -->

# Business Process Choreographer EJB query API

The query method can be called by all users,
and it returns the properties of the objects for which work items
exist. The queryAll method can be called only by
users who have one of the following Java™ EE
roles: BPESystemAdministrator, TaskSystemAdministrator, BPESystemMonitor,
or TaskSystemMonitor. This method returns the properties of all the
objects that are stored in the database.

- Whether the query was invoked by someone with one of the Java EE roles.
- The objects that are queried. Predefined database views are provided
for you to query the object properties.
- The insertion of a from clause, join conditions, and user-specific
conditions for access control.

You can include both custom properties and variable properties
in queries. If you include several custom properties or variable properties
in your query, this results in self-joins on the corresponding database
table. Depending on your database system, these query() calls
might have performance implications.

You can also store queries in the Business Process Choreographer
database using the createStoredQuery method. You
provide the query criteria when you define the stored query. The criteria
are applied dynamically when the stored query runs, that is, the data
is assembled at run time.  If the stored query contains parameters,
these are also resolved when the query runs.

For more information on the Business Process Choreographer APIs,
see the Javadoc in the com.ibm.bpe.api package for process-related
methods and in the com.ibm.task.api package for task-related methods.

- Syntax of the API query method

The syntax of the Business Process Choreographer API queries is similar to SQL queries. A query can include a select clause, a where clause, an order-by clause, a skip-tuples parameter, a threshold parameter and a time-zone parameter.
- User-specific access conditions

User-specific access conditions are added when the SQL SELECT statement is generated from the API query. These conditions guarantee that only those objects are returned to the caller that satisfy the condition specified by the caller and to which the caller is authorized.
- Examples of the query and queryAll methods

These examples show the syntax of various typical API queries and the associated SQL statements that are generated when the query is processed.
- Managing stored queries

Stored queries provide a way to save queries that are run often. The stored query can be either a query that is available to all users (public query), or a query that belongs to a specific user (private query).