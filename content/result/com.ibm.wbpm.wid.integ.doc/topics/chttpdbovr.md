<!-- image -->

# Overview of HTTP data bindings

The Hypertext Transfer Protocol (HTTP) is a widely-used protocol
for transferring information on the web. It has now become a standard
request/response protocol between clients and server as defined by
the HTTP protocol published by the World Wide Web consortium (W3C).
The HTTP binding discussed earlier supports this protocol. Once you
have decided to use HTTP, however, you also need to decide on the
data format transformation you will use with it. The specific HTTP
data format transformation chosen is the implementation of the HTTP
binding.

The data format transformation takes an incoming stream of data in a native format and converts it to a business object to be used by services created with the service component architecture; for example, data from a Java application to a service created with the Integration Designer editors and wizards. The data format transformation can also take an outgoing stream of data in a business object and convert it to a native format.

The data format transformation can work with a data handler. In
this case, the data format transformation delegates the transformation
logic to a data handler. The data binding works as a mediator between
the transport-dependent protocol, in this case, HTTP, and the transport-independent
protocol of the data handler.

In this section, the prepackaged HTTP data format transformations
that come with the product are shown. You are also shown how to develop
your own data format transformation using a data handler.

## Related concepts

- Prepackaged HTTP data format transformations
- Overview of HTTP function selectors
- Prepackaged HTTP function selectors

## Related reference

- Data handlers
- Prepackaged HTTP fault selectors