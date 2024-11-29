# SOAP headers

SOAP is a lightweight, XML-based protocol that you can use to exchange
information in a decentralized, distributed environment. You can use
SOAP to query and return information and to invoke services across
the Internet with SOAP messages.

SOAP messages are exchanged in a request-and-response format. When IBM® Business Automation
Workflow sends
a request to a web service, the web service returns the requested
values. These values are specified in a SOAP message.

- An envelope, which defines what is in the message and how to process
it
- A set of encoding rules for expressing instances of application-defined
data types
- A convention for representing procedure calls and responses

Each SOAP message must contain a SOAP envelope element.
The SOAP envelope describes what is in the message and provides instructions
about how to process it. The SOAP envelope has two child elements:
a body (required) and a header (optional). All the elements must be
declared in the namespace for the SOAP envelope.

The SOAP body element contains the SOAP message that is associated
with a web services request or response. The body typically contains
the value of input parameters for a request message and the value
of output parameters for a response message.

The SOAP header is an optional section in the SOAP
envelope, although some WSDL files require that a SOAP header is passed
with each request. A SOAP header contains application-specific context
information (for example, security or encryption information) that
is associated with the SOAP request or response message. There is
only one SOAP header section in a SOAP request. If the SOAP header
element is present, it must be the first child element of the envelope
element. SOAP headers can be input, output, or input and output, and
you do not need to specify them in the WSDL file.

- Define the SOAP header in the WSDL definition as part of the SOAP binding. You indicate these
headers by using a <soap:header> tag in the
<wsdl:input> and <wsdl:output> elements in the WSDL
file. When Business Automation Workflow sends a request to the
server that hosts the web service, the SOAP message includes the SOAP header.
- Copy headers directly from system variables, or from user-defined variables of the correct type,
into the predefined request and response SOAP header data types. This SOAP header is considered
implicit because it is not part of the SOAP binding. For more information, see Creating implicit SOAP headers for outbound web service integrations.
- Capture an incoming SOAP header in the response. In the Properties view, select the
Data Mapping tab and map the incoming SOAP header to an existing
SOAPHeader or SOAPHeaders variable. System variables are
supplied or you can create your own variables of the SOAPHeader or
SOAPHeaders type. This SOAP header is also considered implicit because it is
not defined in the WSDL file.