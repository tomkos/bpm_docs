<!-- image -->

# Testing web service exports with SOAP messages

## Before you begin

## About this task

## Procedure

1. Open the integration test client, as described in the topic
"Opening the integration test client."
2. In the Configuration field, ensure
that the correct test configuration is selected.
3. In the Module field, ensure that
the correct module is selected.
4. In the Component field, select the
export that you want to test. The test client lists all exports found
in the selected module or in any libraries or projects that are referenced
by the module. If the test client supports the binding type used by
the export, the Binding type is supported check
box is selected.
5. In the Interface and Operation fields, ensure that the correct interface and
operation are selected.
6 In the Initial request parameters section, complete one of the following steps:
    - If you want to work with the XML editor, select the XML Editor button. The XML editor cannot be used with
unreferenced attachments. The XML editor opens and displays the SOAP
message in an XML document format.
    - If you want to work with the value editor, select the Value Editor button. Only the value editor can be used
with unreferenced attachments.The value editor opens and displays
the SOAP message template, as shown in the following figure:
7 Complete one of the following steps: The Import from File window opens.

- If you opened the XML editor, click the Import
from File icon .
- If you opened the value editor, right-click any node in the
editor and select Import from File. (If you
right-click a node at the soap:Envelope level in the value editor
and select Import from File, it is equivalent
to clicking the Import from File button in
the XML editor.)
8. In the Files of type field of the
Import from File window, select either .xml or .http.
9. In the Import from File window, navigate to the XML or
HTTP file that you want to import and click Open. The editor is populated with the SOAP message.
10 If your test uses unreferenced attachments, scroll to thebottom of the value editor pane. Right-click attachments and select Add Elements . The number of elementsidentifies the number of attachments. The default number of elementsis 1 for a single attachment. Enter the number of attachments yourmessage will use and click OK . Follow thesesteps for each attachment:

1. Click the Type column beside
the attachment and select the type of attachment from the drop-down
list. Each type has a category and a content type. For example, image
category and jpg type. Select More to see all
available categories and types. If you want to create your own content
type, enter that type in the cell.
2. Click the Value column and enter
the path to the attachment or browse the file system to find the attachment.
An unreferenced attachment must be located in your workspace.
11. If your test uses MTOM attachments, you will be able to
specify the value of a file for any base64Binary field. In this case,
the Test Client will mark the value of the field so that it will be
sent as an MTOM attachment.
12. Click the Continue icon . If the XML editor is open, its value
is the value that is sent. Similarly, if the value editor is open,
its value is the value that is sent.
13. If your test uses unreferenced or MTOM attachments and
you want to view or save the attachments used in the test, select
the Binding element. Click the View
SOAP attachment icon  or the Save
SOAP attachment icon  to view or save each
attachment.
14. When you have finished your testing, create a test case
from your test results by following the instructions in the topic
"Creating test cases from unit tests".

## What to do next