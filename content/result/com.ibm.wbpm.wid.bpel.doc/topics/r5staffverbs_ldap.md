<!-- image -->

# Predefined people assignment criteria

You can use people assignment criteria (previously known as
staff verbs) in IBM® Integration
Designer to
specify people assignments in a human task.  These criteria are
transformed during modeling and deployment into a set of queries that
can be run on a people directory. The parameters for the following
predefined people assignment criteria are listed here:

- Department members
- Everybody
- Group
- Groups
- Group members
- Group members without named users
- Group members without filtered users
- Group search
- Intersection of group members
- Manager of employee
- Manager of employee by user ID
- Native query
- Nobody
- Person search
- Role members
- User records by user ID
- Users records by user ID without named users
- Users
- Users by user ID
- Users by user ID and groups
- Users by user ID without named users

- If you are working with large groups of people, the Group people
assignment criteria works best because it handles the members of a
group as a unit. This allows you to transfer a human task from one
group to another group easily. A person's group membership is resolved
when the person logs in and accesses a human task.
- To individually assign people that belong to a group to a human
task, the Group Members people assignment criteria
provides an alternative to the group assignment. The Group
Members people assignment criteria creates an assignment
for each person individually. This assignment can then be transferred
to another person. Substitution can occur, that is, a person that
is absent can be replaced by another person. A variant of this people
assignment criteria, Group Members without Named Users supports
the separation-of-duties assignment pattern. Note: Assigning people
to a group individually can affect performance at run time, especially
when assigning more than a few people to the group.
- To assign a few people to a human task that do not all belongto the same group, consider using the User Records by userID people assignment criteria definition. You can also usethis definition when the people assignment is not statically definedduring modeling, but includes replacement expressions. Replacementexpressions can refer to a custom property or the input message ofa human task. In the case of referring to an input message element,the element can also be defined as array. In this case, all arrayelements are used as user IDs. The Users by user ID peopleassignment criteria definition is similar to the User Recordsby user ID definition. Although the Users by userID definition performs better than the User Recordsby user ID definition at run time, it provides less functionality:
    - It does not check if the user IDs are entered correctly
    - It does not retrieve, for example, the email addresses for the
user IDs specified, which makes it less suitable for assigning people
to email escalations
- The Everybody people assignment criteria definition
is also worth considering. It indicates that all authenticated users
are assigned to the human task. While there are cases where all people
in an organization can do a certain job, this definition is particularly
useful during development, or when rapidly prototyping an application.
- The list of people assignment criteria that you see is filtered
by your choice of people directory provider. If you choose Lightweight
Directory Access Protocol (LDAP) as your provider, then criteria that
are appropriate only for virtual member manager will not be displayed.

## Department members

Use this
criteria to retrieve the members of a department. It is supported
by the LDAP, and the virtual member manager people directory providers.

| Parameter                  | Use       | Type    | Description                                                                                                                                                                                                                                    |
|----------------------------|-----------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DepartmentName             | Mandatory | string  | Department name of the users to retrieve. The department name must correspond to one of the following values: For virtual member manager, a unique name of a virtual member manager group For LDAP, a distinguished name (DN) of an LDAP group |
| IncludeNestedDepartments   | Mandatory | boolean | Specifies whether nested departments are considered in the query.                                                                                                                                                                              |
| AlternativeDepartmentName1 | Optional  | string  | An additional department to which the users can belong.                                                                                                                                                                                        |
| AlternativeDepartmentName2 | Optional  | string  | An additional department to which the users can belong.                                                                                                                                                                                        |
| AlternativeDepartmentName3 | Optional  | string  | An additional department to which the users can belong.                                                                                                                                                                                        |
| AlternativeDepartmentName4 | Optional  | string  | An additional department to which the users can belong.                                                                                                                                                                                        |
| AlternativeDepartmentName5 | Optional  | string  | An additional department to which the users can belong.                                                                                                                                                                                        |

## Everybody

Use this criteria
to assign every user that is authenticated by IBM Workflow
Server to
a task role. This criteria has no parameters.

This
criteria is supported by all of the people directory providers.

