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

## Interface QueryResultSet

- All Superinterfaces:
java.io.Serializable

public interface QueryResultSet
extends java.io.Serializable
Provides the results of a query request.
 
 The query result set contains tuples that the calling user is authorized to see
 after any filter criteria specified in the query request have been applied. If a filter
 is not specified, the query result
 set contains all the tuples the caller is authorized to see.
 Tuples of the query result set are sorted on the server according to the sort criteria
 specified in the query request.
 If sort criteria are not specified, there is no intrinsic order of tuples.
 The number of tuples returned is restricted by the threshold and skipTuples parameter
 specified in the query request.
 If threshold and skipTuples parameters are not specified, all the qualifying tuples are returned.
 
 The number of tuples in the query result set can be determined by using the
 size() method.
 Tuples can be read in a relative fashion using the next() method
 or in an absolute fashion using the first() and last()
 methods. Because the implicit cursor of a query result set is
 initially positioned before the first tuple, either first() or next() must be called
 before reading a tuple.
 
 A tuple of the query result set is composed of the selected attributes of objects,
 such as the attributes of task instances.
 The first attribute (column) of a QueryResultSet tuple states the value of the first
 attribute specified in the select clause of the query request.
 The second attribute (column) of a QueryResultSet tuple states the value of the second
 attribute specified in the select clause of the query request,
 and so on.
 
 Values can be retrieved by calling a method that is compatible with the attribute type and
 by specifying the appropriate column index.
 
 For example, issue getString(5) to read an attribute value of type String.
 The attribute is the 5th value of the tuple where the cursor is currently
 positioned. Note that column indizes start with '1'.
Since:
5.1

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

boolean
first()
Positions the cursor on the first tuple in the query result set.

byte[]
getBinary(int columnIndex)
Retrieves the value of the current tuple and the specified column as a byte array.

java.lang.Boolean
getBoolean(int columnIndex)
Retrieves the value of the current tuple and the specified column as a Java boolean.

java.lang.String
getColumnDisplayName(int columnIndex)
Returns a name that can be used to display the column title.

short
getColumnType(int columnIndex)
Returns the type of the values in the specified column.

java.lang.Double
getDouble(int columnIndex)
Retrieves the value of the current tuple and the specified column as a double data type.

java.lang.Integer
getInteger(int columnIndex)
Retrieves the value of the current tuple and the specified column as an integer.

java.lang.Long
getLong(int columnIndex)
Retrieves the value of the current tuple and the specified column as a long data type.

java.lang.Object
getObject(int columnIndex)
Retrieves the value of the current tuple and the specified column as an object.

OID
getOID(int columnIndex)
Retrieves the value of the current tuple and the specified column as an object ID (OID).

java.lang.Short
getShort(int columnIndex)
Retrieves the value of the current tuple and the specified column as a short data type.

java.lang.String
getString(int columnIndex)
Retrieves the value of the current tuple and the specified column as a string.

java.lang.String
getTableDisplayName(int columnIndex)
Returns a name that can be used to display the table title of the specified column.

java.util.Calendar
getTimestamp(int columnIndex)
Retrieves the value of the current tuple and the specified column as a Calendar timestamp.

java.lang.Long
getTimestampAsLong(int columnIndex)
Retrieves the value of the current tuple and the specified column as a numeric value
 representing a timestamp.

boolean
last()
Positions the cursor on the last tuple in the query result set.

boolean
next()
Positions the cursor on the next tuple in the query result set starting from the current position.

int
numberColumns()
Returns the number of columns in the query result set.

boolean
previous()
Positions the cursor on the previous tuple in the query result set starting from the current position.

int
size()
Returns the number of tuples in the query result set.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - first
boolean first()
Positions the cursor on the first tuple in the query result set.
 
 A QueryResultSet cursor is initially positioned before the first tuple in the set.
 This means that first() or next() must be called before the first tuple can be read.
Returns:True if the cursor points to the first tuple in the query result set.
    False if there are no tuples in the query result set.
    - getBinary
byte[] getBinary(int columnIndex)
Retrieves the value of the current tuple and the specified column as a byte array.
Parameters:columnIndex - A value in the range 1 .. numberColumns().
    The first column index is 1, the second is 2, and so on.
