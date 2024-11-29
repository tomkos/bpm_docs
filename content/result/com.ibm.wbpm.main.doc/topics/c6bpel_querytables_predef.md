<!-- image -->

# Predefined query tables

The predefined query tables can be queried directly using the query
table API. When you access the tables using the query table API, you
are offered more options for configuration than when you use the query
API.

## Properties

Predefined query tables have
the following properties:

| Property      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name          | The query table name is the name of one of the predefined database views, in uppercase, for example, TASK.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Attributes    | Attributes of predefined query tables define the pieces of information that are available for queries. These attributes are the names of columns, in uppercase, that are specified by the predefined database views. The attributes are defined with a name and a type. The type is one of the following types:  Boolean: A boolean value  Decimal: A floating point number  ID: An object ID, such as TKIID of the TASK query table TASK Number: An integer, short, or long  String: A string  Timestamp: A timestamp                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Authorization | Predefined query tables use either instance-based or role-based authorization. Predefined query tables with instance data require instance-based authorization. This means that only objects with a work item for the user who performs the query are returned. However, using the AdminAuthorizationOptions object, this verification can be reduced to verifying that a work item exists for any user. The user must have the BPESystemAdministrator Java EE role if the Business Flow Manager EJB is used or the TaskSystemAdministrator Java EE role if the Human Task Manager EJB is used for those queries.  If you use the WorkBasketSystemAdministrator Java EE role for the Human Task Manager EJB, the AdminAuthorizationOptions object can also be used for the WORK\_BASKET query table. Similarly, if you use the BusinessCategorySystemAdministrator Java EE role, the AdminAuthorizationOptions object can be used for the BUSINESS\_CATEGORY query table.  Predefined query tables with template data require role-based authorization, which means that only users in the BPESystemAdministrator Java EE role if the Business Flow Manager EJB is used or the TaskSystemAdministrator Java EE role if the Human Task Manager EJB is used, can access the contents of those query tables. |

## Predefined query tables with instance data

- Can be used as the primary query of a composite query table.
- Use instance-based authorization if queried directly. This is
accomplished with a join (SQL-) with the view that stores authorization
information, that is, the predefined WORK\_ITEM view or query table.
- Contain instance data, for example data of task instances or process
instances.

| Instance data                                           | Query table name                                    |
|---------------------------------------------------------|-----------------------------------------------------|
| Information about activities of a process instance.     | ACTIVITY  ACTIVITY\_ATTRIBUTE  ACTIVITY\_SERVICE      |
| Information about escalations belonging to human tasks. | ESCALATION  ESCALATION\_CPROP  ESCALATION\_DESC       |
| Information about process instances.                    | PROCESS\_ATTRIBUTE  PROCESS\_INSTANCE  QUERY\_PROPERTY |
| Information about human tasks.                          | TASK  TASK\_CPROP  TASK\_DESC                         |
| Information about work baskets                          | WORK\_BASKET   WORK\_BASKET\_LDESC                     |
| Information about business categories                   | BUSINESS\_CATEGORY  BUSINESS\_CATEGORY\_LDESC          |

The WORK\_ITEM query table also contains instance data,
but this is not available as the primary query table or an attached
query table. Work item information is available implicitly when querying
query tables that use instance-based authorization. That is, attributes
of the WORK\_ITEM query table can be used when querying a query table
with instance-based authorization, even though the attributes are
not explicitly specified by the query table.

## Predefined query tables with template data

Predefined
query tables with template data require role-based authorization.
They can be queried only by administrators using the AdminAuthorizationOptions
object.

- Can be used as the primary query table of a composite query table.
- Use role-based authorization if queried directly. This means that
the caller using the API query method must be in the BPESystemAdministrator
Java EE role if the Business Flow Manager EJB is used, or the TaskSystemAdministrator
Java EE role if the Human Task Manager EJB is used, and AdminAuthorizationOptions
must be used.
- Contain template data, for example, the template data of task
templates or process templates.

| Template data                                                  | Query table name                              |
|----------------------------------------------------------------|-----------------------------------------------|
| Information about application components.                      | APPLICATION\_COMP                              |
| Information about escalation templates.                        | ESC\_TEMPL  ESC\_TEMPL\_CPROP  ESC\_TEMPL\_DESC    |
| Information about process templates.                           | PROCESS\_TEMPLATE  PROCESS\_TEMPL\_ATTR          |
| Information about task templates.                              | TASK\_TEMPL  TASK\_TEMPL\_CPROP  TASK\_TEMPL\_DESC |
| Version information about process templates and task templates | PC\_VERSION\_TEMPLATE                           |