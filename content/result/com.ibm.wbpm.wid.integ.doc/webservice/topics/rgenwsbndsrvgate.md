<!-- image -->

# Generating web service bindings for service gateway

Bindings
for imports and exports have different purposes. An import binding
describes the specific way an external service is bound to an import
component. An export binding describes how that export (or service)
will be published or made available to clients outside the module.

## Generating the export web service bindings

1 Add the service gateway interface and schema to your module.
    1. Double-click Dependencies to open the Dependency
Editor.
    2. Expand the Predefined Resources section.
    3. Select Service gateway interface.
    4. Select Native Body schema for Native Body DataHandler.
2. In the Business Integration View, expand your project's Data and Interfaces category.
Note the data types and ServiceGateway interface that are created
under the StandardImportFilesGen folder in each category.
3. When you add the interface to your export, select ServiceGateway as
your interface.
4 In generating your web service binding, you will be given thefollowing choice:

- SOAP1.2/HTTP (default): Select this transport if your web service
conforms to the SOAP 1.2 specification.
This selection is based on the Java API for XML Web Services (JAX-WS), a Java programming API for creating
web services.
- SOAP1.1/HTTP: Select this transport if your web service conforms
to the SOAP
1.1 specification. This selection is also based on the JAX-WS
API.
5. Click OK and the web service binding is
generated.
6. Once generated, in the Binding tab of the Properties view,
you will see the service gateway address, port, service name and namespace,
which can be modified. Advanced properties shows
the function selector, which determines the operation that will be
invoked on the SCA application, and the data format for the service
gateway. The advanced properties are discussed in Advanced properties for service gateway.

## Generating the import web service bindings

1 Add the service gateway interface and schema to your module.
    1. Double-click Dependencies to open the Dependency
Editor.
    2. Expand the Predefined Resources section.
    3. Select Service gateway interface.
    4. Select Native Body schema for Native Body DataHandler.
2. In the Business Integration View, expand your project's Data and Interfaces category.
Note the data types and ServiceGateway interface that are created
under the StandardImportFilesGen folder in each category.
3. When you add the interface to your import, select ServiceGateway as
your interface.
4 In generating your web service binding, you will be given thefollowing choice:

- SOAP1.2/HTTP (default): Select this transport if your web service
conforms to the SOAP 1.2 specification.
This selection is based on the Java API for XML Web Services (JAX-WS), a Java programming API for creating
web services.
- SOAP1.1/HTTP: Select this transport if your web service conforms
to the SOAP
1.1 specification. This selection is also based on the JAX-WS
API.
5. Click OK and the web service binding is
generated.
6. Once generated, in the Binding tab of the Properties view,
you will see the service gateway address, port, service name and namespace,
which can be modified. Advanced properties shows
the data format for the service gateway. The advanced properties are
discussed in Advanced properties for service gateway.

## Additional service gateway information

A
service gateway with a web service binding allows routing to multiple
endpoints. Requests can have headers, body, or both manipulated with
a mediation module before being forwarded onto the service provider. Generating web service bindings for service gateway shows you how to set up two types
of service gateways, a static service gateway and a dynamic service
gateway, including the setup for the runtime.