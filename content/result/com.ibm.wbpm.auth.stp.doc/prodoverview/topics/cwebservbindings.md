<!-- image -->

# Service import and export binding types

You can use a Service Component Architecture (SCA) or default binding
to let your service communicate with other services in other modules.
You can use an import with an SCA binding to access a service in another
module. You can use an export with an SCA binding to offer a service
to other modules. You can use a web service import binding to bind
an external web service to an import."

A web service export binding provides a service to external clients
as a web service. The web service binding can use a transport protocol
of either Simple Object Access Protocol (SOAP) over HTTP (SOAP/HTTP)
or SOAP over  Java™ Message Service
(JMS) (SOAP/JMS).

IBM® Integration
Designer supports several types of JMS data bindings: JMS, MQ JMS
and generic JMS. The only JMS data binding type that is supported
with the web services binding is JMS. Therefore, the only transport
protocol that is supported is SOAP/JMS. The SOAP/MQ, JMS, and SOAP/generic
JMS transport protocols are not supported.

The Hypertext Transfer Protocol (HTTP) binding, in contrast to
the preceding web service binding, assumes the binding is working
with native HTTP applications.

The external service wizard creates imports and exports representing
a service on an Enterprise Information Systems (EIS) . The bindings
created are of an EIS type. An EIS binding provides synchronous communication
with the service on the EIS system. JMS, generic JMS, WebSphere® MQSeries® (MQ) and WebSphere MQSeries JMS (MQ JMS) bindings are used
for interactions with messaging systems, where asynchronous communication
through message queues are critical for reliability. An import (though
not an export) may also have a stateless session EJB binding.

The assembly editor lists the bindings supported, and it simplifies
your work when you want to create an import or export. A properties
view in the assembly editor displays the binding information of any
import or export.

<!-- image -->

## Related concepts

- Selecting appropriate bindings