## Group

Use this criteria to assign
a group to a task role. This assignment creates a group work item
instead of creating user work items for every assigned user.

This
criteria is supported by all of the people directory providers.

| Parameter   | Use       | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------|-----------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GroupId     | Mandatory | string | Group name of the users to retrieve. This parameter supports replacement expressions. The group ID must correspond to one of the following values: For virtual member manager, a unique name of a group entry For LDAP, a DN of a group entry For the user registry provider, the name format you use depends on which user repository is set for the application server where the task is deployed: For the local operating system (deprecated), use a group name that is supported by the local operating system For a stand-alone custom registry (deprecated), use a group name supported by the custom implementation For a stand-alone LDAP registry (deprecated), use a DN of a group entry |

## Groups

Use the Groups criteria
to assign one or more groups to a task role. The Groups criteria creates
group work items instead of creating user work items for every assigned
user. This criteria is supported by all people directory providers.

| Parameter           | Use       | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------------|-----------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GroupId             | Mandatory | string | Group name of the users to retrieve. This parameter supports replacement expressions. The group ID must correspond to one of the following values: For virtual member manager, a unique name of a group entry For LDAP, a DN of a group entry For the user registry provider, the name format you use depends on which user repository is set for the application server where the task is deployed: For the local operating system (deprecated), use a group name that is supported by the local operating system For a stand-alone custom registry (deprecated), use a group name supported by the custom implementation For a stand-alone LDAP registry (deprecated), use a DN of a group entry |
| AlternativeGroupID1 | Optional  | string | An additional group to which the users can belong.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| AlternativeGroupID2 | Optional  | string | An additional group to which the users can belong.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| AlternativeGroupID3 | Optional  | string | An additional group to which the users can belong.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| AlternativeGroupID4 | Optional  | string | An additional group to which the users can belong.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| AlternativeGroupID5 | Optional  | string | An additional group to which the users can belong.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Group members

Use this criteria
to retrieve the members of a group. It is supported by the LDAP, virtual
member manager, and the user registry people directory providers.

| Parameter             | Use       | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------|-----------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GroupName             | Mandatory | string  | Group name of the users to retrieve. This parameter supports replacement expressions. The group ID must correspond to one of the following values: For virtual member manager, a unique name of a group entry For LDAP, a DN of a group entry For the user registry provider, the name format you use depends on which user repository is set for the application server where the task is deployed: For the local operating system (deprecated), use a group name that is supported by the local operating system For a stand-alone custom registry (deprecated), use a group name supported by the custom implementation For a stand-alone LDAP registry (deprecated), use a DN of a group entry |
| IncludeSubgroups      | Mandatory | boolean | Specifies whether nested subgroups are considered in the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| AlternativeGroupName1 | Optional  | string  | An additional group to which the users can belong.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| AlternativeGroupName2 | Optional  | string  | An additional group to which the users can belong.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| AlternativeGroupName3 | Optional  | string  | An additional group to which the users can belong.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| AlternativeGroupName4 | Optional  | string  | An additional group to which the users can belong.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| AlternativeGroupName5 | Optional  | string  | An additional group to which the users can belong.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Group members without named users

| Parameter        | Use       | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|-----------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GroupName        | Mandatory | string  | Group name of the users to retrieve. This parameter supports replacement expressions. The group ID must correspond to one of the following values: For virtual member manager, a unique name of a group entry For LDAP, a DN of a group entry For the user registry provider, the name format you use depends on which user repository is set for the application server where the task is deployed: For the local operating system (deprecated), use a group name that is supported by the local operating system For a stand-alone custom registry (deprecated), use a group name supported by the custom implementation For a stand-alone LDAP registry (deprecated), use a DN of a group entry |
| IncludeSubgroups | Mandatory | boolean | Specifies whether nested subgroups are considered in the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| NamedUsers       | Mandatory | string  | The user IDs of the users to exclude from the retrieved group members list.  This parameter supports replacement expression.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Group members without filtered
users

