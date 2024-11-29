# Local documents

- Local documents at development time
- Local documents at run time
- Duration of a local document
- How to make local documents permanent

## Local documents at development time

You must do set up work at development time to allow your users to create local documents. Begin
by checking that Allow locally managed documents is selected in the
Folder Management section of the Folders tab in the
editor. See Selecting IBM Business Automation Workflow or an external ECM system to manage folders.

```
tw.local.folderId = tw.system.processInstance.processInstanceFolderId;
tw.local.serverName = tw.system.processInstance.caseFolderServerName;
```

```
tw.local.folderId = tw.system.currentProcessInstance.processInstanceFolderId;
tw.local.serverName = tw.system.currentProcessInstance.caseFolderServerName;
```

Depending on your business process, you might also configure a BPM Document
List control to view local documents based on a search criteria that gets all or some local
documents. See BPM Document List.

Local documents are, in structure, workflow documents. They can be constructed and worked with
programmatically by using REST APIs and JavaScript APIs. The local documents that you create are
automatically added to the BPM folder of the instance you attach the document to unless you specify
the input parameter hideInPortal as true. Use the Create document operation
of the BPM document store to
create a local document using a content integration step in a service implementation. To see how Business Automation Workflow documents work with the
IBM® Business Automation
Workflow tools, see
Working with BPM documents. For APIs, see REST APIs and JavaScript API.

To add an already existing local document to a BPM folder, use the Add document to
folder and Remove document from folder operations that are used
with the BPM document store. For information on these operations, see Data mapping in Enterprise Content Management operations, Outbound operations for external ECM systems and BPM stores and Building a service that integrates with an ECM system or a BPM store.

## Local documents at run time

1 Select the type of content, a file, or a link to a URL.
    - Browse to the file, if a file is selected.
    - Enter the URL address, if a URL is selected.
2. Enter a name for the local document. A name is required.
3. Add a check mark to Add another document, if you want to continue
creating more documents.
4. The local document is created when you click OK.

## Duration of a local document

Business
process instances, that is, business processes that are in use, often
last a long time. During that time, new ECM content becomes available
that can be helpful to the users of the business process. Local documents
allow users to bring that ECM content into the business process for
the duration of the business process.

<!-- image -->

If you think a local document can
be useful for other processes, you can take steps to turn it into
a permanent document on an external ECM system. See How to make local documents permanent.

## How to make local documents permanent

1. Start by creating an integration service with a Content Integration
node. Your integration service then can use the operations in the
next steps to move your local document content to a document on an
external ECM system. See Building a service that integrates with an ECM system or a BPM store.
2. Retrieve the content of the local document, that is, the Business Automation Workflow document,
by using a Get document content operation on
the BPM document store.
See Working with document content.
3. Create a document on an external ECM system by using a Create
document operation. Use the output from the previous operation
for the content of the new document by using the Content stream (ECMContentStream)
input parameter. See Outbound operations for external ECM systems and BPM stores.
4. Optionally, add a reference to the new document you created in
the current process instance by using an Add document to
folder operation on the BPM managed store.
See Data mapping in Enterprise Content Management operations.
5. Delete the local document, that is, the Business Automation Workflow document,
by using a Delete document operation on the BPM document store. See Data mapping in Enterprise Content Management operations.