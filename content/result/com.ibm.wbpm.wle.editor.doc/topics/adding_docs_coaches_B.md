# Attaching IBM Business Automation Workflow documents to a
heritage coach (deprecated)

## About this task

When you add the Document Attachment control to a heritage coach, documents that were previously
uploaded during completion of an Business Automation Workflow task
are displayed. You can configure the control to display only those documents that match properties
that you set. For example, you can configure the control to display only those documents associated
with a specific client or customer. Plus, you can limit the displayed documents to only those
documents uploaded during the execution of the current process instance. In addition to displaying
documents, you can also configure the Document Attachment control to enable users to upload
additional documents.

## Procedure

The following procedure describes how to display a list of Business Automation Workflow documents in your heritage coach using the
Document Attachment control:

1. Open the service that contains the heritage coach that you want to work with and then click the
Coaches tab.
2. Drag a Document Attachment control from the palette onto
the design area or click to select an existing control.
3. While the Document Attachment control is selected, click
the Presentation option in the properties.
4. Under Display Documents, select
or clear the Associated Process Instance check
box. This setting causes the control to display only those
documents uploaded in previous steps of the running process instance.
The check box is selected by default. When not selected, the control
displays all documents, regardless of instance, BPD, or process application
from which they originated, when disabled. Important: If
you disable this check box, be sure to set properties that clearly
identify the documents to display. If you do not, the number of displayed
documents could be much larger than expected or than is useful.
5. If you cleared the Associated Process Instance check
box, choose one of the following options:

Option
Description

All Properties
Displays only documents that match all properties
that you add.
Click the Add button to
add the properties that will determine which documents are displayed.
Each property should have a name and a value. For example, you might
add a property with a name of client and a value
of smith.

Any Properties
Displays documents that match any of the properties
that you add.
Click the Add button to
add the properties that will determine which documents are displayed.
Each property should have a name and a value. For example, you might
add a property with a name of client and a value
of smith.

Note: The document properties that you add should match the properties set for uploaded documents.
For example, if you want to display documents that users uploaded in an earlier step, examine the
heritage coach for the earlier step to see the properties established for those uploaded documents.
If you want to display documents from a different process, open the BPD and its services and then
examine the properties established for those uploaded documents.
6 Save the heritage coach and then run the service or BPD to test your configuration.
    - If the same service enables users to upload documents in a preceding step, you can run the
service to test the configuration.
    - If not, you must run the BPD so that the current control has access to documents to
display.
7 To configure the same Document Attachment control to enabledocument uploads, complete the following steps. If youdo not want to configure this control for document uploads, clearthe Enabled check box under Upload Documents.

1. Open the service that contains the heritage coach that you want to work with and then click the
Coaches tab.
2. Drag a Document Attachment control from the palette
onto the design area or click a preexisting Document Attachment control
to select it.
3. While the Document Attachment control is selected, click
the Presentation option in the properties.
4. Verify the Enabled check box
under Upload Documents is selected.  The check box is selected
by default. This setting causes the control to display an Add Document
button. When the service runs, the user can click the Add Document
button and then use the fields provided to browse for the URL or file
that they want to upload, provide a title for the document, and then
click OK to upload the document. The user can upload multiple documents
using the control.
5. If you want to supply a default name for all documents
that the user uploads, type the JavaScript for the default in the
Default Name text box.  For example, type <#=
tw.system.user\_fullName #> to make the current user name
the default name for uploaded documents.If you supply
a default name, but want the user to be able to change the default,
click the User Editable check box to enable
it.
6. Click the Add Properties check
box to enable it if you want to add properties to uploaded documents.
Then click the Add button to add the properties
that you want.  Each property should have a name and a
value. For example, you might add a property with
a name of client and a value of smith.
The properties that you add to uploaded documents enhance
the Display Documents capability of the control. All properties that
you add to uploaded documents can be used to select the documents
to display.
7. Save the heritage coach and then run the service or BPD to test your configuration.

## What to do next

To see how these controls appear to users, work with documents
in the Process Portal.