<!-- image -->

# Services and service-related functions

To bring a service into a business process, you use an
import. To make a service available to business processes, you use
an export.

- web services - Services that are offered over the Internet
- adapter-based services - Services that make enterprise data from
large back end systems like DB2 and SAP accessible
- messaging services - Services that provide data from messaging
systems like WebSphere MQ
- Enterprise JavaBeans - Services that are derived from Enterprise
JavaBeans (EJBs)
- registries - Manage services in organizations
- data handlers - Used for services that require unique and uncommon
data formats
- mediation flows - Intervene dynamically between services to transform,
route or augment data.

- Calling services

Imports and exports allow modules to publish their services and to use services from
other sources. Imports and exports require binding information, which specifies the means of
transporting the data from the modules.
- Accessing web services using web service bindings

Web services are self-contained applications that perform business functions, ranging
from a simple query to complex business process interactions. You can use either of two bindings to
invoke web services - a web service binding or an HTTP binding. This topic discusses generating and
configuring web service bindings to call web services.
- Accessing external services with adapters

Services and artifacts on external systems can be imported into IBM Integration Designer.
A wizard discovers applications and data on an Enterprise Information Systems (EIS) and lets you
generate services from the discovered applications and data. The generated artifacts are interfaces
and business objects, which can be used by components in a module.
- Accessing external services with messaging systems

Messaging uses a loosely-coupled style of interaction among applications. Messaging
involves an intermediary called a messaging provider.
- Creating a service gateway

A Service gateway acts as a proxy to a variety of different services by providing a single entry point for incoming requests.
- Creating a dynamic endpoint selection pattern

The concept of intelligent business services entails invoking several endpoints that can be dynamically executed using a set of predefined policies. This function can be further enhanced with a runtime capability that allows you to dynamically select an endpoint as an integration pattern. Dynamic Endpoint Selection (DES) is an integration pattern for dynamic service routing. DES enables service requesters and service providers to connect seamlessly by adding to the capabilities of service invocation. DES routes the service requester to an appropriate service endpoint based on an inbound message without modifying the message or the core business logic.
- Accessing Enterprise JavaBeans (EJB) services

Imports allow connectivity to services outside of IBM Business Automation Workflow environments, while exports are published interfaces from a component or import that offers its service to the outside world (for example, as a web service). EJB (Enterprise JavaBeans) services are accessed through the creation of EJB imports and exports.
- Working with data handlers, faults and registries

Creating your own data handlers provides a way of handling data formats unique to your
own organization. The binding registry page lets you register your own data handlers with IBM
Integration Designer, allowing them to be reused by yourself or others. Adding faults, lets you
handle error conditions related to your application at run time.
- Hypertext Transfer Protocol (HTTP) binding 

Applications using the well-known HTTP web services standard to send and receive messages
can access Service Oriented Architecture (SOA) applications developed in IBM Integration Designer
with this binding. This binding also permits SOA applications to access web services and other
applications using the HTTP protocol.
- Invoking a REST service using OpenAPI 3.0

Use OpenAPI 3.0 REST to discover and invoke a REST service from an OpenAPI 3.0 specification.
- Integrating BPEL processes with IBM Case Manager cases

Business process management and case management are intersecting domains that are
converging as corporations use both approaches to stay agile in a turbulent and competitive business
market. They have some similarities in that they both have processes, however, their designs are
different though complementary.
- Creating a service for Cognos reports in Integration Designer

You can browse IBM Cognos Analytics reports, view them and select to import a report as a
web service. These web services can be used to access the Cognos reports from an
application.
- Importing external services from registries

Registries such as the IBM WebSphere Service Registry and Repository (WSRR) and Universal
Description Discovery and Integration (UDDI) contain artifacts like interfaces and business objects,
which can be shared within an enterprise. You can examine the artifacts at a registry and retrieve
the applicable artifacts for your service oriented architecture applications by using the external
service wizard.
- Building mediation flows 

Mediation flows provide ESB logic by intercepting and modifying messages that are passed
between existing services (providers) and clients (requesters) that want to use those services.
Mediation flows can be implemented in modules or mediation modules. Mediation modules and modules
can be deployed to a workflow server.