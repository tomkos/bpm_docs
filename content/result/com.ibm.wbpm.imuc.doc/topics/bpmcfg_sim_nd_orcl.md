# Creating profiles, deployment environments, and databases simultaneously
using the BPMConfig command

Use the BPMConfig command to create profiles and deployment
environments. During this process, database scripts are generated,
which you must run to create the tables for the databases.

- Configuring XA transactions for Oracle

You must configure XA transactions after the Oracle database is installed and before you start the server.
- Creating users for Oracle databases

You can create the users for Oracle databases either before or after you run the BPMConfig command with the -create -de parameters to create profiles and configure your deployment environment. Create the cell-scoped user, the deployment environment-level user, the Process database user, the Performance Data Warehouse user, and the three users for the Content database: design object store user, target object store user, and IBM® Content Navigator user. The Process, Performance Data Warehouse, and Content users are not needed for an AdvancedOnly deployment environment.
- Creating profiles, network deployment environments and database tables using the BPMConfig command

You can use the BPMConfig command to create a typical network deployment environment using a properties file that contains all of the values used in the configuration of your deployment environment. At the same time as the deployment environment is created, you can create the required database tables, and create a new deployment manager profile and custom profiles for managed nodes by including settings for these profiles in the properties file used by the BPMConfig command.
- Running the generated Oracle database scripts

If you run the BPMConfig command with the property bpm.de.deferSchemaCreation set to true, or if you used the Deployment Environment wizard and cleared the Create Tables option, you must run the generated database scripts manually to create the database tables.