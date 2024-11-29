# UDDI Endpoint Lookup mediation primitive

## Introduction

You can use the UDDI Endpoint
Lookup mediation primitive to retrieve service endpoint information
from a UDDI version 3 registry. The service endpoint information relates
directly to web services.

To use the UDDI Endpoint Lookup mediation
primitive you might need to add service endpoint information to your
registry.

- Web services using SOAP/HTTP.
- Web services using SOAP/JMS.

When the UDDI Endpoint Lookup mediation primitive receives
a message it sends a search query to the registry. The search query
is constructed using the UDDI properties that you specify and the
query might return nothing, or it might return one or more service
endpoints. You can choose whether to be informed of all endpoints
that match your query, or just one endpoint that matches your query.

## Details

The UDDI Endpoint
Lookup mediation primitive uses the Endpoint Reference structure defined
by the WS-Addressing specification. For more information, see: http://schemas.xmlsoap.org/ws/2004/08/addressing.

Updates made to the SMO by the UDDI
Endpoint Lookup mediation primitive are dependent on the success of
the registry query (matches are found during the registry query) and
the match policy.

- /headers/SMOHeader/Target/address .
    - Can contain the address of a service to call dynamically (the
dynamic callout address).
- /context/primitiveContext/EndpointLookupContext .

- Can contain the results of the UDDI query.
- /headers/SMOHeader/AlternateTarget

- Can contain a list of alternate service addresses. For more information
on the retry function, see: Combining multiple services.

To define the
UDDI servers and specify the connection information: in the Administrative
console, navigate to Service integration > Web services > UDDI References.

## Usage

1. Wire the matching output terminal of the UDDI Endpoint Lookup
mediation primitive to the input terminal of the Message Filter mediation
primitive.
2. Use the Message Filter mediation primitive to check whether the
URL was internal or external, and route external messages to the Mapping
mediation primitive (by wiring one of the Message Filter output terminals
to the Mapping mediation primitive).
3. Use the Mapping mediation primitive to remove private information
from messages.

## SOAP/HTTP example

```
http://<host>:<port>/<moduleName>/sca/<exportName>
```

```
http://<host>:<port>/<service>
```

```
<?xml version="1.0" encoding="UTF-8"?>
<wsdl:definitions name="SOAP\_HTTPExport\_BigEchoHttp\_Service" targetNamespace="http://big.com/Binding3" 
		xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" 
		xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" 
		xmlns:Port\_0="http://big.com" 
		xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" 
		xmlns:this="http://big.com/Binding3" 
		xmlns="http://schemas.xmlsoap.org/wsdl/">
  <wsdl:import namespace="http://big.com" location="BigEcho.wsdl"/>
  <wsdl:binding name="SOAP\_HTTPExport\_BigEchoHttpBinding" type="Port\_0:BigEcho">
    <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
    <wsdl:operation name="echo">
      <soap:operation/>
      <wsdl:input name="echoRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="echoResponse">
        <soap:body use="literal"/>
      </wsdl:output>
      <wsdl:fault name="BadBoyException">
        <soap:fault name="BadBoyException" use="literal"/>
      </wsdl:fault>
    </wsdl:operation>
  </wsdl:binding>
  <wsdl:service name="SOAP\_HTTPExport\_BigEchoHttpService">
    <wsdl:port name="SOAP\_HTTPExport\_BigEchoHttpPort" binding="this:SOAP\_HTTPExport\_BigEchoHttpBinding">
      <soap:address location="http://testhost:9080/RegistryWeb/sca/SOAP\_HTTPExport"/>
    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>
```

The port declaration contains a  soap:address location
of http://testhost:9080/RegistryWeb/sca/SOAP\_HTTPExport.
This indicates that it is an export with a web service binding. To
enable dynamic routing, update the /headers/SMOHeader/Target/address field
in the message with the location value in the soap:address element.

## SOAP/JMS example

```
jms:/queue?destination=jms/WSjmsExport&connectionFactory=jms/WSjmsExportQCF&targetService=WSjmsExport\_ServiceBJmsPort
```

```
jms:/queue?destination=<destName>&connectionFactory=<factory>&targetservice=<service>
```

```
<?xml version="1.0" encoding="UTF-8"?>
<wsdl:definitions name="SOAP\_JMSExport\_BigEchoJms\_Service" targetNamespace="http://big.com/Binding4" 
		xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" 
		xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" 
		xmlns:Port\_0="http://big.com" 
		xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" 
		xmlns:this="http://big.com/Binding4" 
		xmlns="http://schemas.xmlsoap.org/wsdl/">
  <wsdl:import namespace="http://big.com" location="BigEcho.wsdl"/>
  <wsdl:binding name="SOAP\_JMSExport\_BigEchoJmsBinding" type="Port\_0:BigEcho">
    <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/jms"/>
    <wsdl:operation name="echo">
      <soap:operation/>
      <wsdl:input name="echoRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="echoResponse">
        <soap:body use="literal"/>
      </wsdl:output>
      <wsdl:fault name="BadBoyException">
        <soap:fault name="BadBoyException" use="literal"/>
      </wsdl:fault>
    </wsdl:operation>
  </wsdl:binding>
  <wsdl:service name="SOAP\_JMSExport\_BigEchoJmsService">
    <wsdl:port name="SOAP\_JMSExport\_BigEchoJmsPort" binding="this:SOAP\_JMSExport\_BigEchoJmsBinding">
      <soap:address location="jms:/queue?destination=jms/SOAP\_JMSExport&;connectionFactory=jms/SOAP\_JMSExportQCF&;targetService=SOAP\_JMSExport\_BigEchoJmsPort"/>

    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>
```

- UDDI Endpoint Lookup mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)