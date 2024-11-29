# SMO structure

## Introduction

## SMO schema

```
<schema xmlns="http://www.w3.org/2001/XMLSchema"
		xmlns:ecore="http://www.eclipse.org/emf/2002/Ecore"
		xmlns:mq="http://www.ibm.com/xmlns/prod/websphere/mq/sca/6.0.0"
		xmlns:sdoXML="commonj.sdo/xml" xmlns:smo="http://www.ibm.com/websphere/sibx/smo/v6.0.1"
		xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"
		xmlns:wsa10="http://www.w3.org/2005/08/addressing"
		xmlns:httpsca="http://www.ibm.com/xmlns/prod/websphere/http/sca/6.1.0"
		xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope"

		targetNamespace="http://www.ibm.com/websphere/sibx/smo/v6.0.1"

		ecore:nsPrefix="ServiceMessageObject"
		ecore:package="com.ibm.ws.sibx.smobo">
	
	<import namespace="http://www.w3.org/XML/1998/namespace"
			schemaLocation="./xml.xsd"/>

	<import namespace="http://www.ibm.com/xmlns/prod/websphere/mq/sca/6.0.0"
    		schemaLocation="./wmqstructures.xsd"/>

	<import namespace="http://schemas.xmlsoap.org/ws/2004/08/addressing"
    		schemaLocation="./ws-addressing.xsd"/>

	<import namespace="http://www.w3.org/2005/08/addressing"
			schemaLocation="./ws-addr-10.xsd"/>

	<import namespace="http://www.ibm.com/xmlns/prod/websphere/http/sca/6.1.0"
    		schemaLocation="./httpstructures.xsd"/>

	<import namespace="http://www.w3.org/2003/05/soap-envelope"
    		schemaLocation="./soap-envelope.xsd"/>

	<!-- Global element for SMO -->
	<element name="smo" type="smo:ServiceMessageObject"/>

	<!-- Type definition for SMO -->
	<complexType name="ServiceMessageObject">
		<sequence>
			
			<!-- Top-level folders are always present, but may themselves be empty. -->
			<element name="context" type="smo:ContextType"/>
			<element name="headers" type="smo:HeadersType"/>

			<!-- Body may be absent (null as seen through Java/SDO). -->
			<element minOccurs="0" name="body" type="anyType"/>

			<!--  List of attachments -->
 			<element name="attachments" type="smo:AttachmentType" minOccurs="0" maxOccurs="unbounded"/>
 			
		</sequence>
	</complexType>

	<!-- ContextType - container for the individual context elements. -->
	<complexType name="ContextType">
		<sequence>
			<element minOccurs="0" name="correlation" type="anyType"/>
			<element minOccurs="0" name="transient" type="anyType"/>
			<element minOccurs="0" name="failInfo" type="smo:FailInfoType"/>
			<element maxOccurs="1" minOccurs="0" name="primitiveContext" type="smo:PrimitiveContextType"/>
			<element minOccurs="0" name="shared" type="anyType"/>
			<element minOccurs="0" name="dynamicProperty" type="smo:DynamicPropertyContextType"/>
			<element minOccurs="0" name="userContext" type="smo:UserContextType"/>
		</sequence>
	</complexType>

	<complexType name="HeadersType">
		<sequence>
			<element minOccurs="0" name="SMOHeader" type="smo:SMOHeaderType"/>
			<element minOccurs="0" name="JMSHeader" type="smo:JMSHeaderType"/>
			<element maxOccurs="unbounded" minOccurs="0" name="SOAPHeader" type="smo:SOAPHeaderType"/>
			<element minOccurs="0" name="SOAPFaultInfo" type="smo:SOAPFaultInfoType"/>
			<element maxOccurs="unbounded" minOccurs="0" name="properties" type="smo:PropertyType"/>
			<element minOccurs="0" name="MQHeader" type="smo:MQHeaderType"/>
			<element minOccurs="0" name="HTTPHeader" type="smo:HTTPHeaderType"/>
			<element minOccurs="0" name="EISHeader" type="smo:EISHeaderType"/>
			<element minOccurs="0" name="WSAHeader" type="smo:WSAHeaderType"/>
		</sequence>
	</complexType>
	
	<!-- AttachmentType - container for an individual attachment. -->
	<complexType name="AttachmentType">
    	<sequence>
      		<element name="contentID" type="anyURI"/>
      		<element name="contentType" type="token"/>
      		<choice>
        		<element name="data" type="base64Binary"/>
        		<element name="bodyPath" type="string"/>
      		</choice>
    	</sequence>
  	</complexType>

	
	
	<!-- EMF 2.0 generated MessageType as a string, rather than an enumeration,
	     EMF 2.2 generated it as an enumeration. For compatibility, the schema
	     has been changed to make it a string.
	-->
	<complexType name="SMOHeaderType">
		<sequence>
			<element minOccurs="1" name="MessageUUID" type="string"/>
			<element minOccurs="1" name="Version" type="smo:VersionType"/>
			<element minOccurs="0" name="MessageType" type="string"/>
			<element minOccurs="0" name="Operation" type="string"/>
			<element minOccurs="0" name="Action" type="string"/>
			<element minOccurs="0" name="Target" type="smo:TargetAddressType"/>
			<element maxOccurs="unbounded" minOccurs="0" name="AlternateTarget" type="smo:TargetAddressType"/>
			<element minOccurs="0" name="SourceNode" type="string"/>
			<element minOccurs="0" name="SourceBindingType" type="smo:BindingTypeType"/>
			<element minOccurs="0" name="Interface" type="string"/>
		</sequence>
	</complexType>

	<simpleType name="BindingTypeType">
		<restriction base="string">
			<enumeration value="NotSet"/>
			<enumeration value="JMS"/>
			<enumeration value="MQJMS"/>
			<enumeration value="GenericJMS"/>
			<enumeration value="MQ"/>
			<enumeration value="WebService"/>
			<enumeration value="HTTP"/>
			<enumeration value="SCA"/>
			<enumeration value="EIS"/>
			<enumeration value="SLSB"/>
			<enumeration value="WebServiceSOAP1.1"/>
			<enumeration value="WebServiceSOAP1.2"/>
		</restriction>
	</simpleType>
	

	<complexType name="SOAPFaultInfoType">
		<sequence>
			<element name="faultcode" type="QName"/>
			<element name="faultstring" type="string"/>
			<element minOccurs="0" name="faultactor" type="anyURI"/>
			<element minOccurs="0" name="extendedFaultInfo" type="smo:FaultType"/>
		</sequence>
	</complexType>

	<complexType name="FailInfoType">
		<sequence>
			<element name="failureString" type="string"/>
			<element name="origin" type="string"/>
			<element name="invocationPath">
				<complexType>
					<sequence>
						<element maxOccurs="unbounded" name="primitive" type="smo:PrimitiveType"/>
					</sequence>
				</complexType>
			</element>
			<element minOccurs="0" name="predecessor" type="smo:FailInfoType"/>
		</sequence>
		<attribute href="xml:lang"/>
  	</complexType>

	<complexType name="PrimitiveType">
		<attribute name="inTerminal" type="string" use="required"/>
		<attribute name="name" type="string" use="required"/>
		<attribute name="outTerminal" type="string"/>
	</complexType>

	<complexType name="PropertyType">
		<sequence>
			<element name="name" type="string"/>
			<element name="value" type="anySimpleType"/>
			<element minOccurs="0" name="type" type="string"/>
		</sequence>
	</complexType>

	<complexType name="VersionType">
		<sequence>
			<element name="Version" type="integer"/>
			<element name="Release" type="integer"/>
			<element name="Modification" type="integer"/>
		</sequence>
	</complexType>

	<complexType name="TargetAddressType">
		<sequence>
			<element name="address" type="anyURI"/>
		</sequence>
		<attribute name="import" type="string"/>
		<attribute name="bindingType" type="smo:BindingTypeType"/>
		<attribute name="repositoryMetadata" type="string"/>
	</complexType>

	<complexType name="JMSHeaderType">
		<sequence>
			<element minOccurs="0" name="JMSDestination" type="anyURI"/>
			<element minOccurs="0" name="JMSDeliveryMode" type="smo:persistenceType"/>
			<element minOccurs="0" name="JMSMessageID" type="string"/>
			<element minOccurs="0" name="JMSTimestamp" type="long"/>
			<element minOccurs="0" name="JMSCorrelationID" type="string"/>
			<element minOccurs="0" name="JMSReplyTo" type="anyURI"/>
			<element minOccurs="0" name="JMSRedelivered" type="boolean"/>
			<element minOccurs="0" name="JMSType" type="string"/>
			<element minOccurs="0" name="JMSExpiration" type="long"/>
			<element minOccurs="0" name="JMSPriority" type="smo:priorityType"/>
		</sequence>
	</complexType>

	<!-- SOAPHeader - the container for the individual SOAP headers -->
	<complexType name="SOAPHeaderType">
		<sequence>
			<element name="nameSpace" type="anyURI"/>
			<element name="name" type="NCName"/>
			<element minOccurs="0" name="prefix" type="NCName"/>
			<element name="value" type="anyType"/>
		</sequence>
	</complexType>

	<!-- Types used in headers. -->
	<simpleType name="priorityType">
		<restriction base="integer">
			<minInclusive value="0"/>
			<maxInclusive value="9"/>
		</restriction>
	</simpleType>

	<simpleType name="persistenceType">
		<restriction base="string">
			<enumeration value="NonPersistent"/>
			<enumeration value="Persistent"/>
		</restriction>
	</simpleType>

	<!-- MQ Header Type -->
	<complexType name="MQHeaderType">
		<sequence>
			<element minOccurs="0" name="md" type="mq:MQMD"/>
			<element minOccurs="0" name="control" type="mq:MQControl"/>
			<element maxOccurs="unbounded" minOccurs="0" name="header" type="smo:MQChainedHeaderType"/>
		</sequence>
	</complexType>

	<!-- MQ Chained Header Type -->
	<complexType name="MQChainedHeaderType">
		<complexContent>
			<extension base="mq:MQControl">
				<sequence>
					<choice> 
						<element name="value" type="anyType"/>
						<element name="opaque" type="mq:MQOpaqueHeader"/>
						<element name="rfh" type="mq:MQRFH"/>
						<element name="rfh2" type="mq:MQRFH2"/>
					</choice>
				</sequence>
			</extension>
		</complexContent>
	</complexType>

	<!-- UserContextType -->
	<complexType name="UserContextType">
		<sequence>
			<element maxOccurs="unbounded" minOccurs="0" name="entries" type="smo:ComplexPropertyType"/>
		</sequence>
	</complexType>
	
	<complexType name="ComplexPropertyType">
		<sequence>
			<element name="name" type="string"/>
			<element name="value" type="anyType"/>
			<element minOccurs="0" name="type" type="string"/>
		</sequence>
	</complexType>

	<!-- PrimitiveContextType -->
	<complexType name="PrimitiveContextType">
		<sequence>
			<element maxOccurs="unbounded" minOccurs="0" name="EndpointLookupContext" type="smo:EndpointLookupContextType"/>
	  		<element maxOccurs="1" minOccurs="0" name="FanOutContext" type="smo:FanOutContextType"/>
	  		<element maxOccurs="1" minOccurs="0" name="WTXContext" type="smo:WTXContextType"/>
		</sequence>
	</complexType>

	<!-- Start of FaultType -->

	<complexType name="FaultType" final="extension">
		<sequence>
			<element name="Code" type="soapenv:faultcode"/>
			<element name="Reason" type="soapenv:faultreason"/>
			<element minOccurs="0" name="Node" type="anyURI"/>
			<element minOccurs="0" name="Role" type="anyURI"/>
		</sequence>
	</complexType>

	<!-- End of FaultType -->

	<!-- Start of DynamicPropertyContext and related types -->
	
	<complexType name="DynamicPropertyContextType">
		<sequence>
			<element maxOccurs="unbounded" minOccurs="0" name="propertySets" type="smo:DynamicPropertySetType"/>
		</sequence>
       <attribute name="isPropagated" type="boolean" />
	</complexType>
	
	<!-- A dynamic property set holds dynamic properties. -->
	<complexType name="DynamicPropertySetType">
		<sequence>
			<element minOccurs="1" name="group" type="string" />
			<element maxOccurs="unbounded" minOccurs="0" name="properties" type="smo:PropertyType"/>
		</sequence>
	</complexType>

	<!-- End of DynamicPropertyContext and related types -->
	
	<!-- start of EndpointLookupContextType and related types -->
	
	<complexType name="EndpointLookupContextType">
		<sequence>
			<element maxOccurs="1" minOccurs="1" name="endpointReference" type="wsa:EndpointReferenceType"/>
			<element maxOccurs="1" minOccurs="0" name="registryAnnotations" type="smo:RegistryAnnotationsType"/>
		</sequence>
	</complexType>
	
	<complexType name="RegistryAnnotationsType">
		<sequence>
			<element maxOccurs="unbounded" minOccurs="0" name="property" type="smo:RegistryPropertyType"/>
			<element maxOccurs="unbounded" minOccurs="0" name="classification" type="anyURI"/>
			<element maxOccurs="unbounded" minOccurs="0" name="relationship" type="smo:RegistryRelationshipType"/>
		</sequence>
	</complexType>
	
	<complexType name="RegistryPropertyType">
		<sequence>
			<element maxOccurs="1" minOccurs="1" name="name" type="string"/>
			<element maxOccurs="1" minOccurs="0" name="value" type="string"/>
		</sequence>
	</complexType>
	
	<complexType name="RegistryRelationshipType">
		<sequence>
			<element maxOccurs="1" minOccurs="1" name="relationshipName" type="string"/>
			<element maxOccurs="1" minOccurs="0" name="targetName" type="string"/>
			<element maxOccurs="1" minOccurs="0" name="targetNamespace" type="anyURI"/>
			<element maxOccurs="1" minOccurs="0" name="targetVersion" type="string"/>
		</sequence>
	</complexType>
	
	<!-- end of EndpointLookupContextType and related types -->
	
	<!-- start of FanOutContextType -->
	
	<complexType name="FanOutContextType">
	  <sequence>
	    <element maxOccurs="1" minOccurs="0" name="iteration" type="integer"/>
	    <element maxOccurs="1" minOccurs="0" name="occurrence" type="anyType"/>
	  </sequence>
	</complexType>

	<!-- end of FanOutContextType -->

	<!-- start of WTXContextType and related types -->

 	<complexType name="WTXContextType">
        <sequence>
            <element maxOccurs="1" minOccurs="0" name="mapServerLocation" type="anyURI"/>
            <element maxOccurs="1" minOccurs="0" name="dynamicMap" type="hexBinary"/>
            <element maxOccurs="unbounded" minOccurs="0" name="mapInstances" type="smo:WTXMapInstanceType"/>
        </sequence>
    </complexType>

    <complexType name="WTXMapInstanceType">
        <sequence>
            <element maxOccurs="1" minOccurs="1" name="mapInstance" type="integer"/>
            <element maxOccurs="1" minOccurs="1" name="auditInfo" type="string"/>
        </sequence>
    </complexType>

	<!-- end of WTXContextType and related types -->

	<!-- start of HTTPHeaderType -->

	<complexType name="HTTPHeaderType">
	  <sequence>
	    <element name="control" minOccurs="0" type="httpsca:HTTPControl"/>
	    <element name="header" minOccurs="0" maxOccurs="unbounded" type="httpsca:HTTPHeader"/>
	  </sequence>
	</complexType>

	<!-- end of HTTPHeaderType -->

    <!-- start of EISHeaderType -->

    <complexType name="EISHeaderType">
		<sequence>
			<element minOccurs="0" name="EISInteractionSpec" type="anyType"/>
			<element minOccurs="0" name="EISConnectionSpec" type="anyType"/>
		</sequence>
	</complexType>

    <!-- end of EISHeaderType -->

    <!-- start of WSAHeaderType -->

    <complexType name="WSAHeaderType">
        <sequence>
            <element minOccurs="0" href="wsa10:To"></element>
            <element minOccurs="0" name="ReferenceParameters" type="wsa10:ReferenceParametersType"/>
            <element minOccurs="0" href="wsa10:From"></element>
            <element minOccurs="0" href="wsa10:ReplyTo"></element>
            <element minOccurs="0" href="wsa10:FaultTo"></element>
            <element minOccurs="0" href="wsa10:Action"></element>
            <element minOccurs="0" href="wsa10:MessageID"></element>
            <element minOccurs="0" maxOccurs="unbounded" href="wsa10:RelatesTo"/>
        </sequence>
        <attribute name="version" type="smo:WSASchemaType" use="optional"/>
    </complexType>

    <simpleType name="WSASchemaType">
        <restriction base="string">
            <enumeration value="http://www.w3.org/2005/08/addressing"/>
            <enumeration value="http://schemas.xmlsoap.org/ws/2004/08/addressing"/>
        </restriction>
    </simpleType>

    <!-- end of WSAHeaderType -->

</schema>
```

- In an instance of an SMO, the anyType field acts
as a placeholder where a more complex structure can be substituted.
- In an instance of an SMO, the value in an anySimpleType field
can be any of the Java™ simple
types. For example: short, int, long, double, String or boolean.
- In an instance of an SMO, the FailInfoType contains
an attribute whose value is a language code.

## Schema field descriptions

- Referenced attachments, which are defined in a WSDL port type
as parts in an input or output message and which have a binary type,
do not have their data stored in the SMO; instead, the path to the
message body element that holds the data is contained in the bodyPath element.
- Unreferenced attachments, which are not defined in a WSDL port
type, have their data placed in the data element
in the SMO, and have no bodyPath element.

- Web service binding SOAP 1.1/HTTP using
JAX-WS
- Web service binding SOAP 1.2/HTTP using
JAX-WS
- SCA binding

The following elements are mutually exclusive:

This element is used
by unreferenced attachments.

This element is used by referenced
attachments.

- SMO: HTTP schema

The service message object (SMO) schema contains other schemas, including one that describes the HTTP header.
- SMO body structure

The body element of the SMO has a structure that corresponds with the WSDL message that defines the input or output from a given WSDL operation.