# Web services compatibility

If you are experiencing problems when you call an external
web service from a business process, you should first check its compatibility
with IBM® Business Automation
Workflow.
In the topic XML constructs not supported, these compatibility
problems are outlined and explained. Tables are provided that list
errors and warnings caused by incompatibilities. Once you know the
source of the cause you can correct the web service accordingly.

If
you have an Advanced
deployment environment and
experience web services difficulties associated with incompatibilities,
consider using an Advanced Integration Service to give you access
to Integration Designer.
The web services tools in Integration Designer have a
variety of popular bindings and features that can be used to handle
most web services interactions.

Alternatively
in all deployment environments, you can use a SOAP connector. In the
following sections, which show this approach, it is assumed that you
have access to a service using Web Services Description Language (WSDL)
and that you can make a call to the web service using the soapUI open
source tool or another SOAP tool. These instructions describe testing
the web service with soapUI.

- SOAP header: There is only support for a request SOAP header that
passes complex type parameters. There is no support for a SOAP header,
either request or response, that passes simple type parameters.
- SOAP / JMS: SOAP over JMS is not supported.
- SOAP faults are not supported.
- HTTP headers are not supported.
- The Remote Procedure Call (RPC) binding style is not supported.

- Verifying that the web service is working

First check that the web service is working. The web service must be working before you can call it from a business process.
- Calling a web service using a SOAP connector

When you know the web service works, you should test it from within Process Designer.