# Troubleshooting JMS bindings

## Implementation exceptions

- Service Business Exception: this exception is returned if the fault specified
on the service business interface (WSDL port type) occurred.
- Service Runtime Exception: raised in all other cases. In most
cases, the cause exception will contain the original exception
(JMSException).For example, an import expects
only one response message for each request message. If more than
one response arrives, or if a late response (one for which the SCA
response expiration has expired) arrives, a Service Runtime Exception
is thrown. The transaction is rolled back, and the response message
is backed out of the queue or handled by the failed event manager.

## Primary failure conditions

The
primary failure conditions of JMS bindings are determined by transactional
semantics, by JMS provider configuration, or by reference to existing
behavior in other components. The primary failure conditions include:

- Failure to connect to the JMS provider or destination. A failure
to connect to the JMS provider to receive messages will result in
the message listener failing to start. This condition will be logged
in the WebSphere® Application
Server log.
Persistent messages will remain on the destination until they are
successfully retrieved (or expired). 
A failure to connect to
the JMS provider to send outbound messages will cause rollback of
the transaction controlling the send.
- Failure to parse an inbound message or to construct an outbound
message. A failure in the data binding or data handler causes rollback
of the transaction controlling the work.
- Failure to send the outbound message.A failure to send a message
causes rollback of the relevant transaction.
- Multiple or unexpected late response messages. The import expects
only one response message for each request message. Also the valid
time period in which a response can be received is determined by the
SCA Response Expiration qualifier on the request. When a response
arrives or the expiration time is exceeded, the correlation record
is deleted. If response messages arrive unexpectedly or arrive late,
a Service Runtime Exception is thrown.
- Service timeout runtime exception caused by late response when
using the temporary dynamic response destination correlation scheme.The
JMS import will timeout after a period of time determined by the SCA
response expiration qualifier, or if this is not set it will default
to 60 seconds.

## JMS-based SCA messages not appearing in the failed
event manager

If SCA messages originated through a JMS interaction
fail, you would expect to find these messages in the failed event
manager. If such messages are not appearing in the failed event manager,
ensure that the underlying SIB destination of the JMS destination
has a maximum failed deliveries value greater than 1.
Setting this value to 2 or more enables interaction
with the failed event manager during SCA invocations for the JMS bindings.