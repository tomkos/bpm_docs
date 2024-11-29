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

## Class HTTPAuthenticationType

- java.lang.Object
    - org.eclipse.emf.common.util.AbstractEnumerator
        - com.ibm.websphere.http.headers.HTTPAuthenticationType

- All Implemented Interfaces:
org.eclipse.emf.common.util.Enumerator

public final class HTTPAuthenticationType
extends org.eclipse.emf.common.util.AbstractEnumerator

 A representation of the literals of the enumeration 'HTTP Authentication Type',
 and utility methods for working with them.
 
See Also:HeadersPackage.getHTTPAuthenticationType()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
BASIC
The 'Basic' literal value.

static HTTPAuthenticationType
BASIC\_LITERAL
The 'Basic' literal object

static java.lang.String
COPYRIGHT 

static java.util.List
VALUES
A public read-only list of all the 'HTTP Authentication Type' enumerators
    - Method Summary Methods Modifier and Type Method and Description static HTTPAuthenticationType get (int value) Returns the 'HTTP Authentication Type ' literal with the specified integer value static HTTPAuthenticationType get (java.lang.String literal) Returns the 'HTTP Authentication Type ' literal with the specified literal value static HTTPAuthenticationType getByName (java.lang.String name) Returns the 'HTTP Authentication Type ' literal with the specified name

### Method Summary

| Modifier and Type             | Method and Description                                                                                        |
|-------------------------------|---------------------------------------------------------------------------------------------------------------|
| static HTTPAuthenticationType | get(int value) Returns the 'HTTP Authentication Type' literal with the specified integer value                |
| static HTTPAuthenticationType | get(java.lang.String literal) Returns the 'HTTP Authentication Type' literal with the specified literal value |
| static HTTPAuthenticationType | getByName(java.lang.String name) Returns the 'HTTP Authentication Type' literal with the specified name       |

    - Methods inherited from class org.eclipse.emf.common.util.AbstractEnumerator
getLiteral, getName, getValue, toString
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait