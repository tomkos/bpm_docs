<!-- image -->

# Composite query tables

Composite query tables in Business Process Choreographer
do not have a specific representation of data in the database; they
comprise of a combination of data from related predefined and supplemental
query tables. Use a composite query table to retrieve the information
for a process instance list or task list, such as My To Dos.

Composite query tables are designed by client developers and they
allow for a fine-grained configuration of filters and authorization
options for optimized data access when the query is run. They are
realized with SQL, which is optimized for task and process list queries.

It is recommended that you use composite query tables in production
scenarios in place of the standard Business Process Choreographer
query APIs, because composite query tables provide an abstraction
over the actual implementation of the query and thus enable query
optimizations.

Furthermore, you can change composite query tables at run time
without redeploying the client that accesses the query table.

Figure 1. Composite query table content

<!-- image -->

All composite query tables are defined with one primary query table
and zero or more attached query tables.

- Constitute the main information that is contained in a composite
query table.
- Must be one of the predefined query tables.
- Uniquely identify each object in the composite query table by
the primary key. For example, for the TASK predefined query table,
this is the task ID TKIID.
- Authorize the contents of a query table using work items which
are contained in the WORK\_ITEM query table, if instance-based authorization
is used.
- Determine the list of objects that are returned as rows of a table
when querying the composite query table.

- Can be predefined query tables and supplemental query tables,
which are already deployed on the system.
- Are available to provide information in addition to the information
that is provided by the primary query table. For example, if TASK
is the primary query table, the description of the task provided in
the TASK\_DESC query table can be added to the contents of the composite
query table.

- If the composite query table describes a task list, the TASK query
table is the primary query table.
- If the composite query table describes a process list, the PROCESS\_INSTANCE
query table is the primary query table.
- Lists of activities are retrieved using the ACTIVITY primary query
table.
- Lists of human task escalations are retrieved using the ESCALATION
primary query table.
- Lists of work baskets are retrieved using the WORK\_BASKET primary
query table.
- Lists of business categories are retrieved using the BUSINESS\_CATEGORY
primary query table.

## The relationship between primary and attached query
tables

The attached query table and the primary query table
must have a one-to-one or one-to-zero relationship. If the one-to-one
or one-to-zero relationship is violated, a runtime exception occurs
when the query is run.

Primary query tables and attached query
tables are correlated using a join attribute that is defined on the
attached query table. This join attribute cannot be changed for predefined
query tables, because it describes the relationship between the data
in the various query tables of Business Process Choreographer. The
join attribute is usually sufficient to maintain the one-to-one or
one-to-zero relationship. For example, the CONTAINMENT\_CTX\_ID attribute
is used on the TASK query table to attach the related process instance
information that is identified by the PIID attribute on the PROCESS\_INSTANCE
query table.

When a one-to-many relationship exists, you must
specify an additional criterion, known as selection criterion, in
the Query Table Builder when you define the query table. For example,
this could be "LOCALE='en\_US'". A task can have several
descriptions that are identified using different locales for a single
task. To further restrict the items that are returned by the query,
you can attach a supplemental query table with selection criteria
to the composite query table, and enable the optimizeForFiltering
option.

Example 1:

Figure 2. Composite query
table with selection criteria

<!-- image -->

- ID, STATE, and NAME are provided by the TASK primary query table.
- CUSTOMER is a custom property on TASK. Custom properties are stored
in the TASK\_CPROP query table. For a particular task, a custom property
is uniquely identified using its name. This is reflected in the selection
criterion "CUSTOMER='IBM'".
- DESCRIPTION is the description of the task, which is stored in
TASK\_DESC query table. For each task instance, the task description
for a particular task is uniquely identified by its locale. This is
reflected in the selection criterion "LOCALE='en\_US'".

Example 2:

| TASK primary query table information   | TASK\_DESC attached query table information   | TASK\_DESC attached query table information   |
|----------------------------------------|----------------------------------------------|----------------------------------------------|
| NAME                                   | LOCALE                                       | DESCRIPTION                                  |
| task\_one                               | en\_US                                        | This is a description.                       |
| task\_two                               | en\_US                                        | This is a description.                       |
| ...                                    | ...                                          | ...                                          |

| Information from TASK (primary query table)   | Information from TASK\_DESC (attached query table)   | Information from TASK\_DESC (attached query table)   |
|-----------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|
| NAME                                          | LOCALE                                              | DESCRIPTION                                         |
| task\_one                                      | en\_US                                               | This is a description.                              |
| task\_one                                      | de\_DE                                               | Das ist eine Beschreibung.                          |
| ...                                           | ...                                                 | ...                                                 |

