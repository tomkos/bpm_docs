# DBUpgrade troubleshooting

Change the log level to FINEST as described in "Troubleshooting
migration." After you run the command again, check the log file named DBUpgrade\_timestamp.log.
The file is found in deployment\_manager\_profile/logs/.
If you cannot find the cause of the problem, you can provide the log
to IBM support.

The command reads topology information from
the properties file specified by the target.config.property.file property
in the target\_migration.properties file. The
command reads database information from the WebSphere® Application
Server data source,
so if you find that the wrong database connection is used when you
run DBUpgrade, check that the data source configuration
is correct.

## DB2 SQL error

```
Error executing SQL statement: DB2 SQL Error: SQLCODE=-964, SQLSTATE=57011, SQLERRMC=null
```

## Database customizations

```
ORA-01408: such column list already indexed
```

## Not enough disk space to run the command

If
you have a large amount of data, you might run out of disk space when
you run the DBUpgrade command. This command migrates
the BLOB data in the LSW\_BPD\_INSTANCE\_DATA, LSW\_TASK\_EXECUTION\_CONTEXT table,
and also reorganizes the database. It requires about twice as much
disk space as the original database.

```
Executing upgrade step: Enable LOGGED for LOB columns
Error executing SQL statement: DB2 SQL Error: SQLCODE=-2216, SQLSTATE=01H52, SQLERRMC=-289, DRIVER=4.11.69
SQL statement that failed: call sysproc.admin\_cmd('reorg table LSW\_BPD\_INSTANCE\_DATA')
```

```
java.sql.BatchUpdateException: ORA-01653: unable to extend table schema\_name.LSW\_TASK\_EXECUTION\_CONTEXT by 1024 in tablespace tablespace\_name
```

## Out-of-memory error

- To increase the heap size of DBUpgrade, you can configure it in
the install\_root/util/dbUpgrade/upgrade.properties file.
For example:JVM\_HEAPSIZE\_OPTIONS="-Xms512m -Xmx2048m"
$JAVA\_EXE $JVM\_HEAPSIZE\_OPTIONS -cp $CLASSPATHOr, you
can increase the heap size as follows when you create the Java process.
For example:%JAVA\_HOME%\bin\java" -Xms512m -Xmx2048m
- To decrease the number of records to be updated as a batch, configure
the value of database.batch.size in the install\_root/util/dbUpgrade/upgrade.properties file.
For example: database.batch.size=1000Lowering
the value requires less memory but also lowers performance.

## Low performance

1. Open the install\_root/util/dbUpgrade/upgrade.properties file.
2. Increase the value of the worker.thread.size property. By default, the value is
4. The maximum number of threads depends on the processor number of the operating system that has
IBM® Business Automation Workflow installed.

## Manually running the schema upgrade for the Process Server and Performance Data
Warehouse databases

1. Open the upgradeSchema\_ProcessServer.sql file in
target\_deployment\_manager\_profile/dbscripts/Upgrade/cell\_name.de\_name/database\_type/Process\_Server\_database\_name.
2. Find the phases in the file that correspond to your source. Each phase starts with /*
START of phase ProcUpgradeToversion */ and ends with /* END of phase
ProcUpgradeToversion */. For example, if your source version is V7.5.1, the database is
upgraded to V8.0.0 first, and then to V8.0.1, V8.5.0, V8.5.5, and finally V8.5.6. In that case, you
must copy the SQL statements from /* START of phase ProcUpgradeTo751 */ to the end
of the file.
3. Run the SQL statements in your preferred database tool to perform all the database schema
updates.
4. Open the upgrade.xml file in
install\_root/util/dbUpgrade. Search in the file for
<sysproperty key="data.upgrade" value="false" />By default, the value of
the data.upgrade property is false, which means that both schema and data are
upgraded. If the database schema has already been upgraded manually and you want to upgrade the data
only, change this value to true before you run the DBUpgrade
command. DBUpgrade will skip the schema upgrade and do the data upgrade
only.