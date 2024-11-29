# Adding references

## Before you begin

In the editor, you must select Allow external document references ,
Allow external folder references or both from the Folder
Management section of the Folders tab. You must configure a
Responsive Document Explorer control in a coach, which contains the controls to
add the references.

## About this task

Users add references by selecting the ECM server where they want a reference. Then, they add the
reference to a document or folder on that server. The Responsive Document
Explorer that the users work with must be connected to the BPM managed store.

This procedure describes the default behavior when you use the Add Reference control in the
Responsive Document Explorer. However, you can customize this control for your own circumstances.
See the Example section that follows the procedure.

## Procedure

1. Start the Responsive Document Explorer and click +.
Click Add Reference.
2. In the Add Reference dialog, select a server from the External
ECM Server drop-down list. The servers are the Enterprise Content Management servers
that are defined in the Process Application
 Settings page.
For example, you might have two servers. One server provides corporate information for a
division in Toronto and another server for corporate information in New York. You select the Toronto
server. If your process selected both the Allow external document references
and Allow external folder references check boxes, you see the documents and
folders on the Toronto server.
3. Select a document or folder that you want to add to your process.
For example, you select a folder that is called Tax Information that contains tax
documents. Since your process covers both Toronto and New York, in the Reference
As field you add the name Toronto Tax Information Documents. A name in this field is not
necessary. If you do not add a name, the name of the document or folder on the ECM system is
used.
4. Do you want to add several references? Selecting Add another reference
keeps the dialog open for more references.
5 You can also add documents and folders at the same time as adding references to documents andfolders. The ability to add a document or folder is helpful when you realize as you are working withreferences that your process needs to reference new documents and folders. To add a document or folder requires the permission to do so. When you navigate to a serverand folder combination where adding a document or folder is not permitted, then you do not seeAdd Document or Add Folder .
    1. To add a document, click Add Document. Select a file for the content of
the document, a document type, and fill in any require properties. Selecting Add another
document keeps the dialog open to add more documents. Click OK
when finished. Your new documents are listed in the Add Reference
dialog.
    2. To add a folder, click Add Folder. Add a name for the folder. Selecting
Add another folder keeps the dialog open to add more folders. Click
OK when finished. Your new folders are listed in the Add
Reference dialog.
6. Click Create Reference to add the reference. Continue adding references
if you selected Add another reference.
7. From the list of references that are created, you can select actions on these documents and
folders.
For example, you might open the Toronto Tax Information Documents folder. You are working
on the external ECM server when you use these actions. Since you are working on the external ECM
system, you can download documents, add documents to the external ECM server, and create folders.
You can do any action that is allowed on that ECM server.
8. When finished, close the Responsive Document Explorer.

## Example

You can customize the behavior for Add Reference. One way to customize the behavior is to copy
the Default Get Related ECM Folders Service and modify the code. For example, the default service
implementation returns information on the root folders of all available servers of the process application in which
the process instance was started. The service returns the server name, display name, and an object
ID of each root folder. However, in a certain context you might want only information about a
specific folder in the folder structure of a server. By modifying your copy to get only that folder,
your users do not need to browse through the entire set of returned folders. To add your customized
behavior to the Responsive Document explorer, replace the Default Get Related ECM Folders Service
configuration option with your own customized service.

The Default Get Related ECM Folders Service is also available as a
configuration property on the Default Instance Details template. See Default Instance Details template.