<!-- image -->

# Testing a web service gateway

## About this task

To test
a web service gateway module:

## Procedure

1. In the Business Integration view, expand the module and
double-click Assembly Diagram to open the module
in the assembly editor.
2. In the assembly editor, right-click the export and select Test
Component.
3. The Detailed Properties area of
the test client shows the details of the selected export with the
single interface ServiceGateway. In the list
of operations, select either requestOnly or requestResponse.
4. A generic SOAP message is displayed in the value editor.
In this SOAP message, navigate to the message element
under the Body element.
5. Right-click the message element
and choose Select Element.
6 In the Select Element window, select the concrete elementname by completing one of the following steps:
    - If the service interface of the operation that you are trying
to send to the gateway module is of doc/lit/wrapped style, then select
the operation name from the list.
    - If the service interface of the operation that you are trying
to send to the gateway module is of doc/lit style, then select the
element that represents the WSDL input message part from the list.
7. Click OK. The message element is
replaced with the operation element or the input message part element
that you chose, as shown in the following figure:
8. In the value editor, specify values for the message body.
9 Alternatively, you can import a pre-configured SOAP messageand send it to the service gateway. To import a pre-configured SOAPmessage, complete the following steps:

1. Select XML Editor to open the
XML editor.
2. Click the Import Message icon,
as shown in the following figure:
3. Navigate to the file that contains the SOAP message
and click Open.
10. Click the Continue icon  to begin the test. If the value editor
is open, its value is the value that is sent. Similarly, if the XML
editor is open, its value is the value that is sent.