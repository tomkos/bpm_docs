# Creating profiles, deployment environments, and databases simultaneously
using the BPMConfig command

Use the BPMConfig command to create profiles and deployment
environments. During this process, database scripts are generated,
which you must run to create the tables for the databases.

- Creating DB2 databases

You can create the required databases for IBM® Business Automation Workflow either before or after you run the BPMConfig command with the -create -de parameters to create profiles and configure your deployment environment.
- Creating profiles, network deployment environments and database tables using the BPMConfig command

You can use the BPMConfig command to create a typical network deployment environment using a properties file that contains all of the values used in the configuration of your deployment environment. At the same time as the deployment environment is created, you can create the required database tables, and create a new deployment manager profile and custom profiles for managed nodes by including settings for these profiles in the properties file used by the BPMConfig command.
- Running the generated DB2 database scripts

If you run the BPMConfig command with the property bpm.de.deferSchemaCreation set to true, or if you used the Deployment Environment wizard and cleared the Create Tables option, you must run the generated database scripts manually to create the database tables.