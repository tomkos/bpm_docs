<!-- image -->

# Troubleshooting Generic JMS bindings

You can diagnose and fix problems with Generic JMS
binding.

## Implementation exceptions

In response to
various error conditions, the Generic JMS import and export
implementation can return one of two types of exceptions:

- Service Business Exception: this exception is returned if the fault specified
on the service business interface (WSDL port type) occurred.
- Service Runtime Exception: raised in all other cases. In most
cases, the cause exception will contain the original exception
(JMSException).

## Troubleshooting Generic JMS message expiry

A
request message by the JMS provider is subject to expiration.

Request
expiry refers to the expiration of a request message by the
JMS provider when the JMSExpiration time on the
request message is reached. As with other JMS bindings, the Generic JMS
binding handles the request expiry by setting expiration on the callback
message placed by the import to be the same as for the outgoing request.
Notification of the expiration of the callback message will indicate
that the request message has expired and the client should be notified
by means of a business exception.

If the callback destination
is moved to the third-party provider, however, this type of request
expiry is not supported.

Response expiry refers
to the expiration of a response message by the JMS provider when the JMSExpiration time
on the response message is reached.

Response expiry for the
generic JMS binding is not supported, because the exact expiry behavior
of a third-party JMS provider is not defined. You can, however, check
that the response is not expired if and when it is received.

For
outbound request messages, the JMSExpiration value
will be calculated from the time waited and from the requestExpiration values
carried in the asyncHeader, if set.

## Troubleshooting Generic JMS connection factory
errors

When you define certain types of connection factories
in your Generic JMS provider, you might receive an error
message when you try to start an application. You can modify the external
connection factory to avoid this problem.

```
MDB Listener Port JMSConnectionFactory type does not match 
JMSDestination type
```

This problem can arise when
you are defining external connection factories. Specifically, the
exception can be thrown when you create a JMS 1.0.2 Topic Connection
Factory, instead of a JMS 1.1 (unified) Connection Factory (that is,
one that is able to support both point-to-point and publish/subscribe
communication).

1. Access the Generic JMS provider that you are using.
2. Replace the JMS 1.0.2 Topic Connection Factory that you defined
with a JMS 1.1 (unified) Connection Factory.

When you launch the application with the newly defined
JMS 1.1 Connection Factory, you should no longer receive an error
message.

## Generic JMS-based SCA messages not appearing in the
failed event manager

If SCA messages originated through
a generic JMS interaction fail, you would expect to find these messages
in the failed event manager. If such messages are not appearing in
the failed event manager, ensure that the value of the maximum retries
property on the underlying listener port is equal to or greater than
1. Setting this value to 1 or more enables interaction with the failed
event manager during SCA invocations for the generic JMS bindings.