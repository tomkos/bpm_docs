# Configuring additional system lane users

## About this task

- Use a unique system lane user for each application.
- Use an LDAP user for system lane activities.

## Procedure

To configure additional system lane users, complete the
following steps. Run the commands in the wsadmin scripting tool as
shown in the examples:

1. Specify the deployment environment name, and get the configuration
ID for the deployment environment object.  deName = "De1"
de = AdminConfig.getid("/Cell:/BPMCellConfigExtension:/BPMDeploymentEnvironment:%s/" %deName) where De1 must
be replaced by the actual deployment environment name (can be an empty
string if there is exactly one deployment environment in the WebSphere® Application
Server cell).
2 Follow the appropriate option to add, replace, or removea user.
    - To add a system lane user:
        1. Ensure that the system lane user you want is a local security
user or a user that is accessible from LDAP through the federated
repository configuration.
        2. Create a new authentication alias for the system lane user.
        3. Add the new system lane user: AdminConfig.modify(de, [ [ "SystemLaneUserAuthAliasNames", "NewSysLaneUserAlias" ] ] )
where NewSysLaneUserAlias is the authentication
alias of the new system lane user from step b.You can add one or
more aliases by setting a string that contains a semicolon-separated
list of aliases, for example:additionalSystemLaneUserAliases = ";".join( [ 'NewAlias1', 'NewAlias2', 'NewAlias3' ] )
AdminConfig.modify(de, [ [ "SystemLaneUserAuthAliasNames", additionalSystemLaneUserAliases ] ] )
- To replace the existing system lane user aliases with a newlist:
    1. Delete the existing list.AdminConfig.modify(de, [ [ "SystemLaneUserAuthAliasNames", '' ] ] )
    2. Add the replacement list to the now empty list as described in
step c of the section To add a system lane user.
- To remove a system lane user alias from the existing list:

1. Get the list first, and then remove the unwanted entry.systemLaneUserAliases = AdminConfig.showAttribute(de, "SystemLaneUserAuthAliasNames").split(";")
systemLaneUserAliases.remove( "OldAlias" )
2. Replace the existing list with the modified list as described
in the section "To replace the existing system lane user aliases with
a new list".
3. Save the changes.  AdminConfig.save()
4. Synchronize the nodes, and restart the system to enable
the changes to take effect.