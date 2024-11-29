<!-- image -->

# Protocol headers

If a request is received at an export or a response is received at an import, you can access the
transport header information, so that logic in the module is based on header values, and those
headers can be modified. If a response is sent from an export or a request is sent from an import,
transport headers can be included in those messages.

If you enable transport header propagation for received messages, all transport headers
(including customer-defined headers) are visible in the service message object (SMO). You can set
the headers to different values, or create new ones. You cannot check or validate the values you
set, and any improper or incorrect headers might cause web service runtime problems.

## SOAPAction

The SOAPAction header is a transport protocol header (either HTTP or JMS). It is transmitted with
SOAP messages, and provides information about the intention of the web service request, to the
service. The WSDL interface for a web service defines the SOAPAction header value used for each
operation. Some web service implementations use the SOAPAction header to determine behavior.

If a SOAPAction header is set in the inbound SOAP request (through a web service export), its
value is placed in the /headers/SMOHeader/Action field of the Service Message
Object (SMO). Otherwise, the value in /headers/SMOHeader/Action is not set.

| Method of web service invocation from the module                                            | SOAPAction value in the target service WSDL                                     | SOAPAction header value set in the outgoing SOAP message   |
|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|------------------------------------------------------------|
| Standard web service import (including dynamic invocation of a web service using an import) | Valid SOAPAction value defined in the target service WSDL                       | SOAPAction value as defined in the target service WSDL     |
| Standard web service import (including dynamic invocation of a web service using an import) | No SOAPAction or an invalid SOAPAction value defined in the target service WSDL | Default SOAPAction value is generated                      |
| 'Pure' dynamic web service invocation (without an import)                                   | Valid SOAPAction value defined in the target service WSDL                       | SOAPAction value as defined in the target service WSDL     |
| 'Pure' dynamic web service invocation (without an import)                                   | No SOAPAction or an invalid SOAPAction value defined in the target service WSDL | Value from the /headers/SMOHeader/Action field of the SMO  |
| From a Dynamic Service Gateway or Proxy Service Gateway module                              | All cases                                                                       | Value from the /headers/SMOHeader/Action field of the SMO  |

An invalid SOAPAction value in the target service WSDL is not defined in the empty string. A
valid SOAPAction value in the target service WSDL is any standard URI.

When a default SOAPAction value is set in the outgoing SOAP message, the value is generated from
the target service WSDL using the following pattern: [WSDL target namespace]/[WSDL port
type name]/[WSDL input or output name].

- the target namespace as http://MyCompany.com
- the port type name as MyService
- the input name as operation1Request