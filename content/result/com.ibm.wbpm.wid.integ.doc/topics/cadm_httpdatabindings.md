<!-- image -->

# HTTP data bindings

- Use SOAPDataHandler instead of HTTPStreamDataBindingSOAP.
- Use UTF8XMLDataHandler instead of HTTPStreamDataBindingXML
- Use GatewayTextDataHandler instead of HTTPServiceGatewayDataBinding

- Binary data bindings, which treat the body as unstructured binary
data. The implementation of the binary data binding XSD schema is
as follows:<xsd:schema elementFormDefault="qualified"
  targetNamespace="http://com.ibm.websphere.http.data.bindings/schema"
  xmlns:tns="http://com.ibm.websphere.http.data.bindings/schema"
  xmlns:xsd="http://www.w3.org/2001/XMLSchema">

  <xsd:complexType name="HTTPBaseBody">
    <xsd:sequence/>
  </xsd:complexType>

  <xsd:complexType name="HTTPBytesBody">
    <xsd:complexContent>
      <xsd:extension base="tns:HTTPBaseBody">
        <xsd:sequence>
          <xsd:element name="value" type="xsd:hexBinary"/>
     	  </xsd:sequence>
      </xsd:extension>
    </xsd:complexContent>
  </xsd:complexType>
- XML data bindings, which support the body as XML data. The implementation
of the XML data binding is similar to the JMS XML data binding and
has no restrictions on the interface schema.
- SOAP data bindings, which support the body as SOAP data. The implementation
of the SOAP data binding has no restrictions on the interface schema.

## Implementing custom HTTP data bindings

HTTPStreamDataBinding
is the principal interface for handling custom HTTP messages. The
interface is designed to allow handling of large payloads. However,
in order for such implementation to work, this data binding must return
the control information and headers before writing the message into
the stream.

The methods and their order of execution, listed
below, must be implemented by the custom data binding.

- private DataObject pDataObject
- private HTTPControl pCtrl
- private HTTPHeaders pHeaders
- private yourNativeDataType nativeData

- Outbound processing (DataObject to Native format):
    1. setDataObject(...)
    2. setHeaders(...)
    3. setControlParameters(...)
    4. setBusinessException(...)
    5. convertToNativeData()
    6. getControlParameters()
    7. getHeaders()
    8. write(...)
- Inbound processing (Native format to DataObject):

1. setControlParameters(...)
2. setHeaders(...)
3. isBusinessException()
4. getDataObject()
5. getControlParameters()
6. getHeaders()

The convertFromNativeData(...) binding
will not be invoked by the HTTP binding unless isBusinessException()
returns true. If isBusinessException() returns false,
convertFromNativeData(...) will not be invoked until the message data
needs to be read or modified later in the SCA process.

You must
invoke setDataObject(...) in convertFromNativeData(...) to set the
value of dataObject, which is converted from native data to the private
property "pDataObject".

```
public void setDataObject(DataObject dataObject)
			throws DataBindingException {
		pDataObject = dataObject;

}
public void setControlParameters(HTTPControl arg0) {
		this.pCtrl = arg0;
}

public void setHeaders(HTTPHeaders arg0) {
		this.pHeaders = arg0;
}
/*
* Add http header "IsBusinessException" in pHeaders.
* Two steps:
* 1.Remove all the header with name IsBusinessException (case-insensitive) first. 
*   This is to make sure only one header is present.
* 2.Add the new header "IsBusinessException"
*/
public void setBusinessException(boolean isBusinessException) {
		//remove all the header with name IsBusinessException (case-insensitive) first. 
		//This is to make sure only one header is present.
		//add the new header "IsBusinessException", code example:
		HTTPHeader header=HeadersFactory.eINSTANCE.createHTTPHeader();
		header.setName("IsBusinessException");
		header.setValue(Boolean.toString(isBusinessException));
		this.pHeaders.getHeader().add(header);
		
}
public HTTPControl getControlParameters() {
		return pCtrl;
}
public HTTPHeaders getHeaders() {
		return pHeaders;
}
public DataObject getDataObject() throws DataBindingException {
		return pDataObject;
}
/*
* Get header "IsBusinessException" from pHeaders, return its boolean value
*/
public boolean isBusinessException() {
		String headerValue = getHeaderValue(pHeaders,"IsBusinessException");
		boolean result=Boolean.parseBoolean(headerValue);
		return result;
}
public void convertToNativeData() throws DataBindingException {
		DataObject dataObject = getDataObject();
		this.nativeData=realConvertWorkFromSDOToNativeData(dataObject);
}
public void convertFromNativeData(HTTPInputStream arg0){
		//Customer-developed method to 
		//Read data from HTTPInputStream
		//Convert it to DataObject
		DataObject dataobject=realConvertWorkFromNativeDataToSDO(arg0);
		setDataObject(dataobject);
}
public void write(HTTPOutputStream output) throws IOException {
		if (nativeData != null)
		output.write(nativeData);
}
```