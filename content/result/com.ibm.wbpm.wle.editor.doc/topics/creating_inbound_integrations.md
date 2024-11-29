# Creating inbound integrations

See the following topics for instructions and more information:

- Building a sample inbound integration

Several components must work together to complete an inbound integration. You can use the procedures listed in this topic to build and test a complete integration.
- Creating implicit SOAP headers for inbound web service integrations

SOAP headers are used to communicate application-specific context information within SOAP request and response messages. This context information can be anything that you must send along with the web service operation parameters. An implicit SOAP header is one that is not defined in the web service WSDL document. In an inbound web service integration, you can retrieve SOAP headers from an incoming request message and include SOAP headers in the outgoing response message.
- Posting a message to IBM Business Automation Workflow Event Manager

If you want to post a message from an external system to the Event Manager, you must use the message structure that is described in this topic.
- Publishing IBM Business Automation Workflow web services

Business Automation Workflow can publish web services in the same way that it consumes web services. Using a SOAP connection, external applications can call the Business Automation Workflow web service to initiate a particular service or set of services.