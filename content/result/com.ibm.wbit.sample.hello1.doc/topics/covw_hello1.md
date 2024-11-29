<!-- image -->

# Overview

In this sample, your goal is to invoke an existing web
service by using a web service import. This existing web service has
already been implemented and supplied for you, but you need to bring
it into your workspace and deploy it to your server. It is implemented
using a mediation module, but you need not know or care how it is
implemented. You only need to know that there is a WSDL file defining
not only its interface but where and how to invoke it with SOAP over
HTTP.

Your objective is to allow other integration developers to invoke the web service by calling your
mediation module rather than by calling the web service directly. This gives you the flexibility and
resilience to change and evolve the web service without impacting the clients that call it. All
changes are absorbed in the mediation module. Furthermore, using a mediation module allows you to
expose a different interface for the web service, as demonstrated in this sample.

A high-level overview of this sample is shown in the following figure:

<!-- image -->

This sample exposes an interface through which other modules can interact with the existing web
service. The interface is exposed through an export with an SCA binding. SCA bindings are simple to
configure and provide seamless integration between SCA modules. The exposed interface is different
from the interface of the web service that the sample uses through an import with a web service
binding. Consequently you need a mapping between the parameters (request) and what is returned
(response) in a mediation flow component, with one flow for the request and another for the
response. Mediation flows are built from mediation primitives that are wired together. Each
primitive is a pre-supplied capability that acts on or processes the message flowing through it.
Typically, the message contains the request and response parameters that are passed to or returned
from an external call.

For more details on these concepts, see subsequent topics in this sample. For more in-depth
information, see Building mediation flows for ESB logic.