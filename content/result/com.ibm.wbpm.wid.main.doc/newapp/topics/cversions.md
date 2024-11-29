<!-- image -->

# Versions

Versioning provides the ability for the runtime environment
to identify snapshots in the lifecycle of a solution or service and
to be able to concurrently run multiple snapshots at the same time.

The details provided here apply to versions created in Integration Designer and
deployed directly to the Workflow Server. If
you are using IBM Workflow
Center,
a different set of rules apply. See "Versioning in Workflow Center"
in the related links for information about versions in that context.

If you have older applications that are running and those applications
do not need to be changed, you should probably just leave them as
they are. If you are creating new applications or you have older applications
that need to be revised, you should probably associate them with process
applications and run them through the Process Center.

## Why should you use versions?

You assign
version numbers to modules during development. Those numbers are used
in a scrambled form during deployment versioning. The bindings between
modules pick up those versions. If you deploy modules directly to
the Process Server in 7.5, you can still follow that same procedure.

Module
versioning allows you to do a few things. Perhaps more importantly,
you can simultaneously install multiple versions to the same runtime
target.

Versioning is beneficial in a production environment
for a number of reasons. First, you can logically manage modules based
on a defined feature-set, and you can easily deploy a specific version
to fulfill a given purpose. As well, versioning allows you to simultaneously
deploy multiple versions of an SCA module to the same deployment environment
(that is, versioning applies to the production environment, not the
development and testing environment). It also allows you to build
a mediation component declaring a version value and matching policy
to dynamically route to the determined version during the runtime
environment. Set up this mediation process by using the endpoint lookup
primitive (which also requires WSRR).

Creating
a version of a business process allows you to modify the process without
modifying its callers. The existing callers will be able to seamlessly
pick up the newest version of the process the moment it becomes effective.
You can also have several versions of the same process coexist on
the server so that long-running processes can complete without interruption.
The topics that explain how to set up versions of a process also explain
how to plan your solution to allow for the kinds of changes that you
expect to make.

## What can you version?

A module can have
a version number, as can the SCA export bindings in a module. SCA
bindings inherit their version information from the module they are
associated with. SCA imports can specify a target version number.

A
library can be versioned. Use the best practice policy of storing
shared interfaces and business objects (WSDLs and XSDs) in libraries
and setting up dependencies for the modules or libraries that use
those resources. Modules that use a library have a dependency on a
specific version of that library, and libraries can also have dependencies
on specific versions of other libraries.

You can create versions
of a process.

You can create versions of a human task or state
machine, so that multiple versions of the task or state machine can
coexist in the runtime environment.

## The versioning scheme

The version scheme
built into the product uses a three-digit numeric version system in
the format <major>.<minor>.<service>. For example,
an early version of a module might have a version number 1.0.2. The
values are purely subjective; you need to specify their values. You
need to decide when to increment each category, because the product
does not keep track of the incremental module versions. In most cases,
you should use sequential numeric ordering, although that rule is
not enforced.

The versioned module is identified using the
pattern ModuleName\_vX\_Y\_ZApp.ear  where X, Y, and Z are the major,
minor, and service revision numbers.  For example, assume you have
a module, HelloWorldProcess, in your Integration Designer workspace.
You enable versioning and identify the module as version 1.0.1. When
the module is deployed through Add/Remove projects, the resulting
EAR would be named HelloWorldProcessApp.ear. However, with versioning
enabled the module name becomes HelloWorldProcess\_v1\_0\_1App.ear through
serviceDeploy.

Dependent projects and libraries of a versioned
module do not have to be versioned, nor do they have to use the same
version number as the referring module. Module versioning properties
can be set under the module's dependency settings. When you deploy
a module to a test server or production server, the dependent libraries
and modules are deployed as well.

When modules are versioned,
only the module name is uniquely modified. This system allows you
to install two or more copies of the same application in a runtime
environment. However, any BPEL processes or human task templates will
not be changed, and the process or task templates must be unique for
a given process or task container. If you try to simultaneously install
multiple modules versions to the same runtime target without also
versioning the human task or BPEL process, the application will fail
to install. To resolve this problem you either need to version your
BPEL process at design-time, or refactor the BPEL process template
name.

- sca.module The SCA module name is defined in this file.
If module versioning is used, the module name will be renamed during
deployment to append the version number to the module name string
during deployment.
- sca.module.attributes This artifact is only created when
module versioning is enabled. The module number that you specify is
set here.

## Process application scope

There are advantages
to having everything in one process application, but that structure
might not be practical for large applications. In such cases, process
application scope should be at the functional level where it can be
managed as one unit.

The ability to manage and deploy large
solutions using ANT scripts is not supported by process applications.
In some cases, this might be a reason for large organizations to put
off moving to the new model.