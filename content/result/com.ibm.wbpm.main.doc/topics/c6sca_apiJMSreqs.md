<!-- image -->

# (Deprecated) Requirements for BPEL processes in JMS-based client
applications (deprecated)

The requirements are:

1. The interfaces of BPEL processes must be defined using the "document/literal
wrapped" style defined in the Java™ API
for XML-based RPC (JAX-RPC 1.1) specification. This is the default
style for all BPEL processes and human tasks developed with Integration Designer.
2. Fault messages exposed by BPEL processes and human tasks for web
service operations must comprise a single WSDL message part defined
with an XML Schema element. For example:<wsdl:part name="myFault" element="myNamespace:myFaultElement"/>

## Related information

- Java API for XML based RPC (JAX-RPC) downloads
page
- Which style of WSDL should I use?