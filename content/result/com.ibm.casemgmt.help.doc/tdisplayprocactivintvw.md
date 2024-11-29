# Enabling the widget to display process activities

## Before you begin

1. Download and install Business Automation Workflow V20.0.0.1
and its interim fixes, and configure your working environment. If the Business Automation Workflow environment is configured with an external
Content Platform Engine, the minimum required version for Content Platform Engine is V5.5.5.
2. Ensure that you use the latest versions of the emitter and script.
3. Ensure that the following files exist:

File name
Location

CHEventEmitter.war
workflow\_install\_root/CaseManagement/analytics

EnableCH.py
workflow\_install\_root/CaseManagement/analytics

CHEmitterConfig.properties
workflow\_install\_root/CaseManagement/analytics

## About this task

The Case History event emitter emits Business Automation Workflow process events, which
are processed by the Case History server. After the events are processed, Business Automation Workflow process activity
details can be viewed in the Case History Visualizer timeline.

- Installing Case History Emitter
- Updating the Case History emitter application
- Syntax of the EnableCH.py script
- Updating the Case History emitter configuration property values

## Installing Case History Emitter

### About this task

Use the EnableCH.py script to install the Case History emitter application.
For a list of options that are available with EnableCH.py, see Syntax of the EnableCH.py script.

### Procedure

1. Ensure that your Business Automation Workflow environment is
up and running.
2. Update the CHEmitterConfig.properties file. See Updating the Case History emitter configuration property values.
3. Run the following command: 
<Dmgr\_profile\_root>\bin\wsadmin.[bat|sh] -f <Workflow\_Install\_Root>\CaseManagement\analytics\EnableCH.py --enableCH --property=<Workflow\_Install\_Root>\CaseManagement\analytics\CHEmitterConfig.properties
4. Restart your Business Automation Workflow
environment.
5. If your Business Automation Workflow environment is
configured with an externalContent Platform Engine environment,
restart the Content Platform Engine environment after the Business Automation Workflow environment is restarted.

### Results

## Updating the Case History emitter application

### Procedure

1. Make a backup copy of the CHEventEmitter.war and
CHEmitterConfig.properties files that are located in the
<Workflow\_Install\_Root>/CaseManagement/analytics
directory.
2. If more than one deployment environment is available, change the value of the
deploymentEnvironmentName parameter from None to the
name of the deployment environment that you want to update in the
<Workflow\_Install\_Root>/CaseManagement/analytics/CHEmitterConfig.properties
file.
3. Update the application by running the following Jython command: 
<Dmgr\_profile\_root>/bin/wsadmin.[bat|sh] -lang jython -f <Workflow\_Install\_Root>/CaseManagement/analytics/EnableCH.py -u application
4. Optional: If the configuration of the Case History database connection needs
to be updated, run the following Jython command: 
<Dmgr\_profile\_root>/bin/wsadmin.[bat|sh] -lang jython -f <Workflow\_Install\_Root>/CaseManagement/analytics/EnableCH.py -u dbConnection -d <Workflow\_Install\_Root>/CaseManagement/analytics/CHEmitterConfig.properties
5. Restart your Business Automation Workflow
environment. 
Note: If new Case History store database connection information is specified, only Business Automation Workflow process engine events
which start  from the current updated time will be processed by the emitter.

## Syntax of the EnableCH.py script

### About this task

```
wsadmin.(sh|bat) -f EnableCH.py [--enableCH --property=propertyFile] | --update=application | 
--update=dbconnection --property=propertyFile | --help
```

```
wsadmin.(sh|bat) -f EnableCH.py [-e -d propertyFile] | -u application | -u dbconnection -d propertyFile | --help
```

| Parameter                                | Description                                                                                                                                                                                                                                                                                                   |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -e or --enableCH                         | (Optional) Configures the Dynamic Event Framework (DEF) to subscribe to Business Automation Workflow activity events, and installs the CHEventEmitter application to emit Business Automation Workflow process engine events to the Case History store. For details, see the CHEmitterConfig.properties file. |
| -u application or --update=application   | Uses the <Workflow\_Install\_Root>/CaseManagement/analytics/CHEventEmitter.war archive to update the installed CHEventEmitter application.                                                                                                                                                                      |
| -u dbconnection or --update=dbconnection | Updates the application connection information, as specified in the properties file.                                                                                                                                                                                                                          |
| --property=propertyFile                  | Enables you to update the property values in the CHEmitterConfig.properties configuration file.                                                                                                                                                                                                               |
| --help                                   | Displays the parameter documentation.                                                                                                                                                                                                                                                                         |

