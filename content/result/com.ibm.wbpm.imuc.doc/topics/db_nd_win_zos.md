# Configuring profiles, databases, and deployment environments
for DB2 for z/OS

## About this task

When configuring databases, the system default table spaces
are used. However, if you want to use scripts that create custom table spaces
for the Business Space and the Messaging components, see the usetablespaces property
as described in the "Topology" section of  Configuration
properties for the BPMConfig command.

- run BPMConfig -create -sqlfiles properties\_file\_name -outputDir output\_directory
- run BPMConfig -create -de properties\_file\_name when bpm.de.deferSchemaCreation is
set to true.

- Creating profiles, deployment environments, and databases simultaneously using the BPMConfig command

Use the BPMConfig command to create profiles and deployment environments. During this process, database scripts are generated, which you must run to create the tables for the databases.
- Configuring your environment with the IBM Business Automation Workflow Configuration editor

The IBM Business Automation Workflow Configuration editor is a browser-based interface for configuring your new deployment environment. You can graphically edit the configuration properties file that was exported from your source environment by the BPMConfig -export command. After you modify the properties file in the editor, you can use the BPMConfig -create command to create a new deployment environment that is based on the modified file.
- Configuring the profiles and network deployment environment using multiple tools (deprecated)

You can use multiple tools to configure the profiles and the network deployment environment. You can use the manageprofiles command-line utility or the Profile Management Tool to create or augment the network deployment profiles, and the Deployment Environment wizard to create the network deployment environment. If you want to create the deployment manager and managed-node profiles separately from creating the deployment environment, you can use the BPMConfig command.