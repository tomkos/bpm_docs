<!-- image -->

# Service gateway artifacts

- A generic gateway interface, named ServiceGateway.
This interface is imported into the module.
- An export with a ServiceGateway interface,
and one of the supported bindings. The export is configured with a
gateway function selector and a gateway data format handler.
- Business object schemas that are related to the bindings. The
pattern imports these schemas into the module for you.
- An import with a ServiceGateway interface,
and one of the supported bindings for a dynamic gateway.
- An import with the service provider interface and binding for
each service provider in a static gateway.
- A mediation module that contains a mediation flow
component that is wired to the export and imports.
- A mediation flow that implements the gateway.