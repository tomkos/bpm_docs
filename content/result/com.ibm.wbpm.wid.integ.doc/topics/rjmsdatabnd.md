<!-- image -->

# Overview of JMS, MQ JMS and generic JMS bindings

- Data bindings
- JMS data bindings
- MQ JMS and MQ data bindings
- Operation types and input and output for JMS data bindings
- Data binding generator

## Data bindings

Data bindings handle the transformation of data passed as a Service Data Object (SDO) in a
				Service Component Architecture-based (SCA) application and the native format for an
				EIS J2C or messaging JMS system. The data binding function handles the request and
				response arguments for both inbound and outbound communication. A joint
				specification from IBM® and BEA called the
				Enterprise Metadata Discovery introduces a new metadata discovery and import model
				for resource adapters and the enterprise application integration (EAI) tools
				framework. The model allows resource adapters to plug into an integration framework
				and improves the usability of adapters within the framework. This specification also
				includes API information on methods discussed in this section.

```
public interface DataBinding extends Serializable { 

	public DataObject getDataObject() throws DataBindingException;
	public void setDataObject(DataObject dataObject) throws DataBindingException;
}
```

From a service binding, there are three specializations
provided: one for Java EE Connector Architecture (J2C), one for JMS
and one for MQ.

When an EIS or messaging import is invoked,
a data binding is used to transform the content of a Service Data
Object (SDO) into the native format of the EIS or messaging system
by the SCA runtime, and when the reply (if any) is received from the
EIS or messaging import, the data binding is used to transform the
native data format into an SDO. When an EIS or messaging export is
invoked, a data binding is used to transform the native data format
into an SDO, and when the reply (if any) is sent back to the caller
a data binding is used to transform the content of the SDO into the
native format of the EIS or messaging system. SDOs in the SCA environment
are business objects.

A
data binding can be specified in the root portion of an import or
export binding.  This simplifies the model when a common data binding
is used for all input and output arguments of the binding. A specific
data binding can also be specified on the method binding for input
and output arguments. A data binding specified at the method level
takes precedence over the data binding specified at the root level
of the binding.

For EIS, a data binding generator can also
be specified for the EIS import or export binding.  The data binding
generator must be specified in the root portion.  The EIS SCA implementation
will then use it to generate a data binding for each input and output
argument.

A data binding generator can also be used with JMS.

On
the left side of the following diagram, a JMS messaging provider makes
a request (that is, invokes an operation in an SCA application) and
receives a response (that is, some data) from that application. When
the messaging provider initiates the call to an SCA function, it uses
an export to access the SCA application.

On the right side
of the diagram, an SCA application makes a request to the JMS provider,
which in turn would invoke a method in an application. The SCA application
receives a response from the application. When the SCA application
initiates the call to a function outside the SCA application, it uses
an import.

1 JMS export binding elements:
    - A Web Services Description Language (WSDL) interface on the export
lists the operations available in the SCA application and specifies
the types of data that can be passed to the SCA application.
    - A data binding specifies the transformation of the data from a
native format, for example, a stream of bytes, to an SCA format such
as XML.
    - A function selector data binding specifies the operation to invoke
on the SCA application.
2 JMS import binding elements:

- A WSDL interface on the import lists the operations that will
be invoked on the remote application; that is, the application outside
the SCA application containing the import.
- A data binding specifies the transformation of the data from an
SCA format, for example, XML, to a native format such as a stream
of bytes.

<!-- image -->

## JMS data bindings

In the
case of a JMS export binding, the format and structure of each incoming
message must be known by the data binding implementation, which turns
it into a data object (DataObject object). In the
case of a JMS import binding, the reverse occurs; namely, the outgoing
data object is turned into the JMS message that is sent to the external
service. The data binding defined for the JMS Service must implement
the com.ibm.websphere.sca.jms.data.JMSDataBinding interface
shown in the following example.

