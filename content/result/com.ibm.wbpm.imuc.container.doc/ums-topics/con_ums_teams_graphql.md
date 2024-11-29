# User Management Service Teams GraphQL API

- GET: Retrieve team data according to a GraphQL query.
- POST: Retrieve or modify data according to a GraphQL query or mutation. Remember: In
GraphQL terminology, a modification is know as a "mutation".

Whereas the UMS Teams REST API (such as GET teamserver/rest/teams) usually omits
any fields with a null value in the response, GraphQL sets such requested fields explicitly to
null.

UMS Teams does not support GraphQL subscriptions.

- User Management Service Teams GraphQL schema

 Containers: 
UMS Teams supports GraphQL queries with respect to a schema that is defined in the SDL language.
- User Management Service Teams GraphQL error handling

 Containers: 
The GraphQL system does not use the normal REST API error handling.
- User Management Service Teams GraphQL example queries

 Containers: 
GraphQL queries can be sent through the GET API as well as through the POST API.
- User Management Service Teams GraphQL example mutations

 Containers: 
You can use mutations to create, replace, or delete teams. Mutations should always use the POST API.