| Parameter        | Use       | Type    | Description                                                                                                                                                                                                                                   |
|------------------|-----------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GroupName        | Mandatory | string  | Group name of the users to retrieve. This parameter supports replacement expressions. The group ID must correspond to one of the following values: For virtual member manager, a unique name of a group entry For LDAP, a DN of a group entry |
| IncludeSubgroups | Mandatory | boolean | Specifies whether nested subgroups are considered in the query.                                                                                                                                                                               |
| FilterAttribute  | Mandatory | string  | Name of the attribute to use in the search filter.                                                                                                                                                                                            |
| FilterValue      | Mandatory | string  | Filter value to use in the search filter. You can use the wildcard character, asterisk (*), in the filter.                                                                                                                                    |

## Group search

Use this criteria
to search for a group based on attribute matches, and to assign the
members of the group. It is supported by the LDAP, and virtual member
manager people directory providers.

| Parameter          | Use      | Type   | Description                                                   |
|--------------------|----------|--------|---------------------------------------------------------------|
| GroupID            | Optional | string | The group ID of the users to retrieve.                        |
| Type               | Optional | string | The group type of the users to retrieve.                      |
| IndustryType       | Optional | string | The industry type of the group to which the users belong.     |
| BusinessType       | Optional | string | The business type of the group to which the users belong.     |
| GeographicLocation | Optional | string | An indication of where the users are located.                 |
| Affiliates         | Optional | string | The affiliates of the users.                                  |
| DisplayName        | Optional | string | The display name of the group.                                |
| Secretary          | Optional | string | The secretary of the users.                                   |
| Assistant          | Optional | string | The assistant of the users.                                   |
| Manager            | Optional | string | The manager of the users.                                     |
| BusinessCategory   | Optional | string | The business category of the group to which the users belong. |
| ParentCompany      | Optional | string | The parent company of the users.                              |

- GS\_GroupID: cn
- GS\_DisplayName: displayName
- GS\_BusinessCategory: businessCategory

## Intersection of group members

Use
this criteria to retrieve all users who are members of both groups.
It is supported by the LDAP and virtual member manager people directory
providers.

| Parameter        | Use       | Type    | Description                                                                                                                                                                                                                                         |
|------------------|-----------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GroupName        | Mandatory | string  | One group name of the users to retrieve. This parameter supports replacement expressions. The group ID must correspond to one of the following values: For virtual member manager, a unique name of a group entry For LDAP, a DN of a group entry   |
| OtherGroupName   | Mandatory | string  | Other group name of the users to retrieve. This parameter supports replacement expressions. The group ID must correspond to one of the following values: For virtual member manager, a unique name of a group entry For LDAP, a DN of a group entry |
| IncludeSubgroups | Mandatory | boolean | Specifies whether nested subgroups are considered in the query.                                                                                                                                                                                     |

## Manager of employee

Use this
criteria to retrieve the manager of a person using the person's name.
It is supported by the LDAP and virtual member manager people directory
providers.

| Parameter    | Use       | Type   | Description                                                                                                                                                                                                           |
|--------------|-----------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EmployeeName | Mandatory | string | The name of the employee whose manager is retrieved. The employee name must correspond to one of the following values: For virtual member manager, the unique name of a person entry For LDAP, a DN of a person entry |

## Manager of employee by user ID

Use
this criteria to retrieve the manager of a person using the person's
user ID. It is supported by the LDAP and virtual member manager people
directory providers.

| Parameter      | Use       | Type   | Description                                                                                                    |
|----------------|-----------|--------|----------------------------------------------------------------------------------------------------------------|
| EmployeeUserID | Mandatory | string | The login user ID of the employee whose manager is retrieved. This parameter supports replacement expressions. |

## Native query

Use this criteria
to define a native query based on directory-specific parameters. For
LDAP the following parameters apply:

