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

## Class QueryTableKind

- java.lang.Object
    - com.ibm.bpe.api.QueryTableKind

- All Implemented Interfaces:
java.io.Serializable

public final class QueryTableKind
extends java.lang.Object
implements java.io.Serializable
This enumeration class defines symbolic constants for query table kinds.
 These values are to be used when the kinds of query tables are specified.
Since:
6.2
See Also:Serialized Form

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static QueryTableKind
COMPOSITE
Symbolic constant for query table kind COMPOSITE

static java.lang.String
COPYRIGHT 

static QueryTableKind
PREDEFINED
Symbolic constant for query table kind PREDEFINED

static QueryTableKind
SUPPLEMENTAL
Symbolic constant for query table kind SUPPLEMENTAL
    - Method Summary Methods Modifier and Type Method and Description static QueryTableKind newQueryTableKind (java.lang.String kindString) Factory method to create a query table kind by its string representation. java.lang.String toString () Returns a string representation of the query table kind.

### Method Summary

| Modifier and Type     | Method and Description                                                                                                   |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------|
| static QueryTableKind | newQueryTableKind(java.lang.String kindString) Factory method to create a query table kind by its string representation. |
| java.lang.String      | toString() Returns a string representation of the query table kind.                                                      |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait