<!-- image -->

# SOAP/JMS and SOAP/HTTP transport protocols

In most cases, web services are implemented using SOAP/HTTP as a transport protocol. IBM® Business Automation
Workflow supports both SOAP/JMS and SOAP/HTTP protocols in their implementation
of JAX-RPC and JAX-WS bindings. In many cases, SOAP/JMS is selected due to its reliability. But
there are other factors to consider when selecting between SOAP/JMS or SOAP/HTTP.

- Externally facing web services (for example. consumers or providers)
- For simple point-to-point and stateless services

- High-volume distributed messaging
- Asynchronous messaging
- Where a transaction boundary is needed in the middleware
- Where the message consumers are slower than the providers
- Guaranteed delivery, only once delivery of messages, or both
- 

Also consider using the JMS import and export bindings with the SOAP data handler.