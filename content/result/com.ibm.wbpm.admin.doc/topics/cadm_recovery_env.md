# Environment considerations

## Installation

When you install the IBM® Business Automation
Workflow environment as the
root user, there are no special instructions for the primary environment.

For the secondary environment, reinstall the environment
with the same information, such as installation path, product version,
and patch level, as in the primary environment.

## Configuration

Configuration includes creating
profiles and configuring cluster environments.

When you create
profiles in the primary environment, the profile path must be located
in the directory that is targeted at the NFS server. In the secondary
environment, the same directory of the corresponding operating system
must be mounted on the NFS server. No configuration is required before
the restoration.

To configure the cluster environment, follow the normal process of cluster configuration.

Each server except the NFS server in the secondary environment has the same IP address and host
name as the one in the primary environment. The NFS servers in the two environments have different
IP addresses and host names.

Db2 and IBM Business Automation
Workflow
are all installed in the /opt/ibm directory under their installation servers.
IBM Db2 is installed on Machine2, IBM Business Automation
Workflow is installed on
Machine1 and Machine2. For Db2, the databases related to IBM Business Automation
Workflow are created under
/home/db2, and the dmgr and custom profiles for IBM Business Automation
Workflow are created under
/home.

The dmgr files for IBM Business Automation
Workflow are created on
Machine1, IBM Business Automation
Workflow
custom profiles are created on Machine1 and Machine2.

Figure 1. Directories on the NFS server

<!-- image -->