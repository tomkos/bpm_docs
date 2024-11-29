<!-- image -->

# Library

- Business objects
- Interfaces
- Mediation subflow
- Datamap
- Relationship
- Binding resource

1. Sharing of artifacts for development
2. Sharing of artifacts within the solution at run time

Artifacts in a library are public, and they can be shared across modules. Artifacts in a module
are private. Integration developers should organize artifacts by taking into consideration logical
function and visibility. For example, related data types that are used by various pieces of a system
should be placed into a library. Other modules can then easily reuse this library. Only one copy of
each element needs to be created and maintained using this method. Likewise, related business logic
features of the application should be grouped into modules. Structuring an application in this way
will yield a more flexible, easily maintained application. It will also be easier to add new
features to the application.

## Business objects and interfaces

Business objects are containers for application data, such as customer details or an invoice.
Data is exchanged between components by way of business objects. When using imports and exports in
assembly diagrams, it is good practice to put the business objects and interfaces that are used by
the import and exports into a library so that they can be shared. Then, add a dependency on the
library to all of the modules that use these common resources. Avoid copying the same business
objects and interfaces into different modules to use them.

## Mediation subflows

If you have mediation logic that you want to reuse across mediation flows you can define a
mediation subflow within a library. Mediation flows cannot be placed in a library.

## Library resources that are shared

If you choose to deploy a library with a module, which is the default setting, a copy of the
library is made for each module when the module is deployed. After deployment, if shared resources
change in the library, all modules using the resources have to be updated. For example, two modules
share some resources in a library. The applications are deployed. One of the modules has to be
updated, resulting in changes to some of the shared resources in the library. In this case, the
second module also needs to be updated to reflect the changes in the shared resources.