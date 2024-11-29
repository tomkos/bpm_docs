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

## Class QueryColumnInfo

- java.lang.Object
    - com.ibm.bpe.api.QueryColumnInfo

- All Implemented Interfaces:
java.io.Serializable

public class QueryColumnInfo
extends java.lang.Object
implements java.io.Serializable
Provides information on the columns of a query result set.
 In the API, this class is solely used to provide symbolic values for the column type specifications.
Since:
5.0
See Also:Serialized Form

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static short
TYPE\_BINARY
States that the values in the column are binares.

static short
TYPE\_BOOLEAN
States that the values in the column are booleans.

static short
TYPE\_DECIMAL
States that the values in the column are floating point numbers.

static short
TYPE\_ID
States that the values in the column are object IDs.

static short
TYPE\_NUMBER
States that the values in the column are numbers.

static short
TYPE\_STRING
States that the values in the column are strings.

static short
TYPE\_TIMESTAMP
States that the values in the column are timestamps.
    - Constructor Summary

Constructors 

Constructor and Description

QueryColumnInfo(QueryColumnInfo obj)
Copy constructor

QueryColumnInfo(java.lang.String columnName,
               short type,
               boolean isNullable)
Constructor.
    - Method Summary Methods Modifier and Type Method and Description void addConstant (java.lang.String strConstantName, int value) Adds an enumeration constant to the column information. java.lang.String getColumnName () Returns the name of the column. java.lang.Integer getConstant (java.lang.String strConstantName) Returns the enumeration value of the specified constant. java.lang.String getConstantName (int constantValue) Returns the name of the specified enumeration constant. java.lang.String getTableName () Returns the table name. short getType () Returns the type of the column. boolean isNullable () States whether the column allows for null values. void setColmnName (java.lang.String columnName) Sets the column name This information is overwritten if column names are overwritten, e.g. if alias names are used. void setTableName (java.lang.String tableName) Sets the name of the table.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                                          |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                | addConstant(java.lang.String strConstantName,            int value) Adds an enumeration constant to the column information.                                     |
| java.lang.String    | getColumnName() Returns the name of the column.                                                                                                                 |
| java.lang.Integer   | getConstant(java.lang.String strConstantName) Returns the enumeration value of the specified constant.                                                          |
| java.lang.String    | getConstantName(int constantValue) Returns the name of the specified enumeration constant.                                                                      |
| java.lang.String    | getTableName() Returns the table name.                                                                                                                          |
| short               | getType() Returns the type of the column.                                                                                                                       |
| boolean             | isNullable() States whether the column allows for null values.                                                                                                  |
| void                | setColmnName(java.lang.String columnName) Sets the column name  This information is overwritten if column names  are overwritten, e.g. if alias names are used. |
| void                | setTableName(java.lang.String tableName) Sets the name of the table.                                                                                            |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait