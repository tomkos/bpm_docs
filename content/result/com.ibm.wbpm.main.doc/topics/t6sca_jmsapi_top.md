<!-- image -->

# (Deprecated) Developing client applications using the Business
Process Choreographer JMS API (deprecated)

## About this task

JMS
client applications exchange request and response messages with the
JMS API. To create a request message, the client application fills
a JMS TextMessage message body with an XML element representing the
document/literal wrapper of the corresponding operation.

- (Deprecated) Requirements for BPEL processes in JMS-based client applications (deprecated)

BPEL processes developed with IBM® Integration Designer to run on Business Process Choreographer must conform to specific rules to be accessible through the JMS API.
- (Deprecated)Authorization for JMS renderings (deprecated)

To authorize use of the Business Process Choreographer JMS API, security settings must be enabled in WebSphere® Application Server.
- Accessing the Business Process Choreographer JMS API (deprecated)

To send and receive messages through the JMS interface, an application must first create a connection to the BPC.cellname.Bus, create a session, then generate message producers and consumers.
- Copying artifacts for JMS client applications (deprecated)

A number of artifacts can be copied from the Workflow Server environment to help in the creation of JMS client applications.
- Checking the response message for business exceptions in JMS client applications (deprecated)

JMS client applications must check the message header of all response messages for business exceptions.
- Example: executing a long running process using the Business Process Choreographer JMS API (deprecated)

This example shows how to create a generic client application that uses the JMS API to work with long-running processes.