# Retrieving SOAP headers from the SOAP response message

## Before you begin

## Procedure

1. Create a service flow and add a service task.
2. Create a private variable of the type SOAPHeaders.
 This variable will receive the header entries from the SOAP response message.
3. On the Data Mapping tab of the Properties
view, in the Output Header Mapping section, map your newly created
variable to the response SOAP header. When the web service
invocation finishes, this variable is initialized for you and it contains
all the SOAP header entries from the SOAP response message.
4. To access the headers that have been received by the variable, add JavaScript code to Post-execution Assignments on
the Pre & Post tab and add the code there. The following
example shows how to access the header entries. In this example, the private variable
tw.local.responseHeaders is defined on the Variables tab
and mapped to the response SOAP header on the Data Mapping
tab.var myHeader = new tw.object.SOAPHeader();
var numHeaders = tw.local.responseHeaders.headers.listLength();
for (var i = 0; i < numHeaders; i++) {
    if (tw.local.responseHeaders.headers[i].name == "header1") {
        myHeader = tw.local.responseHeaders.headers[i];
    }
}
5. Click Save or Finish Editing.
6. Run the service flow  by clicking Run Service and verify that the SOAP
headers are added to the request message and that the expected SOAP headers are retrieved from the
response SOAP message.