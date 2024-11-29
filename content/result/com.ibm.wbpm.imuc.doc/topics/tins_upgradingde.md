# Upgrading a deployment environment from Standard to Advanced

## About this task

When you run the BPMConfig command to upgrade your deployment environment to Advanced, the
upgrade is based on the properties that are specified in a properties file.

If you added a supported customization to your Standard
deployment environment,
such as a context root prefix or an update to the virtual host mapping, the same customization is
automatically applied to the Advanced
deployment environment during the upgrade. For
example, if you set the bpm.de.contextRootPrefix property and the
bpm.de.virtualHost property in your Standard
deployment environment properties file, the context root and virtual host
mapping of all web modules are automatically updated for the advanced capabilities when the
deployment environment is upgraded.

## Procedure

1 Edit the properties in the properties file that you willuse to upgrade your deployment environment. Sample properties filesthat can be edited and used to upgrade your deployment environmentare found in the following location: install\_root /BPM/samples/config/upgrade When you are specifying the databases that you want to use in the new Advanced deployment environment , you can use your existing Business Automation Workflow databases or you can specify new databases andbuses for the advanced capabilities of the environment. Scripts are provided to generate theresources that are required to support the databases and buses. For example, if you set thebpm.de.deferSchemaCreation property in the properties file tofalse , all of the tables that are required for the advanced environmentcapabilities will be generated automatically in your databases.Notes:

install\_root/BPM/samples/config/upgrade

    - You cannot change the environment type from Workflow Center to Workflow Server (or from Workflow Server to Workflow Center).
    - You cannot change an Advanced
deployment environment to a Standard
deployment environment.
2. Run the following command (where properties\_file is
the name of the properties file that you want to use to upgrade your
deployment environment): 
install\_root/bin/BPMConfig -upgrade -de properties\_file

For
example:

install\_root/bin/BPMConfig -upgrade -de Advanced-DB2.properties

## Related information

- BPMConfig command-line utility
- Upgrading a product installation