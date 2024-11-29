# Permissions for IBM Business Automation
Workflow objects

For some objects, you can set permissions directly on the target
object. This permission type is called direct ACEs. Some objects inherit
permissions from another Content Platform Engine object.
This permission type is called inherited ACEs.

- Case folders
- Case subfolders
- Activities
- Case comments
- Documents

## Direct ACEs

When an object is created, the
creating application can specify its own set of direct ACEs.  Other
direct ACEs are copied from the Default Instance Permissions of the
object ClassDefinition.

For IBM Business Automation
Workflow cases and most of their
related objects, it is a best practice to configure permissions through
inheritance from the Case Type folder, rather than through the Default
Instance Permissions of the Case Type class. Even if you configure
permissions through inheritance, Default Instance Permissions can
still apply to cases and case-related objects that are created. The
default permissions are not always correct for these objects. You
can edit these settings directly as required.

## Inherited ACEs

Because the IBM Business Automation
Workflow event handlers enforce
that case folders reside underneath the Case Type folder, these folders
should inherit their permissions from this case folder. This inheritance
allows permissions for all cases of a given type to be easily adjusted
by changing the permissions on the case type folder.

## CreateInstance permission

Access for creating an instance of a class is controlled by granting the CREATE\_INSTANCE
permission on the ClassDefinition for the class. This access is granted in the class permissions,
not the Default Instance Permissions. By default, CREATE\_INSTANCE permission is granted to
#AUTHENTICATED\_USERS, which means anyone who can log in to the Content Platform Engine. For content management solutions, this setting
means that anyone who can log in can create a document. For case management solutions, however, this
permission might not be appropriate. You might want to allow only certain groups to create a case,
activity, case comment, or document.

## Document classes

While documents can be
associated with a case, they can also be used outside of the case
at the same time. Because of this variation, the case cannot influence
the document permissions. System administrators must configure default
permissions by using default instance security for case-associated
Document classes the same as for documents that are not associated
with a case.