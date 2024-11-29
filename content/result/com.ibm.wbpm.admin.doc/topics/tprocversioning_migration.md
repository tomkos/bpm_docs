<!-- image -->

# Migrating BPEL processes

- Migrating specific BPEL process instances to a different process version

A process template represents a version of a process. Running BPEL process instances can be migrated to a different process template version. You might want to do this, for example, when a newer version of the process becomes available, or because the current version has errors in it and you want to roll back to a previous process version. Use Business Process Choreographer Explorer to migrate selected process instances.
- Migrating BPEL process instances in bulk to a new version of a process template

Use an administrative script to migrate running instances after deploying a new version of a process template, because new process instances are based on the new version, but existing instances based on the old template version continue running until they reach an end state.