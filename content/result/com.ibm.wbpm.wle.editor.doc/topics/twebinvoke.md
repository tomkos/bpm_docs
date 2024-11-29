# Invoking web services in the designer

- Discovering and invoking a web service

Discover a web service from a URL and generate an external service based on the discovered web service. You can then use the external service in a service flow to invoke the web service.
- Adding a web services server in the designer

You can add one or more web services servers to your process application. Each web services server describes the location of a web service endpoint and can be referenced by external services that you use to invoke a web service. This reference enables the sharing of configuration information for invoking web services that start the same endpoint, eliminating the need to configure similar information multiple times. In addition, if you need to change the information that is associated with a particular endpoint, you can change the web services server information and the updated information can be used by any external service that references the web services server.
- Using web services for inter-process application communication

 Traditional: 
If you want to call a web service that is exposed by a process application on the same Business Automation Workflow server from your process application, and you want to use business objects in a toolkit that is referenced by both process applications then you must enable web services interoperability.
- Creating implicit SOAP headers for outbound web service integrations

SOAP headers are used to communicate application-specific context information within SOAP request and response messages. This context information can be anything that you need to send along with the web service operation parameters. An implicit SOAP header is one that is not defined in the web service WSDL document. As part of your outbound web service integrations, you can add  implicit SOAP headers to your web service request messages and retrieve SOAP headers from response messages.
- Setting up message-level encryption

 Traditional: 
 Message-level encryption provides confidentiality by applying encryption to all or parts of a SOAP message. The encryption spans the entire communication chain between the consumer and the provider. To take advantage of this type of encryption during web service integration, you must enable the corresponding configuration settings.
- Troubleshooting web services and outbound web service integrations

Learn how to solve problems that you may have when using web service external services.
- Troubleshooting XML schema messages for web service integrations

When you are using web service external services, you might encounter error and warning messages if you use XML constructs that are not supported or have problems in workflow designer.