# Adding SOAP headers to a SOAP request message

## Procedure

1. Create a service flow and add a service task.
2. Select the service task and click the Variables tab above the diagram
area.
3. Create the private variable that you will later map to
the SOAP header of the request message. To add a single header entry
to the request message, use the variable type SOAPHeader.
To add multiple headers to the request message, use the variable type SOAPHeaders.
4 Initialize the variable that you created in step 3. You can initialize the variable in three ways: The following example of JavaScript code initializes a privatevariable, requestHeader , which is of the type SOAPHeader andcontains a single header entry: tw.local.requestHeader.name = "sessionId";tw.local.requestHeader.nameSpace = "http://acme.com";tw.local.requestHeader.value = "<x:sessionId xmlns:x=\"http://acme.com\">1237314</x:sessionId>"; Note: Makesure namespaces are fully qualified, as they are in the examples. Note: Tryto avoid white spaces in a SOAP header value. Best practice is toadd the XML snippet without any extra white space. You can include more than one header. The following example of JavaScript code initializes two SOAP headers and adds them to therequestHeaders private variable, which is of the typeSOAPHeaders and contains multiple headers:// Initialize the "subscriptionId" headervar header1 = new tw.object.SOAPHeader();header1.name = "subscriptionId";header1.nameSpace = "http://acme.com";header1.value = "<x:subscriptionId xmlns:x=\"http://acme.com\">123-4567-9012</x:subscriptionId>"; // Initialize the "auditLogUUID" header var header2 = new tw.object.SOAPHeader(); header2.name = "auditLogUUID"; header2.nameSpace = "http://acme.com"; header2.value = "<x:auditLogUUID xmlns:x=\"http://acme.com\">ab74-ffce-3333-feab</x:auditLogUUID>"; // Now add the two headers to the SOAPHeaders variable tw.local.requestHeaders.headers[0] = header1; tw.local.requestHeaders.headers[1] = header2;
    - Define a default value on the page where you created the variable.
    - Add JavaScript code
to a server script component.
    - Click Pre & Post and add JavaScript code to the Pre-execution
Assignments section

```
tw.local.requestHeader.name = "sessionId";
tw.local.requestHeader.nameSpace = "http://acme.com";
tw.local.requestHeader.value = "<x:sessionId xmlns:x=\"http://acme.com\">1237314</x:sessionId>";
```

```
// Initialize the "subscriptionId" header
var header1 = new tw.object.SOAPHeader();
header1.name = "subscriptionId";
header1.nameSpace = "http://acme.com";
header1.value = "<x:subscriptionId xmlns:x=\"http://acme.com\">123-4567-9012</x:subscriptionId>";  

// Initialize the "auditLogUUID" header 
var header2 = new tw.object.SOAPHeader(); 
header2.name = "auditLogUUID"; 
header2.nameSpace = "http://acme.com"; 
header2.value = "<x:auditLogUUID xmlns:x=\"http://acme.com\">ab74-ffce-3333-feab</x:auditLogUUID>";  

// Now add the two headers to the SOAPHeaders variable 
tw.local.requestHeaders.headers[0] = header1; 
tw.local.requestHeaders.headers[1] = header2;
```

5. On the Data Mapping tab of the Properties
view, in the Input Header Mapping section, add your newly created
variable (either requestHeader or requestHeaders)
to map it to a request SOAP header.
6. Complete the definition of the web service integration.
7. Click Save or Finish Editing.
8. Run the service flow by clicking Run  and verify that the SOAP headers
are added to the request message.