## Updating the Case History emitter configuration property values

### Procedure

1. Collect details of the Case History store database. The details will be used by CHEventEmitter
to store the Business Automation Workflow activity event
information for further processing by the Case History server.
2 Create a copy of the CHEmitterConfig.properties template file, andedit it to match your needs. Find the CHEmitterConfig.properties template inthe <Workflow\_Install\_Root> \CaseManagement\analytics directory. Refer to the following table for property updates. Table 1. Property values to configurethe Case History emitter Property name Value Description DeploymentEnvironmentName None or a real name The name of the target deployment environment. If only one deployment environment isavailable, you can use None . dbType DB2 or MSSQL or ORACLE orPOSTGRESQL The database server type of the Case History store database. The value can be one of<DB2|MSSQL|ORACLE|POSTGRESQL> . dbServer Database server name The database server name of the Case History store database dbPort Database server port The database server port of the Case History store database dbName Database name The database name of the Case History store dbUser Database user The database username of the Case History store database dbPassword Database password The database password of the Case History store dbPasswordBase64 Database password in base-64 encoded format (Optional) The database password of the Case History store, in base-64 format. The users canprovide either the dbPassword or the dbPasswordBase64 value. dbSchema Database schema name The database schema of the Case History store dbInstance Database instance name (Optional) The database instance of the Case History store. This setting is specific to theMSSQL database server type. dbServiceName Database SID name (Optional) The database SID name of the Case History store. This setting is specific to theOracle database server type. Note: The property values in Table 1 (db*) are used to build a JDBC connection to the database. If youhave more parameters that you would like to specify for the database connection, you can configurethe connection by specifying a JDBC URL manually by using the dbJDBCUrl property:dbJDBCUrl=<JDBC url to connect to db> for example, for Oracle, theJDBC URL would look something like thefollowing: jdbc:oracle:thin:<dbUser>/<dbPassword>@<dbServer>:<dbPort>:<dbServiceName> Limitations:

| Property name             | Value                                       | Description                                                                                                                                               |
|---------------------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| DeploymentEnvironmentName | None or a real name                         | The name of the target deployment environment. If only one deployment environment is available, you can use None.                                         |
| dbType                    | DB2 or MSSQL or ORACLE or POSTGRESQL        | The database server type of the Case History store database. The value can be one of <DB2|MSSQL|ORACLE|POSTGRESQL>.                                       |
| dbServer                  | Database server name                        | The database server name of the Case History store database                                                                                               |
| dbPort                    | Database server port                        | The database server port of the Case History store database                                                                                               |
| dbName                    | Database name                               | The database name of the Case History store                                                                                                               |
| dbUser                    | Database user                               | The database username of the Case History store database                                                                                                  |
| dbPassword                | Database password                           | The database password of the Case History store                                                                                                           |
| dbPasswordBase64          | Database password in base-64 encoded format | (Optional) The database password of the Case History store, in base-64 format. The users can provide either the dbPassword or the dbPasswordBase64 value. |
| dbSchema                  | Database schema name                        | The database schema of the Case History store                                                                                                             |
| dbInstance                | Database instance name                      | (Optional) The database instance of the Case History store. This setting is specific to the MSSQL database server type.                                   |
| dbServiceName             | Database SID name                           | (Optional) The database SID name of the Case History store. This setting is specific to the Oracle database server type.                                  |

```
dbJDBCUrl=<JDBC url to connect to db>
```

```
jdbc:oracle:thin:<dbUser>/<dbPassword>@<dbServer>:<dbPort>:<dbServiceName>
```

    - When using dbJDBCUrl property, all other property values (db*) are
ignored.
    - When using dbJDBCUrl to specify more JDBC parameters, the additional
parameters might be supported by the database vendor, but not by the Case History emitter.