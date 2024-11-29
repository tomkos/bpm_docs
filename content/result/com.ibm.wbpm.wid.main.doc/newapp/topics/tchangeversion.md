<!-- image -->

# Changing the version of a module or library

You can change the versions of modules and libraries for
future deployment to a production environment. You can use the default
version scheme that is applied by IBM® Integration
Designer,
a custom scheme, or you can remove versioning completely.

## About this task

If you have already set up and deployed a project with
a version number, you might need to revise that version number so
you can deploy a patch or a significant revision to the same production
environment.

Note that modules that use a library have a dependency
on a specific version of that library, and libraries can also have
dependencies on specific versions of other libraries.

To change
versions for future deployment, follow these steps:

## Procedure

1. Expand the module or library in the Projects view and open
the dependency editor by double-clicking the dependencies artifact.
2. Expand the Version section of the
dependency editor to change the declared version of the module or
library.
3. Enter a new version number for the module or library as
required.
4. Save the dependency artifact.

## What to do next