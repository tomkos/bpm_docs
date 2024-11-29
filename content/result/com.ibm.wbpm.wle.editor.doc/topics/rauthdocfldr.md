# Authorization of documents and folders in a process

## Authorization levels on ECM folders and documents

When you start a process, a folder structure is determined by the settings in the
Folders tab. Different levels of authorization are granted to workflow users
to access documents and folders. References are also granted to documents and folders in external
Enterprise Content Management (ECM) systems. These levels of authorization depend on the role that
the current user is assigned for the specific process instance.

The following table shows the user authorization on the workflow managed folders and the
references to external ECM system documents and folders, which are in the managed folders. It also
shows the operations that an authorized user may perform on the folders and documents. Privileged
users are system administrators and members of the Process Portal administration team,
as defined in the process application settings of the started process.

In this table, privileged users are
members of the process instance owner team that is specified for the
process and  other process participants are users who
may view the process instance, for example to work on a task within
the instance.

| Operation or privilege   | Object creator   | Privileged users    | Other process participants    | Any other user   |
|--------------------------|------------------|---------------------|-------------------------------|------------------|
| Add children             | Not applicable   | Yes                 | Yes                           | No               |
| View                     | Yes              | Yes                 | Yes                           | No               |
| Update                   | Yes              | Yes                 | No                            | No               |
| Remove                   | Yes              | Yes                 | No                            | No               |

- A privileged user may modify and remove content that other users
added.
- A privileged user may not modify the content that was created
when the process started. That initial and unchanging content is based
on the process definition information, which is on the Folders tab.
- A non-privileged user who works on a process instance may see
the content of the process instance. This user may add references
to more documents or folders from the external ECM systems only if
you specifically allowed users to add references to more documents
or folders. You authorize users to add these references by selecting
the corresponding options in the Folders tab.
These users may modify and remove the content that they added, but
not the content that others added.
- A non-privileged user who does not work on a process instance
is not allowed to see its content.
- A non-privileged user who may not see a document or folder in
the external ECM system cannot see that document or folder in the
context of the process.
- A non-privileged user who has ACTION\_VIEW\_INSTANCE permission on the process instance can view
or download the document.

When a process instance finishes, the system restricts further Create, Update, and Delete
operations on the content if the Allow content operations after completion
option in the Overview section of the process definition is not selected. The system has no control
over the referenced content. For example, a referenced document might be deleted although it is
referenced by a finished process instance. The document then automatically disappears from the
process instance.

A
process that uses an BPM managed store folder
contains references to documents and folders from external ECM systems.
These external ECM systems define their own access control lists for
the referenced items. When you use Document Explorer or the Get
children content integration step, the external ECM system
defines the actions that you may perform on an item.

- The values of properties in the ECMAllowableActions business object,
canGetFolderParent and removeObjectFromFolder, are
controlled based on the rules in Table 1.
Authorizations are affected in this context because then the folder is an BPM managed store folder.
- The canRenameReference property value specifies
whether the current user is allowed to rename the reference.

## Programmatically determining which children may be
added to an BPM managed store folder

- If Allow external folder references is selected, the list contains
cmis:folder.
- If Allow external document references is selected, the list contains
cmis:document.