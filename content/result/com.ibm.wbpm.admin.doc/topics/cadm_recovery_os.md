# Operating system considerations

The host names of the primary and secondary environments are used in the IBM® Business Automation
Workflow configuration data,
for example in the serverindex.xml file.

For an Business Automation Workflow server configuration where
distributed transactions must be recovered, mirror the transaction logs on a different server that
has the same server name, the same host name, and access to the same resource managers as the
original server. Information about each server that is involved in a distributed transaction is
stored in the transaction logs. This information includes the server name and the host name of the
computer on which the server is running. When a distributed transaction is being recovered, the
servers that are involved in the recovery use this stored information to contact each other.
Therefore, if a server fails and the logs must be recovered on a new server, that new server must
have the same server name and host name as the original server. The new server must also have the
same access to the same resource managers, databases, and message queues as the original server.

In the examples that are in the topics that follow, all operating systems are deployed with Red
Hat Enterprise Linux.

- Snapshot support

If you want to back up the primary environment without affecting normal functioning, you need the additional support of an operating system snapshot.
- NFS support

In a distributed environment, the data of the production environment is distributed over several operating systems. Without special configuration, during run time, it is highly possible to get an inconsistent copy of the entire environment even when you use a snapshot. A consistent copy of the entire environment is required to ensure the proper behavior of the system. To ensure consistency, you can use a Network File System (NFS).