<!-- image -->

# Limitations of the web services binding

## Headers propagation

Some web service bindings
do not propagate the header part of message.

- The SOAP/JMS and JAX-RPC bindings do not support the propagation
of JMS headers.
- The SOAP/HTTP and JAX-RPC bindings do not support the propagation
of HTTP headers.
- The JAX-RPC binding does not support the transport layer protocol
headers propagation.

## Web services bindings in the same module

The
following combinations of web service bindings cannot be used on exports
in the same module. If you need to expose components using more than
one of these export bindings, you need to have each in a separate
module and then connect those modules to your components using the
SCA binding:

- SOAP 1.1/JMS and SOAP 1.1/HTTP using JAX-RPC
- SOAP 1.1/HTTP using JAX-RPC and SOAP 1.1/HTTP using JAX-WS
- SOAP 1.1/HTTP using JAX-RPC and SOAP 1.2/HTTP using JAX-WS