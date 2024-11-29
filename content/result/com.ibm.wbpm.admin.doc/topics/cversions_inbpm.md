# Versioning projects

To understand how process applications are versioned, remember that it is a container that holds
various artifacts that it uses. For example, process models, toolkit references, services, or
branches. Any versioning is done at this container level, not at the level of the individual
artifacts.

You can compare snapshots to determine differences between the versions. For example, if a
developer fixed a problem with a service and took a snapshot of the process application or toolkit
that contains it, and then a different developer made changes to the same service and took a new
snapshot, the project manager can compare the two snapshots to determine which changes were made
when and by whom. If the project manager decided that the additional changes to the service were not
worthwhile, the project manager can revert to the snapshot of the original fix.

You can run different snapshots of a process application concurrently on a server. When you
install a new snapshot, either remove the original or leave it running.

## Version context

Each snapshot has unique metadata to identify the version (referred to as version context). You
assign that identifier, but it's a good idea to use a three-digit numeric version system in the
format <major>.<minor>.<service>. For more information
about this versioning scheme, see Naming conventions.

The system assigns a global namespace for each process application. The global namespace is
specifically either the process application's tip or a particular process application snapshot. The
version name used by the server cannot be longer than seven characters, so the assigned name is an
acronym that uses characters from the snapshot name that you assigned. Snapshot acronyms are
identical to their snapshot names if the snapshot names conform to the recommended style and are no
more that seven characters. For example, a snapshot name of 1.0.0 will have an acronym of 1.0.0, and
a snapshot name of 10.3.0 will have the acronym of 10.3.0. The snapshot acronym will be guaranteed
to be unique within the context of the process application within the scope of the playback server.
For that reason, you can't edit the snapshot acronym.

## Versioning considerations for process applications in multiple clusters

You can install the same version of a process application to multiple clusters within the same
cell. To differentiate among these multiple installations of the same version of the process
application, create a snapshot for each installation and include a cell-unique ID in the snapshot
name (for example, v1.0\_cell1\_1 and v1.0\_cell1\_2). Each snapshot is a new version of the process
application (from a pure lifecycle management perspective), but the content and function are the
same.

When you install a process application in a cluster, an automatic synchronization of the nodes is
performed.

## Versioning considerations for toolkits

Remember that process application snapshots are typically taken when you are ready to test or
install. You typically take a snapshot of a toolkit when you are ready for that toolkit to be used
by other projects. Afterward, if you want to update the toolkit, you must take another snapshot of
the tip when you are ready, and then the owners of process applications and toolkits can decide
whether they want to move up to the new snapshot.

- Naming conventions

A naming convention is used to differentiate the various versions of a project as it moves through the lifecycle of updating, deploying, co-deploying, undeploying, and archiving.