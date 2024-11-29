<!-- image -->

# Attribute types for query tables

Attribute types are needed in Business Process Choreographer
when query tables are defined, when literal values are used in queries,
and when values of a query result are accessed. Rules and mappings
are available for each of the attribute types.

A subset of the types that are available in the Java programming
language and databases is used to define the type of an attribute
of a query table. Attribute types are an abstraction of the concrete
Java type or database type. For supplemental query tables, you must
use a valid database type to attribute type mapping.

| Attribute type   | Description                                                                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID               | The ID which is used to identify a human task (TKIID), a process instance (PIID), or other objects. For example, IDs are used to claim or complete a particular human task, which is identified with the specified TKIID.                   |
| STRING           | Task descriptions or query properties can be represented as a string.                                                                                                                                                                       |
| NUMBER           | Numbers are used for attributes, such as the priority on a task.                                                                                                                                                                            |
| TIMESTAMP        | Timestamps describe a point in time, such as the time when a human task is created, or a process instance is finished.                                                                                                                      |
| DECIMAL          | Decimals can be used as the type for query properties, for example when defining a query property with a variable of XSD type double.                                                                                                       |
| BOOLEAN          | Booleans can have one of two values, true or false. For example, human tasks provide an attribute, autoClaim, which identifies whether the task is claimed automatically if only a single user exists as the potential owner for this task. |

- Database type to attribute type mapping

Use attribute types to define query tables in Business Process Choreographer, when you run queries on the query tables, and to access values of a query result.
- Attribute type to literal representation mapping

Attribute types are used when query tables are defined in Business Process Choreographer, when queries are run on the query tables, and when values of a query result are accessed. Use this topic for information on attribute type to literal representation mapping.
- Attribute type to parameter mapping

Use attribute types when you define query tables in Business Process Choreographer, when you run queries on the query tables, and to access values of a query result.
- Attribute type to Java object type mapping

Attribute types are used when query tables are defined in Business Process Choreographer, when queries are run on the query tables, and when values of a query result are accessed. Use this topic for information on attribute type to Java object type mapping.
- Attribute type compatibility

Use attribute types when you define query tables in Business Process Choreographer, when you run queries on the query tables, and to access values of a query result.