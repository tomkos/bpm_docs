# Database considerations

The underlying database must be included in the same recovery scope of the IBM® Business Automation
Workflow production
environment.

In the examples in the topics in this section, Db2 is the underlying
database type.

## Installation

For the database installation in the primary environment, follow the instructions in the IBM Db2
installation manual to install and create the Db2 instance and related database users.

1. Install Db2 with the same installation path and instance name as in the primary environment.
2. Use the same user names and passwords used by Db2 in the system.

## Configuration

The database configuration
involves the creation of the database and table space.

1. Manually create all the necessary databases for the environment.
2. Set the database path to the directory that is mounted on the
NFS server.

For the secondary environment, mount the same directory
of the database server on the NFS server. No configuration is required
before restoration.