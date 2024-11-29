<!-- image -->

# SOAP header propagation

- When requests are received at an export or responses received
at an import, the SOAP header information can be accessed, allowing
logic in the module to be based on header values and allowing those
headers to be modified.
- When requests are sent from an export or responses sent from an
import, SOAP headers can be included in those messages.

To configure the propagation of SOAP headers for an import or export,
you select (from the Properties view of Integration Designer) the Propagate
Protocol Header tab and select the options you require.

## WS-Addressing header

The WS-Addressing header
can be propagated by the web service (JAX-WS) binding.

- If you enable propagation for the WS-Addressing header, the headerwill be propagated into the module in the followingcircumstances:
    - When requests are received at an export
    - When responses are received at an import
- The WS-Addressing header is not propagated into outbound messages
from IBM® Integration
Designer (that
is, the header is not propagated when requests are sent from an import
or when responses are sent from the export).

## WS-Security header

The WS-Security header
can be propagated by both the web service (JAX-WS) binding and the
web service (JAX-RPC) binding.

The web services WS-Security
specification describes enhancements to SOAP messaging to provide
quality of protection through message integrity, message confidentiality,
and single message authentication. These mechanisms can be used to
accommodate a wide variety of security models and encryption technologies.

- If you enable propagation for the WS-Security header, the headerwill be propagated across the module in the following circumstances:
    - When requests are received at an export
    - When requests are sent from an import
    - When responses are received at an import
- The header will not, by default, be propagated when responses
are sent from the export. However, if you set the JVM property WSSECURITY.ECHO.ENABLED to true,
the header will be propagated when responses are sent from the export.
In this case, if the WS-Security header on the request path is not
modified, WS-Security headers might be automatically echoed from requests
into responses.
- The exact form of the SOAP message sent from
an import for a request or from an export for a response might not
exactly match the SOAP message that was originally received. For this
reason, any digital signature should be assumed to become invalid.
If a digital signature is required in messages that are sent, it must
be established using the appropriate security policy set, and WS-Security
headers relating to digital signature in received messages should
be removed within the module.

To propagate the WS-Security header,
you must include the WS-Security schema with the application module.
See Including the WS-Security schema in an application module for
the procedure to include the schema.

## How headers are propagated

|                                        | Export binding with no security policy                                                                                                                                                                | Export binding with security policy                                                                                                                                                                                  |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Import binding with no security policy | Security headers are passed as-is through the module. They are not decrypted. The headers are sent outbound in the same form in which they were received. The digital signature might become invalid. | Security headers are decrypted and passed through the module with signature verification and authentication.  The decrypted headers are sent outbound. The digital signature might become invalid.                   |
| Import binding with security policy    | Security headers are passed as-is through the module. They are not decrypted.  The headers should not be propagated to the import. Otherwise, an error occurs because of duplication.                 | Security headers are decrypted and passed through the module with signature verification and authentication.  The headers should not be propagated to the import. Otherwise, an error occurs because of duplication. |

Configure appropriate policy sets on the export and
import bindings, because this isolates the service requester from
changes to the configuration or QoS requirements of the service provider.
 Having standard SOAP headers visible in a module can then be used
to influence the processing (for example, logging and tracing) in
the module. Propagating SOAP headers across a module from a received
message to a sent message does mean that the isolation benefits of
the module are reduced.

Standard headers, such as WS-Security
headers, should not be propagated on a request to an import or response
to an export when the import or export has an associated policy set
that would normally result in the generation of those headers. Otherwise,
an error will occur because of a duplication of the headers. Instead,
the headers should be explicitly removed or the import or export binding
should be configured to prevent propagation of protocol headers.

## Accessing SOAP headers

When a message that
contains SOAP headers is received from a web service import or export,
the headers are placed in the headers section of the service message
object (SMO). You can access the header information, as described
in Accessing SOAP header information in the SMO.

## Including the WS-Security schema in an
application module

- If the computer on which Integration Designer is runninghas access to the Internet, perform the following steps:
    1. In the Business Integration perspective, select Dependencies for
your project.
    2. Expand Predefined Resources and select
either WS-Security 1.0 schema files or WS-Security
1.1 schema files to import the schema into your module.
    3. Clean and rebuild the project.
- If a computer on which Integration Designer is runningdoes not have Internet access, you can download the schema to a secondcomputer that does have Internet access. You can then copy it to thecomputer on which Integration Designer is running.

1 From the computer that has Internet access, download the remoteschema:
    1. Click File > Import > Business Integration > WSDL and XSD.
    2. Select Remote WSDL or XSD file.
    3 Import the following schemas:
        - http://www.w3.org/2003/05/soap-envelope/
        - http://www.w3.org/TR/2002/REC-xmlenc-core-20021210/xenc-schema.xsd
        - http://www.w3.org/TR/xmldsig-core/xmldsig-core-schema.xsd
2. Copy the schemas to the computer that does not have Internet access.
3 From the computer that has no Internet access, import the schema:

1. Click File > Import > Business Integration > WSDL and XSD.
2. Select Local WSDL or XSD file.
4 Change the schema locations for oasis-wss-wssecurity\_secext-1.1.xsd:

1. Open the schema at workplace\_location/module\_name/StandardImportFilesGen/oasis-wss-wssecurity-secext-1.1.xsd.
2. Change:<xs:import namespace='http://www.w3.org/2003/05/soap-envelope'
schemaLocation='http://www.w3.org/2003/05/soap-envelope/'/> to: 
<xs:import namespace='http://www.w3.org/2003/05/soap-envelope'
schemaLocation='../w3/\_2003/\_05/soap\_envelope.xsd'/>
3. Change:<xs:import namespace='http://www.w3.org/2001/04/xmlenc#' 
schemaLocation='http://www.w3.org/TR/2002/REC-xmlenc-core-20021210/xenc-schema.xsd'/>
to: 
<xs:import namespace='http://www.w3.org/2001/04/xmlenc#' 
schemaLocation='../w3/tr/\_2002/rec\_xmlenc\_core\_20021210/xenc-schema.xsd'/>
5 Change the schema location for oasis-200401-wss-wssecurity-secext-1.0.xsd:

1. Open the schema at workplace\_location/module\_name/StandardImportFilesGen/oasis-200401-wss-wssecurity-secext-1.0.xsd.
2. Change:<xsd:import namespace="http://www.w3.org/2000/09/xmldsig#" 
schemaLocation="http://www.w3.org/TR/xmldsig-core/xmldsig-core-schema.xsd"/>
to: 
<xsd:import namespace="http://www.w3.org/2000/09/xmldsig#" 
schemaLocation="../w3/tr/\_2002/rec\_xmldsig\_core\_20020212/xmldsig-core-schema.xsd"/>
6. Clean and rebuild the project.