<!-- image -->

# External clients

An external client (such as a web portal or an enterprise information
system) can send a message to an SCA module in the server, or it can
be invoked by a component from within the server.

The JMS export components deploy message listeners to listen to
requests incoming to the receive destination specified in the export
binding. The destination specified in the send field is used to send
the reply to the inbound request if the invoked application provides
a reply. Thus, an external client is able to invoke applications with
the export binding.

JMS imports interact with external clients by sending messages
to, and receiving messages from, JMS queues.

- Working with external clients

An external client (that is, outside the server) might need to interact with an application installed in the server.