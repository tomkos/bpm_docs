# Creating profiles, deployment environments, and databases simultaneously
using the BPMConfig command

Use the BPMConfig command to create profiles and deployment
environments. During this process, database scripts are generated,
which you must run to create the tables for the databases.

- Creating profiles, network deployment environments and database tables using the BPMConfig command

You can use the BPMConfig command to create a typical network deployment environment using a properties file that contains all of the values used in the configuration of your deployment environment. At the same time as the deployment environment is created, you can generate the scripts for creating the required database tables, and create a new deployment manager profile and custom profiles for managed nodes by including settings for these profiles in the properties file used by the BPMConfig command.
- Creating and configuring DB2 for z/OS databases after network deployment profile creation

After creating or augmenting profiles, you or your database administrator must create the databases and their tables manually, and you must also run the bootstrapProcessServerData command before you try to start or use the IBM® Business Automation Workflow server.
- Granting table privileges to the JCA authentication alias user ID

If the schema name you are using is not the same as the JCA authentication alias user ID, you must grant a subset of DB2® for z/OS® privileges to the JCA authentication alias user ID.