Returns:The attribute value. If the value is not set for the current tuple, a null object is returned.
Throws:
java.lang.ClassCastException - If the value of the specified column has a type that is incompatible with a byte array.
java.lang.IndexOutOfBoundsException - If the columnIndex is out of range.
    - getBoolean
java.lang.Boolean getBoolean(int columnIndex)
Retrieves the value of the current tuple and the specified column as a Java boolean.
Parameters:columnIndex - A value in the range 1 .. numberColumns().
    The first column index is 1, the second is 2, and so on.
Returns:The attribute value. If the value is not set for the current tuple, a null object is returned.
Throws:
java.lang.ClassCastException - If the value of the specified column has a type that is incompatible with a boolean.
java.lang.IndexOutOfBoundsException - If the columnIndex is out of range.
    - getColumnDisplayName
java.lang.String getColumnDisplayName(int columnIndex)
Returns a name that can be used to display the column title.
 Reading the column title is independent of the current cursor position in the query result set.
Parameters:columnIndex - A value in the range 1 .. numberColumns().
    The first column index is 1, the second is 2, and so on.
Returns:The header or title of the column.
    - getColumnType
short getColumnType(int columnIndex)
Returns the type of the values in the specified column.
 Reading the column type is independent of the current cursor position in the query result set.
Parameters:columnIndex - A value in the range 1 .. numberColumns().
    The first column index is 1, the second is 2, and so on.
Returns:The type of the column values.
    Refer to QueryColumnType for the type definitions.
    - getInteger
java.lang.Integer getInteger(int columnIndex)
Retrieves the value of the current tuple and the specified column as an integer.
Parameters:columnIndex - A value in the range 1 .. numberColumns().
    The first column index is 1, the second is 2, and so on.
Returns:The attribute value. If the value is not set for the current tuple, a null object is returned.
Throws:
java.lang.ClassCastException - If the value of the specified column has a type that is incompatible with an integer.
java.lang.IndexOutOfBoundsException - If the columnIndex is out of range.
    - getLong
java.lang.Long getLong(int columnIndex)
Retrieves the value of the current tuple and the specified column as a long data type.
Parameters:columnIndex - A value in the range 1 .. numberColumns().
    The first column index is 1, the second is 2, and so on.
Returns:The attribute value. If the value is not set for the current tuple, a null object is returned.
Throws:
java.lang.ClassCastException - If the value of the specified column has a type that is incompatible to a long data type.
java.lang.IndexOutOfBoundsException - If the columnIndex is out of range.
    - getObject
java.lang.Object getObject(int columnIndex)
Retrieves the value of the current tuple and the specified column as an object.
Parameters:columnIndex - A value in the range 1 .. numberColumns().
    The first column index is 1, the second is 2, and so on.
Returns:The attribute value. If the value is not set for the current tuple, a null object is returned.
Throws:
java.lang.IndexOutOfBoundsException - If the columnIndex is out of range.
    - getOID
OID getOID(int columnIndex)
Retrieves the value of the current tuple and the specified column as an object ID (OID).
Parameters:columnIndex - A value in the range 1 .. numberColumns().
    The first column index is 1, the second is 2, and so on.
Returns:The attribute value. If the value is not set for the current tuple, a null object is returned.
Throws:
java.lang.ClassCastException - If the value of the specified column has a type that is incompatible with an object ID.
java.lang.IndexOutOfBoundsException - If the columnIndex is out of range.
    - getShort
java.lang.Short getShort(int columnIndex)
Retrieves the value of the current tuple and the specified column as a short data type.
Parameters:columnIndex - A value in the range 1 .. numberColumns().
    The first column index is 1, the second is 2, and so on.
Returns:The attribute value. If the value is not set for the current tuple, a null object is returned.
Throws:
java.lang.ClassCastException - If the value of the specified column has a type that is incompatible with a short data type.
java.lang.IndexOutOfBoundsException - If the columnIndex is out of range.
    - getDouble
java.lang.Double getDouble(int columnIndex)
Retrieves the value of the current tuple and the specified column as a double data type.
 
