<!-- image -->

# Context propagation

Context is information relating to the runtime, module or user that can be propagated using
message headers. Context includes protocol headers, user context and system context. Within a SCA
module, context is stored in the context service. By configuring the binding, the context service
can be propagated through an import or export, into or out of a SCA module.

The default setting is for protocol headers to be propagated into the context service and for
headers defined in the context service to be propagated to outbound messages. The user context and
system context can also be propagated to outbound messages (the SCA binding propagates the system
context by default). The user context is often supplied by clients to provide additional information
not included in the message body. System context is used by the runtime environment to pass
information between SCA modules. This is useful when debugging invocations across linked
modules.