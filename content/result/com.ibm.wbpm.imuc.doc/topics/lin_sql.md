# Configuring profiles and creating a network deployment environment on Linux

- Creating profiles, deployment environments, and databases simultaneously using the BPMConfig command

Use the BPMConfig command to create profiles and deployment environments. During this process, database scripts are generated, which you must run to create the tables for the databases.
- Configuring your environment with the IBM Business Automation Workflow Configuration editor

The IBM® Business Automation Workflow Configuration editor is a browser-based interface for configuring your new deployment environment. You can graphically edit the configuration properties file that was exported from your source environment by the BPMConfig -export command. After you modify the properties file in the editor, you can use the BPMConfig -create command to create a new deployment environment that is based on the modified file.
- Configuring the profiles and network deployment environment using multiple tools (deprecated)

You can use multiple tools to configure the profiles and the network deployment environment. You can use the manageprofiles command-line utility or the Profile Management Tool to create or augment the network deployment profiles, and the Deployment Environment wizard to create the network deployment environment. If you want to create the deployment manager and managed-node profiles separately from creating the deployment environment, you can use the BPMConfig command.