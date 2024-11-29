# Using the IBM Business Automation Workflow data
collector

## About this task

```
profile\_root/bin/bpmdc
```

```
C:/MyProfileDirectory/bin/bpmdc -prefix=TS123456789
```

- After an issue occurs, you can use the basic bpmdc command
to compress the log files for the profile into a .zip file.
- You can re-create an issue by setting a trace string using the
administrative console or the wsadmin command,
and then run the bpmdc command to collect the logs
and send them to IBM.
- After opening a case, you can use the bpmdc -prefix=caseNumber command with
the most relevant type options to prepend the caseNumber number to the collected data file.
- IBM Support provides a specific command or set of commands to
run for your environment that obtains the needed data.
- IBM Support provides a trace string that must be gathered with the commands. With trace enabled,
you can re-create the issue or wait for a recurrence before running the provided commands to gather
and upload the data to IBM.

| Command line parameter   | Default value          | Description                                                                                                                           |
|--------------------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| prefix                   | None                   | prefix | None | The case number that is associated with the data, such as TS123456789.                                                |
| outputDirectory          | install\_root/BPM/isadc | The path to the directory where the output collection .zip file will be stored.                                                       |
| type                     | General                | The type of collection to run. The valid values are General, Install, Dump, or TableDump.                                             |
| config                   | no                     | With a general collection, when you set this parameter to yes, the config directory is included. You can set this value to yes or no. |
| help                     | No values              | When you include this parameter with the command, a description of the command options is displayed.                                  |

| Command line parameter   | Default value   | Description                                                             |
|--------------------------|-----------------|-------------------------------------------------------------------------|
| server                   | None            | The server from which you want to collect JVM dumps.                    |
| soapport                 | None            | The SOAP port for the server.                                           |
| user                     | None            | The user with wsadmin access to the server to which you are connecting. |
| password                 | None            | The password for the user.                                              |

| Command line parameter   | Default value   | Description                                                                                                                                                                                                                              |
|--------------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dumptype                 | Thread          | The type of Java™ virtual machine (JVM) dump to trigger:  Thread - Javacore or thread dump. Heap - Heap dump. System - System dump, with JExtract run on it before the upload. This type can take some time, depending on the heap size. |
| count                    | 1               | The number of JVM dumps to trigger during the collection.                                                                                                                                                                                |
| interval                 | 0               | The number of JVM dumps to trigger during the collection.                                                                                                                                                                                |

| Command line parameter   | Default value   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dbname                   |                 | The name of the database or instance to which you want to connect for the TableDump type. It is optional for Oracle databases.                                                                                                                                                                                                                                                                                                                  |
| dbUserdbPassword         |                 | The user name and password for accessing the database tables for the TableDump type. The user name and password are optional because the data collector by default pulls the details from the data source entities that are defined for the workflow server. The user name and password might be required if the system has a unique permission set. If the database being used is an Oracle database, the user name and password are required. |
| component                |                 | The option to specify the workflow component name for the TableDump type.                                                                                                                                                                                                                                                                                                                                                                       |
| queryFile                |                 | The option to specify the custom query file path that is used to specify tables for the TableDump. It cannot be used together with the component or tableNames option. Ensure that you have the correct database schema name for the tables that you are collecting. A sample query file is found at the following location:BPM/isadc/util/components/Query.txt                                                                                 |
| tableNames               |                 | The option to specify tables for the TableDump type. It cannot be used together with the queryFile or component option. You can include multiple table names that are separated by a comma and enclosed in double quotation mark characters. For example:-tableNames="Table1,Table2"                                                                                                                                                            |
| delim                    | ,               | The option to specify a delimiter for an exported comma-separated value (CSV) for the TableDump type. The character must be enclosed in double quotation marks (" ").                                                                                                                                                                                                                                                                           |
| clusterName              |                 | The option to specify the cluster name of the environment for the TableDump type.                                                                                                                                                                                                                                                                                                                                                               |

You can run the command without any parameters, in
which case the general collection is run and the
log directory is compressed into a .zip file.

The output file name has the following format:
prefix.ProfileName\_type\_timeStampValue.zip

- Profile logs directory (profile\_root/logs).
The collected files include all of the server log files and traces
under this profile directory.
- The results of the versionInfo -maintenancePackages command.
- Optionally, the profile\_root/config directory.
This directory is collected only when the -config=yes option
is used.

- Any temporary launchpad log files
- Installation Manager data directory
- The results of the versionInfo -maintenancePackages command
- Installation logs directory
- Profile logs directory
- Database upgrade script log files
- Various configuration files that are related to the installation process

With the provided server
connection options, the command will connect to the server using the
SOAP port to make a wsadmin connection with the user and password.
Depending on the dump type, it will trigger various JVM dumps until
the count number is reached. The dumps are triggered a set number
of seconds apart based on the interval that is set.

The Dump collection
gathers general collection files such as /logs and
version information, in addition to dump files such as javacores,
heap dumps, and system dump .zip files.