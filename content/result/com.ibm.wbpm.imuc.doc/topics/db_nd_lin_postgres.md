# Configuring profiles, databases, and Standard deployment environments for PostgreSQL

- Creating PostgreSQL databases

You can create the required databases for IBM Business Automation Workflow either before or after you run the BPMConfig command with the -create -de parameters to create profiles and configure your deployment environment.
- Creating profiles, network deployment environments and database tables using the BPMConfig command

You can use the BPMConfig command to create a typical network deployment environment using a properties file that contains all of the values used in the configuration of your deployment environment. At the same time as the deployment environment is created, you can create the required database tables, and create a new deployment manager profile and custom profiles for managed nodes by including settings for these profiles in the properties file used by the BPMConfig command.
- Running the generated PostgreSQL database scripts

If you run the BPMConfig command with the property bpm.de.deferSchemaCreation set to true you must run the generated database scripts manually to create the database tables.
- Configuring your environment with the IBM Business Automation Workflow Configuration editor

The IBM Business Automation Workflow Configuration editor is a browser-based interface for configuring your new deployment environment. You can graphically edit the configuration properties file that was exported from your source environment by the BPMConfig -export command. After you modify the properties file in the editor, you can use the BPMConfig -create command to create a new deployment environment that is based on the modified file.