# Configuring the profiles and network deployment environment using multiple tools
(deprecated)

- Creating or augmenting network deployment profiles (deprecated)

You must create or augment a deployment manager profile and one or more custom profiles before creating the deployment environment. Using profiles, you can have more than one runtime environment on a system, without having to install multiple copies of IBM® Business Automation Workflow.
- Configuring XA transactions for Oracle

You must configure XA transactions after the Oracle database is installed and before you start the server.
- Creating users for Oracle databases (deprecated)

You can create the users for Oracle databases either before or after you create the profiles and the deployment environment. Create the cell-scoped user, the deployment environment-level user, the Process database user, the Performance Data Warehouse user, and the three users for the Content database: design object store user, target object store user, and IBM Content Navigator user. The Process, Performance Data Warehouse, and Content database users are not needed for an AdvancedOnly deployment environment.
- Configuring a network deployment environment using the Deployment Environment wizard (deprecated)

After performing a Custom installation and creating the deployment manager and custom (managed node) profiles, you can create a network deployment configuration based on the topology pattern templates packaged with the software.
- Running the generated Oracle database scripts

If you run the BPMConfig command with the property bpm.de.deferSchemaCreation set to true, or if you used the Deployment Environment wizard and cleared the Create Tables option, you must run the generated database scripts manually to create the database tables.