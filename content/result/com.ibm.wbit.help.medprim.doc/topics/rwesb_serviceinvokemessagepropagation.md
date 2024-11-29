# Service Invoke message propagation

## Default mode

In
default mode, the header
and body of the input message, which is received at the in terminal,
are used in the request message that is sent to the service. The out terminal
uses the header and body of the response message, and the context
of the input message to populate the output message.

The following
figure shows how the SMOs are populated in the message flow.

Figure 1. SMO propagation in default mode

<!-- image -->

## Message Enrichment mode with XPath only configured

In this configuration, XPath expressions are specified
within the input message that will be used for the service invocation,
and XPath expressions also specify where to place the elements of
the response message. The inbound XPath expressions are used to construct
a new body for the request message that is sent to the service. The out terminal
populates the output message by merging the elements of the response
message body with the contents of the input message that was passed
into the mediation primitive.

The following figure shows how
the SMOs are populated in the message flow.

Figure 2. SMO propagation in Message Enrichment mode with XPath only
configured

<!-- image -->

## Message
Enrichment mode with XPath, and request and
response header propagation configured

In
this configuration, XPath expressions are specified within the input
message that will be used for the service invocation, and XPath expressions
also specify where to place the elements of the response message.
Additional settings are specified to propagate request headers to
the service being invoked and to propagate response headers from the
service being invoked. The inbound XPath expressions are used to construct
a new body for the request message that is sent to the service, and
the input message header is also used in the request message. The out terminal
populates the output message with the response message header, the
context and body of the input message that was passed into the mediation
primitive, and also merges in the elements of the response message
body.

The following figure shows how the SMOs are populated
in the message flow.

Figure 3. SMO propagation
in Message Enrichment mode with XPath, and request and response header
propagation configured

<!-- image -->

## Message Enrichment
mode with XPath and request header
propagation configured

In this configuration,
XPath expressions are specified within the input message that will
be used for the service invocation, and XPath expressions also specify
where to place the elements of the response message. An additional
setting is specified to propagate request headers to the service being
invoked. The inbound XPath expressions are used to construct a new
body for the request message that is sent to the service, and the
input message header is also used in the request message. The out terminal
populates the output message with the contents of the input message
that was passed into the mediation primitive, and also merges in the
elements of the response message body.

The following figure
shows how the SMOs are populated in the message flow.

Figure 4. SMO propagation in Message Enrichment mode
with XPath and request header propagation configured

<!-- image -->

## Message Enrichment mode with XPath and response header
propagation configured

In this configuration,
XPath expressions are specified within the input message that will
be used for the service invocation, and XPath expressions also specify
where to place the elements of the response message. An additional
setting is specified to propagate response headers from the service
being invoked. The inbound XPath expressions are used to construct
a new body for the request message that is sent to the service. The out terminal
populates the output message with the response message header, the
context and body of the input message that was passed into the mediation
primitive, and also merges in the elements of the response message
body.

The following figure shows how the SMOs are populated
in the message flow.

Figure 5. SMO propagation
in Message Enrichment mode with XPath and response header propagation
configured

<!-- image -->