<!-- image -->

# BPEL process migration tracking

## Common base events for migration

You can use common base events to monitor process instance migrations.

## Process migration history

A history of each process instance migration is kept in the Business Process Choreographer
database. This information is available for each process instance and it is deleted when the process
instance is deleted.

When a process instance is migrated, the isMigrated property is set to TRUE in the
PROCESS\_INSTANCE database view. The MIGRATION\_FRONT database view provides the migration history for
each process instance migration. This view contains information about where the process instance was
in its navigation when it was migrated to the new version of the process template.