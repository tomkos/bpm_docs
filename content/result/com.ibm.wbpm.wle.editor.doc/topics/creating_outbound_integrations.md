# Creating outbound integrations

To create an outbound integration with an external database, use
the predefined SQL Integration services that are available in the Business Automation Workflow System
Data Toolkit.

## Integration Service implementations

Integration
Service implementations can contain integration step types that you
can configure for the system that you are interacting with. For example,
a Web Service Integration step is useful if you are not passing volumes
of information. A Java Integration step gives you access to the features
of the Java language, including published Java libraries and APIs.
The following table describes the integration step types that are
available for Integration Service implementations.

| Integration step type   | Description                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Web Service Integration | Uses a SOAP connection to access objects from a web service. A Web Service Integration step hides the complexity of the underlying WSDL, SOAP request, and SOAP response. It also converts inputs into the appropriate XML and outputs into the appropriate Business Automation Workflow variables.Supported WSDL styles are: RPC literal Document literal Document literal wrapped |
| Java Integration        | Calls methods from a Java class and interfaces with most third-party Java APIs, and thus supports various integration scenarios.                                                                                                                                                                                                                                                    |
| Content Integration     | Enables business processes that are developed in Process Designer to work with an Enterprise Content Management system.                                                                                                                                                                                                                                                             |
| Invoke UCA              | Uses an undercover agent (UCA) to invoke an Business Automation Workflow service or a business process definition (BPD).                                                                                                                                                                                                                                                            |

## IBM Business Automation
Workflow Integration
Service implementations

| Integration step type        | Description                                                                                                                                  |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| IBM Case Manager Integration | Enables business processes that are developed in Process Designer to work with an IBM Business Automation Workflow case management solution. |
| Invoke UCA                   | Invokes an Business Automation Workflow service or a BPD..                                                                                   |

- Creating outbound integrations to web services

Integration services enable outbound integration with web services so that processes can retrieve and update data that is stored on an external system. You can use a generic web service connector or a Web Service Integration step to enable the access to the web service.
- Calling a Java method in an Integration service (deprecated)

 Traditional: 
If the implementation for an activity requires calling methods from a Java class, you can use the Java Integration step in an Integration service.
- Sending attachments using an SMTP server (deprecated)

 Traditional: 
With a Java Integration component, you can send attachments by using a Simple Mail Transfer Protocol (SMTP) server.
- Using IBM Business Automation Workflow SQL Integration services (deprecated)

To integrate with an external database, you can use the SQL Integration services available in the Business Automation Workflow System Data Toolkit.