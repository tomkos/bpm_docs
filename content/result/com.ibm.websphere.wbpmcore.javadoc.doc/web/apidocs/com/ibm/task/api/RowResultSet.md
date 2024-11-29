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

## Interface RowResultSet

- All Superinterfaces:
java.io.Serializable

public interface RowResultSet
extends java.io.Serializable
Provides the results of a row-based query against a query table.
 
 The row result set returns attributes in rows which match the filter criteria
 that have been specified in the query table and in the query request.
 The rows are sorted according to the sort criteria specified in the query request.
 If sort criteria are not specified, there is no intrinsic order of rows.
 The number of rows returned is restricted by the threshold and skipCount
 parameters specified in the query request.
 If a threshold is not specified, all rows are returned.
 
 The number of rows in the result set can be determined by using the
 size() method.
 Rows can be read in a relative fashion using the next() method
 or in an absolute fashion using the first() and last()
 methods. Because the implicit cursor of a result set is
 initially positioned before the first row, either first() or next() must be called
 before reading a row.
 
 A row of the result set is defined through the selected attributes.
 The selected attributes reference query table attributes, such as attributes of tasks or process instances.
 If the query table requires instance-based authorization, work item information can also be referenced.
 
 Attribute values can be retrieved and casted to a type that is compatible with the attribute type.
 They can be retrieved by name or by specifying a column index.
 The first attribute (column) of a row states the value of the first selected attribute.
 The second attribute (column) of a row states the value of the second selected attribute, and so on.
Since:
7.0

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
Positions the cursor on the first row in the result set.

java.util.List
getAttributeInfo()
Returns information about the attributes in the row.

java.io.Serializable
getAttributeValue(int columnIndex)
Retrieves the value of the attribute specified by its column index.

java.io.Serializable
getAttributeValue(java.lang.String attributeName)
Retrieves the value of the specified attribute.

java.util.Locale
getLocale()
Returns the locale that is calculated for the system variable $LOCALE.

java.lang.String
getPrimaryQueryTableName()
Returns the name of the primary query table that is associated with this query result.

java.lang.String
getQueryTableName()
Returns the name of the query table that is associated with this query result.

boolean
last()
Positions the cursor on the last row in the result set.

boolean
next()
Positions the cursor on the next row in the result set starting from the current position.

boolean
previous()
Positions the cursor on the previous row in the result set starting from the current position.

int
size()
Returns the number of rows in the result set.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getQueryTableName
java.lang.String getQueryTableName()
Returns the name of the query table that is associated with this query result.
Returns:The name of the query table.
    - getPrimaryQueryTableName
java.lang.String getPrimaryQueryTableName()
Returns the name of the primary query table that is associated with this query result.
Returns:The name of the primary query table.
    - next
boolean next()
Positions the cursor on the next row in the result set starting from the current position.
 
 The implicit cursor is initially positioned before the first row in the set.
 This means that either next() or first() must be called before a row can be read.
 
 If next() is used to read the result set, the first row in the result set becomes
 the current row. A further call to next() makes the second row the current row, and so on.
 
 If the cursor is positioned at the last row of the result set and next() is called,
 the cursor position becomes undefined.
 
Returns:True if the cursor points to a row in the result set.
    False if there are no more rows in the result set.
    - first
boolean first()
Positions the cursor on the first row in the result set.
 
 The implicit cursor is initially positioned before the first row in the set.
 This means that first() or next() must be called before the first row can be read.
 
Returns:True if the cursor points to the first row in the result set.
    False if there are no rows in the result set.
    - last
boolean last()
Positions the cursor on the last row in the result set.
 
Returns:True if the cursor points to the last row in the result set.
    False if there are no rows in the result set.
    - previous
boolean previous()
Positions the cursor on the previous row in the result set starting from the current position.
 
Returns:True if the cursor points to a row in the result set.
    False if there are no more rows in the result set.
    - size
int size()
Returns the number of rows in the result set.
 
 The number of rows can be used to preallocate an array
 to hold all rows that are navigated using the next() call.
 
Returns:The number of rows in the result set. 0 is returned if the set is empty.
    - getAttributeInfo
java.util.List getAttributeInfo()
Returns information about the attributes in the row.
 
Returns:A list of AttributeInfo objects that describe the attributes in the row.
    - getAttributeValue
java.io.Serializable getAttributeValue(java.lang.String attributeName)
Retrieves the value of the specified attribute.
 
Parameters:attributeName - The name of the attribute to be retrieved.
 
Returns:The attribute value. If the value is not set for the row, a null object is returned.
 
Throws:
java.lang.IllegalArgumentException - if the specified attribute is not found.
    - getAttributeValue
java.io.Serializable getAttributeValue(int columnIndex)
Retrieves the value of the attribute specified by its column index.
 
Parameters:columnIndex - The column index of the attribute to be retrieved.
    The first column index is 1, the second is 2, and so on.
 
Returns:The attribute value. If the value is not set for the row, a null object is returned.
 
Throws:
java.lang.IndexOutOfBoundsException - if the specified columnIndex is not valid.
    - getLocale
java.util.Locale getLocale()
Returns the locale that is calculated for the system variable $LOCALE.
 
Returns:The locale that is set for $LOCALE.Since:
6.2.0.1