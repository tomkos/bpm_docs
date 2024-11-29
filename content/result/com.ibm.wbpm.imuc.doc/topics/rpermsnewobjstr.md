# Permissions required for the new object store

If you followed the instructions in Configuring an existing external Content Platform Engine, you have the correct
permissions on the new external object store. However, if users are experiencing problems that
indicate they do not have the correct permissions, or if you add a user, use the following
information to set the permissions correctly for the FileNet Content
Manager administrative user and for all
FileNet Content
Manager users.

- CONNECT
- MODIFY\_OBJECTS
- PRIVILEGED\_WRITE
- READ\_ACL
- REMOVE\_OBJECTS
- STORE\_OBJECTS
- WRITE\_ACL
- WRITE\_ANY\_OWNER

An access mask in FileNet Content
Manager defines
the operations that a user is allowed to use. The access mask corresponding to these permissions is
838205440.

In FileNet Content
Manager, these permissions are
found in the default Full Control permission group plus the PRIVILEGED\_WRITE
permission.

All other users require these permissions:

- CONNECT
- MODIFY\_OBJECTS
- REMOVE\_OBJECTS
- STORE\_OBJECTS

An access mask in FileNet Content
Manager defines
the operations that a user is allowed to use. The access mask corresponding to these permissions is
15728640.

In FileNet Content
Manager, these permissions are
found in the default Use object store permission group.