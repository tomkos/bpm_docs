# Configuring your environment graphically with the IBM Business Automation
Workflow Configuration editor

## Before you begin

- SUSE Linux Enterprise Server 11 SP1 or later
- Red Hat Enterprise Linux Server 6.0 or later

```
temp/jdbcdrivers/Oracle
```

## About this task

<!-- image -->

| Label   | Part                   | Description                                                                                                                                                                                                                                                                                                                                                                                  |
|---------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A       | Topology               | Edit the properties of all available components, such as cells, nodes, and deployment environments. Some properties were automatically modified during export and others require manual input. Components that are incorrectly configured are shaded gray. Properties that have missing or invalid values are surrounded with a red border and are flagged with a red exclamation mark icon. |
| B       | Security               | Edit the properties for LDAP. Edit the customizations from WebSphere® Lombardi Edition files, including Process Admin Console, Workflow Server, and other custom properties. The information that you see on this tab depends on your source configuration.                                                                                                                                  |
| C       | Performance            | Edit the properties for data sources, thread pools, activation specifications, work managers, JVM settings, connection factories, ORB data, web containers, and messaging engines.                                                                                                                                                                                                           |
| D       | CaseManagement         | Edit the case management properties.                                                                                                                                                                                                                                                                                                                                                         |
| E       | Summary                | Scroll through all available properties before you save the configuration properties file. Make further edits.                                                                                                                                                                                                                                                                               |
| 1       | Cell                   | Edit the cell properties, such as the cell name. Map the cell administrator role to an authentication alias.                                                                                                                                                                                                                                                                                 |
| 2       | Deployment environment | Edit the deployment environment properties, such as the Business Automation Workflow type. For Workflow Server, you can also change the Workflow Center connectivity properties.                                                                                                                                                                                                             |
| 3       | Databases              | Edit the database properties or map database roles to user aliases.                                                                                                                                                                                                                                                                                                                          |
| 4       | Deployment manager     | Edit the deployment manager properties, such as the host name, node, profile name, and SOAP port.                                                                                                                                                                                                                                                                                            |
| 5       | Node                   | Edit the properties for each node, such as the node name, host name, port, and profile name.                                                                                                                                                                                                                                                                                                 |
| 6       | Cluster                | Edit the properties for each cluster.                                                                                                                                                                                                                                                                                                                                                        |
| 7       | Cluster member         | Edit the properties for each cluster member.                                                                                                                                                                                                                                                                                                                                                 |
| 8       | Aliases                | Edit the authentication alias mappings for the deployment environment administrator, database administrator, and other aliases to users and passwords.                                                                                                                                                                                                                                       |
| 9       | Bus                    | Edit the bus properties, such as the databases that they refer to.                                                                                                                                                                                                                                                                                                                           |
| 10      | Validation messages    | Correct incomplete or incorrect properties by clicking the messages in this table.                                                                                                                                                                                                                                                                                                           |

## Procedure

1 To install the IBM Business AutomationWorkflow Configuration editor, complete the following steps:
    1. Extract the BPMConfigurationEditor.zip configuration
editor package to a directory. The package is in install\_root/BPM/config/ui/.
    2 Make sure that the following filesin the package are executable:
        - install\_root/BPM/config/ui/configEditor.sh
        - install\_root/BPM/config/ui/validation/validate.sh
3. Edit the configEditor.ini file
to set the
JAVA\_HOME location.
For example, JAVA\_HOME=/opt/IBM/BPM/java/jre.

 You can optionally change the port that the editor uses. If you
do not change the port, the default port 8888 is
used. However, if you run the
configEditor command and port 8888 is
already being used by a different process, you will receive the error Error:
listen EADDRINUSE. If you receive the error, you can
either stop the process that is already using port 8888 or
you can specify a new port number in the
configEditor.ini file (such as port 9999).
4 Start the server.
    - In the directory where the configEditor.sh executable
is located, run the
configEditor.sh command. The BPMConfigEditor.log file
is written to the same directory where you run the command.
5 If a browser does not automaticallyopen to run the configuration editor, manually open a browser. Theconfiguration editor allows only local access. On the computer wherethe editor is installed, specify the following URL: Change the port number if you changed it in the configEditor.ini file.

- Pre-19.0.0.1: http://localhost:8888/ibm/bpm/configEditor
- https://localhost:8888/ibm/bpm/configEditor
2. Click Browse and select
the properties file that was created when you ran BPMConfig
-migrate.
For example, DE1-Standard-PS-SingleCluster-DB2.properties.
Click Open Editor to
start configuring your new environment.
3 Configure your target environment. Note: The value of the deployment environment type must be Process Center (PC) (forWorkflow Center) or Process Server (PS) (for Workflow Server). Click Save to save the configuration properties file.