```
public interface JMSDataBinding extends DataBinding {

	public void read(javax.jms.Message message) throws javax.jms.JMSException;

	public void write(javax.jms.Message message) throws javax.jms.JMSException;

	public int getMessageType();

	public boolean isBusinessException();

	public void setBusinessException(boolean isBusinessException);

	static public int OBJECT\_MESSAGE = 0;

	static public int TEXT\_MESSAGE = 1;

	static public int BYTES\_MESSAGE = 2;

	static public int STREAM\_MESSAGE = 3;

	static public int MAP\_MESSAGE = 4;

	static public int JMS\_MESSAGE = 5;

}
```

- com.ibm.websphere.sca.jms.data.impl.JMSDataBindingImplJava -
supports JMSObjectMessage and serializes the DataObject to
or from the object field of the JMSMessage. The object
contents of the message must implement Serializable interface.
 This class extends the general purpose data binding class com.ibm.ws.sca.databinding.impl.DataBindingImplJava,
which provides the function to convert a java.io.serilizable
DataObject to a byte stream and vice versa.
- com.ibm.websphere.sca.jms.data.impl.JMSDataBindingImplXML -
supports JMSTextMessage. This binding serializes
the DataObject into an XML document which conforms
to the schema of the DataObject, and sets it to the
text field of the JMSMessage, or parses an XML document
and sets it into the DataObject. This class extends
the general purpose data binding class com.ibm.ws.sca.databinding.impl.DataBindingImplXML,
which provides the function to convert an XML string to a DataObject and
vice versa.

- setDataObject() - sets the value of the DataObject that
represents the JMS message payload. The DataObject must
conform to the corresponding schema definition.
- getDataObject() - returns a DataObject that
represents the JMS message payload, and which conforms to the corresponding
schema.
- getMessageType() - returns type of JMS message
(defined in the JMSDataBinding interface).
- read(Message message) - sets the value of the DataObject properties
from the JMS message, which is supplied as the method parameter.
- write(Message message) - sets the value of the
payload of the JMS message, which is supplied as the method parameter,
from the DataObject properties.
- isBusinessException() - states whether or not
the DataObject represented by this instance of JMSDataBinding is
to be treated as a business exception or not.
- setBusinessException() - sets whether or not
the DataObject represented by this instance of JMSDataBinding is
to be treated as a business exception.

An example of using the JMSDataBinding can
be seen in Creating a user-defined JMS data binding.

Fault
handling using these methods could be implemented in a similar manner
to the following code:

```
public class Foo implements JMSDataBinding {
	
    private boolean fieldIsBusinessException = false;
	
    public boolean isBusinessException() {
        
        return fieldIsBusinessException;
    }

    public void setBusinessException(boolean isBusinessException) {
    	
    	this.fieldIsBusinessException = isBusinessException;
    }

	public void read(Message message) throws JMSException {
		...
		if(message.propertyExists("IsBusinessException")){
			this.fieldIsBusinessException = message.getBooleanProperty("IsBusinessException");
		} else{ // Unknown other side, default to false
			this.fieldIsBusinessException = false;
		}

	}

	public void write(Message message) throws JMSException {
            ...
		message.setBooleanProperty("IsBusinessException", this.fieldIsBusinessException);
	}
}
```

```
com.ibm.websphere.sca.ServiceManager serviceManager = new 
  com.ibm.websphere.sca.ServiceManager();	
com.ibm.websphere.bo.BOFactory factory = 
(com.ibm.websphere.bo.BOFactory)serviceManager.locateService("com/ibm/websphere/bo/BOFactory");
	DataObject dataObject = factory.create("http://CICSTest/data", "Taderc99");
```

## MQ JMS and MQ data bindings

