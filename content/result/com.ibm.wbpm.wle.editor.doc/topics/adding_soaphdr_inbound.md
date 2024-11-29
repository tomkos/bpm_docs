# Adding SOAP headers to an outgoing response message

## About this task

IBM® Business Process
Manager provides a system variable that allows you to add SOAP headers
to an outbound response message, tw.system.header.soap.response.
You can instantiate the tw.system.header.soap.response variable
from the Variables tab above the process diagram
or in the JavaScript code.

## Procedure

To add a header
that is called sessionToken to the response message,
use JavaScript code such
as the following example. Follow these best practices as you write
your code:

- Make sure namespaces are fully qualified, as they are in the following
examples.
- Avoid white spaces in the XML snippet that constitutes the SOAP
header value.
- Make sure that you only instantiate the tw.system.header.soap.response variable
if it is null.  Otherwise, you could end up clearing out SOAP header
entries that were added by some other component within your general
system service.

```
log.info(">>>>>> Adding a SOAP header to the response message...")

// Create the header object
var myResponseHeader = new tw.object.SOAPHeader()
myResponseHeader.name = "sessionToken"
myResponseHeader.nameSpace = "http://acme.com"
myResponseHeader.value = "<x:sessionToken xmlns:x=\"http://acme.com\">abdf-128974-33-33-fcea-10243-74-33</x:sessionToken>"

// If the response header system variable doesn't exist yet, 
// then you must instantiate it
if (tw.system.header.soap.response == null) {
     tw.system.header.soap.response = new tw.object.SOAPHeaders()
     tw.system.header.soap.response.headers = new Array()
 }  

// Determine which index we need to use when adding the new header entry.
//Add the new header at the end of the array so that the processing does not
// overwrite any existing entries.
var nextIndex = tw.system.header.soap.response.headers.listLength
log.info("Adding new header at index: " + nextIndex)
tw.system.header.soap.response.headers[nextIndex] = myResponseHeader
```

- Only the value of the SOAPHeader is used to construct a response soap message. The name and
namespace are not used. In the example, if you change the value of  
myResponseHeader.name or myResponseHeader.nameSpace, but do not change
myResponseHeader.value, the change is not reflected in the response message.
- Use the next available index when adding your new SOAP header entry to the
tw.system.header.soap.response variable headers field, which is an array
of SOAP header values. Otherwise, you might inadvertently clear out an existing SOAP header entry
that was added by some other component within your general system service.