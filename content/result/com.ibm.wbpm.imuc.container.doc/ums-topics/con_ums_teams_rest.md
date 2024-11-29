# User Management Service Teams REST API

## Documentation

After you have deployed UMS Teams, you can access the OpenAPI documentation for the REST APIs
that are available on the server by directing your browser to the URL
https://ums\_host/ibm/api/explorer

The Team Service API on the context path /teamserver manages global teams as a
central service for enabled Business Automation Workflow apps and components.

## Teams

The teams REST API supports the discovery, creation, retrieval, modification, and deletion of
team resources.

- GET: Retrieve team definitions.
- POST: Create a Team definition.

- GET: Retrieve a team definition.
- PUT: Replace a team definition.
- DELETE: Delete a team definition.
- PATCH: Update a team definition incrementally.

- GET: Retrieve the users that are contained in the specified team.

- GET: Retrieve the groups that are contained in the specified team.

## Users

The users REST API supports retrieving information about the current user, checking their team
memberships, and checking their permissions.

- GET: Retrieve information about the current user.

- GET: Retrieve information about the which teams the current user is a member of.

- GET: Returns true if the current user is a member of any of a specified list of teams.

- GET: Returns a list of team actions, where the value true indicates that the
current user is allowed to perform the action. For
example:{
  "canListMyTeams": true,
  "canListAllTeams": true,
  "canViewTeamDetails": true,
  "canCreateTeam": true,
  "canModifyTeam": true,
  "canReplaceTeam": true,
  "canDeleteTeam": true
}

- GET: Retrieves information about the list of users. You can use it to search for users that
match a filter. Important: If users can have multiple email addresses, see Using multiple email addresses.

- GET: Returns a list of team definitions for the teams that the user is a member of.

- GET: Returns true if the specified user is a member of any of a specified list of teams.

## Groups

The groups REST API supports retrieving information about the groups.

- GET: Retrieves information about the list of groups from the user repository, for example LDAP,
by using SCIM. It allows you to search for groups that match a filter.

- Examples: Using the User Management Service Teams REST API

 Containers: 
The following examples illustrate how to perform common actions on teams by using the REST API.
- User Management Service Teams GraphQL API

 Containers: 
Your applications can access and administer User Management Service (UMS) Teams by using GraphQL calls.