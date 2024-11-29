# References to external ECM systems from a BPM folder

## Retrieving folders by path

When you define the initial folder structure in the Folders tab of a
process model, you can define folder references and identify the folders by their path. Also, you
can define precondition triggers for activities based on a document that is filed into folder. To
identify a folder, you specify its path. To look up folders by path, the
getObjectByPath operation of the CMIS object services is used.  If you use
the function to automatically create folders, the parent of a folder is determined by removing the
last part of the folder path. For example, if the folder path is /a/b/c, then
the parent folder is identified by the /a/b path.

## Adding references to documents or folders

When you add a reference to a document or folder, you specify their identifier in the
Add document to folder or Add folder to folder
operation on the BPM managed store. The entity in the
ECM system is located by using the getObject operation of the CMIS object
services.

## Retrieving the children of a BPM folder

You use the Get children operation on the BPM managed store to get the children,
the subfolders and documents of a BPM folder. To fulfill this request, the query operation of the
CMIS discover services is invoked in the ECM systems that contain the referenced documents and
folders. The CMIS query uses a WHERE clause to filter on the folders by their
cmis:objectId and for documents by their cmis:versionSeriesId.

- cmis:objectId
- cmis:versionSeriesId (documents only)
- cmis:objectTypeId
- cmis:baseTypeId
- cmis:name

The allowable actions for such items are also not accurate. Items that are deleted in the ECM
system are still shown in the BPM folder, but if you perform operations on them, for example to view
a document, these operations will fail.