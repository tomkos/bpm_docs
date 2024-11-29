<!-- image -->

# WS-I compliance with SOAP messages

This page in the wizard will only appear if you selected
a document literal non-wrapped binding style, which is used for operations
with attachments. It lets you choose if your SOAP message will follow
the WS-I Attachments Profile 1.0 specification
or use an automatic configuration used in earlier versions of IBM Integration
Designer.

## Export

This page opens after you have selected
the transport protocol and the target namespace.

1 In the Specify WS-I compliance page, selectone of the following options:
    - Use WS-I compliant SOAP message: Select
this option if you want your SOAP message to comply to the WS-I Attachments
Profile 1.0 specification. In this specification, only one non-binary
part can be bound to the SOAP body. On the following page you can
see the current non-binary part selected and can make a different
selection if there are multiple parts. Click Next.
    - Use non WS-I compliant SOAP message (default):
This option will automatically handle the configuration though the
result is not compliant to the WS-I Attachments Profile 1.0.
2. If you selected Use WS-I compliant SOAP message and
clicked Next, the Specify the part
to bind to the SOAP body page opens. In a WS-I compliant
SOAP message, only one non-binary part can be bound to the SOAP body.
For inputs and outputs with multiple non-binary parts, select the
one that you want bound to the SOAP body and click Finish.

## Import

For an import the page is the same,
but the order to get to the page is different. For an import, the
selection Generate a new web service definition and implementation leads
you to the sequence described previously for an export.