- Keep track of the database properties that you choose when you are adding new database
capabilities. You will create the required new databases in the next step.Tip: In
Business Automation Workflow V22.01, the
common database is split into two pieces. One is cell-scoped and is used for the entire cell. The
other, which includes event sequencing and the failed event manager, is
deployment-environment-scoped, and must be configured for each deployment environment.
- The target environment will use the same databases
as the source environment unless you change the defaults. If you are
using cloned databases to test migration, back up the exported
BPMConfig properties file so that you can restore
the correct database properties after you finish and test the migration.
Then, update the database information in the file to use the cloned
databases.
- If you are using an Oracle or
SQL Server database, set the JDBC driver path (the bpm.dmgr.jdbcDriverPath property)
to point to the custom JDBC driver path where your JDBC driver is
installed. For DB2, the default value is
${WAS\_INSTALL\_ROOT}/jdbcdrivers/DB2. For Oracle
and SQL Server, there is no default value and you must specify the
path, for example,
temp/jdbcdrivers/Oracle.
- For Oracle, if you are using a customized URL for an Oracle database in your source
environment, the URL will be migrated. You can check the value for each database capability in the
databases area of the editor on the Advanced Options tab. Update the
Database URL value if needed, or set the Database Host
and Port on the Basic Options tab instead. Either the
Database URL property or the Database Host and
Port properties must be empty, but the Database Name
property must always be set. If you are migrating from a release earlier than IBM Business
Process Manager V8.0 and you are using an Oracle database with the service name feature enabled, you
should clear the Database URL property and set the Database
Host and Port properties instead, to have the default SCAN format
database URLs created in the Business Automation Workflow
configuration.
- If you are migrating more than one deployment environment,
make sure that the name of the authentication alias for each database
is different if there is a different user name in each deployment
environment. Otherwise, the creation of the second deployment environment
will fail because the authentication alias uses a different user name. For
example, your first deployment environment has the authentication
alias BPM\_DB\_ALIAS with
user1 as the user name.bpm.de.authenticationAlias.3.name=BPM\_DB\_ALIAS
bpm.de.authenticationAlias.3.user=user1
bpm.de.authenticationAlias.3.password=
Before you
create the second deployment environment, check the BPMConfig properties
file to make sure that the same authentication alias does not exist
with a different user name. If so, change the name of the authentication
alias. For example:bpm.de.authenticationAlias.3.name=BPM\_DB\_ALIAS\_2
bpm.de.authenticationAlias.3.user=user2
bpm.de.authenticationAlias.3.password=
- In IBM Business AutomationWorkflow ,you can only use the following characters in a deployment environmentname: If you migrate a pre-8.5.0.0 IBM Business Process Manager deploymentenvironment to IBM Business AutomationWorkflow ,you must ensure that the name of the new deployment environment onlyuses permitted characters. Although you can export a pre-8.5.0.0 deploymentenvironment that has unpermitted characters in the name, you willneed to rename the deployment environment when you use the BPMConfig commandto create the new deployment environment. If the new deployment environmentname contains unpermitted characters, you may see an error messagein the Validation messages pane.
    - a - z
    - A - Z
    - 0 - 9
    - ! ( ) - . ? [ ] \_ ` ~ \ /
- Make sure that any special characters in the user nameand password of your source environment are supported by the new version.Modify the user name and password if necessary. They must containonly the following characters: Tip: It is recommended that you use the same username for the deployment environment administrator authentication alias(DeAdminAlias) as for the BPMAdmin\_Auth\_Alias (tw\_admin). Choose anew user for the cell administration authentication alias (CellAdminAlias),which is used for WebSphere ApplicationServer administration.The password does not need to be the same as it was in your sourceenvironment.

- a - z
- A - Z
- 0 - 9
- ! ( ) - . \_ ` ~ @
- If your source environment is configured for
a web server or load-balancing server, the generated properties file
has entries for bpm.de.processServer. In the
editor, these properties are on the Security tab
in Process Server customized properties. For
example:bpm.de.processServer.processAdminPrefix=https://mzwin7-bpm1/ProcessAdmin
bpm.de.processServer.teamworksWebAppPrefix=https://mzwin7-bpm1/teamworks
bpm.de.processServer.clientLink=https://mzwin7-bpm1/teamworks
bpm.de.processServer.commonPortalPrefix=https://mzwin7-bpm1/portalYou
must change these URLs to match the target environment. If you are
not sure what the new URLs are, delete these entries in the property
file or remove them in the editor. After the migration is complete,
follow the standard procedure for configuring the web server.
- Fix all validation errors to ensure a correct and
complete target environment.

- By default, IBM Case
Manager uses an Embedded
ECM. You also have the option of using an external ECM system instead of the embedded ECM.Important:  Save the properties file to the same location (where you created it when you ran
BPMConfig -migrate), because there are cross-references between it and other
exported configuration files. If you cannot save the file in the same location using the same name
as the exported properties file, you should edit the output properties file and change the name and
location manually.
Tip:  If you see an error that is similar to
properties\_file can't be downloaded, click
Retry to save the file.

## What to do next

- Pre-19.0.0.1: http://localhost:port\_number/bye
- https://localhost:port\_number/bye

## Related information

- Configuration properties for the BPMConfig command