| Parameter            | Use                        | Type   | Description                                                                                                                                                                                                                                                                                                                                           |
|----------------------|----------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QueryTemplate        | Mandatory                  | string | The query template to use. This must be one of the following values: search, user, or usersOfGroup.                                                                                                                                                                                                                                                   |
| Query                | Mandatory                  | string | Specifies the query. This parameter supports replacement expressions. The type of query depends on the query template. search template: a valid LDAP filter user template: a DN of a user entry usersOfGroup: a DN of a group                                                                                                                         |
| AdditionalParameter1 | Mandatory where applicable | string | Specifies the query. This parameter supports replacement expressions. The type of parameter depends on the query template. search template: used to specify whether recursive search is done. Supported values: yes and no user template: not applicable usersOfGroup: Used to specify whether recursive search is done. Supported values: yes and no |
| AdditionalParameter2 | Optional                   | string | Use this criteria to specify a base entry for searching.  a DN of a base entry                                                                                                                                                                                                                                                                        |
| AdditionalParameter3 | Optional                   | string | Use this criteria to specify an additional parameter. If you use the default mapping XSLT files, this parameter is not supported.                                                                                                                                                                                                                     |
| AdditionalParameter4 | Optional                   | string | Use this criteria to specify an additional parameter. If you use the default mapping XSLT files, this parameter is not supported.                                                                                                                                                                                                                     |
| AdditionalParameter5 | Optional                   | string | Use this criteria to specify an additional parameter. If you use the default mapping XSLT files, this parameter is not supported.                                                                                                                                                                                                                     |

For virtual member manager (VMM) people directory providers
the following parameters apply:

| Parameter            | Use                        | Type   | Description                                                                                                                                                                                                                                           |
|----------------------|----------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QueryTemplate        | Mandatory                  | string | The query template to use. This must be one of the following values: search, user, or usersOfGroup.                                                                                                                                                   |
| Query                | Mandatory                  | string | Specifies the query. This parameter supports replacement expressions. The type of query depends on the query template. search template: a valid search expression user template: a unique name of a user entry usersOfGroup: a unique name of a group |
| AdditionalParameter1 | Mandatory where applicable | string | Used to specify whether performing a people or group search.  Mandatory depending on query template. search template: either person or group user template: not applicable usersOfGroup: not applicable                                               |
| AdditionalParameter2 | Optional                   | string | Use this criteria to specify a base entry for searching.  a unique name of a base entry, for example, dc=mycomp, dc=com                                                                                                                               |
| AdditionalParameter3 | Optional                   | string | Used to specify whether recursive search is done. Supported values: true and false.  search template: applicable when AdditioanlParmeter1=group user template: not applicable usersOfGroup: applicable                                                |
| AdditionalParameter4 | Optional                   | string | Use this criteria to specify an additional parameter. If you use the default mapping XSLT files, this parameter is not supported.                                                                                                                     |
| AdditionalParameter5 | Optional                   | string | Use this criteria to specify an additional parameter. If you use the default mapping XSLT files, this parameter is not supported.                                                                                                                     |

## Nobody

Use this criteria to
deny users access to a task role. Only authorization inheritance and
people resolution defaults apply with this criteria. This criteria
has no parameters.

## Person search

Use this criteria
to search for people based on attribute matches. It is supported by
the LDAP, virtual member manager, and the user registry people directory
providers.

| Parameter         | Use      | Type   | Description                                   |
|-------------------|----------|--------|-----------------------------------------------|
| UserID            | Optional | string | The user ID of the users to retrieve.         |
| Profile           | Optional | string | The profile of the users to retrieve.         |
| LastName          | Optional | string | The last name of the users to retrieve.       |
| FirstName         | Optional | string | The given name of the users to retrieve.      |
| MiddleName        | Optional | string | The middle name of the users to retrieve.     |
| Email             | Optional | string | The email address of the users.               |
| Company           | Optional | string | The company to which the users belong.        |
| DisplayName       | Optional | string | The display name of the users.                |
| Secretary         | Optional | string | The secretary of the users.                   |
| Assistant         | Optional | string | The assistant of the users.                   |
| Manager           | Optional | string | The manager of the users.                     |
| Department        | Optional | string | The department to which the users belong.     |
| Phone             | Optional | string | The telephone number of the users.            |
| Fax               | Optional | string | The fax number of the users.                  |
| Gender            | Optional | string | Whether the user is male or female.           |
| Timezone          | Optional | string | The time zone in which the users are located. |
| PreferredLanguage | Optional | string | The preferred language of the user.           |

