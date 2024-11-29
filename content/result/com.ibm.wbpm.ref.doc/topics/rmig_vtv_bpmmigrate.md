# BPMMigrate command-line utility

- Installs your applications in the target environment
- Syncs the managed nodes
- Runs the command to move the SIB messages from the source environment to the target
environment
- Runs the command to re-create the scheduler tasks
- Updates the WebSphere Adapters

## Prerequisites

- The user name and password are taken from the migration.properties file.
The user name must have various WebSphere privileges. The WebSphere
primary administrative user has them all. In the source environment,
you can find the primary administrative user name in the administrative
console by going to Users and Groups > Administrative user roles. In
the target environment, if you do not have access to the administrative
console, you can find  bpm.de.authenticationAlias.#.name=CellAdminAlias in
the BPMConfig properties file. Use the user name
and password for that alias.

## Location

The BPMMigrate command-line utility is in the
install\_root\_24.x/bin
directory.

The log file is in snapshot\_folder/logs.

## Syntax

```
BPMMigrate 
-backupFolder snapshot\_folder 
-propertiesFile target\_migration\_properties\_file
```

## Parameters

You
must check all the target properties in this file and edit them if required.

## Examples

- BPMMigrate -backupFolder /tmp/snapshot -propertiesFile /opt/BPM24.x/util/migration/resources/target\_migration.properties
- BPMMigrate -backupFolder C:\snapshot -propertiesFile "C:\BPM 24.x\util\migration\resources\target\_migration.properties"

- Edit install\_root/bin/wsadmin.sh.
Find PERF\_JVM\_OPTIONS and increase the value of -Xmx256m to
-Xmx512m.
- Edit install\_root\bin\wsadmin.bat.
Find PERFJAVAOPTION and increase the value of -Xmx256m to
-Xmx512m.

- Sample migration.properties files

During migration, you create two migration properties files and call them source\_migration.properties and target\_migration.properties. You update them with information about the source (existing) environment and then with information about the target (new) environment.