Parameters:columnIndex - A value in the range 1 .. numberColumns().
    The first column index is 1, the second is 2, and so on.
 
Returns:The attribute value. If the value is not set for the current tuple, a null object is returned.
 
Throws:
java.lang.ClassCastException - if the value of the specified column has a type
                               that is incompatible with a double data type.
 
java.lang.IndexOutOfBoundsException - if the columnIndex is out of range.
    - getString
java.lang.String getString(int columnIndex)
Retrieves the value of the current tuple and the specified column as a string.
Parameters:columnIndex - A value in the range 1 .. numberColumns().
    The first column index is 1, the second is 2, and so on.
Returns:The attribute value. If the value is not set for the current tuple, a null object is returned.
Throws:
java.lang.ClassCastException - If the value of the specified column has a type that is incompatible with a string.
java.lang.IndexOutOfBoundsException - If the columnIndex is out of range.
    - getTableDisplayName
java.lang.String getTableDisplayName(int columnIndex)
Returns a name that can be used to display the table title of the specified column.
 The table title can be used to differentiate between columns with same names in different tables.
 Reading the table title is independent of the current cursor position in the query result set.
Parameters:columnIndex - A value in the range 1 .. numberColumns().
    The first column index is 1, the second is 2, and so on.
Returns:The header or title of the table.
    - getTimestamp
java.util.Calendar getTimestamp(int columnIndex)
Retrieves the value of the current tuple and the specified column as a Calendar timestamp.
 The Calendar value contains the same timezone value that is passed in the query
 call. If no timezone was given there, the timezone is assumed to be "UTC"
Parameters:columnIndex - A value in the range 1 .. numberColumns().
    The first column index is 1, the second is 2, and so on.
Returns:The attribute value. If the value is not set for the current tuple, a null object is returned.
Throws:
java.lang.ClassCastException - If the value of the specified column has a type that is incompatible with a timestamp.
java.lang.IndexOutOfBoundsException - If the columnIndex is out of range.
    - getTimestampAsLong
java.lang.Long getTimestampAsLong(int columnIndex)
Retrieves the value of the current tuple and the specified column as a numeric value
 representing a timestamp.
 The numeric value represents a timestamp in "UTC" format.
 
Parameters:columnIndex - A value in the range 1 .. numberColumns().
    The first column index is 1, the second is 2, and so on.
 
Returns:The attribute value. If the value is not set for the current tuple, a null object is returned.
 
Throws:
java.lang.ClassCastException - if the value of the specified column has a type
                               that is incompatible with a timestamp.
 
java.lang.IndexOutOfBoundsException - if the columnIndex is out of range.Since:
6.1
    - last
boolean last()
Positions the cursor on the last tuple in the query result set.
Returns:True if the cursor points to the last tuple in the query result set.
    False if there are no tuples in the query result set.
    - next
boolean next()
Positions the cursor on the next tuple in the query result set starting from the current position.
 
 A QueryResultSet cursor is initially positioned before the first tuple in the set.
 This means that either next() or first() must be called before a tuple can be read.
 
 If next() is used to read the query result set, the first tuple in the query result set becomes
 the current tuple. A further call to next() makes the second tuple the current tuple, and so on.
 
 If the cursor is positioned at the last tuple of the query result set and next() is called,
 the cursor position becomes undefined.
Returns:True if the cursor points to a tuple in the query result set.
    False if there are no more tuples in the query result set.
    - numberColumns
int numberColumns()
Returns the number of columns in the query result set.
 The columnIndex parameter in calls that read attribute values
 must be in the range 1 .. numberColumns().
Returns:The number of columns in the query result set.
    - previous
boolean previous()
Positions the cursor on the previous tuple in the query result set starting from the current position.
Returns:True if the cursor points to a tuple in the query result set.
    False if there are no more tuples in the query result set.
    - size
int size()
Returns the number of tuples in the query result set.
 
 The number of tuples can be used to preallocate an array
 to hold all tuples that are navigated using the next() call.
Returns:The number of tuples in the query result set. 0 is returned if the query result set is empty.