<!-- image -->

# Web service API requirements for BPEL processes and human tasks (deprecated)

- The interfaces of BPEL processes and human tasks must be defined
using the "document/literal wrapped" style defined in the Java™ API for XML-based Web Services (JAX-WS
2.0) specification. This is the default style for all BPEL processes
and human tasks developed with Integration Designer.
- Do not use the maxOccurs attribute in parameter
elements of the operations, or ensure that the value of this attribute
is set to the default value, maxOccurs="1".
- Fault messages that are exposed by BPEL processes and human tasks
for web service operations must comprise a single WSDL message part
defined with an XML Schema element. For example:<wsdl:part name="myFault" element="myNamespace:myFaultElement"/>

## Related information

- Java API for XML-based Web Services (JAX-WS
2.0) downloads page
- Which style of WSDL should I use?