<!-- image -->

# JAX-RPC single sign-on security handler

- Creating a JAX-RPC single sign-on handler
- Configuring single sign-on security with Lightweight Third-Party Authentication (LTPA)

## Creating a JAX-RPC single
sign-on handler

Use the following Java code to create a
JAX-RPC handler for single sign-on security, which includes handling
the Lightweight Third-Party Authentication (LTPA) token.

The
final method, cleanHeader, also should be added to
the end of your business process (see Retrieving a Cognos report to see how it
is invoked).

To specify this handler in your application, see Setting a JAX-RPC handler.

```
package com.ibm.wbit.cognos;

import java.security.PrivilegedAction;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

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

import javax.security.auth.Subject;

import com.ibm.websphere.security.auth.WSSubject;
import com.ibm.ws.security.util.AccessController;
import com.ibm.ws.wssecurity.xss4j.dsig.util.Base64;
import com.ibm.wsspi.security.token.SingleSignonToken;

public class CognosRPCHandler implements Handler {
	private static ThreadLocal<SOAPHeader> soapHeader = new ThreadLocal<SOAPHeader>();

	@Override
	public void destroy() {
		// TODO Auto-generated method stub
	}

	@Override
	public QName[] getHeaders() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public boolean handleFault(MessageContext arg0) {
		// TODO Auto-generated method stub
		return true;
	}

	@Override
	public boolean handleRequest(MessageContext arg0) {
		// TODO Auto-generated method stub
		
		SOAPMessageContext context = (SOAPMessageContext)arg0;
		
		try {
			// Get the token from the runAs subject
			String tokenData = "";
			
			final Subject subject = WSSubject.getRunAsSubject();
			Iterator ssoTokensFromSubject = null;
			ArrayList ssoArrayList = new ArrayList();
            // Get the default sso token
            if (subject != null) {
                Set privateCredentials = null;
                Set publicCredentials = null;
                Set newSet = new HashSet();

                privateCredentials = (Set) AccessController.doPrivileged(new PrivilegedAction() {
                    public Object run() {
                        return subject.getPrivateCredentials(SingleSignonToken.class);
                    }
                });
                if (privateCredentials != null && privateCredentials.size() > 0) {
                    newSet.addAll(privateCredentials);
                }

                publicCredentials = subject.getPublicCredentials(SingleSignonToken.class);
                if (publicCredentials != null && publicCredentials.size() > 0) {
                    newSet.addAll(publicCredentials);
                }

                ssoTokensFromSubject = newSet.iterator();
            }

            if (ssoTokensFromSubject != null) {
                while (ssoTokensFromSubject.hasNext()) {
                    SingleSignonToken ssoToken = (SingleSignonToken) ssoTokensFromSubject.next();
                    if (ssoToken != null) {
                        byte[] ssoTokenBytes = ssoToken.getBytes();
                        tokenData = Base64.encode(ssoTokenBytes);
                        break;
                    }
                }
            }
			
			// Set the Cookie
			HashMap sendTransportHeaders = new HashMap();
			sendTransportHeaders.put("Cookie","LtpaToken2=" + tokenData);			
			context.setProperty(com.ibm.websphere.webservices.Constants.REQUEST\_TRANSPORT\_PROPERTIES, sendTransportHeaders);
			
			// Set the soap header
			SOAPMessage message = context.getMessage();
			SOAPPart soapPart = message.getSOAPPart();
			SOAPEnvelope soapEnvelope = soapPart.getEnvelope();
			if (soapEnvelope.getHeader() == null) {
				soapEnvelope.addHeader();
			}
	
			// Set the soap header got from the response
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
	}
	
	public static void cleanHeader() {
		soapHeader.set(null);
	}

}
```

## Configuring single sign-on security
with Lightweight Third-Party Authentication (LTPA)

A single sign-on configuration is a way of letting users access one or more systems by logging on
once. This configuration involves passing a Lightweight Third-Party Authentication (LTPA) token.
Single sign-on security is only available if Cognos is running on WebSphere Application Server.