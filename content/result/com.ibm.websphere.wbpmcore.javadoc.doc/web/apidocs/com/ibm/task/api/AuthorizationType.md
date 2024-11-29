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

## Class AuthorizationType

- java.lang.Object
    - com.ibm.task.api.AuthorizationType

- All Implemented Interfaces:
java.io.Serializable

public final class AuthorizationType
extends java.lang.Object
implements java.io.Serializable
This enumeration class defines symbolic constants for types of authorization.
 These values are used when authorization information about query tables is returned.
Since:
7.0
See Also:Serialized Form

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static AuthorizationType
INSTANCE\_BASED
Symbolic constant for authorization type INSTANCE\_BASED

static AuthorizationType
NONE
Symbolic constant for authorization type NONE

static AuthorizationType
ROLE\_BASED
Symbolic constant for authorization type ROLE\_BASED
    - Method Summary Methods Modifier and Type Method and Description static AuthorizationType newAuthorizationType (java.lang.String typeString) Factory method to create an authorization type by its string representation. java.lang.String toString () Returns a string representation of the authorization type.

### Method Summary

| Modifier and Type        | Method and Description                                                                                                         |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| static AuthorizationType | newAuthorizationType(java.lang.String typeString) Factory method to create an authorization type by its string representation. |
| java.lang.String         | toString() Returns a string representation of the authorization type.                                                          |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait