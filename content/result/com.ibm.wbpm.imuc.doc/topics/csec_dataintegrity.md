# Data integrity and privacy

Data privacy and data integrity are closely related concepts. For a more detailed discussion,
refer to the WebSphere® Application
Server Network Deployment
documentation.

## Privacy

Privacy means that an unauthorized user should not be able to intercept and read
data.

## Integrity

Integrity means that an unauthorized user should not be able to alter data.

## Data integrity and privacy solutions provided in IBM Business Automation Workflow

- Secure Sockets Layer (SSL) protocol: SSL uses a handshake to authenticate
the end points and exchange information used to generate the session
key that will be used by the end points for encryption and decryption.
SSL is a synchronous protocol and is suitable for point-to-point communication.
SSL requires that the two end points maintain a connection with each
other for the duration of the SSL session.
- WS-Security: This standard defines Simple Object Access Control
(SOAP) extensions for securing SOAP messages. WS-Security adds support
for authentication, integrity, and privacy for a single SOAP message.
Unlike SSL, there is no handshake to establish a session key. This
makes WS-Security suitable for securing messages in an asynchronous
environment, such as SOAP over Java™ Message
Service (JMS) or SOAP over Service Integration Bus (SIB). WS-Security
deployment descriptors can be set in your applications before deployment. See related information for more details.

- Accessing web services using a web service binding
- Creating outbound integrations to web services
- Creating an inbound web service

## Configuring a web services web client to use SSL

You
can configure a web services client to invoke a web service using
Secure Sockets Layer (SSL).

The details of how to configure your web services web client to use SSL are provided in the
WebSphere Application
Server
Enabling SSL communication for web services access topic. A more general
discussion of securing web services can be found in the  Securing web services at the transport level topic.

## Related information

- Security planning overview
- Editing module deployment properties