The
MQ JMS data bindings are similar to the JMS data bindings. The default
data bindings are serialized business objects using JMSObjectMessage and
business object XML using JMSTextMessage, which use
the com.ibm.websphere.sca.jms.data.impl.JMSDataBindingImplJava and com.ibm.websphere.sca.jms.data.impl.JMSDataBindingImplXML classes.
A user supplied data binding allows you to specify your own data binding,
though it must conform to the JMS data binding interface. The message
content of an MQ JMS data binding is accessed through the JMS API.

WebSphere® MQ
has its own unique set of data bindings, which are discussed in Overview of MQ data format transformations.

## Operation types and input and output
for JMS data bindings

The expected argument that will be
passed to the JMSDataBinding and JMSObjectBinding depend
on the interface operation and the input, output and fault types.
 In the export case, this is the expected payload of the JMS message
that should be coming on the incoming JMS destination.

For faults,
the outDataBindingType specified on the method binding
is used. If none is specified, the binding level dataBindingType is
used for all serialization and deserialization.

For non-Document-Literal
wrapped style interfaces, there is no unwrapping and the expected
arguments to the data bindings are the input and output of the operations.

For
Document-Literal wrapped style interfaces the argument is unwrapped
and the underlying data is passed.

The following sections show
the various mappings.

```
<xsd:element name="loginAccount">
	<xsd:complexType>
		<xsd:sequence>
			<xsd:element name="credentials" nillable="true"
				type="bons1:CredentialsBO" />
		</xsd:sequence>
	</xsd:complexType>
</xsd:element>
<xsd:element name="loginAccountResponse">
	<xsd:complexType>
		<xsd:sequence>
			<xsd:element name="response" nillable="true"
				type="xsd:string" />
		</xsd:sequence>
	</xsd:complexType>
</xsd:element>
<xsd:element name="loginAccount\_fault1" type="xsd:string" />
</wsdl:types>
<wsdl:message name="loginAccountRequestMsg">
	<wsdl:part element="tns:loginAccount" name="loginAccountParameters" />
</wsdl:message>
<wsdl:message name="loginAccountResponseMsg">
	<wsdl:part element="tns:loginAccountResponse"
		name="loginAccountResult" />
</wsdl:message>
<wsdl:message name="loginAccount\_fault1Msg">
	<wsdl:part element="tns:loginAccount\_fault1" name="fault1" />
</wsdl:message>
<wsdl:operation name="loginAccount">
	<wsdl:input message="tns:loginAccountRequestMsg"
		name="loginAccountRequest" />
	<wsdl:output message="tns:loginAccountResponseMsg"
		name="loginAccountResponse" />
	<wsdl:fault message="tns:loginAccount\_fault1Msg"
		name="credentialsError" />
</wsdl:operation>
```

- Input:   Doc-Lit Wrapped Style with Single argument Data object
- Output:    Doc-Lit Wrapped Style with Single argument simple type
- Fault:    Simple type

- Input: DataObject Requires: JMSDataBinding
- Output: Simple Type: Requires: JMSObjectBinding
- On Input: DataObject representing contents of CredentialsBO
- On Output: String value for response.
- Fault: String representing fault data. IsBusinessException is
set to true.

```
<xsd:element name="selectAccount">
	<xsd:complexType>
		<xsd:sequence>
			<xsd:element name="accountName" nillable="true"
				type="xsd:string" />
		</xsd:sequence>
	</xsd:complexType>
</xsd:element>
</wsdl:message>
<wsdl:message name="selectAccountRequestMsg">
	<wsdl:part element="tns:selectAccount"
		name="selectAccountParameters" />
</wsdl:message>
<wsdl:operation name="selectAccount">
	<wsdl:input message="tns:selectAccountRequestMsg"
		name="selectAccountRequest" />
</wsdl:operation>
```

- Input: Doc Lit wrapped style with single argument String (simple
type)

- Input: Simple Type Requires:JMSObjectBinding
- On Input: String Object.

