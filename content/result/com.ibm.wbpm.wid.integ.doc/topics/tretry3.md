<!-- image -->

# Retrying a different service

## Before you begin

<!-- image -->

1. The primitive ServiceInvoke1 is used to invoke a service.
2. Its output terminal is wired through an optional Mapping primitive,
XSLT1, to transform the response into the form needed for the next primitive.
3. The fault terminal is wired through XSLT2, which is again optional, to
the input of a second Service Invoke primitive, ServiceInvoke2. When the initial
invocation receives a fault response, the message will be propagated to this
second Service Invoke primitive.
4. The output terminal of ServiceInvoke2 is wired through an optional transform,
XSLT3, to the next primitive, while its fault terminal is wired to a fail
primitive which halts the mediation flow.