<!-- image -->

# Specifying values for web services exports with SOAP messages

## Before you begin

## About this task

## Procedure

1. Open a test case for a web services export in the test
suite editor, as described in the topic "Opening the test suite editor."
2. In the Test Cases area, select an
invocation for your export.
3. In the Module field, ensure that
the correct module is selected.
4. In the Component field, ensure that
the export is selected that you want to test. The test suite editor
will list all exports found in the selected module or in any libraries
or projects that are referenced by the module. If the test suite editor
supports the binding type used by the export, the Binding
type is supported check box is selected.
5. In the Interface and Operation fields, ensure that the correct interface and
operation are selected.
6 The SOAP messages can be imported as values or as sourcein both the In column and the Expected column of the test data table. By default, when you import a SOAPmessage, the data table shows the SOAP message values in the datatable fields. If you want to work with the SOAP message as an XMLdocument in the test data table, complete the following steps:
    1. In the test data table, right-click the soap:Envelope
and select Set Format > XML.
    2. In the test data table, right-click the request variable and select Import from File.
The Import from File window opens.
    3. In the Files of type field of
the Import from File window, select either .xml or .http.
    4. In the Import from File window
box, navigate to the XML or HTTP file that you want to import and
click Open. The variable is populated with
the SOAP message and the cell is populated with the source because
you set the format to XML. In the cell editor shown in
the figure you can edit the source directly. Alternatively,
you can copy the content to another editor and then edit it and paste
the edited content back into the cell editor.When the format is
set to XML, the child nodes of the envelope disappear and the envelope
value is editable in either the In or Expected column. When the format is set to Literal, the
child nodes are either already there or can be added using the Add Children menu item. If the XML format has a string
entered and you switch to Literal format, the string will turn red
because it is invalid on a complex type in that format.
    5. If you want to import source from another file, right-click
any node in the editor and select Import from File.