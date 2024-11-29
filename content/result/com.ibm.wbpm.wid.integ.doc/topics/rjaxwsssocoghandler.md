<!-- image -->

# JAX-WS single sign-on security handler

- Creating a JAX-WS single sign-on handler
- Configuring single sign-on security with Lightweight Third-Party Authentication (LTPA)

## Creating a JAX-WS single
sign-on handler

Use the following Java code to create a
JAX-WS handler for single sign-on security, which includes handling
the Lightweight Third-Party Authentication (LTPA) token.

The
final method, cleanHeader, also should be added to
the end of your business process (see Retrieving a Cognos report to see how it
is invoked).

To specify this handler in your application, see Setting a JAX-WS handler.

```
package com.ibm.wbit.cognos;

import java.security.PrivilegedAction;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import javax.xml.namespace.QName;
import javax.xml.ws.handler.MessageContext;
import javax.xml.ws.handler.soap.SOAPHandler;
import javax.xml.ws.handler.soap.SOAPMessageContext;

import java.util.Iterator;

import javax.xml.soap.SOAPEnvelope;
import javax.xml.soap.SOAPHeader;
import javax.xml.soap.SOAPHeaderElement;
import javax.xml.soap.SOAPMessage;
import javax.xml.soap.SOAPPart;

import com.ibm.ws.security.util.AccessController;
import com.ibm.ws.wssecurity.xss4j.dsig.util.Base64;
import com.ibm.wsspi.security.token.SingleSignonToken;

import javax.security.auth.Subject;
import com.ibm.websphere.security.auth.WSSubject;

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
				// Get the LTPA token
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
				Map<String, List<String>> headers = (Map<String, List<String>>)context.get(MessageContext.HTTP\_REQUEST\_HEADERS);					
				if(headers == null){
					headers = new HashMap<String, List<String>>();
					context.put(MessageContext.HTTP\_REQUEST\_HEADERS, headers);
				}				
				List<String> cookie = headers.get("Cookie");
				if(cookie == null){
					cookie = new ArrayList<String>();
					headers.put("Cookie", cookie);
				}
				cookie.add("LtpaToken2=" + tokenData);
				
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

## Configuring single sign-on security
with Lightweight Third-Party Authentication (LTPA)

A single sign-on configuration is a way of letting users access one or more systems by logging on
once. This configuration involves passing a Lightweight Third-Party Authentication (LTPA) token.
Single sign-on security is only available if Cognos is running on WebSphere Application Server.