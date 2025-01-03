# Configuring runtime settings for installed snapshots

Configuration tasks require administrative access to the workflow server on which the snapshots
are installed.

To configure runtime settings, use the Installed Apps tab
in the Process Admin Console. Select a snapshot, and then select the Exposing, Team
Bindings, or Environment Vars option.

The Process App Settings Servers page for a process application or Toolkit Settings Servers page
for a toolkit specifies the connection properties to use for accessing the following servers:
Enterprise Content Management servers and IBM® Operational Decision
Manager servers.

- Configuring exposed processes and services

During development, process authors determine which processes, services, and other items are available and to which teams. After a process application is installed on a workflow server in the test or production environment, you might need to disable exposed items within that application.
- Configuring runtime teams

Teams can be defined statically or dynamically, and can have a team of managers that are associated with them. During development, process authors create the teams for each process application. After a process application is installed on a workflow server in the test or production environment, you might need to add or remove users and groups in those teams so that the appropriate staff can access and perform the tasks that are generated by the process application.
- Configuring runtime environment variables

During development, process authors can set environment variables for each process application. In some cases, the correct value for a particular environment (test or production) might not be known during process design. In those cases, you need to provide the value after installing the process application in the new environment.