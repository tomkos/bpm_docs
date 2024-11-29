# Creating outbound integrations to web services

A generic web service connector, Call WebService via SOAP,
is provided in the System Data Toolkit. This connector abstracts the
complexity of the web service implementation and requires only minimal
configuration. For more information on using the connector, see Calling a web service using a SOAP connector.

However, if you have specific requirements on the web service,
such as the type of security or message encryption, use a Web Service
Integration step to integrate with the service.

- SOAP headers

Use a SOAP header to include application-specific context information in the web service SOAP request and response messages.
- Creating implicit SOAP headers for outbound web service integrations

SOAP headers are used to communicate application-specific context information within SOAP request and response messages. This context information can be anything that you need to send along with the web service operation parameters. An implicit SOAP header is one that is not defined in the web service WSDL document. As part of your outbound web service integrations, you can add  implicit SOAP headers to your web service request messages and retrieve SOAP headers from response messages.
- Adding a web services server in the desktop Process Designer (deprecated)

 Traditional: 
You can add one or more web services servers to your process application. Each web services server describes the location of a web service endpoint and can be referenced by an outbound web service integration. This reference enables the sharing of configuration information between web service integrations that start the same endpoint, eliminating the need to configure similar information multiple times. In addition, if you need to change the information that is associated with a particular endpoint, you can change the web services server information and the updated information can be used by any web service integration that references the web services server.
- Configuring a Web Service Integration component in the desktop Process Designer (deprecated)

 Traditional: 
Use a Web Service Integration component to invoke a web service that is hosted externally. You can configure the WSDL properties, SOAP header information, authentication, signature and encryption properties for the web service integration.
- Security for web service integration

You can secure a web service using policy sets and bindings or by manually creating an authentication method that requires a user name and password.
- Web service faults

Faults are a way of handling exceptions in web services at run time. A fault that helps a user understand a problem and what he can do about it leads to a quick resolution of the problem. If you use a Web Service Integration step from the integration service palette to call an outbound web service, your step can catch and handle faults.
- Serialization of IBM Business Automation Workflow objects for use in web services

You can add metadata to Business Automation Workflow objects to control how those objects are serialized into XML elements in a SOAP request for web services.
- Setting up message-level encryption

 Traditional: 
 Message-level encryption provides confidentiality by applying encryption to all or parts of a SOAP message. The encryption spans the entire communication chain between the consumer and the provider. To take advantage of this type of encryption during web service integration, you must enable the corresponding configuration settings.
- WSDL and XSD cache algorithm for web service integration (deprecated)

 Traditional: 
 IBM BPM Standard V8.5.6.0 applications created in desktop Process Designer cache WSDL and XSD web service files that are associated with integration services when you create the integration services or before the first time the integration services are called. The files for process applications that are created in desktop Process Designer V8.5.6.0 are cached when they are created, by default. The files for migrated process applications are cached when these applications run.
- Troubleshooting web services and outbound web service integrations

Learn how to solve problems that you may have when using web service external services.
- Troubleshooting XML schema messages for web service integrations

When you are using web service external services, you might encounter error and warning messages if you use XML constructs that are not supported or have problems in workflow designer.