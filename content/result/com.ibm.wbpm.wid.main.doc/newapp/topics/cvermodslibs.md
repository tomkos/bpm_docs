<!-- image -->

# Versioned modules and libraries

You can create versioned modules and libraries to use on
a server at run time.

Versioning is beneficial in a production environment for a number
of reasons. You can use versioning to simultaneously deploy multiple
versions of an SCA module to the same deployment environment. This
is possible because versioning applies to the production environment,
not the development and testing environment. You can also use versioning
to build a mediation component declaring a version value and matching
policy to dynamically route to the determined version during the runtime
environment. Set up this mediation process by using the endpoint lookup
primitive (which requires WSRR).

Versioning of modules and libraries is optional. You can select
versioning based on a scheme provided by IBM, or you can choose to
not use versioning at all. The modules that use a library have a dependency
on a specific version of that library, and libraries can also have
dependencies on specific versions of other libraries. Services and
exports inherit their version from the module.

| Library scope                  | Description                                                                                                                                                                                                                                                                                                                                                                                           | Can depend on . . .                                                                                                                                    |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Module                         | A copy of this library exists on the server for each module that uses it.                                                                                                                                                                                                                                                                                                                             | A module-scoped library can depend on all types of libraries.                                                                                          |
| Process application or toolkit | The library is shared among all modules in the scope of the process application or toolkit. This setting takes effect if deployment is done through the IBM Workflow Center. If deployment occurs outside of the IBM Workflow Center, the library is copied into each module.Note: Libraries created in IBM Integration Designer version 8 have a sharing level of Process App or Toolkit by default. | A library of this type can depend only on global libraries.                                                                                            |
| Global                         | The library is shared among all modules that are running.                                                                                                                                                                                                                                                                                                                                             | A global library can depend only on other global libraries. Note: You must configure a WebSphere shared library in order to deploy the global library. |

- Creating versioned modules and libraries

You can create versioned modules and libraries in IBM Integration Designer for future deployment to a production environment.
- Modules and libraries associated with process applications or toolkits

You do not need to version modules and libraries associated with process applications or toolkits.
- Changing the version of a module or library

You can change the versions of modules and libraries for future deployment to a production environment. You can use the default version scheme that is applied by IBM Integration Designer, a custom scheme, or you can remove versioning completely.
- Versioning scenarios

Versioning is used when working in a development team environment as well as to facilitate production evolution and the management of services that are running in an SCA production environment. This topic discusses some of the typical scenarios in which versioning can be used.
- Considerations when versioning

The considerations listed in this topic help you version modules and libraries in IBM Integration Designer.