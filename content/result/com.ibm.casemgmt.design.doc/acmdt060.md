# Planning for target environments

## About this task

As you plan your target environments, ensure that you assign the appropriate user privileges when
you create a target object store in the object store creation wizard. It is recommended that you
manage users in LDAP groups so that you can assign groups of users to target environments.

It is a best practice to create a case management master group to use for assigning access to
object stores at the time that you create the object store. Give this group Use object store
permission. You can grant new users access to the object store by adding them to the master group,
which automatically grants the new users permission to access the target environment. This approach
can prevent issues with changing security on an established object store. For information, see Planning for security in the production environment .

Also, use an LDAP group to manage administrator access to the target object store. Give this LDAP
group administration privileges to the target object store. If you need to add an administrative
user to the target environment, add the user to this LDAP group.

When you set up a workflow system, you must assign users who is working in the target environment
to the workflow system administration group.

You can associate a target environment with multiple IBM Content Navigator desktops by adding the
target object store repository to your desktop or by running the task to register the target
environment multiple times. However, only one IBM Content Navigator desktop is used by the test and
assigns  roles URL that is returned by the deployed solution. This desktop is the desktop that was
specified the last time that the register target environment task was run.