<!-- image -->

# (Deprecated) Structure of a Business Process Choreographer
JMS message (deprecated)

A Java Message Service (JMS) message consists of:

- A message header for message identification and routing information.
- The body (payload) of the message that holds the content.

The Business Process Choreographer supports text message formats
only.

## Message header

JMS allows clients to access
a number of message header fields.

Each response message contains the following
JMS header fields:

- IsBusinessException"False" for WSDL output messages,
or "true" for WSDL fault messages.

ServiceRuntimeExceptions are not returned to asynchronous
client applications. When a severe exception occurs during the processing
of a JMS request message, it results in a runtime failure, causing
the transaction that is processing this request message to roll back.
The JMS request message is then delivered again. If the failure occurs
early, during processing of the message as part of the SCA Export
(for example, while deserializing the message), retries are attempted
up to the maximum number of failed deliveries specified by the SCA
Export's receive destination.

After the maximum number
of failed deliveries is reached, the request message is added to the
system exception destination of the Business Process Choreographer
bus. If, however, the failure occurs during actual processing of the
request by the Business Flow Manager's SCA component, the failed request
message is handled by the failed event management infrastructure,
that is, it may end up in the failed event management database if
retries do not resolve the exceptional situation.

## Message body

Operations exposed by BPEL
processes or human tasks must comply with the document/literal wrapper
style. The JMS message body is a String containing an XML document
that represents the document/literal wrapper element of the operation.
The generic operations of the JMS message interface propagate the
document-wrapper element to and from the operation that is implemented
by the BPEL process or human task.

The following example shows a simple valid request message
body:

```
<bfm:queryProcessTemplates 
     xmlns:bfm="http://www.ibm.com/xmlns/prod/websphere/business-process/services/6.0">
  <whereClause>PROCESS\_TEMPLATE.STATE IN (1)</whereClause>
</bfm:queryProcessTemplates>
```

The bfm:sendMessage element
is the document wrapper element of the JMS API operation. It includes
the cns:updateCustomer element, which is the document
wrapper element for the operation that is implemented by the process.
This process has, for example, a bpel:receive activity
that references the cns:customerProcessPortType WSDL
port type, and the updateCustomer WSDL operation.

```
<bfm:sendMessage 
     xmlns:bfm="http://www.ibm.com/xmlns/prod/websphere/business-process/services/6.0">
  <processTemplateName>customerProcessTemplate</processTemplateName>
  <portType xmlns:cns="http://example.com/customerProcess">cns:customerProcessPortType</portType>
  <operation>updateCustomer</operation>
  <cns:updateCustomer xmlns:cns="http://example.com/customerProcess">
    <street>1600 Pennsylvania Avenue Northwest</street>
    <city>Washington, DC 20006</city>
  </cns:updateCustomer>
</bfm:sendMessage>
```