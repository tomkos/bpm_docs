<!-- image -->

# Creating a service gateway

All requesters interact with a single endpoint address exposed
by the gateway. The gateway is responsible for performing a common
operation on every message and routing the request to the correct
service provider.

A service gateway has a single generic export and a single generic
gateway interface, which allows the gateway to handle messages for
different port types. Messages entering the gateway can have the headers,
body or both manipulated within a mediation flow before being forwarded
onto the service provider.

- In a dynamic service gateway, the endpoint address of the
service provider is determined within the mediation flow by looking
up information from a database, a registry or from the message contents.
The mediation flow typically modifies the header information in the
message.
- In a static service gateway, the import is created using
a specific interface known before the message enters the gateway.
The mediation flow typically modifies the information contained in
the body and header of a message.

- Web service
- HTTP
- JMS
- Generic JMS
- MQ JMS
- MQ

- Static service gateway examples

Examples of service gateway patterns where the routing is static, that is, messages are routed to specific service providers.
- Creating a static service gateway

IBM Integration Designer provides a pattern that is a fast path to generate a service gateway, along with all the required artifacts. In a static service gateway, the endpoint address of the service provider is known before the message enters the gateway. The mediation flow typically modifies the information contained in the body and header of a message.
- Creating a dynamic service gateway

IBM Integration Designer provides a pattern that is a fast path to generate a service gateway, along with all the required artifacts. In a dynamic service gateway, the endpoint address of the service provider is determined within the mediation flow by looking up information from a database, a registry or from the message contents. The mediation flow typically modifies the header information in the message.
- Dynamic service gateway examples

Examples of service gateway patterns where the routing is dynamic, that is, service providers are determined dynamically at run time.
- Service gateway artifacts

These are the artifacts that are required to create a service gateway in IBM Integration Designer. The pattern generates these artifacts for you.