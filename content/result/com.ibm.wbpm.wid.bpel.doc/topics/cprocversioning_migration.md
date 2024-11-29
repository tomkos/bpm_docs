<!-- image -->

# Migrating running process instances to a new version of the
BPEL process

- Create a new version of the BPEL process in Integration Designer, and deploy
it to Workflow Server.
- Update a process in IBM®
WebSphere® Business Modeler Version
7.0.0.2 or later, export it to Integration Designer, and deploy
it to a process server.
- Create a new version of the BPEL process in Integration Designer, deliver
it to Workflow Center,
and deploy the corresponding process application or toolkit.
- Create a new snapshot of a process application or a toolkit that
contains a BPEL process, which has not been modified, and deploy it.

<!-- image -->

In general, for a new version of a BPEL process to become a migration
target, you must deploy a migration specification together with the
new version of the process. If you deploy a new snapshot of a process
application or toolkit with the same BPEL process implementation as
a previously deployed snapshot, the new version the BPEL process automatically
becomes a migration target for the previously deployed snapshot.

To migrate running process instances to a new version of the process,
you can use either an administrative script to migrate process instances
in bulk, or Business Process Choreographer Explorer to migrate specific
instances.When migration is triggered, the process, the variables,
and the activities that are at the current position of the process
navigation now refer to the new version of the BPEL process and the
follow-on navigation depends on the logic of the new version of the
BPEL process. The activities that have already been navigated when
the process instance is migrated are not migrated. During the migration
of a process instance, all the instances of inline human tasks, which
belong to this process instance and are not yet in an end state, are
also migrated.

If the changes to the process that are contained in the new version
of the process do not affect the process logic, such as the display
name or description of an activity, a running process instance can
be migrated any time during the process navigation. However, if the
changes affect the process logic, such as new activities, variables,
or conditional expressions are changed, you can migrate a running
process instance to a newer version only if all of the changes that
affect the logic of the process are after the current position in
the process navigation.

For example, any change to an inline human task is considered to
affect the logic of the process. You can migrate a running process
instance to a newer version only if all of the changed inline human
tasks are after the current position in the process navigation.

If events are defined for the BPEL process, you can track process
migration using Common Base Events. An event can be generated when
the migration is started and again when the migration is complete.
A history of process migrations is also kept in the Business Process
Choreographer database.

- BPEL process model changes and runtime migration

The changes that were made to the process to create the new version determine when and how existing BPEL process instances can be migrated in the runtime environment. Changes to the descriptive or quality-of-service properties are handled differently from changes to the business logic.
- Creating a new version of your process - migrate running instances

Process instance migration enables you to migrate running instances to a newer version by creating a process migration specification. This topic explains how to create a new version of your process that you can use as the target of a process instance migration in the runtime environment.
- Creating a new version of your process - running instances use old version

Create a new version of your process whose binding may be dynamically resolved in the runtime environment. This procedure does not include the generation of a Migration Specification, which would be necessary to move running instances of the process to the new version.
- BPEL process migration tracking

If events are defined for a BPEL process, you can track process migration using common base events. An event can be generated when the migration is started and again when the migration is complete. In addition, a history of process migrations is kept for each process instance in the Business Process Choreographer database.