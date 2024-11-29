# Creating DB2 databases and validating database connections

## Procedure

For each deployment environment that
you are creating, complete the following steps:

1 Create required databases. If you are migrating to a Standard deployment environment : If you are migrating to an Advanced deployment environment : For each database, make any required changes and run the followingscript:install\_root \BPM\dbscripts\DB2\Create\createDatabase.sql
    - Create a messaging engine database if you want to use a single messaging engine bus in the new
environment (recommended). If you want to use multiple buses, you can reuse the previous messaging
engine database and schema.
    - Create a Business Process Choreographer database.
    - Create a messaging engine database if you want to use a single messaging engine bus in the new
environment (recommended). If you want to use multiple buses, you can reuse the previous messaging
engine database and schema.

```
install\_root\BPM\dbscripts\DB2\Create\createDatabase.sql
```

2 For case management, you must create at least one additional database. Youcan create either one database (CPEDB) or three databases, one for IBM ContentNavigator (ICN), onefor the design object store (DOS), and one for the target object store (TOS). This step assumes thatyou are creating three separate databases.

1. Find the files to create the databases in
install\_root\BPM\dbscripts\DB2\Create.
2 To create the IBM ContentNavigator database,replace the parameters in the following file: createDatabase\_ICN.sql where:

```
createDatabase\_ICN.sql
```

    - @DB\_NAME@ is the database name of the IBM Content Navigator (ICN) database, for example,
ICNDB.
    - @DBUSER@ is the user name for the database.
3. Copy the file to the database computer and run it to create the IBM Content
Navigator
database.

createDatabase\_ICN.sql
4 To create the databases for IBM Enterprise Content Management, using the embedded Content Platform Engine , find the followingdatabase creation files. createDatabase\_ECM.batcreateDatabase\_ECM.sql Make two copies of the files. Name thefiles:createDatabase\_ECM\_DOS.batcreateDatabase\_ECM\_TOS.batcreateDatabase\_ECM\_DOS.sqlcreateDatabase\_ECM\_TOS.sql Replace the parameters with the design object store (DOS)parameters in one file and with the target object store (TOS) parameters in the other file.

```
createDatabase\_ECM.bat
createDatabase\_ECM.sql
```

```
createDatabase\_ECM\_DOS.bat
createDatabase\_ECM\_TOS.bat
createDatabase\_ECM\_DOS.sql
createDatabase\_ECM\_TOS.sql
```

- Use the backslash ("\") to replace the forward slash as the file separator.
- @DB\_NAME@ is the name of the database. For example, the names could be DOSDB and TOSDB.
- @DB\_DIR@ is the data directory of your database, for example, BPMINST/Node0000.Important: Make sure that the @DB\_DIR@\@DB\_NAME@ path already exists on your database
computer. You will use this value when you update the properties file later.
- @ECM\_DATA\_TS@ is the data table space used by the design object store (DOS) or the target object
store (TOS). The default value for DOS is WFDOSDATATS. The default value for TOS is WFTOSDATATS. You
can set these values in the SQL files.
- @ECM\_IDX\_TS@ is the index table space used by DOS or TOS. The default value for DOS is
WFDOSINDEXTS. The default value for TOS is WFTOSINDEXTS. You can set these values in the SQL
files.
- @ECM\_LOB\_TS@, is the LOB table space used by DOS or TOS. The default value for DOS is
WFDOSLOBTS. The default value for TOS is WFTOSLOBTS, You can set these values in the SQL files.
- @DB\_USER@ is the user name for the database.
- @DOS\_SCHEMA@ is the schema for DOS, for example, DOSSA. The name must not be longer than five
characters.
- @TOS\_SCHEMA@ is the schema for TOS, for example, TOSSA. The name must not be longer than five
characters.
5. Copy the following four files to the database computer:

createDatabase\_ECM\_DOS.bat
createDatabase\_ECM\_TOS.bat
createDatabase\_ECM\_DOS.sql
createDatabase\_ECM\_TOS.sql
6. Run the files to create the Enterprise Content Management databases.
For example:createDatabase\_ECM\_DOS.bat
createDatabase\_ECM\_TOS.bat
3 On the target deployment manager computer,validate that all database connections are correctly configured byrunning the BPMConfig -validate command. Usethe following syntax:target\_install\_root \bin\BPMConfig -validate -db configuration\_properties\_file where The command checks each connection anddisplays a message similar to the following message:A JDBC connection to the 'BusinessSpaceDb' (CMNDB.bpmadmin) has been successfully established.

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