<!-- image -->

# External clients

An external client (such as a web portal or an enterprise information
system) can send a message to an SCA component in the application
by way of an export or it can be invoked by an SCA component
in the application by way of an import.

The WebSphere MQ JMS
export binding deploys message driven beans (MDBs) to listen
to requests incoming to the receive destination
specified in the export binding. The destination specified in the send field
is used to send the reply to the inbound request if the invoked application
provides a reply. Thus, an external client is able to invoke applications
via the export binding.

WebSphere MQ JMS imports
bind to, and can deliver message to, external clients. This message
might or might not demand a response from the external client.

More information on how to interact with external clients using WebSphere MQ can be found
at the WebSphere MQ
documentation.