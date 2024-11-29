# Installing snapshots

## Before you begin

To install snapshots onto workflow run times, ensure you meet the needed requirements. For more
information, see Snapshot deployment requirements.

- Snapshot deployment requirements

Before you install a snapshot, make sure that you have the proper requirements.
- Snapshot installation

When you install a snapshot to a workflow server, the library items for that snapshot (including toolkit snapshots) are copied from the repository to the selected workflow server if they do not exist on the workflow server. The workflow server can be connected or offline. Depending on your needs and whether the workflow server is connected or offline, you can use Workflow Center or wsadmin commands to install the snapshot.
- Installing snapshots to a connected workflow server

You can install snapshots to a connected workflow server by using Workflow Center or by using wsadmin commands.
- Installing snapshots to an offline server

You can install process applications on an offline workflow server by using Workflow Center or by using wsadmin commands and generic or custom installation packages. To test your snapshots in Process Designer and for more flexibility with the installation process, you can use the offline installation process to also install a snapshot on a connected workflow server.
- Building a custom deployment service flow

A deployment service flow is created by default when you create a new process app or case solution and is used when you install a snapshot. You can customize the service flow to handle advanced requirements in your target environment.
- Troubleshooting snapshot installations

Exceptions, timeouts, and other failures in the installation process can result in the snapshot not being installed on the server, or in an incomplete snapshot installation.