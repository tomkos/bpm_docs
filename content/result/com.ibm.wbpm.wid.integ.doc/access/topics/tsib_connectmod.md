<!-- image -->

# Invoking a service from another module

## About this task

You can invoke any type of module from any other type
of module. You can invoke one mediation module from another mediation
module. Or, if you are running your application on the WebSphere® Process
server you can invoke a mediation module from a business integration
module.

To integrate two modules, you use the Service Component
Architecture (SCA) binding. You can generate SCA bindings automatically
in the assembly editor. The kind of binding determines what kind of
client is supported; an SCA binding makes it available to other SCA
modules.

Bindings for imports and exports have different purposes.
An import binding describes the specific way an external service is
bound to an import component. An export binding describes how that
export (or service) will be published or made available to clients
outside the module.

To access a module from another module,
you need an export and an import with the same interface, and with
SCA binding. You also need to point the import to the module and export
that it will access.

## Procedure

To invoke a service from another module, complete the
following steps:

1. In the module whose service you want to use, create an
export, and add an interface.
2. Right-click the export and select Generate
Binding > SCA Binding.
Save the export.
3. In the module that will import the service from the module
that you created in step 1, add an import, and give it the same interface
as the export that you want to access.  Tip:  An
interface must be in a dependent library in order to be shared between
modules.
4. Right-click the import and select Generate
Binding > SCA Binding.
5. To add the service that you want to import, right-click
the import and select Select Service to Import.
Available services (exports) are listed for you. Select
the export of the module that you want to invoke.

## Example