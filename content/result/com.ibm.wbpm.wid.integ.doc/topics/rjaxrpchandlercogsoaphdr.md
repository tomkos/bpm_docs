<!-- image -->

# JAX-RPC handler for a SOAP header

- Creating a JAX-RPC handler
- Setting a JAX-RPC handler

## Creating a JAX-RPC handler

Use
the following Java code to create a JAX-RPC handler for working with
the SOAP header.

The final method, cleanHeader,
also should be added to the end of your business process (see Retrieving a Cognos report to see how it
is invoked).

```
package com.ibm.wbit.cognos;

import java.util.Iterator;

import javax.xml.namespace.QName;
import javax.xml.rpc.handler.Handler;
import javax.xml.rpc.handler.HandlerInfo;
import javax.xml.rpc.handler.MessageContext;
import javax.xml.rpc.handler.soap.SOAPMessageContext;

import javax.xml.soap.SOAPEnvelope;
import javax.xml.soap.SOAPHeader;
import javax.xml.soap.SOAPHeaderElement;
import javax.xml.soap.SOAPMessage;
import javax.xml.soap.SOAPPart;

public class CognosRPCHandler implements Handler {
	private static ThreadLocal<SOAPHeader> soapHeader = new ThreadLocal<SOAPHeader>();

	@Override
	public void destroy() {
		// TODO Auto-generated method stub
		System.out.println("@@@@@ CognosRPCHandler: In destroy. Current thread: " + Thread.currentThread().getId() + " Handler instance: " + this.hashCode());
	}

	@Override
	public QName[] getHeaders() {
		// TODO Auto-generated method stub
		System.out.println("@@@@@ CognosRPCHandler: In getHeaders");
		return null;
	}

	@Override
	public boolean handleFault(MessageContext arg0) {
		// TODO Auto-generated method stub
		System.out.println("@@@@@ CognosRPCHandler: In handleFault");
		return true;
	}

	@Override
	public boolean handleRequest(MessageContext arg0) {
		// TODO Auto-generated method stub
		System.out.println("@@@@@ CognosRPCHandler: In handleRequest. Current thread: " + Thread.currentThread().getId() + " Handler instance: " + this.hashCode());
		SOAPMessageContext context = (SOAPMessageContext)arg0;
		
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
		
		return true;
	}

	@Override
	public boolean handleResponse(MessageContext arg0) {
		// TODO Auto-generated method stub
		System.out.println("@@@@@ CognosRPCHandler: In handleResponse. Current thread: " + Thread.currentThread().getId() + " Handler instance: " + this.hashCode());
		SOAPMessageContext context = (SOAPMessageContext)arg0;
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
		
		return true;
	}

	@Override
	public void init(HandlerInfo arg0) {
		// TODO Auto-generated method stub
		System.out.println("@@@@@ CognosRPCHandler: In init. Current thread: " + Thread.currentThread().getId() + " Handler instance: " + this.hashCode());
	}
	
	public static void cleanHeader() {
		soapHeader.set(null);
	}

}
```

## Setting a JAX-RPC handler

To
set the JAX-RPC handler for a service, use the deployment editor.

1. Right-click the module in the Business Integration view
and select Open deployment editor.
2. When the deployment editor opens, check the handler is included
in the configuration.