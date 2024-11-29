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

## Class HTTPBindingUtil

- java.lang.Object
    - com.ibm.websphere.http.data.util.HTTPBindingUtil

- public class HTTPBindingUtil
extends java.lang.Object
An utility class to help in interacting with HTTP Data Binding APIs.

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Constructor Summary

Constructors 

Constructor and Description

HTTPBindingUtil()
    - Method Summary Methods Modifier and Type Method and Description static boolean containsHeader (java.lang.String name, HTTPHeaders headers) Returns a boolean indicating whether the named http header has already been set. static java.lang.String getHeader (java.lang.String name, HTTPHeaders headers) Returns the value of the specified http header as a String. static void removeHeader (java.lang.String name, HTTPHeaders headers) Removes all headers with the specified name(case-insensitive). static void setHeader (java.lang.String name, java.lang.String value, HTTPHeaders headers) Sets a http header with the given name and value.

### Method Summary

| Modifier and Type       | Method and Description                                                                                                                                    |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| static boolean          | containsHeader(java.lang.String name,               HTTPHeaders headers) Returns a boolean indicating whether the named http header has already been set. |
| static java.lang.String | getHeader(java.lang.String name,          HTTPHeaders headers) Returns the value of the specified http header as a String.                                |
| static void             | removeHeader(java.lang.String name,             HTTPHeaders headers) Removes all headers with the specified name(case-insensitive).                       |
| static void             | setHeader(java.lang.String name,          java.lang.String value,          HTTPHeaders headers) Sets a http header with the given name and value.         |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait