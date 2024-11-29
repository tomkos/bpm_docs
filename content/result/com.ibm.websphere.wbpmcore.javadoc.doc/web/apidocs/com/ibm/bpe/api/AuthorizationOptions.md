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

## Class AuthorizationOptions

- java.lang.Object
    - com.ibm.bpe.api.AuthorizationOptions

- All Implemented Interfaces:
java.io.Serializable

Direct Known Subclasses:
AdminAuthorizationOptions

public class AuthorizationOptions
extends java.lang.Object
implements java.io.Serializable
States authorizations options for a query that uses a predefined or composite query table.
 Authorization options are ignored for supplemental query tables.
 
 Authorization options are added to any authorization specification defined for the
 query table. This means that they can be used to further restrict authorization checks
 but not to weaken those checks.
 
 For example, if the authorization specification of a query table states that everybody
 work items should be considered, the authorization options passed to the actual query
 may specify that they are not to be used.
 The other way round, if the authorization specification of a query table states that everybody
 work items should not be considered, the authorization options passed to the actual query
 cannot specify that they are to be used.
 
 If authorization options are not specified or specified by a system administrator or monitor,
 a query is executed without special privileges for the logged-on user.
 In other words, if specified by a system administrator or monitor, the system administrator
 or monitor is treated like a normal user.
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

AuthorizationOptions()
Default constructor to initialize the authorization options.

AuthorizationOptions(java.lang.Boolean everybodyUsed,
                    java.lang.Boolean individualsUsed,
                    java.lang.Boolean groupsUsed,
                    java.lang.Boolean inheritedUsed)
Constructor that builds an authorization option from the passed values.
    - Method Summary Methods Modifier and Type Method and Description java.lang.Boolean areGroupsUsed () Returns whether group work items should be considered for a query. java.lang.Boolean areIndividualsUsed () Returns whether individual work items should be considered for a query. java.lang.Boolean areInheritedWorkItemsUsed () Returns whether inherited work items should be considered for a query. java.lang.Boolean isEverybodyUsed () Returns whether everybody work items should be considered for a query. void setEverybodyUsed (java.lang.Boolean everybodyUsed) Sets whether everybody work items should be considered. void setGroupsUsed (java.lang.Boolean groupsUsed) Sets whether group work items should be considered. void setIndividualsUsed (java.lang.Boolean individualsUsed) Sets whether individual work items should be considered. void setInheritedUsed (java.lang.Boolean inheritedUsed) Sets whether inherited work items should be considered. java.lang.String toString () Returns a string representation of the AuthorizationOptions object.

### Method Summary

| Modifier and Type   | Method and Description                                                                                         |
|---------------------|----------------------------------------------------------------------------------------------------------------|
| java.lang.Boolean   | areGroupsUsed() Returns whether group work items should be considered for a query.                             |
| java.lang.Boolean   | areIndividualsUsed() Returns whether individual work items should be considered for a query.                   |
| java.lang.Boolean   | areInheritedWorkItemsUsed() Returns whether inherited work items should be considered for a query.             |
| java.lang.Boolean   | isEverybodyUsed() Returns whether everybody work items should be considered for a query.                       |
| void                | setEverybodyUsed(java.lang.Boolean everybodyUsed) Sets whether everybody work items should be considered.      |
| void                | setGroupsUsed(java.lang.Boolean groupsUsed) Sets whether group work items should be considered.                |
| void                | setIndividualsUsed(java.lang.Boolean individualsUsed) Sets whether individual work items should be considered. |
| void                | setInheritedUsed(java.lang.Boolean inheritedUsed) Sets whether inherited work items should be considered.      |
| java.lang.String    | toString() Returns a string representation of the AuthorizationOptions object.                                 |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait