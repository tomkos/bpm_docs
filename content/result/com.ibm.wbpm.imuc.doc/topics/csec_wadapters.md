# Considerations for securing WebSphere Adapters

- WebSphere® Adapters enable managed, bidirectional
connectivity between an EIS and Java EE components supported by IBM® Business Automation Workflow.
- For inbound communication from WebSphere Adapters into IBM Business Automation Workflow, there
is no authentication mechanism. JCA also lacks inbound security support;
therefore, WebSphere Adapters also have no authentication
mechanism for inbound communication.
- The entry from an adapter to IBM Business Automation Workflow always
employs a Service Component Architecture (SCA) export. The SCA export
has to be wired to an SCA component, such as mediation, business process,
SCA Java™ component, or Selector.
- The security solution is to define a runAs role
on the component that is the target for the WebSphere Adapter
export. This is done using the SCA qualifier SecurityIdentity during
development. When the component runs, it does so under the identity
defined in the runAs role.
- The value for SecurityIdentity is a role, not
a user. Nevertheless, when the EAR file is deployed to IBM Business Automation Workflow, you
must provide a user name and password for the identity that is to
be used. The use of SecurityIdentity prevents exceptions
being thrown if a downstream component is secured and requires the
client to have an authenticated identity.Note: The use of SecurityIdentity does
not secure the communication between the adapter and the EIS.
- WebSphere Adapters reside in the JVM of
the IBM Business Automation Workflow,
and therefore only the communication between the adapter and the target
EIS needs to be secured. The protocol between the adapter and the
EIS is EIS-specific. The documentation of the EIS provides information
about how to secure this link.