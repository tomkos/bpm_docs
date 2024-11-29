<!-- image -->

# Namespaces

A namespace is a logical container in which all the names
are unique; that is, a name can appear in multiple namespaces but
cannot appear twice in the same namespace.

A namespace is, literally, a space in which to store some names.
Namespaces provide a way to group artifacts, an abstract equivalent
to folders in a file system. Each namespace should gather resources
together that have some relationship to one another. In runtime processes,
the unique identifier for an artifact is composed of the namespace
and the artifact's local name.

You can see the namespaces for resources in the Business Integration
view. Click the Show Namespaces button in the
toolbar to show the namespaces of the resources.

The default namespace for an artifact is derived from the file
path. You can change this default namespace, but make that change
carefully. Read the rest of this topic and the related task "Changing
a namespace" for more information.

- Do not split a namespace across two dependent projects.
- Avoid name collisions within a namespace.

## Splitting a namespace

A single namespace
should not be used in two dependent projects; each module or library
requires its own set of unique namespaces.

You are likely to
encounter problems if you use the same namespace for multiple modules
or libraries. Consider this example. A module depends on two libraries
that have artifacts with a common namespace. The module references
Artifact A in one of the libraries and Artifact B of the same type
in the other library. (Artifacts A and B could both be business objects,
WSDL files, maps, or some other element.) If the library containing
Artifact A is listed first in the dependency editor, the program can
find Artifact A but not Artifact B. If the libraries are listed in
the reverse order, the program will find Artifact B but not Artifact
A.

The same problem will occur if a module that depends on a
library has artifacts that have the same type and namespace as artifacts
in the library. The program will find the artifacts in the module
but not in the library.

IBM® Integration
Designer and IBM Workflow
Server require
that all artifacts with the same namespace reside in the same library
or module. The same namespace should not be used by artifacts in two
libraries or modules. IBM Integration
Designer generates
unique namespaces by default when artifacts are created.

Do
not create artifacts with the same namespace in different projects.
If you encounter this condition, use the refactoring actions to either
move the artifacts to the same project or to assign the artifacts
different namespaces. It is a good practice to ensure that the namespace
for an artifact shows the actual location of the artifact.

## Name collisions

1. If the definitions are the same, delete one of them. Clean and
rebuild your project. Correct any errors that might result by pointing
existing business object or interface files to the file containing
the definition that you did not delete.
2. If the definitions are not the same and you must use both of the
definitions in your migrated service, rename the definition name or
the namespace. If there are only a few definitions in the entire file
that are duplicates, then changing their names is recommended. If
all of the definitions in the file are duplicates, then changing the
namespace of all of the definitions is recommended.
3. Clean and rebuild the project, ensuring that the artifacts that
you want to use in the definitions that you modified reference the
new definition name or namespace.
4. When you have two import statements for the same namespace in
an interface (WSDL file), you can remedy this problem by chaining
the imports in such a way that one of these interfaces imports the
other, which imports the next one, and so on., so that there is only
one import for this namespace per interface. Then clean and rebuild
the project.

## Moving namespaces

You need to pay some attention
to namespaces when you move artifacts from one library to another
or from a module to a library. IBM Integration
Designer and IBM Workflow
Server require
that all artifacts with the same namespace reside in the same library
or module (see "Splitting a namespace" above). Artifacts in two dependent
projects should not use the same namespace. Similarly, the same namespace
should not be used for artifacts in a module and for artifacts in
libraries on which the module has dependencies. When you move an artifact
to a library, first change the namespace to reflect the new location,
or at least change the namespace to one that is not being used by
the original project.

## Optimizing performance

If you are working
with more than one business object, you can improve performance if
you put each one in a separate namespace. If you put them all in the
same namespace, all of the business objects will get loaded each time
one of them is called, and the overall performance of the tool will
degrade.