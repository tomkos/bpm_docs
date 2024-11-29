# Configuring the profiles and network deployment environment using multiple tools
(deprecated)

- Creating or augmenting network deployment profiles

You must create or augment a deployment manager profile and one or more custom profiles before creating the deployment environment. Using profiles, you can have more than one runtime environment on a system, without having to install multiple copies of IBM® Business Automation Workflow.
- Creating DB2 databases (deprecated)

You can create the required databases for IBM Business Automation Workflow either before or after you create the profiles and the deployment environment.
- Configuring a network deployment environment using the Deployment Environment wizard (deprecated)

After performing a Custom installation and creating the deployment manager and custom (managed node) profiles, you can create a network deployment configuration based on the topology pattern templates packaged with the software.
- Running the generated DB2 database scripts

If you run the BPMConfig command with the property bpm.de.deferSchemaCreation set to true, or if you used the Deployment Environment wizard and cleared the Create Tables option, you must run the generated database scripts manually to create the database tables.