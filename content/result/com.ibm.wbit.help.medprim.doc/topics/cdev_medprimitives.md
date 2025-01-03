# List of mediation primitives

- Business Object Map mediation primitive

Use the Business Object Map mediation primitive to transform messages. You can define message transformations graphically, using a business object map.
- Custom Mediation primitive

Use the Custom Mediation primitive to call custom logic.
- Data Handler mediation primitive

Use the Data Handler mediation primitive to transform part of a message. The Data Handler primitive is used to convert an element of a message from a physical format to a logical structure, or from a logical structure to a physical format.
- Database Lookup mediation primitive

Use the Database Lookup mediation primitive to modify a message, using information from a database.
- Endpoint Lookup mediation primitive

Use the Endpoint Lookup mediation primitive to dynamically route messages to appropriate service endpoints. The Endpoint Lookup searches for service information in a WebSphere® Service Registry and Repository (WSRR).
- Event Emitter mediation primitive

Use the Event Emitter mediation primitive to emit significant business events from inside a mediation flow.
- Fail mediation primitive

Use the Fail mediation primitive to stop a mediation flow, and generate an exception.
- Fan In mediation primitive

Use the Fan In mediation primitive to help you combine multiple messages.
- Fan Out mediation primitive

Use the Fan Out mediation primitive to create different messages from a repeating element in the input message. Also, use the Fan Out mediation primitive, together with the Fan In mediation primitive, to aggregate (combine) service responses.
- Flow Order mediation primitive

Use the Flow Order mediation primitive to specify the order in which branches of a flow are fired. If you do not use the Flow Order mediation primitive, the execution order of the branches is undefined.
- Gateway Endpoint Lookup mediation primitive

Use the Gateway Endpoint Lookup mediation primitive to route service requests within a Service Gateway. There are three different modes: URL, XPath and Action. The URL and XPath modes will be used when the module is acting as a proxy gateway and endpoint lookups are based on the virtual service name. The Action mode is used to resolve SOAP Actions or WS-Addressing Actions within WebSphere Service Registry and Repository for Dynamic and Static Service Gateway patterns.
- HTTP Header Setter mediation primitive

Use the HTTP Header Setter primitive to create, modify, copy or delete HTTP message headers.
- JMS Header Setter mediation primitive

Use the Java Messaging Service Header Setter primitive to create, modify, copy or delete JMS message headers.
- Mapping mediation primitive

Use the Mapping mediation primitive to transform messages
- Message Element Setter mediation primitive

Use the Message Element Setter mediation primitive to set the content of messages.
- Message Filter mediation primitive

Use the Message Filter mediation primitive to selectively route messages.
- Message Logger mediation primitive

Use the Message Logger mediation primitive to store messages in a relational database. Alternatively, you can use the custom logging functionality to write to other storage mediums.
- Message Validator mediation primitive

Use the Message Validator mediation primitive to validate some, or all, parts of a message.
- MQ Header Setter mediation primitive

Use the MQ Header Setter mediation primitive to create, set, copy or delete WebSphere MQ message headers.
- Policy Resolution mediation primitive

Use the Policy Resolution mediation primitive to dynamically configure a mediation flow, using mediation policies. Mediation policies are stored in, and retrieved from, WebSphere Service Registry and Repository (WSRR).
- Service Invoke mediation primitive

Use the Service Invoke mediation primitive to call a service from inside a mediation flow, as an alternative to using the callout mechanism at the end of the mediation flow.
- Set Message Type mediation primitive

Use the Set Message Type mediation primitive to overlay message fields with more detailed structures. You can then manipulate message content more easily.
- SLA Check mediation primitive

Use the SLA Check mediation primitive to check that a service level agreement exists.
- SLA Endpoint Lookup mediation primitive

Use the SLA Endpoint Lookup mediation primitive to look up endpoints referenced from an active service level agreement (SLA) between a service consumer and a service provider.
- SOAP Header Setter mediation primitive

Use the SOAP Header Setter mediation primitive to create, set, copy or delete SOAP message headers.
- Stop mediation primitive

Use the Stop mediation primitive to stop a path in the flow, without generating an exception.
- Subflow mediation primitive

A mediation subflow is a preconfigured set of mediation primitives that are wired together to realize a common pattern or use case. The subflow mediation primitive provides a way to invoke a subflow in a parent mediation flow, and can be used in mediation flows or in subflows.
- Synchronous Transaction Rollback mediation primitive

You can use the Synchronous Transaction Rollback mediation primitive to roll back the current transaction and then continue processing the flow. The Synchronous Transaction Rollback can be used only in mediation flows that use a synchronous invocation style.
- Trace mediation primitive

Use the Trace mediation primitive to write trace messages to the server logs or to log files. The trace messages can help in developing and debugging a mediation flow.
- Type Filter mediation primitive

Use the Type Filter mediation primitive to selectively route messages.
- UDDI Endpoint Lookup mediation primitive

Use the UDDI Endpoint Lookup mediation primitive to dynamically route messages to appropriate service endpoints.
- WebSphere eXtreme Scale: Store mediation primitive

Use the eXtreme Scale Store mediation primitive to store information into the cache.
- WebSphere eXtreme Scale: Retrieve mediation primitive

Use the eXtreme Scale Retrieve mediation primitive to retrieve information from a eXtreme Scale cache.