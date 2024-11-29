# NFS support

If a snapshot is performed at the operating system level, the snapshot for different operating
systems might correspond to the state at different points in time.

When you use a Network File System (NFS), users on a client computer can access files over the
network as if the files were on their local server. In this architecture, a file server is
configured on one operating system, which functions as the central repository for all files. The NFS
client operating system can connect with the file server and mount the specific directory to the
file server. The NFS client operates transparently on the directory mapped on the file server.

When NFS is enabled, therefore, the configuration and installation data of the production
environment can be configured on a centralized NFS file server. In combination with the snapshot
support of the file server operating system, you can create a consistent backup of the entire
production system.

Before you create a snapshot, you must set up your NFS server and clients.

1. Configuring the NFS server

The first step in configuring your NFS environment is to configure the NFS server, which functions as the central repository for all files.
2. Configuring the NFS clients

The second step in configuring your NFS environment is to configure the NFS clients.