# Version-aware bindings

Process applications can contain SCA modules that include
import and export bindings. When you co-deploy applications, the binding
for each version of the application must be unique. Some bindings
are automatically updated during deployment to ensure the uniqueness
between versions. In other cases, you have to update the binding after
deployment to ensure its uniqueness.

A version-aware binding is scoped to a particular
version of a process application, which guarantees its uniqueness
between process applications. The following sections describe the
bindings that are automatically updated to be version-aware as well
as any actions you need to take at run time when a binding is not
version-aware. For information about things to consider when you create
modules, see Considerations when using bindings.

## SCA

The target of an SCA binding is automatically
renamed to be version-aware during deployment if the import and export
bindings of the module are defined in the same process application
scope.

If the bindings are not defined in the same process application
scope, an information message is logged. You must modify the import
binding after deployment to change the endpoint target address. You
can use the administrative console to change the endpoint target address.

## Web service (JAX-WS or JAX-RPC)

- You followed the default naming convention for the address:http://ip:port/ModuleNameWeb/sca/ExportName
- The endpoint address is SOAP/HTTP.
- The import and export bindings of the module are defined in the
same process application scope.

- If you are co-deploying your process application, you must manually
rename the SOAP/HTTP endpoint URL or the SOAP/JMS destination queue
to be unique between versions of the process application. You can
use the administrative console after deployment to change the endpoint
target address.
- If you are deploying only a single version of the process application,
you can ignore this message

- If the import and target export are in the same process application,perform the following steps before you publish the process applicationin Workflow Center andcreate the snapshot:
    1. Change the endpoint URL of the export. Make sure the destination
and connection factory are unique.
    2. Change the endpoint URL of the import so that it is the same as
the one you specified for the export in the previous step.
- If the import and target export are in different process applications,perform the following steps:

1. Change the endpoint URL of the export. Make sure the destination
and connection factory are unique.
2. Publish the process application in Workflow Center.
3. Create the snapshot.
4. Deploy the process application to the process server.
5. Use the WebSphere administrative console to change the endpoint
URL of the corresponding import so that it is the same as the one
you specified for the export.

## HTTP

- You followed the default naming convention for the address:http(s)://ip:port/ModuleNameWeb/contextPathinExport
- The import and export bindings of the module are defined in the
same process application scope.

- If you are co-deploying your process application, you must manually
rename the endpoint URL to be unique between versions of the process
application. You can use the administrative console after deployment
to change the endpoint target address.
- If you are deploying only a single version of the process application,
you can ignore this message

## JMS and generic JMS

- Endpoint configuration
- Receive destination queue
- Listener port name (if defined)

## MQ/JMS and MQ

No automatic renaming occurs
during deployment to enable bindings of type MQ/JMS or MQ to be version-aware.

- Endpoint configuration
- Receive destination queue

Set the matching Send destination if you change the target
module endpoint.

## EJB

No automatic renaming occurs during
deployment to enable bindings of type EJB to be version-aware.

You
must rename the JNDI names attribute to be unique between versions
of the process application.

Note that client applications also
need to be updated to use the new JNDI names.

## EIS

A resource adapter is automatically
renamed to be version-aware during deployment as long as the default
resource name (ModuleNameApp:Adapter Description)
was not modified.

If the default resource name was modified,
the resource adapter names must be unique between versions of the
process application.

If the resource adapter names are not
unique, an informational message is logged during deployment to alert
you. You can manually rename the resource adapters after deployment
using the administrative console.