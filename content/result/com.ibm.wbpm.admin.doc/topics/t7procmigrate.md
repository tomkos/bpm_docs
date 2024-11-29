<!-- image -->

# Migrating specific BPEL process instances to a different process
version

## Before you begin

## About this task

When a new version of a BPEL process is deployed, you
can base new process instances on this process version if you start
them in Business Process Choreographer Explorer from the corresponding
template. However, existing process instances which are based on a
previous version of the process continue to run with this version
until they reach an end state. You can migrate these existing process
instances to a different process version; you do not need to migrate
all of the instances to the same version.

You can also use the migrateProcessInstances.py script
to migrate process instances in bulk. For more information, see the
related information section.

In Business Process Choreographer
Explorer, perform the following steps to migrate process instances.

## Procedure

1. Navigate to a page that shows a list of process instances.
For example, click All Versions, select
one or more process templates, then click Instances.
2. Select the relevant process instance entries and click Migrate.
3. In the Process Instance Migration page,
select the process template version to migrate the process instances
to.
4. Optional: Test whether the process instances
can be migrated to the process template version by clicking Test.
5. Click Migrate to migrate the process
instances to the specified process template version.

## Results

<!-- image -->