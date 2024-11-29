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

## Interface ConnectionFactory

- public interface ConnectionFactory
Creates or retrieves a collection of connection objects. Connection objects
 denote configuration or reference information which must be available before accessing
 a backend module, that is, an EJB. Each connection must be registerd under a name that is unique
 within the application. In the Business Process Choreographer Explorer, the connection 
 objects can either be a BFMConnection 
 or a HTMConnectionobject. The implementor of this interface
 can extend this factory to provide other connection objects, for example, to databases.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
(C) Copyright IBM Corporation 2005.
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.Object
getConnectionByName(java.lang.String connectionName)
Provides a connection object by its name.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
(C) Copyright IBM Corporation 2005.
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getConnectionByName
java.lang.Object getConnectionByName(java.lang.String connectionName)
Provides a connection object by its name. It is the caller's responsibility to make use 
 of the returned object.
Parameters:connectionName - The name by which the connection is known to the application.
Returns:A connection object that the caller can use, or null if the connection ID is unknown.