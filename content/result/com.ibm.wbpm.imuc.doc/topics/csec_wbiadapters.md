# Considerations for securing WebSphere Business Integration
Adapters

- WebSphere® Business Integration Adapters
consist of a collection of software, application program interfaces
(APIs), and tools that enable applications to exchange business data
through an integration broker. WebSphere Business
Integration Adapters rely on JMS messaging which does not support
security context propagation.
- For inbound communication from WebSphere Business Integration
Adapters into IBM® Business Automation Workflow, there
is no authentication mechanism. The reliance on JMS messaging precludes
security context propagation.
- The entry from an adapter to IBM Business Automation Workflow always
employs a Service Component Architecture (SCA) export. The SCA export
has to be wired to an SCA component, such as mediation, business process,
SCA Java™ component, or Selector.
- The value for SecurityIdentity is a role, not
a user. Nevertheless, when the EAR file is deployed to IBM Business Automation Workflow, you
must provide a user name and password for the identity that is to
be used. The use of SecurityIdentity prevents exceptions
being thrown if a downstream component is secured and requires the
client to have an authenticated identity.Note: The use of SecurityIdentity does
not secure the communication between the adapter and the EIS.
- WebSphere Business Integration Adapters
send data to IBM Business Automation Workflow as
JMS messages over the service integration bus.