<!-- image -->

# JAX-WS handler for a SOAP header

- Creating a JAX-WS handler
- Setting a JAX-WS handler

## Creating a JAX-WS handler

Use
the following Java code to create a JAX-WS handler for working with
the SOAP header.

The final method, cleanHeader,
also should be added to the end of your business process (see Retrieving a Cognos report to see how it
is invoked).

```
public class CognosSOAPHandler implements SOAPHandler<SOAPMessageContext> {
	
	private static ThreadLocal<SOAPHeader> soapHeader = new ThreadLocal<SOAPHeader>();

	@Override
	public Set<QName> getHeaders() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public void close(MessageContext context) {
		// TODO Auto-generated method stub

	}

	@Override
	public boolean handleFault(SOAPMessageContext context) {
		// TODO Auto-generated method stub
		return true;
	}
	
	@Override
	public boolean handleMessage(SOAPMessageContext context) {
		Boolean outboundProperty = (Boolean) context.get(MessageContext.MESSAGE\_OUTBOUND\_PROPERTY); 
		
		if (outboundProperty.booleanValue()) { 
			try {
				SOAPMessage message = context.getMessage();
				SOAPPart soapPart = message.getSOAPPart();
				SOAPEnvelope soapEnvelope = soapPart.getEnvelope();
				if (soapEnvelope.getHeader() == null) {
					soapEnvelope.addHeader();
				}
				
				// set the soap header
				SOAPHeader latestSOAPHeader = soapHeader.get();
				if (latestSOAPHeader != null) {
					Iterator iterator = latestSOAPHeader.getChildElements();				
					while(iterator.hasNext()) {
						SOAPHeaderElement soapHeaderElement = (SOAPHeaderElement)iterator.next();
						soapEnvelope.getHeader().addChildElement(soapHeaderElement);
					}
				}	
			} catch (Exception e) {
				e.printStackTrace();
			}
		} else {
			try {
			SOAPMessage message = context.getMessage();
			SOAPPart soapPart = message.getSOAPPart();
			SOAPEnvelope soapEnvelope = soapPart.getEnvelope();
			soapHeader.set(soapEnvelope.getHeader());
			
			// clear the default soap header.
			soapEnvelope.getHeader().detachNode();			
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		
		return true;
	}
	
	public static void cleanHeader() {
		soapHeader.set(null);
	}
}
```

## Setting a JAX-WS handler

To
set the JAX-WS handler for a service, use the Assembly editor.

1. Select your import, and then in the properties view, select the Binding
> JAX-WS Handlers tab.
2. Add and select your handler from the list and save.