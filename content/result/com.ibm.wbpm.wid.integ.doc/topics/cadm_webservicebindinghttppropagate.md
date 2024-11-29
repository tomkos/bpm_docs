<!-- image -->

# Transport header propagation

- When requests are received at an export or responses are received at an import, the transport
header information can be accessed, allowing logic in the module to be based on header values and
allowing those headers to be modified.
- When responses are sent from an export or requests are sent from an import, transport headers
can be included in those messages.

- With interim fix JR62209 installed, proxyHost,
proxyPort, and proxyType are honored when specified in the
HTTP ProxySettings header information.
- Authentication-related settings are honored when username and
password are specified in the HTTP authentication header.

## Specifying propagation of headers

1. From the Properties view of Integration Designer, select Binding > Propagation.
2. Set the transport header propagation option that you require.

## Accessing the header information

When transport
header propagation is enabled for received messages, all transport
headers (including customer-defined headers) are visible in the service
message object (SMO). You can set the headers to different values
or create new ones. Note, however, that there is no checking or validation
of the values you set, and any improper or incorrect headers might
cause web service runtime problems.

- Any changes to the headers that are reserved for the web service
engine will not be honored in the outbound message. For example, the
HTTP version or method, Content-Type, Content-Length and SOAPAction
headers are reserved for the web service engine.
- If the header value is a number, the number (rather than the string)
should be set directly. For example, use Max-Forwards = 5 (rather
than Max-Forwards = Max-Forwards: 5) and Age
= 300 (rather than Age = Age: 300).
- If the request message is less than 32 KB in size, the web service
engine removes the Transfer-Encoding header and instead sets the Content-Length
header to the fixed size of the message.
- The Content-language is reset by WAS.channel.http on the response
path.
- An invalid setting for Upgrade results in a 500 error.
- The following headers append the value reserved by the web serviceengine to the customer settings:
    - User-Agent
    - Cache-Control
    - Pragma
    - Accept
    - Connection

- Using a mediation primitive to access the SMO structuresSee
the Related Information links to find information about using
mediation primitives.
- Using the context service SPIThe following sample code reads
the HTTP transport headers from the context service:HeadersType headerType = ContextService.INSTANCE.getHeaders();
HTTPHeaderType httpHeaderType = headerType.getHTTPHeader();
List HTTPHeader  httpHeaders = httpHeaderType.getHeader();
if(httpHeaders!=null){
	for(HTTPHeader httpHeader: httpHeaders){
	  String httpHeadername = httpHeader.getName();
	  String httpHeaderValue = httpHeader.getValue();
		 	 }
}
List PropertyType  properties = headerType.getProperties();
if(properties!=null){
	 for(PropertyType property: properties){
	  String propertyName = property.getName();
	  String propertyValue = property.getValue().toString();
		 	 }
}

## Troubleshooting

If you encounter problems
when sending the revised headers, you can intercept the TCP/IP message
by using tools such as the TCP/IP Monitor in Integration Designer. You access
the TCP/IP Monitor by selecting Run/Debug > TCP/IP Monitor from the Preferences
page.

You can also view the header values using the JAX-WS engine
trace: org.apache.axis2.*=all: com.ibm.ws.websvcs.*=all: