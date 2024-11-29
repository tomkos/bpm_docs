<!-- image -->

# SOAP header information with a JAX-WS handler

Often a specific application needs to manipulate a SOAP
header before execution sends the header to the SOAP components. For
example, you may want to add a SOAP header, remove a SOAP header or
access a SOAP header. To do this, you need to add a JAX-WS handler
or JAX-RPC handler to manipulate the SOAP header with Java code. It
is recommended you have a corresponding schema created as well. This
section provides an example of the code you would create

- Creating a JAX-WS handler for SOAP header information
- Creating a schema for a SOAP header

## Creating a JAX-WS handler for SOAP
header information

To create a JAX-WS handler to access
SOAP header information, first create a basic Java API for XML Web Services (JAX-WS) handlers for your export or
import. It will create stubs for the methods. You next need to implement
the handleMessage method. The following code demonstrates
how to create a SOAP header by using APIs in the javax.xml.soap package.

At
the beginning of the code, comments indicate the XML output that will
result from the handler. To produce that output we create the header
entry element followed by two child elements. The first child element
has a client type that identifies a JAX-WS client. The second child
element has an attribute, which is the information we are looking
for in the SOAP header. Our handler creates a user ID identified by
an email address.

```
public boolean handleMessage(SOAPMessageContext context) {

		try {
			SOAPFactory factory = SOAPFactory.newInstance();

			SOAPMessage m = context.getMessage();
			SOAPPart sp = (SOAPPart) m.getSOAPPart();
			SOAPEnvelope soapEnv = sp.getEnvelope();
			SOAPHeader soapHeader = soapEnv.getHeader();

			// the following XML instance will be created by the code below.
			// <hc:Header1ContextElement
			// soapenv:mustUnderstand="0"
			// xmlns:hc="http://JaxwsHandlerTest">
			// <hc:client\_type>jaxws client</hc:client\_type>
			// <hc:user\_id hc:id\_type="email">joe@ca.ibm.com</hc:user\_id>
			// </hc:Header1ContextElement>

			// create header entry element.
			Name headerContextName = soapEnv.createName(
					"Header1ContextElement", "hc", "http://JaxwsHandlerTest");
			SOAPHeaderElement soapHeaderElement = soapHeader
					.addHeaderElement(headerContextName);
			// mustUnderstand attribute is used to indicate
			// whether the header entry is mandatory or optional for the
			// recipient to process.
			soapHeaderElement.setMustUnderstand(false);

			// create the first child element and set the value
			SOAPElement element1 = soapHeaderElement.addChildElement(
					"client\_type", "hc");
			element1.setValue("jaxws client");

			// create the second child element
			SOAPElement element2 = soapHeaderElement.addChildElement("user\_id",
					"hc");
			// create and set the attribute of second child element.
			Name attributeName = soapEnv.createName("id\_type", "hc",
					"http://JaxwsHandlerTest");
			element2.addAttribute(attributeName, "email");
			// set the element value
			element2.setValue("joe@ca.ibm.com");

		} catch (SOAPException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}

		return true;
	}
```

## Creating a schema for a SOAP header

Next,
we create a schema for our SOAP header. It is in fact good programming
practice to always create a schema for your SOAP messages though IBM® Integration
Designer does
not force you do so. However, you must create a schema if you want
to access SOAP header information in an SCA component. You can create
this schema with the Business Object editor or the XML Schema editor.

In
the code that follows, we specify a client type element and a user
ID element within the header entry element. The namespace name matches
the previous one in the JAX-WS handler, JaxwsHandlerTest.

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema targetNamespace="http://JaxwsHandlerTest"
	xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:Q1="http://JaxwsHandlerTest">
	<xsd:element name="Header1ContextElement">
		<xsd:complexType>
			<xsd:sequence>
				<xsd:element name="client\_type" type="xsd:string" />
				<xsd:element name="user\_id">
					<xsd:complexType>
						<xsd:simpleContent>
							<xsd:extension base="xsd:string">
								<xsd:attribute name="id\_type" type="xsd:string" />
							</xsd:extension>
						</xsd:simpleContent>
					</xsd:complexType>
				</xsd:element>
			</xsd:sequence>
		</xsd:complexType>
	</xsd:element>
</xsd:schema>
```