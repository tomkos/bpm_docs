<!-- image -->

# Comparison of the programming interfaces for interacting with
BPEL processes and human tasks

|               | EJB interface                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Web service interface                                                                                                                                                                                                             | JMS message interface  (Deprecated)                                                                                                                                                                                                     | REST interface                                                                                                                                                 |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Functionality | This interface is available for both BPEL processes and human tasks. Use this interface to build clients that work generically with processes and tasks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | This interface is available for both BPEL processes and human tasks. Use this interface to build clients for a known set of processes and tasks.For the JMS transport layer, this interface is available for BPEL processes only. | This interface is available for BPEL processes only.                                                                                                                                                                                    | This interface is available for both BPEL processes and human tasks. Use this interface to build web 2.0-style clients for a known set of processes and tasks. |
| Data handling | Supports remote artifact loading of schemas for accessing business object metadata. If the EJB client application is running in the same cell as the Workflow Server that it connects to, the schemas that are needed for the business objects of the processes and tasks do not have to be available on the client, they can be loaded from the server using the remote artifact loader (RAL).  RAL can also be used cross-cell if the client application runs in a full Workflow Server server installation. However, RAL cannot be used in a cross-cell setup where the client application runs in a Workflow Server client installation. | Schema artifacts for input data, output data, and variables, must be available in an appropriate format on the client.                                                                                                            | Schema artifacts for input data, output data, and variables, must be available in an appropriate format on the client.                                                                                                                  | Schema artifacts for input data, output data, and variables, must be available in an appropriate format on the client.                                         |
| Security      | Java™ Platform, Enterprise Edition (Java EE) security.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Web services security.                                                                                                                                                                                                            | Java Platform, Enterprise Edition (Java EE) security for the Workflow Server installation. You can also secure the queues where the JMS client application puts the API messages, for example, using WebSphere® MQ security mechanisms. | Client applications that call the REST methods must use an appropriate HTTP authentication mechanism.                                                          |

- In web service and REST interfaces, all object identifiers, such
as PIID, AIID, and TKIID are represented by a string type. Only the
EJB API interface expects a type-safe object ID.
- Operation overloading is only used for EJB methods and not for
WSDL operations. In some cases, multiple WSDL operations exist, in
other cases, only one WSDL operation exists that allows all of the
parameter variations either by omission (minOccurs="0"),
or null values (nillable="true").
- In some EJB methods, XML namespaces and local names are passed
as separate parameters. Most WSDL operations use the QName XML schema
type to pass these parameters.
- The EJB interface returns a set of API objects, which expose getter
and setter methods for the contained fields. web service and REST
interfaces return complex-typed (XML or JSON) documents to the client.
- Some Human Task Manager services operating on human tasks are
also available as Business Flow Manager services operating on activities
that call a human task.
- The declaration of the replyTo parameter of the
callAsync() WS API reuses elements from the WS-Addressing Specification (wsa.xsd)
but doesn't actually implement the WS-A specification. The correlation mechanism, as referred to in
the WS-Addressing Specification, states that using the MessageID header field,
the Element ReferenceParameters or ReferenceProperties
EndpointReferenceType properties, or extensions is not supported. To correlate a request
and response message, use an unique property of your business data. For example, use
processInstanceName, set processInstanceName in the
callAsync() request, and add it to your business data of the response message.

- Business Flow Manager API comparison

The Busness Flow Manager API provides EJB, Web service, JMS, and REST generic programming
interfaces. Each of these interface supports different API operations.
- Human Task Manager API comparison

The Human Task Manager API provides EJB, Web service, and REST generic programming
interfaces. Each of these interface supports different API operations.
- Business Process Archive Manager EJB API support

Only a subset of the Business Process Choreographer EJB API operations can be used on a Business Process Archive Manager configuration. Custom clients that already access the EJB API of Business Process Choreographer can be redirected to a Business Archive Manager configuration to read or delete BPEL process and task data that has been moved to the archive.