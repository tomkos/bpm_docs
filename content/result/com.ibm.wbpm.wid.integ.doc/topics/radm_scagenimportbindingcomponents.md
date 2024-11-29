# Key features of Generic JMS bindings

Generic imports

Like the
MQ JMS import application, the Generic JMS implementation
is asynchronous and supports three invocations: one-way, two-way (also
known as request-response), and callback.

When the JMS import
is deployed, a message driven bean (MDB) provided by the runtime environment
is deployed. The MDB listens for replies to the request message. The
MDB is associated with (listens on) the destination sent with the
request in the replyTo header field of the JMS
message.

Generic exports

Generic
JMS export bindings differ from EIS export bindings in their handling
of the return of the result. A Generic JMS export explicitly
sends the response to the replyTo destination specified
on the incoming message. If none is specified, the send destination
is used.

When the Generic JMS export is deployed, a
message driven bean (a different MDB than the one used for Generic JMS
imports) is deployed. It listens for the incoming requests on the
receive destination and then dispatches the requests to be processed
by the SCA runtime.

## Special headers

Special header properties
are used in Generic JMS imports and exports to tell the target
binding how to handle the message.

## Java EE resources

A number of Java EE resources
are created when a JMS binding is deployed to a Java EE environment.

- Listener port for listening on the receive (response) destination
(two-way only) for imports and on the receive (request) destination
for exports
- Generic JMS connection factory for the outboundConnection (import)
and inboundConnection (export)
- Generic JMS destination for the send (import) and receive (export;
two-way only) destinations
- Generic JMS connection factory for the responseConnection (two-way
only and optional; otherwise, outboundConnection is used for imports,
and inboundConnection is used for exports)
- Generic JMS destination for the receive (import) and send (export)
destination (two-way only)
- Default messaging provider callback JMS destination used to access
the SIB callback queue destination (two-way only)
- Default messaging provider callback JMS connection factory used
to access the callback JMS destination (two-way only)
- SIB callback queue destination used to store information about
the request message for use during response processing (two-way only)

The installation task creates the ConnectionFactory,
the three destinations, and the ActivationSpec from
the information in the import and export files.