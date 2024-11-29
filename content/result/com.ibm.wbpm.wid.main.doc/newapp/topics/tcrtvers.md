<!-- image -->

# Creating versioned modules and libraries

You can create versioned modules and libraries in IBM® Integration
Designer for
future deployment to a production environment.

## Before you begin

To determine if newly created modules and libraries have
versioning by default, click Window > Preferences > Business Integration > Module And Library Versions.
To enable versioning by default, select the IBM Supplied
Version Scheme from the drop-down list. You can also choose
the IBM Supplied Version Scheme from the dependency editor as outlined
in the steps below. Modules and libraries associated with process
applications or toolkits are not versioned as the Workflow Center handles
versions with snapshots.

## Procedure

To create versioned modules and libraries, complete the
following steps:

1. Create a module or a library using the New Module or New
Library wizards. To use the New Module or New Library wizards, click File > New > Module or File > New > Library.
2. Expand the module or library in the Projects view and open
the dependency editor by double-clicking the dependencies artifact:
3. Expand the Version section to select
the version for the module or library. By default, versioning is not
set and if you did not set the default in the Preferences, click the
drop-down arrow and select IBM Supplied Version Scheme.
4. Enter a version number for the module or library as required.
The default scheme uses three numbers for version, release, and modification.
5. Save the dependency artifact. You will see the following
message when adding a version to a module.
6. Click OK.

## Results

## What to do next

Export your logic using an SCA export. SCA bindings inherit
their version information from the module they are associated with.
When you create an SCA import binding by drag of a versioned SCA export
binding, the new SCA import binding will be tagged with the version
of the export. The static binding will resolve to the specific export
binding and module version during run time. Although the binding is
statically declared, you can modify the SCA import binding at the
runtime environment using the administrative console to reset the
version value to use a different deployed version of the export or
module. If an export is not known within the workspace, you must be
aware of whether the export has a version assigned to it and manually
assign that version value to the import binding.

You
can only create a version-aware EAR file using the serviceDeploy command.
Modules that you export as EAR files build and install properly, but
they will not be versioned. The same is true of applications that
you add to the UTE using Add/Remove projects.

Export a business
integration module specifying command line service deployment. You
can then use the serviceDeploy command to generate a version-aware
EAR file. Input to the serviceDeploy command is the output compressed
file from the business integration module export.