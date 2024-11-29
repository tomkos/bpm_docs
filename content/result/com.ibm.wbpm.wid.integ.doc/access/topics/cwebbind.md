<!-- image -->

# Web service bindings

A web service binding provides a specification for transmitting
messages to and from a web service. You can use a web service import binding
to call an external web service to an import. You can use a web service export binding
to provide  a service to external clients as a web service.

Most components have WSDL interfaces. WSDL files are also used
to describe services, ports, and bindings. A web service binding describes
how the service is bound to a messaging protocol, particularly the
SOAP messaging protocol. The web service binding of an export or import
references a port. That port holds details of binding information
for exports or imports. The port and service are generated automatically
when you create the binding for an export; however, deleting an export
or an import does not delete the port.

If you want to use a web service binding between exports and imports,
you need to share the port. You can create an export with a web service
binding and drag it into another module to create an import there
with a matching interface. When a web service binding is generated
for an export, a WSDL file is generated in the same folder as the
interface. If you want to store interfaces in a library where they
can be shared, do that before generating a web service binding for
the export if you can. If you have already generated the export and
the binding and need to share the interface and the port later, you
will need to manually move the web service port.

## Limitations

There can be many ports for
an interface, but a port can only apply to one interface. Therefore,
a component that needs to export or import multiple interfaces requires
multiple exports or imports. Each export or import needs to have one
interface and a web service binding configured with a corresponding
port. The location of the port matches the location of the interface
from which it is generated. Exports and imports use ports, but they
do not own them.

- Moving an existing web service port to a library

To share an existing web service port, move the web service port to a library.