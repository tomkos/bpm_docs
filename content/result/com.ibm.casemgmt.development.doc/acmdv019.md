# Managing workflows, roles, and in-baskets by using the Content Platform Engine REST Service

- Retrieve the contents of an in-basket that are based on the role
of a case worker
- Retrieve the workflow step element when the case worker opens
a workflow
- View and update the work items in a workflow
- Track workflow processes
- Retrieve the process history for a workflow
- View and update workflow roles, including adding users and groups
to roles
- View all assigned work in a case

| Resource                                        | URI resource name                                  | Description                                                                                                                                                                                                                             |
|-------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Application space names                         | /appspacenames                                     | Gets the collection of the names of the application spaces, including the application spaces to which the current user does not have access permissions. You can use this information to select an application space for page creation. |
| MyRoles                                         | /appspacenames/{appspace}/myroles                  | Gets a collection of roles within an application space.                                                                                                                                                                                 |
| Role                                            | /appspacenames/{appspace}/roles/{role}             | Get the role information and in-baskets that are associated with the specified role.                                                                                                                                                    |
| Writeable application space roles               | /writableappspaces/{appSpace}/roles                | Gets the collection of roles defined for an application space to which you can assign members. To access this resource, you must have write access to the application space.                                                            |
| Writeable application space role members        | /writableappspaces/{appspace}/roles/{role}/members | Gets the set of members that are assigned to a specified role. To access this resource, you must have write access to the application space.                                                                                            |
| Writeable application space role members update | /writableappspaces/{appspace}/roles/{role}/members | Updates the role membership for the specified role. To access this resource, you must have write access to the application space.                                                                                                       |
| Security domains                                | /securitydomains                                   | Gets the names of all the security domains (LDAP realms) found. You can use this information to narrow the scope of users and groups for subsequent operations, such as querying user information for role membership changes.          |
| Users                                           | /users                                             | Gets a collection of users from LDAP. You can limit the search scope by using the domainName GET parameter to specify the domain.                                                                                                       |
| Groups                                          | /groups                                            | Gets a collection of groups from LDAP. You can use this information to select groups for role memberships or work item assignments.  You can limit the search scope by using the domainName GET parameter to specify the domain.        |
| Current user                                    | /currentuser                                       | Gets the name and ID of the user that is currently logged on to the application space.                                                                                                                                                  |

```
http://myserver:9080/CaseManager/P8BPMREST/p8/bpm/v1/appspaces/
Candidate%20Selection%202/myroles?cp=newportvm24\_796\_tos02
```

```
{
  "Customer Service Representative":
  {
    "name":"Customer Service Representative",
    "URI":"appspaces\/Dannay+Insurance+Claims\/roles\/Customer+Service
      +Representative"
  },
  "Adjuster":
  {
    "name":"Adjuster",
    "URI":"appspaces\/Dannay+Insurance+Claims\/roles\/Adjuster"
  }
}
```