```
<xsd:element name="updateAccount">
	<xsd:complexType>
		<xsd:sequence>
			<xsd:element name="performCredit" nillable="true"
				type="xsd:boolean" />
			<xsd:element name="amount" nillable="true" type="xsd:float" />
		</xsd:sequence>
	</xsd:complexType>
</xsd:element>
<xsd:element name="updateAccountResponse">
	<xsd:complexType>
		<xsd:sequence>
			<xsd:element name="balance" nillable="true"
				type="xsd:float" />
		</xsd:sequence>
	</xsd:complexType>
</xsd:element>
</wsdl:message>
<wsdl:message name="updateAccountRequestMsg">
	<wsdl:part element="tns:updateAccount"
		name="updateAccountParameters" />
</wsdl:message>
<wsdl:message name="updateAccountResponseMsg">
	<wsdl:part element="tns:updateAccountResponse"
		name="updateAccountResult" />
</wsdl:message>
<wsdl:message name="updateAccount\_fault1Msg">
	<wsdl:part element="tns:updateAccount\_fault1" name="fault1" />
</wsdl:message>
<wsdl:operation name="updateAccount">
	<wsdl:input message="tns:updateAccountRequestMsg"
		name="updateAccountRequest" />
	<wsdl:output message="tns:updateAccountResponseMsg"
		name="updateAccountResponse" />
	<wsdl:fault message="tns:updateAccount\_fault1Msg"
		name="insufficientFunds" />
</wsdl:operation>
```

- Input: Doc Lit wrapped style with multiple arguments, which are
simple types. DataObject with 2 simple types as properties
- Output: Doc Lit wrapped style with single argument, which is simple
type.
- Fault: DataObject

- Input: DataObject with 2 arguments Requires: JMSDataBinding
- Output: Simple Type Requires: JMSObjectBinding
- Fault: DataObject representing the fault message. Requires: JMSDataBinding

```
<xsd:element name="updateAccount2">
	<xsd:complexType>
		<xsd:sequence>
			<xsd:element name="performCredit" nillable="true"
				type="xsd:boolean" />
			<xsd:element name="amount" nillable="true" type="xsd:float" />
			<xsd:element name="dummyInfo" nillable="true"
				type="bons1:DummyBO" />
		</xsd:sequence>
	</xsd:complexType>
</xsd:element>
<xsd:element name="updateAccount2Response">
	<xsd:complexType>
		<xsd:sequence>
			<xsd:element name="balance" nillable="true"
				type="xsd:float" />
		</xsd:sequence>
	</xsd:complexType>
</xsd:element>
</wsdl:message>
<wsdl:message name="updateAccount\_fault1Msg">
	<wsdl:part element="tns:updateAccount\_fault1" name="fault1" />
</wsdl:message>
<wsdl:message name="updateAccount2RequestMsg">
	<wsdl:part element="tns:updateAccount2"
		name="updateAccountParameters" />
</wsdl:message>
<wsdl:message name="updateAccount2ResponseMsg">
	<wsdl:part element="tns:updateAccount2Response"
		name="updateAccountResult" />
</wsdl:message>
<wsdl:operation name="updateAccount2">
	<wsdl:input message="tns:updateAccount2RequestMsg"
		name="updateAccount2Request" />
	<wsdl:output message="tns:updateAccount2ResponseMsg"
		name="updateAccount2Response" />
	<wsdl:fault message="tns:updateAccount\_fault1Msg"
		name="insufficientFunds" />
</wsdl:operation>
```

- Input: DocLit wrapped style with multiple arguments (Mixed Types),
which are simple types and a DataObject DataObject with 2 simple types
and a DataObject as properties
- Output: Doct Lit wrapped style with single argument, which is
simple type.
- Fault: DataObject

- Input: DataObject with 3 arguments Requires: JMSDataBinding
- Output: SimpleType Requires: JMSObjectBinding
- On Fault: DataObject representing the fault message. Requires:
JMSDataBinding

