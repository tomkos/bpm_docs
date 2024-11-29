# Creating and managing groups

## Before you begin

## About this task

The default installation of Business Automation Workflow provides a federated
repository that contains the WebSphere® Application
Server file registry. To
implement an external security provider, which uses a different user registry than the WebSphere Application
Server file registry, you must
add the provider to the federated repository. Several types of repositories are supported, including
the local operating system registry, a stand-alone Lightweight Directory Access Protocol (LDAP)
registry, a stand-alone custom registry, and federated repositories.

See the related links for more information about registries and external security providers.

- Users and groups created in the WebSphere Application
Server administrative console are
stored in the file registry.
- Internal users and groups are managed through the Process Admin Console.

For a list of default groups, see IBM Business Automation Workflow default group types.

## Procedure

- To create and remove groups, add users to groups, and remove users from groups, go to themenu in the Server Admin area of the Process Admin Console and locate the option that youneed. Tips: Restriction: You can't delete a group that has tasks assigned or is configured asbpmAdminGroup in the BPMServerSecurityGroups configuration.
    - To see all the groups, enter ** in the Select Group to
Modify field.
    - * is the only recognized wildcard character supported for the Search
for Name field.
- To return a list of members of a nested group for an LDAPrepository:

1. Run the following
command: $AdminTask setIdMgrCustomProperty { -id Ldap Repository Id -name com.ibm.ws.wim.adapter.ldap.returnNestedNonGroupMembers -value true}For
example:wsadmin>$AdminTask setIdMgrCustomProperty { -id LDAP1 -name com.ibm.ws.wim.adapt er.ldap.returnNestedNonGroupMembers -value true}
2. Save the changes and exit. 
wsadmin>$AdminConfig save
wsadmin> exit
3. Restart the server.