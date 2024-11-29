<!-- image -->

# Versioning BPEL processes

Business processes evolve over time. They need to reflect changing
environments and business needs. These changes might be business-driven
changes, such as changes in regulations, or optimizations of processes.
Business process applications can include long-running BPEL instances.
These instances can run for weeks, months, or even years. This characteristic
imposes specific requirements on the introduction of new versions
of BPEL processes.

- In the likelihood that your BPEL process will need to be modified
over time, but its callers will not. In such a case, you will want
the existing callers to be able to seamlessly pickup the newest version
of the process the moment it becomes effective.
- You have a solution where multiple versions of the same BPEL process
must coexist. Although the solution as a whole cannot be uninstalled
and reinstalled, you will need to be able to deploy new versions of
the process in such a way as to ensure that new instances use the
latest version and, wherever possible, existing instances also migrate
to the latest version.

To create a new version of your BPEL process, create a new version
of the corresponding module in Integration Designer, and make
the changes that you need for the new process version. If the process
is not part of a process application or toolkit, you must also give
the new version of the process a valid-from date. To enable the migration
of any existing process instances to the new version, you must also
define a process migration specification in Integration Designer, and deploy
it with the new version of the process.

After the new version of the BPEL process is deployed, new process
instances can be created from the new version of the process. Existing
instances continue to complete using the version that they were created
and started with, or depending on the nature of the changes to the
process, they can be migrated to the new version. In some situations,
for example, when you want to correct an error in the process, you
might also want to migrate the running instances of a process to the
newer version so that they complete using this version.

## Planning for different process versions

To
create a version of a BPEL process, it is important that you plan
ahead. Specifically, you will need to consider how the client interacts
with the process, and how the process itself is set up. To allow for
seamless introduction of new versions, it is a good idea to anticipate
the need ahead of time, and set things up in the manner described
in the associated topics.

One important consideration is whether
instances of the process that are already running should move to the
new version. If you want to migrate running instances you need to
create a Migration Specification. If you are content to allow
existing instances to use the old version you do not need to create
a migration specification.

## Differentiating process versions

A version is
a copy of an existing process that is slightly different from the
original. To understand how this differentiation takes place, you
must first understand what identifies a version of a business process.

- same process component name
- same target namespace
- different valid-from date

- A process version that is part of the process application, orpart of a toolkit that is referenced by a process application canbe identified in one of the following ways:
    - Process application acronym, process application snapshot name,
and process name
    - Process application snapshot ID and process name
- A process version that is part of a top-level toolkit (a top-leveltoolkit is not referenced by a process application), or part of atoolkit that is transitively referenced by the top-level toolkit canbe identified in one of the following ways:

- Top-level toolkit acronym, top-level toolkit snapshot name, and
process name
- Top-level toolkit snapshot ID, and process name

- Correlation set specifications of different process versions need
be the same.
- Interface specifications of different process versions need to
remain the same. If you change the WSDL definition in any way, you
need to change the BPEL process to incorporate those changes. If the
WSDL has changed, you will need to load the new WSDL into IBM® Integration
Designer,
because when you deploy the module to the runtime environment, it
requires the service definitions in the consumer and provider to match.

Of critical importance, the two versions must have the
same name and namespace, but have different valid-from dates or
snapshot ID's. In addition, where applicable, they must also have
the same interface, and correlation set specifications. It is with
different valid-from dates that multiple versions of the same BPEL
processes are distinguished. In practice, at run time the process
engine could use a new version of a process that is set to become
valid today, even if an older version of that process was still being
used.

## Invoking versions of a BPEL process

When a client invokes a BPEL process, that client can
be configured either to choose a specific version each time, or to
pick up the currently valid version of the process. This is the basic
concept behind early binding and late binding.

With early
binding, a client is hard-wired to a process in such a way as
to force a continued relationship between the two of them, even if
another version of the process becomes available. In contrast, with late
binding the relationship between the client and the process is dynamic in
that it is resolved in the runtime environment.

If the caller instantiates
a process using early binding, a specific version of the process is
used to create that instance. If the caller uses a late binding, the
currently valid version of the business process is used.

Process
instance migration tools help you to update versions of running instances
of processes in a late-binding situation. You create a process
instance migration which, when deployed to the runtime environment,
moves running instances of the process to the new version whenever
possible. This facility is useful when you have very long-running
processes.

- Using SCA wiring
- Using the Business Process Choreographer APIs (generic EJB API
or generic web services API)

- Through the partner link extension in cases where a process that
is acting as a client calls another BPEL process.
- Using the Business Process Choreographer APIs (generic EJB API
or generic web services API)

## Example

- Invoking different versions of a BPEL process

Client applications can invoke a specific version of a process (early binding), or dynamically invoke the version of a process that is currently valid (late binding).
- Migrating running process instances to a new version of the BPEL process

When you introduce a new version of a BPEL process, you might want this version to apply to both new process instances and to instances that have already started. This can be important in environments where changes to processes are needed frequently, but where an individual process instance can be relatively long-lived. In such cases you need to migrate the process instances that are running to the newer version.
- Creating versions of your process to be used with SCA components and exports

This section explains how late binding between two processes can be used to allow late binding for arbitrary SCA components and exports. This pattern is only to be used when other means to apply late binding such as using the Business Process Choreographer API are not applicable.
- Late binding using a partner link extension

When you late bind one process to another one, the connection is resolved dynamically in the runtime environment. In that situation, the calling process will always pick up the currently valid version of the process that it is invoking. New instances will always use the latest version of the process, and if you use the migration verification tools you can also migrate running instances to the latest version.
- Process Migration Specification

Use a Process Migration Specification to migrate business process instances.