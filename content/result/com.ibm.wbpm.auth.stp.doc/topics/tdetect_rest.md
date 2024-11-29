# Invoking a REST service using OpenAPI 3.0

## About this task

To invoke an OpenAdmin 3.0 service you must first discover a REST service from an OpenAPI 3.0
specification (formerly known as Swagger) to generate the wsdl interface, data xsd and SCA import
including an HTTP/REST binding based on the discovered REST service. Then you invoke the REST
service.

You must define the REST service in a valid and complete, self-contained OpenAPI 3.0
specification. The OpenAPI format can be either JSON or YAML. To verify that your OpenAPI
specification is valid, open the file in an OpenAPI editor or a Swagger editor.

To discover and invoke an existing REST service with an OpenAPI specification and generate an SCA
Import with a REST binding, complete the following steps in Integration Designer:

## Procedure

1. Select Outbound Imports from the palette of the Assembly editor.
2. Select the new REST import from the list of available outbound imports and drag it to the
canvas of the Assembly editor.  The "New REST Import Service" opens.
3. Specify the name and location of the OpenAPI 3.0 service specification.
4. Click Finish. The REST import service is added to the
assembly diagram. An SCA REST import is created with an intermediate representation (interface) of
the detected service and a list of data (business objects). Use this import in the same way as you
use other imports. If the service detection is not successful, the Problems
view lists the issues. To correct the service definition, see Restrictions invoking a REST API 3.0 service.
5. Create a new component, for example, a BPEL process, "esb" and wire it the SCA import.
 Refer to the HTTP binding configuration when invoking the REST outbound. See Generating an HTTP import binding.When you invoke a REST service, an operation input
parameter is mapped to the REST requests and the REST responses are mapped to the operation output
or fault output. The interaction style of the REST import binding is synchronous.

- Configuring authentication for a REST API 3.0 service

The REST Outbound component in IBM® Integration Designer has support for both APIKey and Basic authentication when invoking REST services via OpenAPI 3.0 Schema definition.
- Restrictions invoking a REST API 3.0 service

Some support restrictions apply to OpenAPI specifications and type mappings between OpenAPI types and XSD types.