# Creating SQL Server databases and validating database connections

## Procedure

For each deployment environment that
you are creating, complete the following steps:

1 Create required databases. If you are migrating to a Standard deployment environment : If you are migrating to an Advanced deployment environment : For each database, make any required changes and run the followingscript:install\_root \BPM\dbscripts\SQLServer\Create\createDatabase\_CaseSensitive.sql
    - Create a messaging engine database if you want to use a single messaging engine bus in the new
environment (recommended). If you want to use multiple buses, you can reuse the previous messaging
engine database and schema.
    - Create a Business Process Choreographer database.
    - Create a messaging engine database if you want to use a single messaging engine bus in the new
environment (recommended). If you want to use multiple buses, you can reuse the previous messaging
engine database and schema.

```
install\_root\BPM\dbscripts\SQLServer\Create\createDatabase\_CaseSensitive.sql
```

2 For case management, you must create at least one additional database. Youcan create either one database (CPEDB) or three databases, one for IBM ContentNavigator (ICN), onefor the design object store (DOS), and one for the target object store (TOS). This step assumes youare creating three databases and three users. To use the same user for all three databases, go tothe next step instead.

1. Find the files to create the databases in
install\_root\BPM\dbscripts\SQLServer\Create.
2 To create the IBM ContentNavigator database,replace the parameters in the following files: createDatabase\_ICN.sqlcreateUser.sql where:

```
createDatabase\_ICN.sql
createUser.sql
```

    - @ECMClient\_DBNAME@ is the name of the ICN database, for example, ICNDB.
    - @DB\_LOGIN@ is the login name of the database user.
3. Run the files to create the IBM Content
Navigator
database.

createDatabase\_ICN.sql
createUser.sql
Note: If you would like to use the same user as for the Process database, manually run the following
SQL to attach the same user to the ICN database:USE @DB\_NAME@
GO
CREATE USER @DB\_USER@ FOR LOGIN @DB\_USER@ WITH DEFAULT\_SCHEMA=@DB\_USER@
GO
4 To create the databases for IBM Enterprise Content Management, using the embedded Content Platform Engine , find the followingdatabase creation SQL files and make two copies of them. createDatabase\_ECM.sqlcreateUser.sql Name the files:createDatabase\_ECM\_DOS.sqlcreateUser\_ECM\_DOS.sqlcreateDatabase\_ECM\_TOS.sqlcreateUser\_ECM\_TOS.sql Replace the parameters with the design object store (DOS)parameters in one file and with the target object store (TOS) parameters in the other file.

```
createDatabase\_ECM.sql
createUser.sql
```

```
createDatabase\_ECM\_DOS.sql
createUser\_ECM\_DOS.sql
createDatabase\_ECM\_TOS.sql
createUser\_ECM\_TOS.sql
```

- Use the backslash ("\") to replace the forward slash as the file separator.
- @DB\_NAME@ is the name of the database. For example, the names could be DOSDB and TOSDB.
- @DB\_DIR@ is the data directory of your database.Important: Make sure that the
@DB\_DIR@\@DB\_NAME@ path already exists on your database computer.
- @DOS\_SCHEMA@ is the schema used by DOS, for example, DOS.
- @TOS\_SCHEMA@ is the schema used by TOS, for example, TOS.
5. In the createUser.sql file, uncomment the following lines:
--EXEC sp\_addrolemember 'db\_securityadmin', @DB\_USER@;
--EXEC sp\_addsrvrolemember @DB\_USER@, 'bulkadmin';by removing the
dashes:EXEC sp\_addrolemember 'db\_securityadmin', @DB\_USER@;
EXEC sp\_addsrvrolemember @DB\_USER@, 'bulkadmin';
6. Run the files to create the Enterprise Content Management databases.
For example:createDatabase\_ECM\_DOS.sql
createUser\_ECM\_DOS.sql
createDatabase\_ECM\_TOS.sql
createUser\_ECM\_TOS.sql
3 For case management, if you want to use a single user who already exists,use this step instead of the previous step. You must do either step 2 or step 3.

1. Find the files to create the databases in
install\_root\BPM\dbscripts\SQLServer\Create.
2 To create the IBM ContentNavigator database,replace the parameters in the following files: createDatabase\_ICN.sqlcreateSchema\_ECM.sql In createDatabase\_ICN.sql : In createSchema\_ECM.sql :

```
createDatabase\_ICN.sql
createSchema\_ECM.sql
```

    - @ECMClient\_DBNAME@ is the name of the ICN database, for example, ICNDB.
    - @DB\_LOGIN@ is the login name of the database user.
    - @DBNAME@ is the name of the ICN database that you created in
createDatabase\_ICN.sql.
    - @SCHEMA@ is the login name of the database schema, for example, ICN.
    - @ECMClient\_DBUSER@ is the user you created.
3. Run the files to create the IBM Content
Navigator
database.

createDatabase\_ICN.sql
createSchema\_ECM.sql
Note: If you would like to use the same user as for the Process database, manually run the following
SQL to attach the same user to the ICN database:USE @DB\_NAME@
GO
CREATE USER @DB\_USER@ FOR LOGIN @DB\_USER@ WITH DEFAULT\_SCHEMA=@DB\_USER@
GO
4 To create the databases for IBM Enterprise Content Management, using the embedded Content Platform Engine , find the followingdatabase creation SQL files and make two copies of them. createDatabase\_ECM.sqlcreateSchema\_ECM.sql Name the files:createDatabase\_ECM\_DOS.sqlcreateSchema\_ECM\_DOS.sqlcreateDatabase\_ECM\_TOS.sqlcreateSchema\_ECM\_TOS.sql Replace the parameters with the design object store (DOS)parameters in one file and with the target object store (TOS) parameters in the other file.IncreateDatabase\_ECM.sql : In createSchema\_ECM.sql :

```
createDatabase\_ECM.sql
createSchema\_ECM.sql
```

```
createDatabase\_ECM\_DOS.sql
createSchema\_ECM\_DOS.sql
createDatabase\_ECM\_TOS.sql
createSchema\_ECM\_TOS.sql
```

- @DB\_NAME@ is the name of the database. For example, the names could be DOSDB and TOSDB.
- @DB\_DIR@ is the data directory of your database.
- @DOS\_SCHEMA@ is the schema used by DOS, for example, DOS.
- @TOS\_SCHEMA@ is the schema used by TOS, for example, TOS.

- @DB\_NAME@ is the name of the database that you created in
createDatabase\_ECM.sql.
- @SCHEMA@ is the login name of the database schema. It should be the same as @DOS\_SCHEMA@ or
@TOS\_SCHEMA@.
- @ECMClient\_DBUSER@ is the user you created.
5. Run the files to create the Enterprise Content Management databases.
For
example:createDatabase\_ECM\_DOS.sql
createSchema\_ECM\_DOS.sql
createDatabase\_ECM\_TOS.sql
createSchema\_ECM\_TOS.sql
4 On the target deployment manager computer,validate that all database connections are correctly configured byrunning the BPMConfig -validate command. Usethe following syntax:target\_install\_root \bin\BPMConfig -validate -db configuration\_properties\_file where The command checks each connection anddisplays a message similar to the following message:A JDBC connection to the 'BusinessSpaceDb' (CMNDB.bpmadmin) has been successfully established.

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