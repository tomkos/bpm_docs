# Creating DB2 for z/OS databases and validating database connections

## Procedure

For each deployment environment that
you are creating, complete the following steps:

1 Create required databases. If you are migrating to a Standard deployment environment : If you are migrating to an Advanced deployment environment : For each database, make any required changes and run the following script: install\_root \BPM\dbscripts\DB2zOS\Create\createDatabase.sql Use the DB2® command line processorto run the createDatabase.sql files on the database server; forexample:db2 -tvf cell\_scoped\_subdir /createDatabase.sql db2 -tvf cluster\_scoped\_subdir /createDatabase.sql
    - Create a database for Business Space if you did not have one in the source environment.
    - Create a messaging engine database if you want to use a single messaging engine bus in the new
environment (recommended). If you want to use multiple buses, you can reuse the previous messaging
engine database and schema.
    - Create a database for Business Space if you did not have one in the source environment.
    - Create a Business Process Choreographer database.
    - Create a messaging engine database if you want to use a single messaging engine bus in the new
environment (recommended). If you want to use multiple buses, you can reuse the previous messaging
engine database and schema.

For each database, make any required changes and run the following script:

```
install\_root\BPM\dbscripts\DB2zOS\Create\createDatabase.sql
```

```
db2 -tvf cell\_scoped\_subdir/createDatabase.sql
```

```
db2 -tvf cluster\_scoped\_subdir/createDatabase.sql
```

2 On the target deployment manager computer,validate that all database connections are correctly configured byrunning the BPMConfig -validate command. Usethe following syntax:target\_install\_root \bin\BPMConfig -validate -db configuration\_properties\_file where The command checks each connection anddisplays a message similar to the following message:A JDBC connection to the 'BusinessSpaceDb' (CMNDB.bpmadmin) has been successfully established.

```
target\_install\_root\bin\BPMConfig -validate -db configuration\_properties\_file
```

- configuration\_properties\_file is the full path
and name of the properties file that you copied over to the target
environment after you extracted information using the BPMConfig
-migrate command. Update the properties in the file for any
new databases that you created.

```
A JDBC connection to the 'BusinessSpaceDb' (CMNDB.bpmadmin) has been successfully established.
```

## Results

After all connections are checked,
you see a message that the BPMConfig -validate command
completed successfully.

## Related information

- BPMConfig command-line utility