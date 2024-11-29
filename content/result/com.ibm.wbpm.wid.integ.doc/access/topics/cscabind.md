<!-- image -->

# SCA bindings

The SCA binding lets your service communicate with other services
in other modules. You can use an import with an SCA binding to access
a service in another SCA module. You can use an export with an SCA
binding to offer a service to other modules.

All imports and exports need bindings. Within the assembly editor,
by default, a runtime process applies an SCA binding to an export
with no binding.

If modules are running on the same server, an SCA binding is the
easiest and fastest binding to use. The same is also true of modules
deployed in the same cluster. If you want a service to be published
as a web service and to be available to other modules in the same
cluster, consider using two exports, one with a web service binding
and one with an SCA binding.

An SCA binding on an import specifies an SCA-bound export in another
module. That export can be connected to either a component or an import.
As a result, the SCA import binding requires only two pieces of information:
the name of the export it is calling and the module containing that
export. The export must also have an SCA export binding. If the export
has any export binding other than SCA, you cannot import it in another
module with the SCA import binding. You must import it with the corresponding
import binding type.