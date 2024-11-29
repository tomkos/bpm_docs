<!-- image -->

# Authorization options for the query table API

Use an instance of the com.ibm.bpe.api.AuthorizationOptions class
or the com.ibm.bpe.api.AdminAuthorizationOptions class
if the Business Flow Manager EJB is used, or an instance of the com.ibm.task.api.AuthorizationOptions class
or the com.ibm.task.api.AdminAuthorizationOptions class
if the Human Task Manager EJB is used, to specify additional authorization
options when the query is run.

If instance-based authorization is used, instances of the AuthorizationOptions class
allow the specification of the type of work items used to identify
eligible instances that are returned by the query.

An instance of the AuthorizationOptions class
can be passed to the query table API if the query is run on a predefined
query table that contains instance data. It can also be passed if
the query is run on a composite query table with a primary query table
that contains instance data and instance-based authorization is configured
to be used. If the query is run on a predefined query table with template
data or a composite query table with role-based authorization configured,
an com.ibm.bpe.api.EngineNotAuthorizedException exception
is thrown if the Business Flow Manager EJB is used or com.ibm.task.api.NotAuthorizedException is
thrown if the Human Task Manager EJB is used. In all other cases,
the authorization options passed to the query table API are ignored.

Composite query tables can restrict the types of work items that
are considered when identifying objects (or entities) that are contained
in it. For example, if the authorization options that are passed to
the query table API are configured to use everybody work items, this
is only taken into account if everybody work items are defined for
use on the definition of the composite query table. As a simple rule,
a work item type that is not specified to be considered on the query
table definition cannot be overwritten to be considered by the query
table API, but a work item type that is specified to be considered
on the query table definition can be overwritten not to be used. Also,
the authorization type of a composite or predefined query table cannot
be overwritten by the query table API.

Depending on the type of query table that is queried, different
authorization option defaults apply if the authorization object is
not specified or if the related attributes (everybody, individual,
group, or inherited) are set to null, which is the default.

The following table shows the authorization option defaults for
the instance-based authorization for the query table type and work
item type used.

| Query table type                                        | Everybody work item   | Individual work item   | Group work item   | Inherited work item   |
|---------------------------------------------------------|-----------------------|------------------------|-------------------|-----------------------|
| Predefined with instance data                           | TRUE                  | TRUE                   | TRUE              | FALSE                 |
| Predefined with template data                           | N/A                   | N/A                    | N/A               | N/A                   |
| Composite with a primary query table with instance data | TRUE                  | TRUE                   | TRUE              | TRUE                  |
| Composite with a primary query table with template data | N/A                   | N/A                    | N/A               | N/A                   |
| Supplemental                                            | N/A                   | N/A                    | N/A               | N/A                   |

N/A means that instance-based authorization is not used and, therefore,
any setting on the authorization object with respect to work items
is ignored.

If TRUE is specified, the resulting query will only consider the
specific work item type if the query table is defined to use this
type of work item. This is true for all predefined query tables with
instance data, but might not be true for a composite query table.
For the group work item, the latter must also be enabled on the human
task container. An example of the inherited work item set to TRUE
is that the administrator of a process instance may see participating
human task instances that are created for that process instance.

- A query is run on a query table with role-based authorization.
Predefined query tables with template data require role-based authorization,
and composite query tables with a primary query table with template
data can be configured to require role-based authorization.
- A query is run on a query table with instance data or on a composite
query table with a primary query table that contains instance data.
It should return the content of that query table, regardless of restrictions
due to authorization for a particular user. This behavior is equivalent
to using the queryAll method on the query API (as
distinct from the query table API).
- A query should be executed on behalf of another user.

| Situation                             | Description                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| onBehalfUser set to null              | If the query is run on a query table with role-based authorization, all contents of that query table are returned. If the query is run on a query table which uses instance-based authorization, the particular objects contained in the query table are not checked for work items for a particular user. All objects that are contained in the query table are returned. |
| onBehalfUser set to a particular user | The query is run with the authority of the specified user, and the objects in the query table are checked against the work items for this user, if instance-based authorization is used.                                                                                                                                                                                   |

If you specify AdminAuthorizationOptions, the
caller must be in the BPESystemAdministrator or BPESystemMonitor Java
EE role if the Business Flow Manager EJB is used, or in the TaskSystemAdministrator
or TaskSystemMonitor Java EE role if the Human Task Manager EJB is
used.

If the predefined query table or primary query table in a composite
query table is WORK\_BASKET or WORK\_BASKET\_LDESC, the WorkBasketSystemAdministrator
can also use the AdminAuthorizationOptions for the Human Task Manager
EJB. Similarly, If the predefined query table or primary query table
in a composite query table is BUSINESS\_CATEGORY or BUSINESS\_CATEGORY,
the BusinessCategorySystemAdministrator can also use the AdminAuthorizationOptions
for the Human Task Manager EJB.