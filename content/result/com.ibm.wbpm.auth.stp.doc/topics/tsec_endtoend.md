<!-- image -->

# Creating end-to-end security

## Before you begin

## Procedure

1. Determine which of the examples provided in this section
most closely match your security needs. In some instances,
your needs might involve a combination of information from more than
one of the scenarios.
2. Read the security information for the relevant scenarios
and apply it to your security needs.

## Example

In this scenario, a web service client invokes a component in IBM Integration
Designer. The request passes through several
components in the IBM Integration
Designer environment before
being passed to an EIS by an adapter.

You
can authenticate the web service client as an SSL client, using HTTP Basic authentication or using
WS-Security authentication. When the client is authenticated, access control is applied based on the
SecurityPermission qualifier. Between the client and the IBM Integration
Designer instance, you can secure the data integrity
and privacy using SSL or WS-Security. SSL secures the entire pipe, whereas with WS-Security, you can
encrypt or digitally sign parts of the SOAP message. For web services, WS-Security is the preferred
standard.

In this scenario, the inbound request can be from an adapter, a web service client, or an
HTTP client. A component in IBM Integration
Designer (for
example a  component) invokes an
external web service.

As
for the inbound web service request, you can authenticate with the external web service as an SSL
client, using HTTP Basic authentication or using WS-Security authentication. Use
LTPACallBackHandler as the callback mechanism to extract the
usernameToken from the current RunAs subject. Between IBM Integration
Designer and the target web service, you can ensure
data privacy and integrity using WS-Security.