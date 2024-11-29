# HTTP bindings

- SCA-hosted services can invoke HTTP applications using an HTTP
import.
- SCA-hosted services can expose themselves as HTTP-enabled applications,
so they can be used by HTTP clients, using an HTTP export.
- IBM® Integration
Designer and Workflow Server can communicate
between themselves across an HTTP infrastructure, consequently users
can manage their communications according to corporate standards.
- IBM Integration
Designer and Workflow Server can act
as mediators of HTTP communications, transforming and routing messages,
which improves the integration of applications using a HTTP network.
- IBM Integration
Designer and Workflow Server can be
used to bridge between HTTP and other protocols, such as SOAP/HTTP
Web services, Java™ Connector
Architecture (JCA)-based resource adapters, JMS, and so on.

Detailed information about creating HTTP import and export bindings
can be found in the Integration Designer information
center. See the Developing integration applications > Accessing external services with HTTP> topics.

- HTTP bindings overview

 The HTTP binding provides connectivity to HTTP-hosted applications. It mediates communication between HTTP applications and allows existing HTTP-based applications to be called from a module.
- HTTP headers

HTTP import and export bindings allow configuration of HTTP headers and their values to be used for outbound messages. The HTTP import uses these headers for requests, and the HTTP export uses them for responses.
- HTTP data bindings

For each different mapping of data between a Service Component Architecture (SCA) message and an HTTP protocol message, a data handler or an HTTP data binding must be configured. Data handlers provide a binding-neutral interface that allows reuse across transport bindings and represent the recommended approach; data bindings are specific to a particular transport binding. HTTP-specific data binding classes are supplied; you can also write custom data handlers or data bindings.