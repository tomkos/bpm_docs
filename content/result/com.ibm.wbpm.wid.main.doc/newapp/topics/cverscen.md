<!-- image -->

# Versioning scenarios

Versioning is used when working in a development team environment
as well as to facilitate production evolution and the management of
services that are running in an SCA production environment. This topic
discusses some of the typical scenarios in which versioning can be
used.

## Versions in a team environment

When you
are developing an application, you can use versions to distinguish
levels of completion. However, you need to use an external source
code repository for that purpose. You can only keep one version of
a project in your workspace, because project names must be unique.

Through
Eclipse, IBM® Integration
Designer provides
a client for the Concurrent Versions System (CVS). You can also share
a project and save versions using Rational® Team
Concert or other repositories. See the related links for topics about
specific source management systems.

You will often find it
useful to assign each version to a new branch or stream in the repository
so that you can revert to it if necessary or make changes to a previous
version that is still in use. You can minimize confusion if you match
the version numbers used in the runtime environment with the branch
or stream names.

## Versioning modules

By using versioning,
you can create a module, put it into production, then decide to create
a new version of that module and also put that module into production.

Modules
are only version-aware when they are deployed through serviceDeploy.
Versioned modules exported as EAR files through Integration Designer or
added to the UTE through Add/Remove Projects do not recognize a module's
version properties.

Integration Designer does
not enforce an incremental module versioning pattern. Instead, you
can assign any three-part version number to your module. This means
that you can theoretically have a module 5.2.5 that contains older
content than module 1.0.0.

When you commit versioned modules
as branches, specify the module version number in the branch name.
Add appropriate branch comments that identify the version number.
This practice assists other users by providing information on the
version they are checking out.

Do not overuse module versioning.
Ideally, each module version should fulfill a specific purpose-for
example, a versioned module that handles traffic during seasonal operations.
Module versioning should never take the place of source control management
versioning and revision history. Let the source control management
system handle the typical day-to-day development changes.

## Versioning SCA imports

SCA bindings inherit
their version information from the module they are associated with.
When you create an SCA import binding by dragging a version of an
SCA export binding, the new SCA import binding will be tagged with
the version of the export. The static binding will resolve to the
specific export binding and module version during run time. Although
the binding is statically declared, you can modify the SCA import
binding at run time using the administrative console to reset the
version value to use a different deployed version of the export or
module. If an export is not known within the workspace, you must be
aware of whether the export has a version assigned to it and manually
assign that version value to the import binding.

The SCA import
has a static binding to one particular export, which means an import
can establish a connection only to the export for which it was built
and configured. So if the import has no version declared, it is expected
to be bound to a non-versioned export. If there are multiple numbered
versions of the service deployed to the runtime environment and the
import does not have a version declared, the import would fail to
resolve to any export.

You can build a mediation component
that contains an endpoint lookup primitive and assign a version and
match policy (latest compatible match) to it. This implementation
allows for dynamic routing to the appropriate version of the export
or module. If you promote the version property from the mediation,
you can dynamically modify the value in the runtime environment using
the administrative console.

## Refactoring versioned modules and libraries

1. From the dependency editor, change the version number. The refactoring
information bar opens.
2. Press Alt+Shift+R. The Change Version wizard
opens. Changed the declared version number of the module or library
as required. Note that you can click Preview to
see the refactoring actions that will be performed to complete the
change across the application.
3. Save the dependency artifact.

## Designing and changing encapsulated solutions

Encapsulation
in this context refers to grouping and isolating areas of functionality
- such as service implementations - so that they can be changed independently
from other parts of the system. You should design so that you will
be able to change the service implementation independently of its
consumers and of the service providers that it calls.

Even
if you have separated your service implementation from the module
that is its consumer, you need to pay attention to versioning when
you make changes. The consuming module should not be affected by additional
operations or optional attributes, but the old implementation might
not be able to build against the new objects if they are passing different
versions of objects over SCA bindings or between BPEL processes. Fully
decoupled interfaces surfaced as web services are less likely to cause
problems.

- Changes to operation parameters
- New mandatory structures or attributes on the request object
- New parameters (optional or mandatory) on the response object
- Changes to existing operation names
- Changes to namespaces

## Versions for long-running processes

Applications
that involve long-running components are vulnerable to changes in
their environment and require extra consideration at development time
about how process changes will be accommodated. You want new instances
of a process to follow the new design and existing ones to be dynamically
updated. IBM Workflow
Server supports
these goals with process versioning, late binding, and process instance
migration.

Process versioning enables you to keep multiple
definitions of a process in existence, simultaneously, at run time.
Existing instances continue to run according to their original designs.
New instances pick up the new definition if late binding is used.

IBM Integration
Designer provides
two distinct styles of invocation. Refer to the list below for more
detail.

Refer to the following for versioning in IBM Integration
Designer.

- Versioning scenarios
- Versioning BPEL processes
- Versioning business state machines

Also refer to the following files for versioning:

- Migrating running process instances to a new version of the BPEL process
- Supporting documentation for process instance migration