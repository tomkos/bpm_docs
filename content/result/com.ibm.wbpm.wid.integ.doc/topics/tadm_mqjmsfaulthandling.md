# Troubleshooting WebSphere MQ JMS bindings

## Implementation exceptions

- Service Business Exception: this exception is returned if the fault specified on the service business interface
(WSDL port type) occurred.
- Service Runtime Exception: raised in all other cases. In most
cases, the cause exception will contain the original
exception (JMSException).For example, an import expects only one response
message for each request message. If more than
one response arrives, or if a late response (one for which the SCA
response expiration has expired) arrives, a Service Runtime Exception
is thrown. The transaction is rolled back, and the response message
is backed out of the queue or handled by the failed event manager.

## WebSphere MQ JMS-based SCA messages not
appearing in the failed event manager

If SCA messages originated
through a WebSphere MQ JMS interaction fail, you
would expect to find these messages in the failed event manager. If
such messages are not appearing in the failed event manager, ensure
that the value of the maximum retries property on the underlying listener
port is equal to or greater than 1. Setting this
value to 1 or more enables interaction with the failed
event manager during SCA invocations for the MQ JMS bindings.

## Misusage scenarios: comparison with WebSphere MQ
bindings

The WebSphere MQ JMS binding is
designed to interoperate with JMS applications deployed against WebSphere MQ, which exposes messages according
to the JMS message model. The WebSphere MQ import and export,
however, are principally designed to interoperate with native WebSphere MQ applications and expose the
full content of the WebSphere MQ message body
to mediations.

The following scenarios should be built using
the WebSphere MQ JMS binding, not the WebSphere MQ binding:

- Invoking a JMS message-driven bean (MDB) from an SCA module, where
the MDB is deployed against the WebSphere MQ
JMS provider. Use a WebSphere MQ JMS import.
- Allowing the SCA module to be called from a Java EE component servlet
or EJB by way of JMS. Use a WebSphere MQ JMS export.
- Mediating the contents of a JMS MapMessage, in transit across WebSphere MQ. Use a WebSphere MQ
JMS export and import in conjunction with the appropriate data handler or data binding.

There are situations in which the WebSphere MQ
binding and WebSphere MQ JMS binding might be expected
to interoperate. In particular, when you are bridging between Java EE
and non-Java EE WebSphere MQ applications, use a WebSphere MQ export and WebSphere MQ
JMS import (or vice versa) in conjunction with appropriate data bindings
or mediation modules (or both).