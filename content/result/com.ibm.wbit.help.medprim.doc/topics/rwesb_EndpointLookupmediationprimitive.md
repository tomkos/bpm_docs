# Endpoint Lookup mediation primitive

## Introduction

In
order to use the Endpoint Lookup mediation primitive you might need
to add service endpoint information to your WSRR registry. If you
want to extract service endpoint information about web services, your
WSRR registry must contain either the appropriate WSDL documents,
or SCA modules that contain exports using web service bindings. If
you want to extract service endpoint information about exports that
use the other SCA bindings, your WSRR registry must contain the appropriate
SCA modules. If you want to extract service endpoint information about
services that are accessed using MQ, JMS or HTTP but are not defined
in a SCA module, your WSRR registry must contain an appropriate Manual
JMS/HTTP/MQ endpoint with associated Interface Business Object
with the endpoint information and associated interface correctly set.

- Web services using SOAP/HTTP.
- Web services using SOAP/JMS.
- SCA module exports with web service bindings, using SOAP/HTTP.
- SCA module exports with web service bindings, using SOAP/JMS.
- SCA module exports with the default SCA binding.
- SCA module exports with the MQ binding.
- SCA module exports with the MQ JMS binding.
- SCA module exports with the JMS binding.
- SCA module exports with the Generic JMS binding.
- SCA module exports with the HTTP binding.
- Manually defined MQ endpoints with associated interfaces.
- Manually defined JMS endpoints with associated interfaces.
- Manually defined HTTP endpoints with associated interfaces.

When the Endpoint Lookup mediation primitive receives
a message it sends a search query to the registry. The search query
is constructed using the Endpoint Lookup properties that you specify
and the query might return nothing, or it might return one or more
service endpoints. You can choose whether to be informed of all endpoints
that match your query, or just one endpoint that matches your query.

## Details

The Endpoint Lookup mediation primitive
uses the Endpoint Reference structure defined by the WS-Addressing
specification. For more information, see: http://schemas.xmlsoap.org/ws/2004/08/addressing.

Updates
made to the SMO by the Endpoint Lookup mediation primitive are dependant
on the success of the registry query (matches are found during the
registry query) and the match policy.

- /headers/SMOHeader/Target/address .
    - Can contain the address of a service to invoke dynamically (the
dynamic callout address).
- /context/primitiveContext/EndpointLookupContext .

- Can contain the results of the WSRR query.
- /headers/SMOHeader/AlternateTarget

- Can contain a list of alternate service addresses. For more information
on the retry function, see: Combining multiple services.

## Usage

You can use the Endpoint Lookup mediation
primitive to dynamically route messages based upon customer classification.
For example, you might want messages for customers of type A routed
to URL X, and messages for customers of type B routed to URL Y. If
you set up your registry to key URLs against customer types, then
you can dynamically route customer requests according to customer
type.

1. Wire the matching output terminal of the Endpoint Lookup mediation
primitive to the input terminal of the Message Filter mediation primitive.
2. Use the Message Filter mediation primitive to check whether the
URL is internal or external, and route external messages to the Mapping
mediation primitive (by wiring one of the Message Filter output terminals
to the Mapping mediation primitive).
3. Use the Mapping mediation primitive to remove private information
from messages.

## Matching latest compatible service versions

If
you have created versioned SCA modules, and have loaded these SCA
modules into WSRR, you might want to use the latest compatible version
of the service provider that is available.

| 1.0.0          |
|----------------|
| 1.0.1          |
| 1.0.2          |
| 1.0.3          |
| 1.1.0          |
| 1.1.3          |
| 1.1.4          |
| 1.3.0          |
| 1.3.1          |
| 1.3.4          |
| 2.0.0          |
| 2.1.0          |

| Version property setting   | Latest Compatible Match   |
|----------------------------|---------------------------|
| 1.0.1                      | 1.0.3                     |
| 1.0.4                      | NO MATCH                  |
| 1.0 or 1.0.*               | 1.0.3                     |
| 1.2 or 1.2.*               | NO MATCH                  |
| 1 or 1.*                   | 1.3.4                     |

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
      <soap:address location="jms:/queue?destination=jms/SOAP\_JMSExport&;connectionFactory=jms/SOAP\_JMSExportQCF
		&;targetService=SOAP\_JMSExport\_BigEchoJmsPort"/>
    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>
```

## SCA default binding example

```
sca://<moduleName>/<exportName>
```

For
services that use the SCA binding, the URI is never physically present
in the resources that define that service.

If using an Endpoint
Lookup mediation primitive to retrieve endpoint information about
services using the SCA binding from a service registry, the Endpoint
Lookup will derive this URI from the information returned by the registry.

```
<?xml version="1.0" encoding="UTF-8"?>
<scdl:export xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ns1="http://big.com" 
		xmlns:scdl="http://www.ibm.com/xmlns/prod/websphere/scdl/6.0.0" 
		xmlns:wsdl="http://www.ibm.com/xmlns/prod/websphere/scdl/wsdl/6.0.0" 
		displayName="SCAExport" name="SCAExport">
  <interfaces>
    <interface xsi:type="wsdl:WSDLPortType" portType="ns1:BigEcho">
      <method name="echo"/>
    </interface>
  </interfaces>
</scdl:export>
```

- Endpoint Lookup mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)