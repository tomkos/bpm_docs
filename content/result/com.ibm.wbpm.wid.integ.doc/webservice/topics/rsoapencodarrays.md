<!-- image -->

# Using SOAP-encoded arrays

Though commonly used in web services, SOAP-encoded arrays
can cause problems when used with Web Service Description Language
(WSDL) based applications. SOAP-encoded arrays are often created when
you work with tools from Microsoft. SOAP-encoded arrays are not Web
Services Interoperability (WS-I) compliant, which is the standard
for IBM® Integration
Designer.

Since
these arrays are sometimes used with a web services binding based
on Java API for XML-based RPC (JAX-RPC), IBM Integration
Designer provides
a quick fix that you can use should errors appear in the problems
view. The quick fix changes the XML Schema Definition (XSD) using
these arrays to have an unbounded attribute assigned to the field
using the array type. In most cases, this quick fix will resolve problems
with this kind of array.

You should only use SOAP-encoded arrays
with the JAX-RPC transport protocol.