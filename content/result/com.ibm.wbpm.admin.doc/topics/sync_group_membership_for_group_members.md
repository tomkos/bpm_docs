# Traditional: 
Synchronizing
group membership by groups

Synchronization for group membership takes into account only users that are already in the
Business Automation Workflow database, unless -addMode
users or all is specified. That is, users that either have logged in to
Business Automation Workflow or have been synchronized to Business Automation Workflow using one of the available user synchronization
commands. All other users will not be considered by the synchronization commands to be group
members. If -addMode users or all is specified, synchronization of
group membership will add users that are members of the affected groups to the Business Automation Workflow database, if those users don't already exist in
the database.

To synchronize group membership by groups, use the following commands, which are located in the
deployment manager profile\_root/bin
directory and are available for both Windows and Linux environments:

- If you omit the addMode parameter, groups are added but no users are
added.
- If you specify groups, the groups found in the user registry but not found in
the database are added to the database before synchronizing the group memberships. Otherwise, only
groups that already exist in the database are synchronized.
- If you specify users, the users that are members of the affected groups in the
user registry are added to the database while synchronizing the group memberships. Otherwise, only
the group membership of users that already exist in the database are synchronized, but no user is
added to the database.
- If you specify all, the groups and the users of the affected groups are added
to the database while synchronizing their group memberships.
- If you specify none, no group or user is added to the database, but the group
memberships of users and groups that exist already in the database are updated.

The output of the command indicates the number of synchronized
groups.

- The group is not available in the user registry
- The group has a short name that occurs more than once in the user
registry
- The group is already defined with the same short name in Business Automation Workflow as a
non-security group (that is, a group created using the Process Admin
Console)

If federated repositories are not configured for Websphere security,
the Websphere user registry interface is used for execution.

If federated repositories are configured for WebSphere Application
Server security, the Virtual Member Manager (VMM) of the Websphere
module is accessed directly, which results in significantly better
performance. Because of this, consider employing federated repositories.

If federated repositories are configured and VMM is used along
with Lightweight Directory Access Protocol (LDAP) directories, apply
the configuration described in  Traditional: Configuring VMM and IBM Business Automation Workflow for optimized group membership synchronization for VMM and Business Automation Workflow, respectively.

- Traditional: Configuring VMM and IBM Business Automation Workflow for optimized group membership synchronization

Use this task to configure Virtual Member Manager (VMM) and IBM Business Automation Workflow for optimized group membership synchronization.
- Configuring Business Automation Workflow to handle white space and letter case variations in the LDAP server

You can configure Business Automation Workflow to 			enable or disable the actions of detecting and removing white spaces and normalizing 			capitalization in distinguished names in a Virtual Member Manager (VMM) LDAP 			repository.