- PS\_UserID: uid
- PS\_LastName: sn
- PS\_FirstName: givenName
- PS\_MiddleName: initials
- PS\_Email: mail
- PS\_DisplayName: displayName
- PS\_Secretary: secretary
- PS\_Manager: manager
- PS\_Department: departmentNumber
- PS\_Phone: telephoneNumber
- PS\_PreferredLanguage: preferredLanguage

## Role members

Use this criteria
to retrieve the users associated with a role. It is supported by the
LDAP and virtual member manager people directory providers.

| Parameter            | Use       | Type    | Description                                                 |
|----------------------|-----------|---------|-------------------------------------------------------------|
| RoleName             | Mandatory | string  | Role name of the users to retrieve.                         |
| IncludeNestedRoles   | Mandatory | boolean | Specifies whether nested roles are considered in the query. |
| AlternativeRoleName1 | Optional  | string  | An additional role name for the user.                       |
| AlternativeRoleName2 | Optional  | string  | An additional role name for the user.                       |
| AlternativeRoleName3 | Optional  | string  | An additional role name for the user.                       |
| AlternativeRoleName4 | Optional  | string  | An additional role name for the user.                       |
| AlternativeRoleName5 | Optional  | string  | An additional role name for the user.                       |

## User records by user ID

Use
this criteria to define a query for a user whose user ID is known.
It is supported by the LDAP, virtual member manager people directory
providers. This criteria returns the user IDs, the email information,
and the preferred locale, if set, for these users.

| Parameter      | Use       | Type   | Description                                                                           |
|----------------|-----------|--------|---------------------------------------------------------------------------------------|
| UserID         | Mandatory | string | The user ID of the user to retrieve. This parameter supports replacement expressions. |
| AlternativeID1 | Optional  | string | An additional  user ID. Use this parameter to retrieve more than one user.            |
| AlternativeID2 | Optional  | string | An additional  user ID. Use this parameter to retrieve more than one user.            |
| AlternativeID3 | Optional  | string | An additional  user ID. Use this parameter to retrieve more than one user.            |
| AlternativeID4 | Optional  | string | An additional  user ID. Use this parameter to retrieve more than one user.            |
| AlternativeID5 | Optional  | string | An additional  user ID. Use this parameter to retrieve more than one user.            |

## Users records by user ID
without named users

Use this criteria to define a query
for users whose user ID is known, while excluding an explicitly named
user ID. It is supported by the LDAP, virtual member manager, and
user registry people directory providers. This criteria returns the
user IDs and the email information for these users.

| Parameter      | Use       | Type   | Description                                                                                                  |
|----------------|-----------|--------|--------------------------------------------------------------------------------------------------------------|
| UserID         | Mandatory | string | The user ID of the user to retrieve. This parameter supports replacement expressions.                        |
| AlternativeID1 | Optional  | string | An additional  user ID. Use this parameter to retrieve more than one user.                                   |
| AlternativeID2 | Optional  | string | An additional  user ID. Use this parameter to retrieve more than one user.                                   |
| AlternativeID3 | Optional  | string | An additional  user ID. Use this parameter to retrieve more than one user.                                   |
| AlternativeID4 | Optional  | string | An additional  user ID. Use this parameter to retrieve more than one user.                                   |
| AlternativeID5 | Optional  | string | An additional  user ID. Use this parameter to retrieve more than one user.                                   |
| NamedUsers     | Mandatory | string | The user IDs of the users to exclude from the user ID list. This parameter supports replacement expressions. |

## Users

Use this criteria to define
a query for a user who is known by name. It is supported by all of
the people directory providers.

