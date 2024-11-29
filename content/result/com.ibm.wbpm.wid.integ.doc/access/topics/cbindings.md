<!-- image -->

# Bindings

Bindings for imports and exports have different purposes. An import
binding describes the specific way an external service is bound
to an import component. An export binding describes how that
export (or service) will be published or made available to clients
outside the module.

A key to service-oriented architecture is the ability to expose
services with a number of binding options and the ability to call
services using industry norms. Binding types are associated with imports
and exports using the assembly editor.

The kind of binding determines what kind of client is supported;
for example, a web service binding makes the service available to
any web-based client, while an SCA binding makes it available to other
SCA modules. Import bindings tell the SCA runtime processes how to
access an external service. For example, if you publish a service
with an SCA export binding, an import with a JMS binding will not
be able to successfully call it. The SCA binding is the default binding;
if no binding is specified for an export, the runtime process assumes
an SCA binding when the module is deployed. You can use an import
with an SCA binding to access a service in another SCA module. You
can use a web service import binding to bind an external web service
to an import. The import binding does not have to be defined at development
time; it can be defined at deployment time.

Creating an export specifies that a component or import is being
externalized for use outside the module. The main reason for specifying
the SCA binding type on the export is that it allows for the most
efficient cross-module calls of the exported entity. If, for example,
you specify the web service export binding, the component or import
is invoked across the web instead of through a construct that approximates
a direct call. A reason to not use the SCA export binding would
be to allow clients outside of the SCA programming model to invoke
the exported component or import. Note that you can create more than
one export for a component or import, so you could effectively export
the component or import with more than one binding if you specify
a different binding type on each of the exports. You could even choose
to export one set of interfaces with one binding type and another
set of interfaces with another binding type.  Because the SCA bindings
are easy to use (for example, the SCA export binding requires no binding
information), you might choose to use them for prototyping work, and
replace or augment them as the prototype later evolves.

If modules are running on the same server, an SCA binding is the
easiest and fastest to use. The same is also true of modules deployed
in the same cluster. If you want a service to be published as a web
service and to be available to other modules in the same cluster,
consider using two exports, one with a web service binding and one
with an SCA binding.

The enterprise service discovery wizard creates imports and exports
representing a service on an EIS system. These bindings are discussed
in "Accessing external services with adapters." The bindings created
are of an EIS type. An EIS binding provides synchronous communication
with the service on the EIS system.

Java™ Message Service (JMS), WebSphere® MQSeries® (MQ)
and WebSphere MQSeries JMS
(MQ JMS) bindings are used for interactions with messaging systems,
where asynchronous communication through message queues are critical
for reliability. These bindings are discussed in "Accessing external
services with messaging systems."

Another binding is the HTTP binding. The Hypertext Transfer Protocol
(HTTP) is a widely-used protocol for transferring information on the
web as defined by the World Wide Web Consortium (W3C). Today many
standard HTTP requests such as GET, POST, PUT, and DELETE are a part
of this widely used protocol. This binding is discussed in "HTTP data
binding."

An import can also have a stateless session Enterprise JavaBean
(EJB) binding, but an export cannot.

Binding resource configurations extend the supplied bindings with
bindings that you can create yourself. For information on binding
resource configurations, see "Working with configurations that access
external services."

The assembly editor lists the bindings supported and simplifies
the creation of them when you want to create an import or export.
The import and export have different icons to indicate the type of
binding. The following image shows an import and an export with no
bindings: A properties view in the
assembly editor displays the binding information of any import or
export.

<!-- image -->