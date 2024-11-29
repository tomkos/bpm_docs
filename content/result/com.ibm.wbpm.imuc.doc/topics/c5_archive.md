<!-- image -->

# BPEL process archive overview

## Architecture

- Business Process Archive Manager
- Business Process Archive Explorer
- Business Process Archive database
- The archive.py script
- Business Process Archive Manager EJB API

Figure 1. Business Process Choreographer
using one Business Process Archive

<!-- image -->

To create a Business Process Archive Manager, you must add
entries to the properties file before you create the deployment environment.
For more information about editing the properties file, see Configuring Business Process Archive Manager.

- You can create a Business Process Archive Manager only on the
support cluster in a three-cluster setup.
- A Business Process Choreographer configuration can only use a
Business Process Archive Manager configurations that is in the same
cell.
- A Business Process Archive Manager configuration can be used to
archive data from only one Business Process Choreographer configuration.
- Each Business Process Archive Manager configuration must have
its own Business Process Archive database.

A new method, OperationMode
getOperationMode() is provided, which indicates whether the client is connected to a
Business Process Choreographer configuration or a Business Process Archive Manager configuration.
This can be used to write custom clients that can connect to and operate appropriately on runtime
configurations and archive configurations.

For more information about the Business Process
Archive Manager API, see the Javadoc for the packages com.ibm.bpe.api
and com.ibm.task.api.

Depending on your authorization,
you can use the Business Process Archive Explorer to browse instances
and possibly delete instances too. You cannot update instances or
create new instances.

- Users who are in the Business Process Archive Manager system monitor
role can read and view all process instances and all task instances
in the archive database.
- Users who are in the Business Process Archive Manager system administrator
role can also delete any top-level process instances and top-level
task instances in the archive database.
- Users who are not in the system monitor or system administrator
roles can see only the instances that they created or started themselves,
but they cannot view any details about the instances.
- No one (not even users in the system administrator roles) can
modify any of the data that is associated with any instances in the
archive database.
- Instance-based authorization information, such as the potential
owner or reader information, is not archived. Therefore, this data
is not available in the archive. The only exception to this rule is
the information about the starter and creator of processes and tasks.
- Users must be in the WebClientUser role to use
the Business Process Archive Explorer.

## Which data is archived

Only top-level process
instances and top-level stand-alone human task instances that have
reached one of the end states (Finished, Terminated, Failed,
or Expired) can be moved to the archive database.
When a top-level instance is archived, certain data is also moved
with it to the archive, and other data is deleted.

- Instance data such as activities, variables, inline human tasks,
input messages, and output messages are moved.
- Child processes and related data are moved recursively.
- If any related metadata such as process templates and task templates
are not already in the archive database, a copy of them is created.
- Query tables and stored queries are not moved nor copied to the
archive database.
- Work items that are associated with an archived instance are deleted
without being archived.

- Instance data such as input messages and output messages are moved.
- Escalation instances are moved.
- Child tasks, including follow-on tasks, are moved.
- If related metadata such as task templates are not already in
the archive database, a copy of them is created.
- Work items that are associated with an archived instance are deleted
without being archived.