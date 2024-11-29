<!-- image -->

# Generating SCA bindings

## About this task

Bindings for imports and exports have different purposes.
An import binding describes the specific way an external service is
bound to an import component. An export binding describes how that
export (or service) will be published or made available to clients
outside the module.

The kind of binding determines what kind
of client is supported; an SCA binding makes it available to other
SCA modules. You can generate an SCA binding when you use the palette
in the assembly editor to create imports and exports.

## Procedure

To generate an SCA binding, complete the following steps:

1. If there is no interface defined on the import or export,
add the interface first. See related tasks for instructions on adding
the interface.
2 Do one of the following:
    - For an import, under the Outbound Imports section,
select SCA and drag it onto the canvas. Add
your interface to it.
    - For an export, under the Inbound Exports section,
select SCA and drag it onto the canvas. Add
your interface to it.
    - Alternately, under Components, drag an
import or export onto the canvas. Right-click the import or export
and select Generate Binding > SCA Binding. An SCA binding is
generated without requiring you to supply additional information.
Here is an import with an SCA binding:
3. To add the service that you want to import, right-click
the import and select Select Service to Import.
Available services are listed for you.

## Results