## Properties

Composite query tables have the
following properties:

| Property      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name          | The query table name must be unique within a Business Process Choreographer installation. When the query is run, this query table name is used to identify the query table that is queried. A query table is uniquely identified using its name, which is defined as prefix.name for composite query tables. The maximum length of the prefix.name is 28 characters. The prefix must be different from the reserved prefix 'IBM', for example, 'COMPANY.TODO\_TASK\_LIST'.  Do not use a digit at the end of the table name. If a table is used multiple times within a query, the name of the table is extended with a number ranging from 0 to 9. For example, CUSTOM\_VIEW0, CUSTOM\_VIEW1 and so on. If there is already a digit at the end of your table name, Business Process Choreographer will remove this digit, which causes an QueryUnknownTableException.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Attributes    | Attributes of composite query tables define the pieces of information that are available for queries. The attributes are defined with a name, in uppercase. The type is inherited from the referenced attribute, which is one of the following types:  Boolean: A boolean value  Decimal: A floating point number  ID: An object ID, such as TKIID of query table TASK Number: An integer, short, or long  String: A string  Timestamp: A timestamp  Attributes of composite query tables are defined using a reference to attributes of the primary query table or the attached query tables. The attributes of the composite query tables inherit the types and constants of referenced attributes. In addition to the attributes that are part of the query table definition, work item information can be queried at run time. This is possible if the primary query table contains instance data, such as TASK or PROCESS\_INSTANCE, and if instance-based authorization is used on the composite query table. For example, the query can be defined to return only human tasks of which the user is a potential owner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Authorization | Each composite query table defines if instance-based, role-based, or no authorization is used when queries are run on it. If instance-based authorization is defined, only objects with a work item for the user who performs the query are returned. However, using AdminAuthorizationOptions this verification can be reduced to a verification of the existence of a work item of any user. The user must be in the BPESystemAdministrator Java EE role if the Business Flow Manager EJB is used or the TaskSystemAdministrator Java EE role if the Human Task Manager EJB is used, for those queries, and AdminAuthorizationOptions must be passed to the query table API. If role-based authorization is defined, the user must be in the BPESystemAdministrator Java EE role if the Business Flow Manager EJB is used or the TaskSystemAdministrator Java EE role if the Human Task Manager EJB is used, for those queries, and AdminAuthorizationOptions must be passed to the query table API. If you use the WorkBasketSystemAdministrator Java EE role for the Human Task Manager EJB, the AdminAuthorizationOptions object can also be used for the WORK\_BASKET query table. Similarly, if you use the BusinessCategorySystemAdministrator Java EE role, the AdminAuthorizationOptions object can be used for the BUSINESS\_CATEGORY query tables. If no authorization is defined, the query is run without checks against the existence of work items of the related objects in the query table. All authenticated users can see the contents of the query table. Instance-based authorization can be defined if the primary query table contains instance data; role-based authorization can be defined if the primary query table contains template data. No authorization can be defined on composite query tables regardless of which primary query table is used. |

## Filters

Figure 3. Filters in composite query tables

<!-- image -->

- Primary query table, as the primary query table filter.
- Implicitly available WORK\_ITEM query table which is responsible
for authorization if the primary query table contains instance data.
This filter is called the authorization filter, and is available only
if the composite query table is configured to use instance-based authorization.
- Composite query table, as the query table filter.
- Composite query table, as an attached supplemental query table
with selection criteria and the optimizeForFiltering option enabled.

Filters are defined during query table development. For
example, a composite query table with the TASK primary query table
can filter on tasks that are in the ready state ("STATE=STATE\_READY" as
the primary query table filter).

## Authorization

- If instance-based authorization is configured for use, the data
contained in the composite query table is verified for existing work
items in the WORK\_ITEM query table. This verification is made against
the primary query table. Everybody, individual, group, and inherited
work items are used for the verification, depending on the configuration
of the composite query table. If inherited work items are specified,
objects that have a process instance as parent, such as a participating
human task, with a related everybody, individual, or group work item
as configured, are contained in the composite query table. Typically,
inherited work items are useful only for administrators.
- Composite query tables with a primary query table that contains
template data must not be set to use instance-based authorization.
If role-based authorization is used, queries can be run only by users
that are in the BPESystemAdministrator Java EE role if the Business
Flow Manager EJB is used or the TaskSystemAdministrator Java EE role
if the Human Task Manager EJB is used, and the AdminAuthorizationOptions
object must be used.