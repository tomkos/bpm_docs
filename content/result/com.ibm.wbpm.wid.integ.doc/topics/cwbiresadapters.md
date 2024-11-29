<!-- image -->

# Using WebSphere Business
Integration Adapters

- Right-click your module and from the menu, select New >
External Service. Select Messaging in
the New External Service wizard and click Next.
- Select WBI Adapter Artifact Importer. Continue
with the wizard sequence completing the fields necessary for using
a WebSphere Business Integration
adapter.

The WebSphere Business
Integration Adapter artifacts must first be created using the toolset
provided with the WebSphere Business
Integration Adapter Framework. Unlike the IBM WebSphere Adapters,
none of these adapters are supplied for development purposes.

- WebSphere Adapters
rely on standard JCA contracts to manage lifecycle tasks such as stopping,
starting; WebSphere Business
Integration Adapters rely on the WebSphere Adapter
Framework to manage connectivity.
- With WebSphere Adapters,
you use an external service wizard in IBM Integration
Designer to
discover an EIS system and its available information. The external
service wizard develops business objects from the discovered information. WebSphere Business Integration
Adapters use a separate Object Discovery Agent (ODA) to probe an EIS
and generate business object definition schemas.
- An outbound service type in WebSphere Adapters
is known as request processing with WebSphere Business Integration Adapters.
An inbound service type in WebSphere Adapters
is known as event processing with WebSphere Business
Integration Adapters.
- WebSphere Business
Integration Adapters always reside outside of an application server
at run time. The server communicates with this type of adapter through
a Java™ Messaging Service (JMS)
transport layer.

To see a complete list of supported WebSphere Business Integration Adapters,
go to WebSphere Adapters.

1. Migrate the artifacts used by the WebSphere Business Integration
Adapter to those expected by the IBM Workflow
Server.
2. Install and configure the migrated application.