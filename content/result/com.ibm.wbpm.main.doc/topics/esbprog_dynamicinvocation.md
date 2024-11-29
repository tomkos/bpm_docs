<!-- image -->

# Dynamic invocation

Applications can override or change the configuration and reroute messages at run time. You might
do this dynamically by overriding a value specified for an endpoint address. Alternatively, you can
select a new target import. In each case, the message flow changes according to the information in
the message.

For example, you can use Integration Designer to
create a binding on an import. The import contains endpoint information, specifying the location of
a remote service. This fixed endpoint information can be overridden dynamically by information
carried in the message.

If a message flow is changed dynamically within a mediation module, the new route applies only to
that message and any response coming back. When the message has been sent and any response returned,
the dynamic routing changes are discarded and the original fixed values defined in the module are
used as the default values again. Any response to a dynamic invocation returns using the same route
as the dynamic invocation.

- Dynamic override of a fixed endpoint, in which a service is called using any supported import
binding. The service is available at a different endpoint from the endpoints originally specified
when the mediation module was created and deployed.
- Dynamic invocation with a target import, in which a service is called using any
supported import binding. The binding must already be available within the mediation module. It is
selected at run time according to information contained in the message.
- Pure dynamic invocation, in which a service is called without needing an import in the mediation
module. No additional information is required apart from the details in the message.

```
/headers/SMOHeader/Target/address
/headers/SMOHeader/Target/@bindingType
/headers/SMOHeader/Target/@import
/headers/SMOHeader/AlternateTarget/address
/headers/SMOHeader/AlternateTarget/@bindingType
/headers/SMOHeader/AlternateTarget/@import
```

- If the URI begins with sca, this indicates an SCA component.
- A URI prefix of http or jms is assumed by default to indicate
a web service endpoint.
- A URI prefix of http does not by default indicate an HTTP service, and a URIprefix of jms does not by default indicate a JMS service. However, if the referenceis wired to an import, or a target import is specified with a JMS or an HTTP binding, the URI isassumed to be JMS or HTTP, and not web services.
    - The bindingType field in the Endpoint Reference can be used to change this. For
example, using the SCA Endpoint Reference API to set the bindingType field to a
value of EndpointReference.BINDING\_TYPE\_HTTP or a mediation flow to set the
Target@bindingType attribute to HTTP, results in a URI prefix of
http in the EPR being interpreted as indicating an HTTP binding for that
message.

- Dynamic override of a fixed endpoint

Dynamic invocation by overriding a fixed endpoint can take place, when a service is called using any supported import binding.
- Dynamic invocation with a target import

Dynamic invocation of endpoints can be enhanced using the Target@import attribute within the SMO header.
- Pure dynamic invocation

Pure dynamic invocation calls a service without needing an import in the mediation module.
- Version-aware dynamic invocation

You can configure mediation flow components to route messages to endpoints that are determined dynamically at run time. When you create the mediation module, you configure the endpoint lookup to use version-aware routing.
- Dynamic endpoint selection

In a mediation flow, you can select a service address based on a condition or property in your flow, and call an endpoint using the selected service. This section details some of the different mediation primitives that retrieve an endpoint address from a registry, to route the message to the retrieved endpoint.