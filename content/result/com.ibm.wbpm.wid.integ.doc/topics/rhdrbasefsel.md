<!-- image -->

# Header-based fault selector

This fault selector can be used with JMS,
MQ JMS, MQ, generic JMS and HTTP imports.

The section below
explains the behavior of the header-based fault selector when default
configuration is used.

## Business faults

If an application wants
to indicate that the incoming message is a business fault, then there
must be two headers in the incoming message for business faults, which
is shown as follows:

```
Header name = FaultType, Header value = Business
Header name = FaultName, Header value = <user defined native fault name>
```

## Runtime exceptions

If an application wants
to indicate that the incoming response message is a runtime
exception, then there must be one header in the incoming message,
which is shown as follows:

```
Header name = FaultType, Header value = Runtime
```

## Normal message

If an application wants to
indicate that the incoming message is a normal message, then none
of these headers should be present in the incoming response message
or the header value for FaultType should be something other than Business or Runtime.