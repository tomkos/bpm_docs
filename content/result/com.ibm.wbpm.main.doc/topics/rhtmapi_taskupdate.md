# Additional restrictions when updating a task instance

Even though a user may be logged on to the client application
with a role that is authorized to update a task, there may be additional
restrictions on which task properties they are authorized to update.

The following table shows which task properties may be updated
by which role.

| Property Name               | Caller's Principal Role   | Caller's Principal Role   | Caller's Principal Role   | Caller's Principal Role   | Caller's Principal Role   | Caller's Principal Role   | Caller's Principal Role   | Caller's Principal Role   | Caller's Principal Role   |
|-----------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
|                             | Administrator             | Editor                    | Originator                | Owner                     | Potential Owner           | Potential Starter         | Reader                    | Starter                   | TaskSystemAdministrator   |
| businessRelevance           | Yes                       | Yes                       | Yes                       | Yes                       | No                        | No                        | No                        | Yes                       | Yes                       |
| contextAuthorizationOfOwner | Yes                       | No                        | Yes                       | No                        | No                        | No                        | No                        | No                        | Yes                       |
| deletionTime                | Yes                       | No                        | Yes                       | No                        | No                        | No                        | No                        | No                        | Yes                       |
| description                 | Yes                       | Yes                       | Yes                       | Yes                       | No                        | No                        | No                        | Yes                       | Yes                       |
| displayName                 | Yes                       | Yes                       | Yes                       | Yes                       | No                        | No                        | No                        | Yes                       | Yes                       |
| dueTime                     | Yes                       | Yes                       | Yes                       | Yes                       | No                        | No                        | No                        | Yes                       | Yes                       |
| durationUntilDeleted        | Yes                       | No                        | Yes                       | No                        | No                        | No                        | No                        | No                        | Yes                       |
| durationUntilDue            | Yes                       | Yes                       | Yes                       | Yes                       | No                        | No                        | No                        | Yes                       | Yes                       |
| durationUntilExpires        | Yes                       | No                        | Yes                       | No                        | No                        | No                        | No                        | No                        | Yes                       |
| escalated                   | Yes                       | No                        | Yes                       | No                        | No                        | No                        | No                        | Yes                       | Yes                       |
| eventHandlerName            | Yes                       | No                        | Yes                       | No                        | No                        | No                        | No                        | No                        | Yes                       |
| expirationTime              | Yes                       | No                        | Yes                       | No                        | No                        | No                        | No                        | No                        | Yes                       |
| name                        | Yes                       | Yes                       | Yes                       | Yes                       | No                        | No                        | No                        | Yes                       | Yes                       |
| namespace                   | Yes                       | Yes                       | Yes                       | Yes                       | No                        | No                        | No                        | Yes                       | Yes                       |
| parentContextID             | Yes                       | No                        | Yes                       | No                        | No                        | No                        | No                        | No                        | Yes                       |
| priority                    | Yes                       | No                        | Yes                       | No                        | No                        | No                        | No                        | Yes                       | Yes                       |
| read                        | Yes                       | Yes                       | Yes                       | Yes                       | No                        | No                        | No                        | Yes                       | Yes                       |
| supportsClaimIfSuspended    | Yes                       | Yes                       | Yes                       | Yes                       | No                        | No                        | No                        | No                        | Yes                       |
| supportsDelegation          | Yes                       | No                        | Yes                       | No                        | No                        | No                        | No                        | No                        | Yes                       |
| supportsFollowOnTasks       | Yes                       | No                        | Yes                       | No                        | No                        | No                        | No                        | No                        | Yes                       |
| supportsSubTasks            | Yes                       | No                        | Yes                       | No                        | No                        | No                        | No                        | No                        | Yes                       |
| type                        | Yes                       | Yes                       | Yes                       | Yes                       | No                        | No                        | No                        | Yes                       | Yes                       |
| workBasketName              | Yes                       | No                        | Yes                       | No                        | No                        | No                        | No                        | No                        | Yes                       |

For example, the table is read as:

- The task owner can transfer his ownership to a user who is already
a potential owner of the task or a task administrator.
- The task administrator can transfer the ownership from the present
owner to anybody.