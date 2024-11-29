# Configuring a file store for an existing object store

## About this task

When you create an object store by using createObjectStoreForContent, a
database storage area is used by default. However, other storage options are available for creating
an object store or for creating additional storage areas.

By default, when an object store is created using a database storage area, a Default
Database Storage Area and a Default Database Storage Policy are
created. For the purposes of this example, say an object store named NEWDB already exists. In the
NEWDB object store, the Storage Areas folder contains the Default
Database Storage Area, and the Storage Policies folder contains
the Default Database Storage Policy.

- Create a file store.
- Update the Default Database Storage Policy with the new file store.
- Remove the Default Database Storage Area from the Default
Database Storage Policy.
- Create a document to store in the new file store.

## Procedure

1 Create a file store:
    1. Create a directory to host the file store content. If the directory is on another system, mount
it on the system where the Content Platform Engine is
installed.
 In this example, a directory named /opt/filestore/ is used to host the
content of the file store.
    2. In the tree view, right-click Storage Areas, and select New
Storage Area. Under Storage Area Type, ensure that
File is selected, and then click Next.
    3. Specify a display name, for example, New File Store Storage Area, then
click Next.
    4. Specify the root directory that hosts the file store content, for example,
/opt/filestore/, and set the Directory structure size to
Large.
    5. Accept the default values for Maximum number of elements
(Unlimited), Maximum size (Maximum allowed
on device), and Deletion method
(Clear).
    6. Set Encryption method to AES Counter Mode with 128-bit
key.
    7. Keep the default values for the remaining fields and properties.
2 Update the Default Database Storage Policy with the new filestore:

1. Click Next to see the Storage Policy options.
2. Under Policy names, select the Default Database Storage Policy,
then click Next to review the summary of the settings that you
specified.
3. Click Finish to complete the creation of the new file store.
3 Remove the Default Database Storage Area from the DefaultDatabase Storage Policy :

1. In the tree view, select Default Database Storage Policy.
2. Under Associated Storage Areas, select Default Database Storage
Area, and then click Remove.
 After the removal, the only remaining storage policy under Default Database
Storage Policy is New File Store Storage Area.

Note: You cannot add new documents to the Default Database Storage Area
because the Default Database Storage Policy points to the New File
Store Storage Area. However, you can still access existing documents that were created
in the Default Database Storage Area.
3. Click Save to save your changes, then click
Refresh.
4 Create a document to store in the new file store:

1. In the tree view, under Browse, right-click Root
Folder and create a new folder named Test.
2. Under Test, create a new document, specify its title (for example,
Doc1), then set Class to
Document, select With content, and then click
Next.
3. Under Document Content Source, click Add to add
content to the new document.
4. Select a large document that helps you to see where the document was stored. , then click
Next
5. Click Next to go through the remaining screens and accept all the
default values, and then click Finish to complete the creation of the
document.
 Note that when you create documents, the default storage policy is always Default
Database Storage Policy, as you removed the Default Database Storage
Area from the Default Database Storage Policy earlier.
6. In the tree view, under Administrative > Storage, select Storage Areas. In the Storage
Areas tab, the New File Store Storage Area is displayed.
7. Under Properties, see the properties of the document that is stored in
the New File Store Storage Area.

Note: For a document that is checked out from a Database Storage Area, any
new document version that is checked in is added to the New File Store Storage
Area. Previous document versions are stored in the Default Database Storage
Area, and all the new versions are stored in the New File Store Storage
Area.

## Results