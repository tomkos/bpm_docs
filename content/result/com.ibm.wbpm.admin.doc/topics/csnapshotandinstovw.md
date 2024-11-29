# Snapshot and process instance migration overview

Migration tasks are performed in the following order during snapshot and instance migration.

1. Exposed process variable (EPV) changes are migrated.
2. Environment variable changes are migrated.
3. Team users and groups are merged from the source to the target.
4. The source snapshot is deactivated.
5. The target snapshot is activated.
6. The target is set as the default snapshot if the source snapshot was the default.
7. Undercover agents (UCAs) are activated.

1. Each process instance is locked while it is migrated.
2. Tasks associated with the instances are migrated.
3. The process execution context and variables are migrated.
4. Case folders and ad hoc tasks are migrated.
5. The token migration policy file is applied.
6. The task search index is updated.
7. Monitored events are triggered.