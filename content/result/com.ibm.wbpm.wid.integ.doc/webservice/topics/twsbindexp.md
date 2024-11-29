<!-- image -->

# Generating web service bindings for exports

## About this task

Bindings for imports and exports have different purposes.
An import binding describes the specific way an external service is
bound to an import component. An export binding describes how that
export (or service) will be published or made available to clients
outside the module.

The kind of binding determines what kind
of client is supported; a web service binding makes the service available
to any web-based client.

When you use the palette in the assembly
editor to create an export, you can generate a web service binding
by following these steps:

## Procedure

1. If there is no interface defined on the export, add the
interface first. See related tasks for instructions on adding the
interface.
2. Under Inbound Exports, drag Web
Service onto the canvas. Add your interface.
3. Alternately, under Components, drag
an export onto the canvas. Right-click the export and select Generate Binding > Web Service Binding.
4 Select one of the following transports and click Next :
    1. SOAP1.2/HTTP: Select this transport if your web service
conforms to the SOAP 1.2 specification.
This selection is based on the Java API for XML Web Services (JAX-WS), a Java programming API for creating
web services.
    2. SOAP1.1/HTTP (default): Select this transport if your
web service conforms to the SOAP
1.1 specification. This selection is also based on the JAX-WS
API.
    3. SOAP1.1/HTTP using JAX-RPC: Select this transport if you want to create web services
that use a SOAP-encoded message based on the Java API for XML-Based RPC.
    4. SOAP1.1/JMS: Select this transport if your web service conforms to the SOAP 1.1
specification and receives requests from a JMS queue. Note that the interaction style of SOAP/JMS is
synchronous.
5 The Specify the Web Service Binding Target Namespace pageopens. Select whether you want to use the same namespace as the interfaceor create a new one:

- Use the port type (interface) namespace - This selection is
best suited if you will be merging this service later with other artifacts
and exporting everything in a single file. In such cases, the export
is simplified if all artifacts share the same namespace.
- Specify a new namespace - This selection is suitable if you
want to have a unique namespace for your service.
6. A web service binding is generated without requiring you
to supply additional information. Click the Binding tab in the Properties
view to see the generated port and service and their namespace. The
location of the port is the same as the location of the interface.
You can see the port in the Business Integration view.
7. Optional: Double-click the binding or the port in the Business
Integration view to open the WSDL editor to see the WSDL description
and edit it if necessary.

## What to do next

The binding will be generated for the export and its icon
will change to indicate the type of binding that it has. To change
the binding for an export, you can use Regenerate Binding or Remove
Binding actions. Exports have binding properties that
can be modified in the Properties view. Select the export in the assembly
diagram to see its properties in the Properties view.