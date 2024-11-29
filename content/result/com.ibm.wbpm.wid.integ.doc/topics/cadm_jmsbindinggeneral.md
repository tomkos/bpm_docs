<!-- image -->

# JMS bindings overview

## JMS bindings

- Resource adapter: enables managed, bidirectional connectivity
between an SCA module and external JMS systems
- Connections: encapsulate a virtual connection between a client
and a provider application
- Destinations: used by a client to specify the target of messages
it produces or the source of messages it consumes
- Authentication data: used to secure access to the binding

## Key features of JMS bindings

Special header properties are used in JMS imports and exports
to tell the target how to handle the message.

For example, TargetFunctionName maps
from the native method to the operation method.

A number of Java EE resources is created when JMS imports and
exports are deployed to a Java EE environment.

- Send destination: on an import, this is where the request or outgoing
message is sent; on an export, this is the destination where the response
message will be sent, if not superseded by the JMSReplyTo header
field in the incoming message.
- Receive destination: where the incoming message should be placed;
with imports, this is a response; with exports, this is a request.
- Callback destination: SCA JMS system destination used to store
correlation information. Do not read or write to this destination.

The installation task creates the ConnectionFactory and
three destinations. It also creates the ActivationSpec to
enable the runtime message listener to listen for replies on the receive
destination. The properties of these resources are specified in the
import or export file.