<!-- image -->

# Query table API methods

| Purpose                     | Methods                                                                                                                                                                                          |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Query contents              | queryEntities queryRows  Both methods return contents of the query table. The queryEntities method returns content based on entities and queryRows returns content based on rows.                |
| Query the number of objects | queryEntityCount queryRowCount  Both methods return the number of objects in the query table, while the actual number can depend on whether the entity-based or the row-based approach is taken. |

Entity-based queries, using the queryEntities method
and the queryEntityCount method, assume that a
query table contains uniquely identifiable entities, as defined by
the primary key on the primary query table.

Row-based queries, using the queryRows method
and the queryRowCount method, return a result set
like JDBC, which is row-based, and provides first and next methods
for navigating in it. The result set that is returned when you run
a query on a query table using the query table API can be compared
to QueryResultSet that is returned by the query
API. In general, the number of rows is greater than the number of
entities that are contained in a query table. The same entity, for
example, a human task which is identified by its task ID, such as
TKIID, might occur multiple times in the row result set.

A specific instance that is contained in any predefined query table
exists only once in a Business Process Choreographer environment.
Examples of instances are human tasks and BPEL processes. Those instances
are uniquely identified using an ID or a set of IDs. This is the TKIID
for instances of human tasks and the PIID for process instances.

Composite query tables are composed of a primary query table and
zero or more attached query tables. Objects that are contained in
composite query tables are uniquely identified by the unique ID of
the objects that are contained in the primary query table. The primary
query table of a composite query table determines its entity type.
For example, a composite query table with the TASK primary query table
contains entities of the TASK type. The one-to-one or one-to-zero
relationship between the primary and attached query tables ensures
that the attached query tables do not result in duplicate entities.

Entity-based queries exploit the uniquely identifiable entities
of a query table, as defined by the primary key on the primary query
table. A client application programmer for user interfaces is typically
interested in unique instances without duplicates, for example, to
display a human task once only on the user interface. Unique instances
are returned if the entity-based query table API is used.

- Information from the WORK\_ITEM query table is retrieved with the
query. For example, if the WI.REASON attribute is
retrieved in addition to the attributes that are defined on the query
table, multiple rows qualify for the result. This is because there
can be multiple reasons why a user can access an entity, such as,
a task or a process instance.
- Instance-based authorization is used, and distinct is not specified.
Even though work item information is not retrieved, multiple rows
may be returned if instance-based authorization is used.

- Entity-based queries are always run with the SQL distinct operator.
- Entity-based queries return a result which allows array values
for work-item-related information.