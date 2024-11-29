# Runtime user availability and lifecycle

Business Automation Workflow retrieves its user
information from the WebSphere® Application
Server user registry. Similarly,
WebSphere Application
Server retrieves its
user information from the configured user registries, such as LDAP or a custom user registry. For
more information, see Securing process applications.

## User activation

- A user logs in to the product.
- You use the usersSync or usersFullSync
command to synchronize the Business Automation Workflow database with the user
registry. For information about these commands, see Synchronizing users.
- You create a user in the WebSphere Application
Server default file repository by
using the user management section of the Process Admin Console.
- The user or users REST API resource is called with the
refreshUser parameter.

You can also use these options to activate deactivated users. Generally, users are also
activated when a user refers to another user for the first time through one of the runtime
APIs.

## User deactivation

While users can be removed from the user registry, you cannot delete user entries from the
Business Automation Workflow database.
Therefore, these inactive users are still available for task assignments and collaboration
invitations. However, you can deactivate the inactive users by running the
syncExistingUsers command. This command flags users that are no longer in the
user registry as deactivated in the database. Each time that you run the command, the activation
status of the users is synced with their availability in the user registry. For more information,
see Synchronizing users.

The deactivation flag is checked for new runtime assignments and collaboration invitations that
are triggered either by a REST or JavaScript API call, or by the system as a BPD task assignment.

To handle deactivated users in clients, the user detail objects that are
returned by REST and JavaScript API methods include a user availability status flag. In addition,
the existing REST API method for looking up users allows you to restrict the result to only active
or deactivated users. To identify deactivated users, you can use available methods to search for
tasks that are possibly assigned to the deactivated users and decide on their reassignment.

In some cases, the task
is assigned to a deactivated user or an empty group. Consider defining an alternative user to own
these tasks by configuring the userToOwnTask property of the BPMServerSecurityUsers configuration
object. If the userToOwnTask user is also deactivated, the task is assigned to this user anyway to
make it easier to find these tasks. For more information, see Security configuration properties.