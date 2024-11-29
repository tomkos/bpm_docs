<!-- image -->

# Accessing the WebSphere MQ header

In addition to the standard function selector and data handler configuration, the WebSphere MQ
binding provides optional configuration for custom header data bindings.

- MQMD (MQ Message Descriptor)
- MQRFH (MQ Rules and Formatting Header)
- MQRFH2 (MQ Rules and Formatting Header 2)
- MQIIH (MQ IMS Information Header)
- MQCIH (MQ CICS Information Header)
- MQOpaqueHeader

The MQOpaqueHeader data binding, processes unrecognized MQ headers in a standard MQ format. It
creates a DataObject with a structure ID, version, structure length, encoding, CCSID, format, and
flags. The remaining data is set into a byte array. To fully parse user-defined headers, you must
use a custom WebSphere MQ data binding. This is described in more detail in Using Java to access the WebSphere MQ header.

- Using Java to access the WebSphere MQ header

When an import or export, with a WebSphere MQ binding receives a WebSphere MQ message, the headers are parsed and made available in the context service. Consequently the headers are available for authors of custom function selectors, data handlers and mediation components.
- Using a mediation flow component to access the WebSphere MQ header

The MQ Header Setter mediation primitive provides a mechanism for managing MQ headers in a message.