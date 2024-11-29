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

## Class AdminAuthorizationOptions

- java.lang.Object
    - com.ibm.bpe.api.AuthorizationOptions
        - com.ibm.bpe.api.AdminAuthorizationOptions

- All Implemented Interfaces:
java.io.Serializable

public final class AdminAuthorizationOptions
extends AuthorizationOptions
implements java.io.Serializable
Describes administrative authorizations options for a query that uses a predefined or composite query table.
 They are ignored for supplemental query tables.
 
 Only a system administrator or system monitor can specify these options.
 They must be specified when the query is run on predefined query tables.
 When the query is run on composite query tables and the primary view contains template data,
 administrative options must be specified if role-based authorization is required.
 
 When specified for a predefined query table that contains instance data or for
 a composite query table with a primary view that contains instance data, then
 all data contained in the query table is returned.
Since:
6.2
See Also:Serialized Form

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

AdminAuthorizationOptions()
Default constructor to initialize the admin authorization options.

AdminAuthorizationOptions(java.lang.String onBehalfUser)
Constructor that builds an admin authorization option from the passed values.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getOnBehalfUser () Returns the user on whose behalf the query is to be executed. void setOnBehalfUser (java.lang.String onBehalfUser) Sets the user on whose behalf the query is to be executed. java.lang.String toString () Returns a string representation of the AdminAuthorizationOptions object.

### Method Summary

| Modifier and Type   | Method and Description                                                                                    |
|---------------------|-----------------------------------------------------------------------------------------------------------|
| java.lang.String    | getOnBehalfUser() Returns the user on whose behalf the query is to be executed.                           |
| void                | setOnBehalfUser(java.lang.String onBehalfUser) Sets the user on whose behalf the query is to be executed. |
| java.lang.String    | toString() Returns a string representation of the AdminAuthorizationOptions object.                       |

    - Methods inherited from class com.ibm.bpe.api.AuthorizationOptions
areGroupsUsed, areIndividualsUsed, areInheritedWorkItemsUsed, isEverybodyUsed, setEverybodyUsed, setGroupsUsed, setIndividualsUsed, setInheritedUsed
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait