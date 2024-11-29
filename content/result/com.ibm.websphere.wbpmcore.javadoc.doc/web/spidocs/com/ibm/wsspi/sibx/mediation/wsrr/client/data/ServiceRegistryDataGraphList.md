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

## Interface ServiceRegistryDataGraphList

- public interface ServiceRegistryDataGraphList
Represents a list of data graphs that have been returned from WSRR.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.util.List<DataGraphType>
getDataGraphs()
Get the list of DataGraphType objects returned from WSRR

long
getTimeStamp()
Get the time stamp of the query

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- $sccsid
static final java.lang.String $sccsid
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getDataGraphs
java.util.List<DataGraphType> getDataGraphs()
Get the list of DataGraphType objects returned from WSRR
Returns:The list of DataGraphType objects returned from WSRR
    - getTimeStamp
long getTimeStamp()
Get the time stamp of the query
Returns:The time stamp in milliseconds