# Attaching ECM documents to a heritage coach (deprecated)

## Before you begin

When you add the Document Attachment control to a heritage coach, documents from the connected
ECM repository can be displayed. You should configure the control to display only those documents
that match properties that you set. For example, you can configure the control to display only those
documents associated with a specific client or customer. In addition to displaying documents, you
can also configure the Document Attachment control to enable users to upload additional documents to
the ECM repository.

Before you can attach documents stored in an Enterprise Content Management (ECM) repository to a
heritage coach, you need to establish a connection to the repository as described in Choosing the type of documents to attach to a heritage coach. After the connection is established, you can use the Document
Attachment heritage coach control as described in the following procedure.

## Procedure

The following procedure describes how to display a list of ECM documents in your
heritage coach using the Document Attachment control:

1. Open the service that contains the heritage coach that you want to work with and then click the
Coaches tab.
2. Drag a Document Attachment control from the palette onto
the design area or click to select an existing Document Attachment
control.
3. While the Document Attachment control is selected, click
the Presentation option in the properties.
4. In the Item Class Name field, enter
the name of the document type that you want to retrieve from the ECM
repository, and click the Add button.
All properties that exist for the document type that you
specify are displayed. This enables you to choose the properties to
use to determine the documents to display.
5 Determine whether you want to remove or filter any of thelisted properties: For example, if one of the properties for a document typeis ClientIndustry , you could limit the results toa specific industry by entering the following text in the Filter Valuecolumn: automotive . You can also use an * (asterisk)as a wildcard when establishing filters. For example, enter the followingtext to filter for all properties that begin with auto : auto* .Or, simply enter an asterisk to retrieve documents for all properties: * .
    - To remove unwanted properties, click the property name and
then click the Remove button.
    - To filter for particular properties, enter a value in the Filter
Value column. Important: The filters that
you specify must match the actual property values in the ECM repository.
6 Click All Properties or AnyProperties .

- If you select All Properties, documents
must match all properties that you add to be displayed.
- If you select Any Properties, if documents
match any one of the properties that you specify, the control displays
them.
7. In the Display table, enter the value that you want the heritage coach interface to use as the
label for each property, and enter a value in the Display Value column for each property.
8. Save the heritage coach and then run the service or BPD to test your configuration.
9 Choose one of the following options to configure whetherusers can upload documents to the connected ECM repository using theDocument Attachment control:

- If you do not want to configure the Document Attachment control
to enable document uploads, clear the Enabled check
box under Upload Documents.
- If you want to configure the Document Attachment control to
enable document uploads, complete the following steps:

1. Open the service that contains the heritage coach that you want to work with and then click the
Coaches tab.
2. Drag a Document Attachment control from the palette
onto the design area or click a preexisting Document Attachment control
to select it.
3. While the Document Attachment control is selected, click
the Presentation option in the properties. By default,
the Enabled check box under Upload Documents
is selected. This setting causes the control to display an Add Document
button. When the service runs, the user can click the Add Document
button and then use the fields provided to browse for the file that
they want to upload to the ECM repository, provide a title for the
document, and then click OK to upload the document. The user can upload
multiple documents to the connected ECM repository using the control.
4. If you want to supply a default name for all documents
that the user uploads, type the JavaScript for the default in the
Default Name text box.  For example, type <#=
tw.system.user\_fullName #> to make the current user name
the default name for uploaded documents.
5. If you supply a default name, but want the user to be
able to change the default, click the User Editable check
box to enable it.
6. Click the Add Properties check
box to enable it if you want to add properties to uploaded documents.
Then click the Add button to add the properties
that you want.  Each property should have a name and a
value.
7. Save the heritage coach and then run the service or BPD to test your configuration.

## What to do next

To see how these controls appear to users, work with documents
in the Process Portal.