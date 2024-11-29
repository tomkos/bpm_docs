# Configuring your environment with the IBM Business Automation
Workflow Configuration editor

## Before you begin

- SUSE Linux Enterprise Server 11 SP1 or later
- Red Hat Enterprise Linux Server 6.0 or later

```
install\_root/ojdbc
```

## About this task

<!-- image -->

| Label   | Part                   | Description                                                                                                                                                                                                                                                                                                                                                                                  |
|---------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A       | Topology               | Edit the properties of all available components, such as cells, nodes, and deployment environments. Some properties were automatically modified during export and others require manual input. Components that are incorrectly configured are shaded gray. Properties that have missing or invalid values are surrounded with a red border and are flagged with a red exclamation mark icon. |
| B       | Security               | Edit the properties for LDAP. Edit the customizations from WebSphere® Lombardi Edition files, including Process Admin Console, Workflow Server, and other custom properties. The information that you see on this tab depends on your source configuration.                                                                                                                                  |
| C       | Performance            | Edit the properties for data sources, thread pools, activation specifications, work managers, JVM settings, connection factories, ORB data, web containers, and messaging engines.                                                                                                                                                                                                           |
| D       | CaseManagement         | Edit the properties for case management.                                                                                                                                                                                                                                                                                                                                                     |
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
    1. Extract the BPMConfigurationEditor.zip configuration editor package to a
directory.
The package is in install\_root/BPM/config/ui/.
    2 Make sure that the following files in the package are executable:
        - install\_root/BPM/config/ui/configEditor.sh
        - install\_root/BPM/config/ui/validation/validate.sh
3. Edit the configEditor.ini file to set the JAVA\_HOME
location. You can optionally change the port that the editor uses.

If you do not change the port, the default port 8888 is used. However, if
you run the configEditor command and port 8888 is
already being used by a different process, you will receive the error Error: listen
EADDRINUSE. If you receive the error, you can either stop the process that is already
using port 8888 or you can specify a new port number in the
configEditor.ini file (such as port 9999).
4 Start the server.
    - In the directory where the configEditor.sh executable is located, run the
configEditor.sh command. The BPMConfigEditor.log file is
written to the same directory where you run the command.
5 If a browser does not automatically open to run the configuration editor, manually open abrowser. The configuration editor allows only local access. On the computer where the editor isinstalled, specify the following URL: Change the port number if you changed it in the configEditor.ini file.

- Pre-19.0.0.1: http://localhost:8888/ibm/bpm/configEditor
- https://localhost:8888/ibm/bpm/configEditor
2. Click Browse and select
the properties file that was created when you ran BPMConfig
-export.
For example, DE1-Advanced-PS-SingleCluster-DB2.properties.
Click Open Editor to
start configuring your new environment.
3 Configure your target environment. Note: The value of the deployment environment type must be Process Center (PC) (forWorkflow Center) or Process Server (PS) (for Workflow Server).

- Keep track of the database properties that you choose when you are adding new database
capabilities. You will create the required new databases in the next step.Tip: In
Business Automation Workflow
24.x, the common
database is split into two pieces. One is cell-scoped and is used for the entire cell. The other,
which includes event sequencing and the failed event manager, is deployment-environment-scoped, and
must be configured for each deployment environment.
- The target environment will use the same databases as the source environment unless
you change the defaults. If you are using cloned databases, back up the exported
BPMConfig properties file so that you can restore the correct database properties
after you finish. Then, update the database information in the file to use the cloned
databases.
- Set the bpm.dmgr.jdbcDriverPath
property to point to the custom JDBC driver path where your JDBC driver is installed. There is no
default value and you must specify the path, for example,
install\_root/ojdbc.
- If you are using a customized URL for an Oracle database in your source environment,
the URL will be exported. You can check the value for each database capability in the databases area
of the editor on the Advanced Options tab. Update the Database
URL value if needed, or set the Database and
Host on the Basic Options tab instead. Either the
Database URL property or the Database and
Host properties must be empty.
- If you use a file-based user registry in the source environment, use the same
primary administrative user name for the cell administrator as you used in the source environment.
Reusing the administrative user name as the cell administrator ensures that the data in the database
has the same security context and can still work with the same user after exportation.
- If you are exporting more than one deployment environment, make sure that the name
of the authentication alias for each database is different if there is a different user name in each
deployment environment. Otherwise, the creation of the second deployment environment will fail
because the authentication alias uses a different user name. For example, your first deployment
environment has the authentication alias BPM\_DB\_ALIAS with
user1 as the user
name.bpm.de.authenticationAlias.3.name=BPM\_DB\_ALIAS
bpm.de.authenticationAlias.3.user=user1
bpm.de.authenticationAlias.3.password=
Before
you create the second deployment environment, check the BPMConfig properties file
to make sure that the same authentication alias does not exist with a different user name. If so,
change the name of the authentication alias. For
example:bpm.de.authenticationAlias.3.name=BPM\_DB\_ALIAS\_2
bpm.de.authenticationAlias.3.user=user2
bpm.de.authenticationAlias.3.password=
- Fix all validation errors to ensure a correct and complete target
environment.
- Click Save to save the configuration properties file.Important:  Save the properties file to the same location (where you created it when you ran
BPMConfig -export), because there are cross-references between it and other
exported configuration files. If you cannot save the file in the same location using the same name
as the exported properties file, you should edit the output properties file and change the name and
location manually.
Tip:  If you see an error that is similar to
properties\_file can't be downloaded, click
Retry to save the file.

## What to do next

- Pre-19.0.0.1: http://localhost:port\_number/bye
- https://localhost:port\_number/bye