```
<xsd:element name="getCustomerInfo">
	<xsd:complexType>
		<xsd:sequence />
	</xsd:complexType>
</xsd:element>
<xsd:element name="getCustomerInfoResponse">
	<xsd:complexType>
		<xsd:sequence>
			<xsd:element name="result" nillable="true"
				type="bons1:CustomerInfoBO" />
		</xsd:sequence>
	</xsd:complexType>
</xsd:element>
</wsdl:message>
<wsdl:message name="getCustomerInfoRequestMsg">
	<wsdl:part element="tns:getCustomerInfo"
		name="getCustomerInfoParameters" />
</wsdl:message>
<wsdl:message name="getCustomerInfoResponseMsg">
	<wsdl:part element="tns:getCustomerInfoResponse"
		name="getCustomerInfoResult" />
</wsdl:message>
<wsdl:operation name="getCustomerInfo">
	<wsdl:input message="tns:getCustomerInfoRequestMsg"
		name="getCustomerInfoRequest" />
	<wsdl:output message="tns:getCustomerInfoResponseMsg"
		name="getCustomerInfoResponse" />
</wsdl:operation>
```

- Input: Doc Lit wrapped style, with no arguments (null). DataObject
representing wrapper, used and no properties.
- Output: Doc Lit wrapped style, with Data Object

- Input: DataObject set to null. Requires: JMSDataBinding
- Output:DataObject represenitng the value contained in the wrapper.
Requires: JMSDataBinding

```
<xsd:element name="updateCustomerInfo">
	<xsd:complexType>
		<xsd:sequence>
			<xsd:element name="customerInfo" nillable="true"
				type="bons1:CustomerInfoBO" />
		</xsd:sequence>
	</xsd:complexType>
</xsd:element>
<xsd:element name="updateCustomerInfoResponse">
	<xsd:complexType>
		<xsd:sequence>
			<xsd:element name="result" nillable="true"
				type="bons1:CustomerInfoBO" />
		</xsd:sequence>
	</xsd:complexType>
</xsd:element>
</wsdl:message>
<wsdl:message name="updateCustomerInfoRequestMsg">
	<wsdl:part element="tns:updateCustomerInfo"
		name="updateCustomerInfoParameters" />
</wsdl:message>
<wsdl:message name="updateCustomerInfoResponseMsg">
	<wsdl:part element="tns:updateCustomerInfoResponse"
		name="updateCustomerInfoResult" />
</wsdl:message>
<wsdl:operation name="updateCustomerInfo">
	<wsdl:input message="tns:updateCustomerInfoRequestMsg"
		name="updateCustomerInfoRequest" />
	<wsdl:output message="tns:updateCustomerInfoResponseMsg"
		name="updateCustomerInfoResponse" />
</wsdl:operation>
```

- Input: Doc Lit wrapped style, with DataObject
- Output: Doc Lit wrapped style, with Data Object

- Input: DataObject representing the value contained in the wrapper.
Requires: JMSDataBinding
- Output: DataObject representing the value contained in the wrapper.
Requires: JMSDataBinding

```
<xsd:element name="updateCustomerInfo2">
	<xsd:complexType>
		<xsd:sequence>
			<xsd:element name="customerInfo" nillable="true"
				type="bons1:CustomerInfoBO" />
			<xsd:element name="dummyInfo" nillable="true"
				type="bons1:DummyBO" />
		</xsd:sequence>
	</xsd:complexType>
</xsd:element>
<xsd:element name="updateCustomerInfo2Response">
	<xsd:complexType>
		<xsd:sequence>
			<xsd:element name="result" nillable="true"
				type="bons1:CustomerInfoBO" />
		</xsd:sequence>
	</xsd:complexType>
</xsd:element>
</wsdl:message>
<wsdl:message name="updateCustomerInfo2RequestMsg">
	<wsdl:part element="tns:updateCustomerInfo2"
		name="updateCustomerInfoParameters" />
</wsdl:message>
<wsdl:message name="updateCustomerInfo2ResponseMsg">
	<wsdl:part element="tns:updateCustomerInfo2Response"
		name="updateCustomerInfoResult" />
	<wsdl:operation name="updateCustomerInfo2">
		<wsdl:input message="tns:updateCustomerInfo2RequestMsg"
			name="updateCustomerInfo2Request" />
		<wsdl:output message="tns:updateCustomerInfo2ResponseMsg"
			name="updateCustomerInfo2Response" />
	</wsdl:operation>
</wsdl:message>
```

