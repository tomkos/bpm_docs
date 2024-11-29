<!-- image -->

# Query results

The elements of the result set are properties of the objects
that satisfy the where clause given by the caller, and that the caller
is authorized to see. You can read elements in a relative fashion
using the API next method or in an absolute fashion
using the first and last methods. Because
the implicit cursor of a query result set is initially positioned
before the first element, you must call either the first or next methods
before reading an element. You can use the size method to determine
the number of elements in the set.

An element of the query result set comprises the selected attributes
of work items and their associated referenced objects, such as activity
instances and process instances. The first attribute (column) of a
QueryResultSet element specifies the value of the first attribute
specified in the select clause of the query request. The second attribute
(column) of a QueryResultSet element specifies the value of the second
attribute specified in the select clause of the query request, and
so on.

You can retrieve the values of the attributes by calling a method
that is compatible with the attribute type and by specifying the appropriate
column index. The numbering of the column indexes starts with 1.

| Attribute type   | Method                                               |
|------------------|------------------------------------------------------|
| String           | getString                                            |
| OID              | getOID                                               |
| Timestamp        | getTimestamp  getString  getTimestampAsLong          |
| Integer          | getInteger  getShort  getLong  getString  getBoolean |
| Boolean          | getBoolean  getShort  getInteger  getLong  getString |
| byte[]           | getBinary                                            |

## Example

```
QueryResultSet resultSet = process.query("ACTIVITY.STARTED, 
                                          ACTIVITY.TEMPLATE\_NAME AS NAME, 
                                          WORK\_ITEM.WIID, WORK\_ITEM.REASON",
                                          (String)null, (String)null, 
                                          (Integer)null, (TimeZone)null);
```

The
returned query result set has four columns:

- Column 1 is a time stamp
- Column 2 is a string
- Column 3 is an object ID
- Column 4 is an integer

```
while (resultSet.next())
{
	java.util.Calendar activityStarted = resultSet.getTimestamp(1);
	String templateName = resultSet.getString(2);
	WIID wiid = (WIID) resultSet.getOID(3);
	Integer reason = resultSet.getInteger(4);
}
```

```
resultSet.getColumnDisplayName(1) returns "STARTED"
resultSet.getColumnDisplayName(2) returns "NAME"
resultSet.getColumnDisplayName(3) returns "WIID"
resultSet.getColumnDisplayName(4) returns "REASON"
```