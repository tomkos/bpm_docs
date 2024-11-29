<!-- image -->

# Accessing web services using web service bindings

- Generating web service bindings for exports

Create a web service binding as an easy way to offer web services.
- Generating web service bindings for imports

Create a web service binding as an easy way to consume web services.
- Generating web service bindings for service gateway

Create web service bindings for your service gateway.
- Advanced properties for service gateway

Additional properties that you would use if your application works with the service gateway are discussed.
- Working with attachments

Attachments provide a way to pass additional information in a message in an efficient manner by holding the attachment data separate from the message body. For example, a SOAP message or email might contain a person's resume with an attachment that holds the person's photograph.
- Referenced and swaRef-type attachments

Referenced and swaRef-type attachments can be added to exports with a web services binding.
- WS-I compliance with SOAP messages

When working with attachments, previous versions of IBM® Integration Designer handled Web Services Interoperability (WS-I) compliance for SOAP messages automatically. A page in the wizard to generate a web services binding lets you select either this previous automatic configuration or lets you choose which of the non-binary parts of an operation should be bound to the message body.
- Policy sets

Policy sets reduce the complexity of configuring web services by providing reusable configurations.
- Endpoint updates in a web services binding

Web services can be moved to a different server. You should know how to change the endpoint URL address in such cases as the endpoint provides the server location of the web service you are using.
- Java API for XML Web Services (JAX-WS) handlers

JAX-WS handlers can be used with the web services binding.
- SOAP header information with a JAX-WS handler

SOAP header information can be passed to an SOA application by creating a JAX-WS handler and a schema.
- Enabling MTOM support in JAX-WS bindings

IBM Integration Designer (IID) provides configuration options to enable JAX-WS bindings to send and receive web service messages which include SOAP Message Transmission Optimization Mechanism (MTOM) attachments. This mechanism improves the transmission efficiency of large binary attachments in SOAP messages.
- Propagation

Context propagation lets you take information associated with a runtime or an application and pass it along with requests that are the result of interactions with that runtime or application.
- Using SOAP-encoded arrays

Passing SOAP-encoded arrays can cause problems if not understood.
- Limitations of the web services binding

Limitations of using the web services binding are discussed.