| Parameter        | Use       | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------|-----------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name             | Mandatory | string | The name of the user to retrieve. For virtual member manager, the unique name of a person entry For LDAP, a DN of a person entry For the user registry provider, the name format you use depends on which user repository is set for the application server where the task is deployed: For the local operating system (deprecated), use the user ID of the user to assign For a stand-alone custom registry (deprecated), use a person name supported by the custom implementation For a stand-alone LDAP registry (deprecated), use a DN of a person entry |
| AlternativeName1 | Optional  | string | An additional user name. Use this parameter to retrieve more than one user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| AlternativeName2 | Optional  | string | An additional user name. Use this parameter to retrieve more than one user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| AlternativeName3 | Optional  | string | An additional user name. Use this parameter to retrieve more than one user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| AlternativeName4 | Optional  | string | An additional user name. Use this parameter to retrieve more than one user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| AlternativeName5 | Optional  | string | An additional user name. Use this parameter to retrieve more than one user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## Users by user ID

Use this criteria
to define a query for a user whose user ID is known. Use short names
to specify values, for example, wpsadmin. This criteria does not require
access to a people directory. It is supported by all of the people
directory providers.

| Parameter      | Use       | Type   | Description                                                                           |
|----------------|-----------|--------|---------------------------------------------------------------------------------------|
| UserID         | Mandatory | string | The user ID of the user to retrieve. This parameter supports replacement expressions. |
| AlternativeID1 | Optional  | string | An additional  user ID. Use this parameter to retrieve more than one user.            |
| AlternativeID2 | Optional  | string | An additional  user ID. Use this parameter to retrieve more than one user.            |

## Users by user ID and groups

Use
this criteria to assign one or more groups and one or more users whose
user IDs are known to a task role. This assignment creates user work
items and group work items for every assigned user and group.

| Parameter           | Use       | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------------|-----------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UserID              | Mandatory | string | The user ID of the user to retrieve. This parameter supports replacement expressions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| GroupId             | Mandatory | string | Group name of the users to retrieve. This parameter supports replacement expressions. The group ID must correspond to one of the following values:  For virtual member manager, a unique name of a group entry For LDAP, a DN of a group entry For the user registry provider, the name format you use depends on which user repository is set for the application server where the task is deployed: For the local operating system (deprecated), use a group name that is supported by the local operating system For a stand-alone custom registry (deprcated), use a group name supported by the custom implementation For a stand-alone LDAP registry (deprecated), use a DN of a group entry |
| AlternativeGroupID1 | Optional  | string | An additional group to which the users can belong.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| AlternativeGroupID2 | Optional  | string | An additional group to which the users can belong.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| AlternativeGroupID3 | Optional  | string | An additional group to which the users can belong.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| AlternativeGroupID4 | Optional  | string | An additional group to which the users can belong.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| AlternativeGroupID5 | Optional  | string | An additional group to which the users can belong.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| AlternativeID1      | Optional  | string | An additional user ID. Use this parameter to retrieve more than one user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| AlternativeID2      | Optional  | string | An additional user ID. Use this parameter to retrieve more than one user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| AlternativeID3      | Optional  | string | An additional user ID. Use this parameter to retrieve more than one user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| AlternativeID4      | Optional  | string | An additional user ID. Use this parameter to retrieve more than one user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| AlternativeID5      | Optional  | string | An additional user ID. Use this parameter to retrieve more than one user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Users by user ID without named
users

Use this criteria to define a query for users whose
user ID is known, while excluding an explicitly named user ID. Use
short names to specify values, for example, wpsadmin. This criteria
does not require access to a people repository. It is supported by
all of the people directory providers.

| Parameter      | Use       | Type   | Description                                                                           |
|----------------|-----------|--------|---------------------------------------------------------------------------------------|
| UserID         | Mandatory | string | The user ID of the user to retrieve. This parameter supports replacement expressions. |
| AlternativeID1 | Optional  | string | An additional  user ID. Use this parameter to retrieve more than one user.            |
| AlternativeID2 | Optional  | string | An additional  user ID. Use this parameter to retrieve more than one user.            |
| AlternativeID3 | Optional  | string | An additional  user ID. Use this parameter to retrieve more than one user.            |
| AlternativeID4 | Optional  | string | An additional  user ID. Use this parameter to retrieve more than one user.            |
| AlternativeID5 | Optional  | string | An additional  user ID. Use this parameter to retrieve more than one user.            |
| NamedUsers     | Optional  | string | An additional  user ID. Use this parameter to retrieve more than one user.            |