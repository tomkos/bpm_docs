# Embedding documents in a heritage coach (deprecated)

## About this task

The Document Viewer heritage coach control enables you to display the contents of an Enterprise
Content Management (ECM) or IBM® Business Automation Workflow document
in a separate frame directly within a heritage coach. You can configure the Document Viewer heritage
coach control to display one of several documents that the user chooses from a list, or to display a
single document. The heritage coach control works with IBM Content Integrator Enterprise Edition,
enabling users to access documents from FileNet P8 Content Manager and Content Manager.

## Procedure

The following procedure describes how to configure the Document Viewer heritage coach
control to enable users to display a document from a list and configure the Document Viewer heritage
coach control to display a single document:

1. Open the service that contains the heritage coach that you want to work with and then click the
Coaches tab.
2. Drag a Document Viewer control from the palette onto the
design area or click a preexisting Document Viewer control to select
it.
3. Click the Document Viewer option in the properties.
4. For the Association field, choose Document Attachment from
the drop-down list.
5. For the Control field, choose the Document Attachment control currently included in your
heritage coach that you want to associate with this Document Viewer control.
The Document Attachment control establishes the list of documents from which the user can
choose. When a user selects one of the documents, it is displayed in the viewer.
6. Save the heritage coach and then run the service or BPD to test your configuration.
After testing the configuration, you can configure the Document Viewer heritage coach control
to display a single document by choosing the connection type and then completing the configuration
for the chosen connection type.
7 Configure the Document Viewer heritage coach control to display a single document by choosingthe connection type:
    1. Open the service that contains the heritage coach that you want to work with and then click the
Coaches tab.
    2. Drag a Document Viewer control from the palette onto the design area or click a preexisting
Document Viewer control to select it.
    3. Click the Document Viewer option in the properties.
    4. For the Association field, choose None from the drop-down list.
    5. Click the Presentation option in the properties.
    6 Select the Connection Type from the drop-down list: Business Automation Workflow documents, IBM Content Integrator, or URL.
        - Business Automation Workflow
documents
        - IBM Content Integrator
        - URL
8 Complete the configuration for the connection type youselected:

- If you selected Business Automation Workflow documents,
complete the following steps:

1. If not already selected, click the Presentation option
in the properties.
2. Under Display Documents, select
or clear the Associated Process Instance check
box. This setting causes the control to display only those
documents uploaded in previous steps of the running process instance.
The check box is selected by default. When not selected, the control
displays all documents, regardless of instance, BPD, or process application
from which they originated, when disabled. Important: If
you disable this check box, be sure to set properties that clearly
identify the documents to display. If you do not, the number of displayed
documents could be much larger than expected or than is useful.
3 For the First Document Matching field, click AllProperties or Any Properties . The Document Viewer control displays the first document thatmatches the properties that you choose.
    - If you select All Properties, documents
must match all properties that you add to be displayed.
    - If you select Any Properties, if a document
matches any one of the properties that you specify, the control displays
it.
4. Click the Add button to add the
properties that will determine which document is displayed. Each
property should have a name and a value.For example,
you might add a property with a name of client and
a value of smith.Note: The document properties that you add should match the properties set for uploaded documents.
For example, if you want to display a document that the users uploaded in an earlier step, examine
the heritage coach for the earlier step to see the properties established for those uploaded
documents. If you want to display a document from a different process, open the BPD and its services
and then examine the properties established for those uploaded documents.
5. Save the heritage coach and then run the service or BPD to test your configuration.
If the same service enables users to upload documents in a preceding step, you can run
the service to test the configuration. If not, you must run the BPD so that the current control has
access to documents to display.

- If you selected IBM Content Integrator,
complete the following steps:

1. If not already selected, click the Presentation option
in the properties.
2. Provide the following information for the IBM Content
Integrator connection: Note: Before you can access documents
from an ECM repository using the Document Viewer control, IBM Content
Integrator SOA web services must be deployed on an application server.
The IBM Content Integrator documentation provides information
about the WAR file that you can use for deployment and instructions
for configuring the WAR file. See Deploying > Deploying SOA Web Services in
the IBM Content Integrator documentation.
Table 1. Input
required for the IBM Content Integrator connection

Value
Description

IBM Content Integrator (ICI) web service
URL
Select the environment variable that
contains the root URL of the deployed application (SOA web services).
See Setting environment variables to learn how to define
an environment variable of type ICI web service URL.

Repository ID
Select the environment variable that
contains the name of the IBM Content Integrator connector that you
want to use to access the ECM repository. See Setting environment variables to learn how to define an environment
variable of type ICI Connector Name.

User name
User name required to log in to the
ECM repository.

Password
Password required to log in to ECM
repository.
3. In the Item Class Name field,
enter the name of the document type that you want to retrieve from
the ECM repository, and click the Add button.
All properties that exist for the document type that you
specify are displayed. This enables you to choose the properties to
use to determine the document to display. The control displays the
first document that matches the properties that you choose.
4. To remove unwanted properties, click the property name
and then click the Remove button.
5. Optional: Limit the results by entering
filterable text in the Filter Value column.  Note: The
filters that you specify must match the actual property values in
the ECM repository.
For example, if one of the
properties for a document type is ClientIndustry ,
you could limit the results to a specific industry by entering the
following text in the Filter Value column: automotive .
6 For the First Document Matching field, click AllProperties or Any Properties .
    - If you select All Properties, the document
must match all properties that you add to be displayed.
    - If you select Any Properties, if a document
matches any one of the properties that you specify, the control displays
it.
7. Save the heritage coach and then run the service or BPD to test your configuration.

- If you selected URL as the connection
type for the Document Viewer control, complete the following steps:

1. If not already selected, click the Presentation option
in the properties.
2. In the URL field, type the location
of the document that you want to display.
3. Save the heritage coach and then run the service or BPD to test your configuration.