# Moving the deployment environment

## Procedure

To move the deployment environment to new hardware, complete
the following steps:

1. Export the configuration from the current deployment environment.
BPMConfig –export –profile profile\_name -de de\_name -outputDir output\_directoryImportant: Specify a different output directory for each deployment
environment. In the case where a cell has multiple deployment environments,
a unique output directory is required for each deployment environment.
The
output directory contains files similar to the following files, based
on your deployment environment type.
Table 1. Configuration files for each deployment
environment

Sample name
Description

DE\_name.properties
This properties file contains the configuration properties from your source
environment. You use this file when you configure the target environment. For more information about
the configuration properties, see the topic Configuration properties for the BPMConfig command.

fileRegistry.xml
If you use a file-based user registry, the user registry file is copied from
the source environment to be added to the target environment.

ltpa.jceks
If you use LTPA, the LTPA key file is copied from the source environment to be
added to the target environment.

ldap\_additional\_properties.xml
If you use a federated repository and an unencrypted LDAP connection in the
source environment, user-defined additional properties of the LDAP server are copied from the source
environment to the output directory, where they are later used automatically to create the target
environment.Restriction: If you extend the federated repository to use a custom login
property (such as userPrincipalName) in addition to the default
uid property in the source environment, LDAP is not configured for the target
environment, with the following warning: CWMCB0600W: LDAP could not be configured! You may
configure LDAP separately after BPMConfig has terminated successfully. If you see this
warning, manually configure LDAP with the login properties you want to use after the migration is
complete.

ProcessServer\_100SourceCustomMerged.xml and
PDW\_100SourceCustomMerged.xml
If you have XML configuration properties files, they are copied from the
source environment. The exported configuration files are merged and renamed to
101CustomMigrated.xml in the target environment.

Application-config-bpc.xml and
resources-bpc.xml
If you have Business Process Choreographer that are configured in the source
environment, the configuration files are copied from the source environment to the output directory,
where they are later used automatically to create the target environment.

Support-config-bpc.xml
If you have Business Process Choreographer Archive Manager configured on the
support cluster in the source environment, the configuration is copied from the source environment
to the output directory, where it is later used automatically to create the target
environment.

In addition
to the information exported by the BPMConfig –export command,
you can use the exportWASConfig.py script to export
other WebSphere® Application
Server configuration
from your source environment to refer to when you create your new
deployment environment.
2 Use the IBM Business AutomationWorkflow Configuration editorto update the exported properties file to match your requirements for the new deploymentenvironment. Make sure the file matches the environment on the new hardware, including the following properties: See the instructions in Configuring your environment with the IBM Business Automation Workflow Configuration editor . Notes: The created deployment environment will have the same topology as your sourceenvironment, such as environment type, cluster number, and node number.
    - Host name of the deployment manager and the nodes
    - Installation path
    - Environment type
    - Database properties. If you are not moving your Business Automation Workflow databases, you do not need to update any
database properties. However, if you are moving the databases, you must update the connection
properties. In either case, you must keep the database schema names and database user names.
    - Keep the same cell name, database schema names, and database user names.
    - Keep the same cell administrator/password and deployment environment administrator/password.
    - Keep the same application cluster name if you are moving an Advanced or AdvancedOnly deployment
environment.
    - Make sure that bpm.de.deferSchemaCreation is set to true in the
properties file.
    - If possible, use the same LDAP server as the source environment.
    - By default, IBM Case
Manager uses an Embedded
ECM. You also have the option of using an external ECM system instead of the embedded ECM.
3. Save the updated properties file, keeping it in the same
output directory. Copy the output directory to the new hardware that
you want to move to.
4. Install the same version of IBM Business Automation Workflow on all
the new servers designated for the nodes and the deployment manager.
5 On the new deployment manager system, validate that all database connections are correctlyconfigured by running the BPMConfig -validate command. Use the followingsyntax:target\_install\_root /bin/BPMConfig -validate -db configuration\_properties\_file where The command checks each connection and displays a message similar to the followingmessage:A JDBC connection to the 'BusinessSpaceDb' (CMNDB.bpmadmin) has been successfully established. After all connections are checked, you see a message that the command completed successfully.

```
target\_install\_root/bin/BPMConfig -validate -db configuration\_properties\_file
```

- configuration\_properties\_file is the full path and name of the properties
file that you copied over to the target environment.

```
A JDBC connection to the 'BusinessSpaceDb' (CMNDB.bpmadmin) has been successfully established.
```

6. Create the deployment environment on the new deployment manager system by running the
BPMConfig -create command.

BPMConfig –create –de output\_directory/updated\_properties\_file
If any of the new nodes is not on the same physical computer as the new deployment manager, run
the command on the node with the same updated properties file.

A new deployment environment is created on the new hardware with the configuration
information that you specified.

## Related information

- exportWASConfig.py script