<!-- image -->

# Generating web service bindings for imports

## About this task

Bindings for imports and exports have different purposes.
An import binding describes the specific way an external service is
bound to an import component. An export binding describes how that
export (or service) will be published or made available to clients
outside the module.

When you use the palette in the assembly
editor to create an import, you can generate a web service binding
by following these steps:

## Procedure

1. If there is no interface defined on the import, add the
interface first or generate an interface by wiring the import to an
SCA component. See the related tasks for instructions on adding the
interface.
2. Under Outbound Imports, drag Web
Service onto the canvas. Add your interface.
3. Alternately, under Components, drag
an import onto the canvas. Right click the import and select Generate Binding > Web Service Binding. Because the import will connect to some
specific service outside the module, you will need to identify that
service. The editor cannot generate the binding automatically, as
it can in some circumstances for an export.
4 In the Import Details window box, choose one of the threeoptions described below. The first choice sensible choice for mostsituations.
    - Choose an existing web service port to use for the binding.
The port must be in the module or in a shared library. Click Browse to
see which ports are available. The editor extracts the needed information
from the port WSDL file.
    - Generate a new web service definition and implementation.
This choice is for advanced users. Options differ depending on whether
you are working top-down (creating an import before creating an export)
or bottom-up (you are choosing an existing export from which to import
a service). The Web Services wizard will guide you through the choices
you need to make and provide a skeleton of what to implement.
    - Do not specify a web service port at this time. To complete
the binding in this approach, you will need to add details in the
Properties for this import's binding. If you are creating the import
using the palette, you will have to specify a binding type for the
external service technology in order to test it.
5 If you made the second selection, the Specifythe Web Service Binding Target Namespace page will alsobe used. Select whether you want to use the same namespace as theinterface or create a new one:

- Use the port type (interface) namespace - This selection is
best suited if you will be merging this service later with other artifacts
and exporting everything in a single file. In such cases, the export
is simplified if all artifacts share the same namespace.
- Specify a new namespace - This selection is suitable if you
want to have a unique namespace for your service.
6. The binding will be generated and its icon will change
to indicate the type of binding that it has.
7. Optional: It is recommended that you set the
Join Transaction qualifier so that the import performs the invocation
within a transaction. See related information for more details about
configuring the Join Transaction qualifier.

## What to do next

To change the binding for an import, you can use Regenerate
Binding or Remove Binding actions.
Imports have binding properties that can be modified in the Properties
view. Select the import in the assembly diagram to see its properties
in the Properties view.

If you have created a web service port
and you drag it onto the assembly editor in order to regenerate a
binding, you will only generate a JAX-RPC binding. To properly regenerate
with a choice of bindings, you need to remove the binding and then
add another one.