<!-- image -->

# Example of a custom fault selector

In this incomplete code sample, a framework of code selects
a fault from the payload in the body of a SOAP message. The sample
finds the correct fault by examining details, which your implementation
would provide (see faultName = "deduce from fault detail";).

```
package com.ibm.wbiserver.faults;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.Reader;
import java.util.Map;

import javax.xml.soap.Detail;
import javax.xml.soap.MessageFactory;
import javax.xml.soap.SOAPBody;
import javax.xml.soap.SOAPException;
import javax.xml.soap.SOAPFault;
import javax.xml.soap.SOAPMessage;

import com.ibm.websphere.dhframework.faults.FaultSelector;
import com.ibm.websphere.sca.bindingcore.WPSBindingContext;

/**
 * This is only a sample. This is not IBM supported code as is.
 */
@SuppressWarnings("unchecked")
public class SOAPFaultDetailFaultSelectorSample implements FaultSelector {
	private static final long serialVersionUID = 6799865355976712457L;
	String faultName = null;
	Map context = null;

	public String getFaultName(Object source) {
		return faultName;
	}

	public ResponseType getResponseType(Object source) {
		ResponseType LocalResponseType = null;
		InputStream inputStream = null;
		if (source instanceof InputStream) {
			inputStream = (InputStream) source;
		} else {
			try {
				inputStream = convertReader((Reader) source, "UTF-8");
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}

		MessageFactory factory;
		try {
			factory = MessageFactory.newInstance();
			SOAPMessage msg = factory.createMessage(null, inputStream);
			context.put(WPSBindingContext.TRANSFORMED\_DATA, msg);
			LocalResponseType = setResponseAndFault(msg);
		} catch (SOAPException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		return LocalResponseType;
	}

	public static InputStream convertReader(Reader source, String encoding)
			throws IOException {

		Reader sourceReader = (Reader) source;
		char[] ch = new char[2];
		StringBuffer buffer = new StringBuffer();
		int len = sourceReader.read(ch);
		while (len != -1) {
			buffer.append(ch, 0, len);
			len = sourceReader.read(ch);
		}
		String sourceString = buffer.toString();
		byte[] sourceBytes = null;
		if (encoding != null) {
			sourceBytes = sourceString.getBytes(encoding);
		} else {
			sourceBytes = sourceString.getBytes();
		}
		ByteArrayInputStream byteArrayInputStream = new ByteArrayInputStream(
				sourceBytes);

		return byteArrayInputStream;
	}

	/**
     * 
     */
	protected FaultSelector.ResponseType setResponseAndFault(SOAPMessage msg)
			throws SOAPException {

		ResponseType theResponse = null;
		SOAPBody body = msg.getSOAPBody();
		SOAPFault soapFault = body.getFault();
		String faultCode = soapFault.getFaultCode();
		Detail faultDetail = soapFault.getDetail();

		// TODO not complete - look at faultDetail and set values
		if (ok) {
			faultName = "deduce from fault detail";
			theResponse = FaultSelector.ResponseType.BUSINESS\_FAULT;
		} else {
			faultName = null;
			theResponse = FaultSelector.ResponseType.RUNTIME\_EXCEPTION;
		}
		return theResponse;
	}

	public void setBindingContext(Map context) {
		this.context = context;
	}

}
```