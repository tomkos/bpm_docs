<!-- image -->

# Creating exports

## About this task

- Select the export from the palette and drop it into the assembly
diagram.
- Select the component in the assembly diagram. Right-click to select Export and the type of binding. For information about
bindings, see the related tasks.
- Drag an interface or import into the assembly diagram. When prompted,
select the Export with No Binding or Export with Web Service Binding. Later, you can use the
right-click actions to generate, remove, or replace the binding. To
use interfaces from a library, open the module with the dependency
editor and add a dependency on the library. You will be prompted if
the dependency has to be set.
- Drag a web service port from the Business Integration view into
the assembly diagram. An export is created with that port. If you
use this method, you need to provide an address for the export in
proper form.
- To create an export that uses an adapter, from the Inbound Adapters
folder on the assembly editor palette, select an adapter and drag
it onto the canvas. Complete the fields in the wizard to generate
the export.