<!-- image -->

# Exporting WSDL and XSD files for BPEL process and human task
web services applications

## About this task

- HTTP transport layer
- JMS transport layer

This procedure must be repeated for each BPEL process
or human task that your client application needs to interact with.

For example, to create
and start a human task, the following items of information must be
passed to the task interface:

- The task template name
- The task template namespace
- An input message, containing formatted business data
- A response wrapper for returning the response message
- A fault message for returning faults and exceptions

These items are encapsulated within a single business object.
All operations of the web service interface are modeled as a document/literal
wrapped operation. Input and output parameters for these operations
are encapsulated in wrapper documents. Other business objects define
the corresponding response and fault message formats.

In order
to create and start the BPEL process or human task through a web service,
these wrapper objects must be made available to the client application
on the client side.

This is achieved by exporting the business
objects from the WebSphere® environment as Web Service Definition
Language (WSDL) and XML Schema Definition (XSD) files, and importing
the data type definitions into your client programming environment.

## Procedure

1. Launch the IBM® Integration
Designer Workspace
if it is not already running.
2. Select the Library module containing the business objects
to be exported. A Library module is a compressed file that
contains the necessary business objects.
3. Export the Library module.
4. Copy the exported files to your client application development
environment.

## Example

Assume a BPEL process exposes the
following web service operation:

```
<wsdl:operation name="updateCustomer">
    <wsdl:input message="tns:updateCustomerRequestMsg" 
                name="updateCustomerRequest"/>
    <wsdl:output message="tns:updateCustomerResponseMsg" 
                 name="updateCustomerResponse"/>
    <wsdl:fault message="tns:updateCustomerFaultMsg" 
                name="updateCustomerFault"/>
  </wsdl:operation>
```

with the WSDL messages defined as:

```
<wsdl:message name="updateCustomerRequestMsg">  
    <wsdl:part element="types:updateCustomer" 
               name="updateCustomerParameters"/> 
  </wsdl:message>
  <wsdl:message name="updateCustomerResponseMsg">
    <wsdl:part element="types:updateCustomerResponse" 
               name="updateCustomerResult"/> 
  </wsdl:message>
  <wsdl:message name="updateCustomerFaultMsg">
    <wsdl:part element="types:updateCustomerFault" 
               name="updateCustomerFault"/> 
  </wsdl:message>
```

The concrete customer-defined elements types:updateCustomer, types:updateCustomerResponse,
and types:updateCustomerFault must be passed to and
received from the web services APIs using UserData parameters
in all generic operations (call, sendMessage,
and so on) performed by the client application.

The customer-defined
elements are created, serialized and deserialized on the client application
side using classes generated using the exported XSD files. The generation
of these classes is part of the web service proxy generation where
the exported WSDL and XSD files are included.

```
<soapenv:Envelope xmlns:soapenv="..." ...>
  <soapenv:Header>
    ...
  </soapenv:Header>
  <soapenv:Body>
    <bfm:sendMessage 
         xmlns:bfm="http://www.ibm.com/xmlns/prod/websphere/business-process/services/7.0">
      <processTemplateName>customerProcessTemplate</processTemplateName>
      <portType xmlns:cns="http://example.com/customerProcess">cns:customerProcessPortType</portType>
      <operation>updateCustomer</operation>
      <input>
        <cns:updateCustomer xmlns:cns="http://example.com/customerProcess">
          <street>1600 Pennsylvania Avenue Northwest</street>
          <city>Washington, DC 20006</city>
        </cns:updateCustomer>
      </input>
    </bfm:sendMessage>
  </soapenv:Body>
</soapenv:Envelope>
```