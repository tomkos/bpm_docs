<!-- image -->

<!-- image -->

<!-- image -->

# Planning for security in the production environment

If you must set security on an individual case solution, you can
use the security tools that are included with FileNet® P8 components
to adjust the security settings of a solution.

Solution administrators are responsible for importing and deploying
solutions. Solution administrators also manage post-deployment tasks
such as assigning security to the deployed solution. The users that
act as solution administrators and the groups that are used to manage
them must have GCD domain administrator rights, administrator rights
on the target object store, and Content Platform Engine process
services group rights.

Solution administrators are also involved with defining and applying
security and audit definition configurations. In some organizations
this process might be in collaboration with the business analyst or
solution developer who designed the solution. In that situation, consider
adding those users to the solution administrators group or create
another group to represent those users.

It is a best practice to create a case management master group
to use for assigning access to object stores at the time that you
create the object store. Give this group Use object store permission.
With this method, you can grant new users access to the object store
by adding them to the master group. This approach can prevent issues
with changing security on an established object store.

| Group               | Description                                                                                                                                                                                                                                                                                                                                 |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Case viewers        | Has only read-only access to a case.                                                                                                                                                                                                                                                                                                        |
| Case initiators     | Creates new cases. They might also be able to view case properties. For some applications, this group might be a superset of case workers, or might be combined with case workers.                                                                                                                                                          |
| Case workers        | Views and updates cases and case-related objects. They cannot create cases, delete cases, or change the permission or the owner of case-related objects.                                                                                                                                                                                    |
| Case administrators | Control all case-related objects, including case folders, subfolders, comments, and tasks. Can view the list of roles for a solution for reassigning work only if the group has access to the application space in Content Platform Engine. This group does not necessarily have full control of documents that are associated with a case. |