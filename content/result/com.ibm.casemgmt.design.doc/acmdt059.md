# Planning for project areas

## About this task

When creating the target object store, you must add users or groups to the administration group
for the target object store so that in the Case administration client  you can easily add the
users to a project area. Users also require access to the target object store for testing in the
design environment or for resetting the test environment. A test environment reset requires that the
target object store users have system administration privileges.

The Case administration client handles
the privileges that are required for a user to access the design object store of the project area.
The Case administration client does not add
the privileges for the group in the target object store and workflow system region, which is why it
is recommended that you plan master group access to a project area before you create the target
object store and workflow system. Doing so saves you the extra step of reconfiguring the target
object store and workflow system configuration group. Add the master group with User object store
permission when you create the object store.

When you set up the workflow system region, you must assign users that is working in project
areas to the workflow system security groups.

In a default project area, it is recommended that you manage users in an LDAP group so that you
can assign the group to the default project area. If you need to add a user later, you can add the
user to the LDAP group and the new user is added automatically to the default project area. The
group designated as the workflow system configuration group is the LDAP group that provides
configuration privileges to the workflow system region associated to the project area. The group
designated as the workflow system administration group is the LDAP group that provides
administration privileges to the workflow system region associated with the project area.

You should also use an LDAP group to manage access to the target object store and give the LDAP
group administration privileges to the object store. If you need to add a user to the project area,
you only need to add the user to the LDAP group to provide the user the administration privileges to
the target object store of the project area.