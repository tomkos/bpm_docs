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

## Class HTTPVersion

- java.lang.Object
    - org.eclipse.emf.common.util.AbstractEnumerator
        - com.ibm.websphere.http.headers.HTTPVersion

- All Implemented Interfaces:
org.eclipse.emf.common.util.Enumerator

public final class HTTPVersion
extends org.eclipse.emf.common.util.AbstractEnumerator

 A representation of the literals of the enumeration 'HTTP Version',
 and utility methods for working with them.
 
See Also:HeadersPackage.getHTTPVersion()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
\_10
The '10' literal value.

static HTTPVersion
\_10\_LITERAL
The '10' literal object

static int
\_11
The '11' literal value.

static HTTPVersion
\_11\_LITERAL
The '11' literal object

static java.lang.String
COPYRIGHT 

static java.util.List
VALUES
A public read-only list of all the 'HTTP Version' enumerators
    - Method Summary Methods Modifier and Type Method and Description static HTTPVersion get (int value) Returns the 'HTTP Version ' literal with the specified integer value static HTTPVersion get (java.lang.String literal) Returns the 'HTTP Version ' literal with the specified literal value static HTTPVersion getByName (java.lang.String name) Returns the 'HTTP Version ' literal with the specified name

### Method Summary

| Modifier and Type   | Method and Description                                                                            |
|---------------------|---------------------------------------------------------------------------------------------------|
| static HTTPVersion  | get(int value) Returns the 'HTTP Version' literal with the specified integer value                |
| static HTTPVersion  | get(java.lang.String literal) Returns the 'HTTP Version' literal with the specified literal value |
| static HTTPVersion  | getByName(java.lang.String name) Returns the 'HTTP Version' literal with the specified name       |

    - Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
getLiteral, getName, getValue, toString
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait