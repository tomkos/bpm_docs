# Installing snapshots onto a connected server by using Workflow Center

## Before you begin

In addition, ensure that
the user ID that you are using has access to install snapshots to the connected workflow servers.
For information, see Managing access to workflow projects for access to process applications and
Configuring authentication to deploy to a production
environment for access to case solutions.

## About this task

When you install a process application or case solution, you install a snapshot of that process
application or case solution. You also install the toolkit snapshots that it depends on unless these
snapshots already exist on the workflow server. To update the process application or case solution,
you install additional snapshots. The last snapshot that you install becomes the default snapshot
and it is automatically active.

## Procedure

1. Log in to Workflow Center.
2. In the Process apps or Case solutions page, click
the process application or case solution that you want to install, and then click
Snapshots.
The Snapshots list displays all available snapshots and the status of each.
3. Click Install  next to the snapshot you want to install.
The Install a snapshot to a server window opens.
4. Select the server that you want to install the snapshot onto, and then click
Install.
Workflow Center begins the installation
and lists the server under the snapshot name. You can track its progress by expanding Installation
details under the server name.
5. Optional: 
If necessary, set environment variables.
For example, the correct value for a particular environment (such as test or production)
might not be known during the design phase. In these situations, provide the value after installing
the snapshot in the new environment.
For information, see BPMSetEnvironmentVariable command or Configuring runtime environment variables.
6. Optional: 
If necessary, establish runtime teams.
For example, after you install a snapshot in a new environment (such as test or
production), you might need to add or remove users in the teams for that project. That is, users in
the test environment might not have been available in the development environment.
For information, see Configuring runtime teams.
7. Optional: If necessary,
control exposed processes and services. For example,
after you install a snapshot in a new environment (such as test or
production), you might need to disable a particular exposed process
or service within that process applicationFor information,
see Configuring exposed processes and services.

## Results

The snapshot is installed in an active state and becomes
the default snapshot.