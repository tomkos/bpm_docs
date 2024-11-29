<!-- image -->

# Exports

Exports have interfaces that are the same as or a subset of the
interfaces of the component or import that they are associated with
so that the published service can be called. An export dragged from
another module into an assembly diagram automatically creates an import.
Exports that are shown under the module assembly in the Business Integration
view can also be used to create imports in other modules.

Each export has an address at which it is deployed on the server.
The export can be exposed at that address.

Imports and exports require binding information, which specifies
the means of transporting the data from the modules. When you use
the Generate Export action from the menu of
a component, you need to select the binding so that the binding is
generated when the export is created. An export binding describes
the specific way a module's services are made available to clients.
If an export in a module assembly does not have any binding, when
deployed, SCA binding is assumed.

For enterprise information systems (EIS), an export allows an event
in the enterprise system, such as the creation of a business object
in SAP, to drive an action. Unlike other exports, you cannot drag
an export with an EIS binding to create an EIS import.