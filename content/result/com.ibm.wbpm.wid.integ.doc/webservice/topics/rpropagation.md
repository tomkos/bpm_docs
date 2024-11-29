<!-- image -->

# Propagation

The following sections describe the aspects
of propagation:

- Types of propagation
- Lifecycle of a context service
- Using propagate system context
- Setting up propagation context in a client

## Types of propagation

There are
several types of context information, which are selectable from the Propagation tab
of a binding's properties.

- Propagate protocol header passes runtime
context information. It is selected by default.
- Propagate user context passes context information
related to an application. It is not selected by default.
- Propagate system context passes context
information related to a system. It can be used with the cross component
trace function to capture system information in logs, which can be
helpful when debugging an application. It is not selected by default.
- Propagate operation name passes the operation
associated with the message to an IBM Integration Bus messaging provider.
It is only used with an import using the MQ binding. It is not selected
by default.
- Propagate the HTTP transport headers This
option is only available for imports and exports that have a JAX-WS
web service binding. It is not available for imports and exports that
have a JAX-RPC web service binding. The option lets you to enable
or disable the propagation of HTTP transport headers. If propagation
is enabled, you can access the transport headers in received web service
messages. You can also set values for transport headers in sent web
service messages to ensure that they are formed as expected by the
receiving service or client. The option is not selected by default.

Context propagation is available on both imports and exports
with the exception of propagation of the operation name used only
on an MQ import binding. SCA imports always propagate the system context.

A
context service is responsible for propagating the context (including
the protocol headers, such as the JMS header, and the user context,
such as account ID) along a Service Component Architecture (SCA) invocation
path.

When the context service propagation is bi-directional,
that is, a request-response situation, the response context will always
overwrite the current context. When you are running an invocation
from one SCA component to another, a response will contain a different
context. A service component will have an incoming context, but when
you invoke another service, the other service will overwrite the original
outgoing context. The response context becomes the new context.

When
the context service propagation is one-way, the original context remains
the same.

## Lifecycle of a context service

The
lifecycle of a context service is associated with an invocation. A
request has associated context, and the lifecycle of that context
is bound to the processing of that particular request. When that request
is finished processing, then the lifecycle of that context ends.

For
a short-running Business Process Execution Language (BPEL) process,
the response context overwrites the request context. It takes the
response context back from the first request and pushes it to the
next request. For a long-running BPEL process, the response context
is discarded by the BPEL framework. It stores the original context
and uses that context when making other outgoing calls.

For
example, the context including a protocol header is propagated throughout
the invocation path starting with a request coming in to BPEL from
a SOAP web service. The BPEL processes it, and calls out of BPEL are
made sequentially to a web service binding outbound, and then to another
web service binding outbound. A request from the SOAP web service
uses the context service to pass on the protocol header. It takes
the context service from the inbound request and pushes the protocol
header outbound.

## Using propagate system context

This
property passes system information in the context. It is selected
by default. SCA imports always propagate the system context.

System
information is helpful when debugging an application that involves
multiple environments such as clients and servers using various protocols
and operating systems. Since the context is passed through the environments,
you can effectively trace errors to a particular system. This system
information is displayed in the server logs view, a view which is
typically used when debugging an application using cross component
trace.

There is a slight cost to performance for having this
property selected.

## Setting up propagation context in
a client

The following code shows how you would setup a
context on the client to be used with propagation support in your
modules.

```
//Import the necessary classes;
import com.ibm.bpm.context.ContextService;
import com.ibm.websphere.bo.BOFactory;
import com.ibm.websphere.sca.ServiceManager;
import com.ibm.websphere.sibx.smobo.HeadersType;
import com.ibm.websphere.sibx.smobo.SOAPHeaderType;
import com.ibm.websphere.sibx.smobo.ServiceMessageObjectFactory;
import commonj.sdo.DataObject;

//Locate ContextService;
ContextService contextService = (ContextService)ServiceManager.INSTANCE.locateService("com/ibm/bpm/context/ContextService");

//Get the protocol headers;
HeadersType smoHeaders = contextService.getHeaders();

//operate the protocol headers;
.....

//set the modified protocol headers back to ContextService;
contextService.setHeaders(smoHeaders);
```

See Service message objects for more information on context and its structure
in a message.