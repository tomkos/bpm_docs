# Content Management toolkit

There is a separate version of the Content Management toolkit for each of the following target
installation environments:

- Traditional (8.6.0.0)
- Traditional or Container (8.6.0.0\_TC)

- The dependency on the Responsive Coaches toolkit
- The BPMDocumentOptions, BPMDocumentDisplayOptions, BPMDocumentUploadOptions, and
CMISDocumentOptions DocumentSelection business objects
- All managed assets not prefixed with BPMExt

The help topics for these Traditional-only views and services are flagged with the following
icon:

Traditional:

- To customize a view, always clone both the view and its corresponding service and scripts, and
make your changes on the copies of the artifacts.
- If you create Process Portal dashboards by usingthe views and services in the toolkit, the behavior or visualization of the page might change if youupgrade to a newer version of the toolkit. If you want to retain the existing behavior of theProcess Portal application,take one of the following actions:
    - Copy the views and the services and scripts that you need to the new version of the
application.
    - Do not upgrade to the newer version of the toolkit.
- The views in the Content Management toolkit are built using the views in the UI toolkit. When
customizing any content views, the above points should also be considered for the UI toolkit
views.

- Settings for upload of large documents

In order to upload large documents of sizes greater than 1GB, some configuration settings are required.
- BPM Document List

The BPM Document List view displays (in tabular form) files in the BPM content store. It provides under one view the ability to upload, delete, and change the properties of documents. It also allows users to view revisions associated with a file. This view aggregates the BPM File List, BPM File Properties, BPM File Revisions, and BPM File Uploader views as a simpler-to-use but less customizable alternative to the modular views it contains.
- BPM File Dropzone

Using the BPM File Dropzone view, you can drag or select files from your computer file system to store in the BPM document store.
- BPM File List

The BPM File List view displays (in tabular form) files and documents contained in the BPM content store.
- BPM File Properties

The BPM File Properties view enables users to view, change, and delete properties associated with a BPM file or document.
- BPM File Revisions

The BPM File Revisions view displays (in tabular form) revisions of a BPM file or document for an associated ID. Events can be fired from user actions on the list, such as clicking on a file to view its content.
- BPM File Uploader

The BPM File Uploader view allows the user to select and upload a file from their computer. The file can be assigned specific properties and targeted to a particular BPM folder.
- Document Explorer

The Document Explorer view displays documents in the BPM content store and any other referenced ECM folders and documents in the folder structure of a process instance. If users are authorized, they can search, create, delete, and rename folders. They can also upload, view, check out, and remove documents.
- Document Reference

The Document Reference view displays referenced files and folders.
- ECM Document List

The ECM Document List view displays (in tabular form) files and documents from a folder in a configurable ECM store. Events can be fired from user actions on the list, such as clicking file to view its content. Files can also be deleted from the list, if allowed through configuration.
- ECM File List

The ECM File List view displays (in tabular form) files and documents from a folder in a configurable ECM store.
- ECM File Properties

The ECM File Properties view enables users to view, change, and delete properties associated with an ECM file or document.
- ECM File Revisions

The ECM File Revisions view displays (in tabular form) revisions of an ECM file or document for the associated ID. Events can be fired from user actions on the list, such as clicking on a file to view its contents.
- ECM File Uploader

The ECM File Uploader view enables users to select and upload a file from their computer. The file can be assigned specific properties and targeted to a particular ECM folder.
- ECM Folder List

The ECM Folder List view displays (in tabular form) folders from the ECM content store. Events can be fired from user actions on the list, such as clicking on a folder to view its content. Folders can also be deleted from the list, if allowed through configuration.
- File Viewer

Use the File Viewer view to display the contents of a document for a specified URL.
- Services in the Content Management toolkit

The following services are available in the Content Management toolkit for creating user interfaces to work with documents.
- Responsive Document Explorer view (deprecated)

 Traditional: 
Use the Responsive Document Explorer view to display a list of documents and folders for a process instance that is stored in the BPM content store. You can configure a Responsive Document Explorer so that users can add, view, or delete individual folders, and add, view, checkout, download, and remove documents. The Document Explorer uses services to perform these functions.
- Responsive Document List view (deprecated)

 Traditional: 
Use the Responsive Document List view to display a list of documents that are found by a CMIS query in the document repository.
- Responsive Document Viewer view (deprecated)

 Traditional: 
Use the view to display the contents of a document for a given URL.
- Heritage Document Explorer control (deprecated)

 Traditional: 
Use the control to display a list of documents and folders for a case instance that are stored in the BPM content store. You can set configuration options so that users can view, add, or delete individual folders, check documents in and out of the content store, and view, add, or delete documents.
- Heritage Document List control (deprecated)

 Traditional: 
Use the control to display a list of documents that are found by a CMIS query in the document repository. You can set configuration options so that users can create new documents or update existing documents and view the revisions.
- Heritage Document Viewer control (deprecated)

 Traditional: 
Use the control to display the contents of a document for a given URL.