<!-- image -->

# Partitioning libraries and modules

When you put artifacts in libraries, you can share those
artifacts with modules. The method that you use to package the libraries
and their contents can affect maintenance and scalability.

The most important consideration is to package according
to the encapsulation boundary, by minimizing library and module dependencies.
You can use this approach to make changes within the boundary with
the confidence that you will not affect things outside it, and to
assign stronger ownership of the design and runtime artifacts based
on these boundaries. The picture below illustrates this approach.

<!-- image -->

- 1  If you need to share an artifact
between modules or mediation modules, place it in a library.
- 2  Avoid putting all your artifacts
in a single library that is shared by multiple modules. If you need
to replace an artifact, you must rebuild and redeploy all of the modules
that depend on the library.
- 3  A library should contain only
those artifacts that are needed by the modules that reference it.
However, artifacts that share namespaces must be in the same library.
- 4  Use a dedicated public library
for interfaces and wsdl files of exports that are callable by clients.
Artifacts that are not needed by clients should not be in a public
library.
- 5  You often use special interfaces
and business objects internally that match neither the publicly exposed
interfaces and business objects, nor the proprietary interfaces and
business objects of external services or endpoints. As explained in
point #3, these artifacts should go in their own private libraries.
This division isolates the internal implementation from the outside
world. The more logic there is inside the boundary, the more important
it is to have a separate set of libraries.
- 6  Use dedicated libraries to contain
artifacts for calling external services, for example imported Web
Service Definition Language (WSDL) files for third party libraries
or industry schemas. Typically, you would not need to edit the contents
of these libraries, because they are owned externally. Consider minimizing
the contents of these libraries by including only those artifacts
that you will use, especially if the library will be referenced by
multiple modules. For example, if the library has 400 data types and
you are going to use only 20, try to keep only the 20 data types that
you use in your library.
- 7  If a library is extremely large, perhaps because of an industry
schema, consider using runtime sharing. For more information, see Considerations when using shared libraries.