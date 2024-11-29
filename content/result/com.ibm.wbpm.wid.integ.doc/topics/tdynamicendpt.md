<!-- image -->

# Selecting endpoints dynamically

## About this task

An endpoint in a mediation module can be selected either
statically by using an import's binding, or dynamically by using an
endpoint address identified by a target address element in the message
header. This endpoint address can be added to the target address element
in the message header by mediation primitives within a mediation flow.
The endpoint address could be updated with information from a registry,
a database, or with information from the message itself.

In
order for the runtime to implement dynamic routing on a request, the Use
dynamic endpoint property of the callout node must be
set. When this property is set, the callout will route the message
using the endpoint address in element  /headers/SMOHeader/Target/address in
the message. If there is no endpoint address information in the message
header, a service will be selected statically, if an import is wired
to the associated reference of the callout in the mediation flow component.
By default, the Use dynamic endpoint property
is set, and therefore dynamic routing is enabled. For a summary of
this behavior, see "Message routing when dynamic endpoint property
is set" in the topic links below:

Dynamic endpoint support does
not require you to wire a reference to an import.  However, if you
want to provide default configuration settings for the dynamic endpoint,
 you can use a wired import. After a reference is wired to an import,
the configuration settings of the  import apply to all dynamic endpoints
using that reference.  For example, if you want to influence whether
a service is called synchronously or asynchronously,  from the callout
or Service Invoke primitive, you can specify the Preferred interaction
style on the  import; and wire the reference to this import. Similarly,
you can configure the security settings for a  web service dynamic
endpoint, by using a wired import with web service binding.

- WebSphere Service Registry and Repository (WSRR)

WebSphere® Service Registry and Repository (WSRR) allows you to store, access, and manage information about services. You can use this information to select, invoke, and reuse services.
- Selecting endpoints dynamically from WSRR

Use an Endpoint Lookup primitive to retrieve service endpoints by querying the WebSphere Service Registry and Repository (WSRR). The endpoints that are returned by the query are stored in the message, and can then be used to dynamically invoke a service.
- Selecting endpoints dynamically without using a registry

You can choose which service is used at run time by looking up service endpoints from a database, or with information from the message itself.
- Dynamic endpoint example URIs

When an endpoint is determined dynamically, the message is routed to the Universal Resource Indicator (URI) specified in the target address element of the SMOHeader, /headers/SMOHeader/Target/address. This topic lists the valid URI formats for the target types that are supported for dynamic endpoints in mediation flows.
- Message routing when dynamic endpoint property is set

The URI that is invoked by a mediation flow at run time depends on the setting of the Use dynamic endpoint property of the callout node, the existence of a URI in the target address element or AlternateTarget address element in the SMOHeader, and the wiring of the callout node.