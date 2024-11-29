<!-- image -->

# Enabling MTOM support in JAX-WS bindings

## Before you begin

- MTOM is not supported when the business object parsing mode is
set to eager parsing (support is limited to a JAX-WS web service using
business object lazy parsing mode).
- MTOM is not supported when using a JAX-WS handler (support is
limited to a JAX-WS web service which does not use any JAX-WS handlers).
The JAX-WS handlers specified on the web service should be removed.
- When using a service gateway mediation module, the Data Handler
primitive cannot be used with MTOM messages. If direct access to the
MTOM attachment data is required within the module, then a non-service
gateway module must be used.
- When MTOM is enabled on a JAX-WS export binding, all responses
will be sent using MTOM. If some clients do not support MTOM, use
two JAX-WS exports - one with MTOM enabled and one with it disabled
and ensure client applications use the correct endpoint address.
- MTOM is not supported when using the JAX-RPC binding for SOAP/HTTP
or SOAP/JMS.

## About this task

## Procedure

1. In IBM Integration Developer, using the Properties for
the export or import, click the Binding tab and select the MTOM check
box. This will enable the optimization of the transmission of binary
data in the SOAP attachment.
2. Optionally, you can provide an integer value greater than
or equal to zero in the Threshold field to
indicate the minimum size of binary data to be sent using MTOM. When
sending requests from an import or responses from an export, any binary
data whose length is greater than or equal to this value will be sent
using MTOM. Binary data whose length is less than this value is inlined
in the XML document. A value of zero indicates that all binary elements
should be sent using MTOM. Note that this value is a hint to the runtime
and under some circumstances the value may not apply. For example,
where a binary element is received as an attachment from a client
using a lower threshold value, the element may remain as an attachment
and may not be moved inline into the XML document.