<!-- image -->

# HTTP binding overview

The following sections provide an overview of the HTTP binding:

- What is the HTTP binding?
- Why has the HTTP binding grown in importance?
- Comparing the HTTP binding to the web services binding
- HTTP binding at run time

## What is the HTTP binding?

Hypertext
Transfer Protocol (HTTP) is a widely-used protocol for transferring
information on the web. Though originally designed to publish and
retrieve HTML pages, it has now become a standard request/response
protocol between clients and server as defined by the HTTP protocol published
by the World Wide Web consortium (W3C). Today many standard HTTP methods
such as GET, POST, PUT, DELETE and so on are a part of this widely-used
protocol.

When working with an external application using the
HTTP protocol, an HTTP binding is necessary. The HTTP binding handles
the transformation of data passed in as a message in a native format
to a business object in a Service Component Architecture-based (SCA)
application. The HTTP binding also can transform data passed out as
a business object to the native format expected by the external application.
for an incoming messaging.

## Why has the HTTP binding grown in importance?

As
the SOAP/HTTP (referred to as SOAP over HTTP) web services binding
gained momentum, businesses began seeing the potential of the HTTP
protocol for business needs and application integration. SOAP/HTTP
web services became the most common means for business-to-business
transactions over the Internet. However, adding more robustness to
SOAP/HTTP to suit business needs such as the Web Service Description
Language (WSDL), supporting the XML Schema specification and adding
Quality of Service (QOS) led to interoperability problems among vendors
and additional complexity of the initial specification. It also led
to the need for more skills to use SOAP/HTTP.

Users realized
that there were many situations that did not need the extra functions
added to SOAP/HTTP but wanted to take advantage of the ubiquitous
web infrastructure to send or receive relatively simple information
using the HTTP protocol. They started using HTTP-based services to
send and receive data in a set of different loosely-defined formats.

The
HTTP binding is suited for this type of user as it combines the ease-of-use
and simplicity of the original HTTP protocol with integration to large,
scalable and secure SOA applications. Conversely, the HTTP binding
allows SOA applications to take advantage of the many existing HTTP-based
applications, bringing them into the SOA framework. The binding also
provides access from an SOA application to services conforming to
the Web 2.0 specification. In summary, the HTTP binding allows applications
developed for IBM® Workflow
Server to
communicate with and mediate between the many web services using HTTP
and other protocols, which will make this binding only more important
over time.

## Comparing the HTTP binding to
the web services binding

- The web services binding only supports the SOAP (and JMS) protocols.
- The web services binding assumes that it is working with web services-based
applications and so exposes the same model. In contrast, the HTTP
binding assumes that it is working with native HTTP applications and
exposes a model more familiar to this audience.
- Therefore, the web services binding provides first class support
within the SCA architecture for web services applications communicating
with the HTTP protocol and other protocols; whereas the HTTP binding
allows IBM Workflow
Server to
mediate between, and communicate with, any HTTP application thus bringing
any HTTP application into the Service Oriented Architecture framework.

## HTTP binding at run time

In IBM Integration
Designer,
the HTTP binding can be used on imports and exports.

An import
with an HTTP binding at run time sends a request with or without data
in the body of the message from the SCA application to the external
web service; that is, the request is made from the SCA application
to the external web service. Optionally, the import with the HTTP
binding may receive data back from the web application in a response
to the request.

<!-- image -->

With
an export, the request is made by a client application to a web service.
The web service is a web application running on the server. The export
is implemented in that web application as a servlet so the client
sends its request to a URL address. The servlet passes the request
to the SCA application at run time. Optionally, the export may send
data to the client application in response to the request.

<!-- image -->

The interaction style of the HTTP import
or export binding is synchronous.

## Related concepts

- Uses of the HTTP binding
- HTTP data bindings

## Related tasks

- Generating an HTTP import binding
- Generating an HTTP export binding

## Related reference

- Example of the HTTP binding
- Limitations of the HTTP binding