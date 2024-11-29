# Configuring coach views for storing and viewing Enterprise Content Management (ECM)
documents

## Before you begin

- BPM document store
- An external ECM server

- Columns: Provides a set of columns to display in the document lists.
- Filter: Provides a set of columns and values to filter on when searching for
documents.
- Document object type ID: Specifies a document type to search for. The default document
type is cmis:document.

You can also provide a full CMIS query value by configuring the CMIS query
option. This query will override all other options described above. Finally, you can also override
the search service associated with this view and provide your own. For more information, see the
topic ECM Document List.

## About this task

Add one of the document coach views to a coach to enable business users to store or view
documents on an ECM server. All of the following steps apply to both the Document Explorer view and
the ECM Document List view, except when otherwise specified.

## Procedure

1. Create a client-side human service.
2. Select a Coach from the palette and drag it onto the canvas.
Specify an appropriate name for the coach and save your work.
3. Open the new coach, and from the palette beneath Content, drag one of
the document coach views onto the canvas.
If you also want to view documents in the coach, drag a File Viewer view onto the canvas.
Tip: If you do not see a Content section on the palette, select
that section from the Filter list.
4. Select the other configuration options that you want for your implementation of the document
coach view that you are using to list documents.
For more information about the configuration properties, see the topics Document Explorer and ECM Document List.
5 Implement the corresponding event handler in the document coach view if you are using the FileViewer view to display a document in the list:
    1. To trigger the File Viewer to display the selected document, implement the following code in
the event handler (where VIEW\_ID is the control ID of the File Viewer
coach):

${VIEW\_ID}.setUrl(doc.url);
For more information, see the topic User-defined events.
    2. For the Document Explorer, implement the On document clicked event
handler. For the ECM Document List view, implement the On file clicked event
handler. Set the data binding for the document coach view.
6. Test the implementation of the document coach view by clicking the Run
service icon in the upper right section of the page:

## What to do next

You might want to update bindings in the documents coach view by using a script; for example,
because the value of your CMIS query provided to the ECM Document List view changed. If you run a
script to update the binding, you must change the previous value. In the following JavaScript
example, the columns are updated by appending text that changes the older values:

```
tw.local.cmisQueryString = "SELECT cmis:name, cmis:objectId ";
if (tw.local.photoCatagory) tw.local.cmisQueryString = tw.local.cmisQueryString + ", PhotoCatagory";
if (tw.local.photoSubject) tw.local.cmisQueryString = tw.local.cmisQueryString + ", PhotoSubject";
if (tw.local.photoLocation) tw.local.cmisQueryString = tw.local.cmisQueryString + ", PhotoLocation";
if (tw.local.photoDate) tw.local.cmisQueryString = tw.local.cmisQueryString + ", PhotoDate";
tw.local.cmisQueryString = tw.local.cmisQueryString + " FROM acpPhoto";

tw.local.testCoachRefresh = tw.local.testCoachRefresh + "XYZ ";
```

The following steps show how to create a search service for the ECM Document
List view:

1. Ensure that you have the correct input and output variables and types by copying the ECM
Document Search Service to your process application.
2. Rename the ECM Document Search Service to an appropriate name; for example,
MySearch.
3. Update the search service as required.The default service handles queries for the ECM
Document List and BPM Document List. You can customize the flow by
removing unnecessary nodes. You can maintain and update the Search ECM Documents node.
4. Use the auto-map function to create the map between the input and output service parameters and
the variables.