- Input: Doc Lit wrapped style, with 2 arguments of type DataObject
- Output: Doc Lit wrapped style, with Data Object

- Input: DataObject representing wrapper with the argument DataObject
as properties. Requires: JMSDataBinding
- Output: DataObject representing the value contained in the wrapper.
Requires: JMSDataBinding

```
<wsdl:types>
	<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
		<xsd:import namespace="http://jms.quote.data"
			schemaLocation="JmsQuote.xsd">
		</xsd:import>
	</xsd:schema>
</wsdl:types>

<wsdl:message name="JmsQuoteRequest">
	<wsdl:part name="request" element="data:JmsQuote"></wsdl:part>
</wsdl:message>

<wsdl:message name="JmsQuoteReply">
	<wsdl:part name="request" element="data:JmsQuote"></wsdl:part>
</wsdl:message>

<wsdl:portType name="JmsQuotePT">
	<wsdl:operation name="getJmsQuote">
		<wsdl:input message="tns:JmsQuoteRequest"></wsdl:input>
		<wsdl:output message="tns:JmsQuoteReply"></wsdl:output>
	</wsdl:operation>
</wsdl:portType>
```

- Input: DataObject representing JmsQuote
- Output: DataObject representing JmsQuote

- Input: DataObject Requires: JMSDataBinding
- Output: DataObject Requires: JMSDataBinding

## Data binding generator

A data
binding generator is an implementation class, which at application
assembly time will generate a type specific data binding implementation
for an input or output parameter of a particular operation. The data
binding generator generates a standard implementation class unlike
the unique custom data binding. It automates the process of implementing
a data binding.

The generator is invoked during application
assembly, when the artifacts needed to deploy SCA module are generated.
This approach ensures the data binding implementation is always matching
the latest version of the possibly edited type (schema). The commonj.connector.metadata.description.DataBindingGenerator interface
is presented as follows:

```
public interface DataBindingGenerator {	

    public DataBindingDescription[] generateDataBinding(
				QName complexType, URL schema)
					throws MetadataException;
}
```

For the generateDataBinding() method,
it passes as arguments the QName of the input or output complexType and
the URL of its schema. The complexType QName refers
to a global complexType. The DataBindingGenerator implementation
is then responsible for loading the schema, including resolving any
schema imported or included. It then finds the complex type definition
specified by the QName, and by looking at it or annotations in the
schema generates one or more data bindings to handle the complex type
definition.

For the generator to be found at application assembly
time, it must be registered by using the extension point "connector.metadata.databinding\_generator"
or be supplied by and be in the classpath of the resource adapter.
The class name is specified in the root portion of an import or export
binding. The lookup depends if the generator was registered by extension
point, or is part of the resource adapter. If it is registered by
extension point, the regular Eclipse extension point mechanisms are
used to load the class. If the generator is part of the resource adapter,
then the lookup for the generator class is done using the class name
and looking in the classes supplied by the resource adapter. So the
lookup is for a specific class on the classpath of the resource adapter.

The
following is an example of this extension:

```
<extension point="connector.metadata.databinding\_generator">
	<databinding\_generator
		class="com.xyz.DataBindingGenerator"
		name="My Generator"
		id="com.xyz.DataBindingGenerator"/>
</extension>
```

## Related concepts

- Prepackaged JMS data format transformations
- JMS function selectors

## Related reference

- Data handlers
- Working with the simple JMS data bindings
- Business object XML using JMS text message serialization
- Prepackaged JMS and MQ fault selectors