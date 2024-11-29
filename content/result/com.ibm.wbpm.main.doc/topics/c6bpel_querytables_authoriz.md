<!-- image -->

# Authorization for query tables

You can use instance-based authorization, role-based authorization,
or no authorization when you run queries on query tables.

- Instance-based authorization indicates that objects in the query
table are authorized using a work item. This is done by verifying
if a suitable work item exists.
- Role-based authorization is based on Java EE roles. It indicates
that the caller using the API query method must be in the BPESystemAdministrator
Java EE role if the Business Flow Manager EJB is used or the TaskSystemAdministrator
Java EE role if the Human Task Manager EJB is used to see the contents
of the query table. It is available for predefined query tables with
template data and for composite query tables with a primary query
table that contains template data. Objects in those query tables do
not have related work items.
- When no authorization is specified, all authenticated users can
see all contents of the query table, after filters are applied.

| Query table   | Instance-based authorization                                                                                                                                                                                                                                                                                                                                                                       | Role-based authorization                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | No authorization                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| Predefined    | Required for predefined query tables with instance data.                                                                                                                                                                                                                                                                                                                                           | Required for predefined query tables with template data.                                                                                                                                                                                                                                                                                                                                                                                                                                      | N/A                                                                                         |
| Composite     | Can be turned off which means that no authorization is used and the security constraints are overridden. That is, every authenticated user can use the query table to retrieve data, independently of whether they are authorized for the corresponding objects.Composite query tables with a primary query table that contains template data must not be set to use instance-based authorization. | Can be turned off, for example for composite query tables with a primary query table that contains template data. This means that no authorization is used and the security constraints are overridden. That is, every authenticated user can use the query table to retrieve data, independently of whether they are authorized for the corresponding objects.Composite query tables with a primary query table that contains instance data must not be set to use role-based authorization. | All authenticated users can see all contents of the query table, after filters are applied. |
| Supplemental  | Supplemental query tables must not be set to use instance-based authorization because they are not managed by Business Process Choreographer, and therefore it has no authorization information for the contents of these tables.                                                                                                                                                                  | Supplemental query tables must not be set to use role-based authorization.                                                                                                                                                                                                                                                                                                                                                                                                                    | All authenticated users can see all contents of the query table, after filters are applied. |

Figure 1. Instance-based
authorization for query tables

<!-- image -->

*) If the onBehalfUser is set, (A) applies

- (A) Queries on predefined or composite query tables using the
AuthorizationOptions object return entities that correlate with a
related work item for this particular user. This is also the case
if the AdminAuthorizationOptions object is used and onBehalfUser is
set. Standard clients which present task or process lists to users
usually use this combination of query tables and query table API parameters.
- (B) The full content of a query table consists of the entities
that have a related work item, as configured with the instance-based
authorization of the query table. Instance-based authorization considers
four types of work items: everybody, individual, group, and inherited.
The caller using the API query method must be in the BPESystemAdministrator
Java EE role if the Business Flow Manager EJB is used or the TaskSystemAdministrator
Java EE role if the Human Task Manager EJB is used. This combination
of query tables and query table API parameters is intended for use
in administrative scenarios where the full list of available tasks
or processes must be shown or searched.
- (C) Queries on query tables that do not use instance-based or
role-based authorization return the same result if AdminAuthorizationOptions
or AuthorizationOptions is passed into the query table API. This is
available for supplemental and composite query tables. There is no
check on work items or Java EE roles, therefore all authenticated
users see the full content. Clients that do not want to restrict object
visibility by applying the instance-based or role-based authorization
constraints that are provided by Business Process Choreographer can
turn off authorization checks when query table definitions are developed.
When using claim and complete, however, users must have related work
items.
- (D) Template data in predefined query tables or composite query
tables with role-based authorization configured can be accessed only
with role-based authorization. This requires the caller using the
API query method to be in the BPESystemAdministrator Java EE role
if the Business Flow Manager EJB is used or the TaskSystemAdministrator
Java EE role if the Human Task Manager EJB is used. The query table
API can be used to access template information instead of the query
API.

## Work items and instance-based authorization

Instance-based
authorization provided by Business Process Choreographer is based
on work items. Each work item describes who has which rights on what
object. This information is accessible using the WORK\_ITEM query table,
if instance-based authorization is used.

| Work item type   | Description                                                                                                                                                                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| everybody        | Allows all users to access a specific object, such as a task or a process instance. In this case, the EVERYBODY attribute of the related work item is set to TRUE.                                                                                                                                          |
| individual       | Work items that are created for particular users. The OWNER\_ID attribute of the related work item is set to a specific user. Multiple work items which differ in the OWNER\_ID attribute can exist for an object, such as a task.                                                                            |
| group            | Work items that are created for users of a particular group. The GROUP\_NAME attribute of the related work item is set to a specific group.                                                                                                                                                                  |
| inherited        | Readers and administrators of process instances are also allowed to inherit the access to the human tasks which belong to these process instances, including escalations. Checks for an inherited work item in task queries are performed with complex SQL joins at run time, which impacts on performance. |

Work items are created by Business Process Choreographer
in different situations. For example, at task creation, work items
are created for the different roles, such as reader and potential
owner, if related people assignment criteria were specified.

| Work item type   | Related people assignment criteria                                       |
|------------------|--------------------------------------------------------------------------|
| everybody        | Everybody                                                                |
| individual       | All people assignment criteria except verbs Nobody, Everybody, and Group |
| group            | Group                                                                    |

## Authorization filter on composite query tables

On
composite query tables, you can specify an authorization filter if
instance-based authorization is used. This filter restricts the work
items which are used for authorization, based on certain attributes
of work items. For example, the authorization filter "WI.REASON=REASON\_POTENTIAL\_OWNER" on
a composite query table with the TASK primary query table restricts
the tasks that are returned when a person runs a query. The result
contains only tasks that represent a to-do for that person, that is,
the result is restricted to those tasks the person is authorized to
claim. This filter can also be specified as the query table filter
or as the query filter, but for query performance reasons, it is beneficial
to specify these filters as the authorization filter.