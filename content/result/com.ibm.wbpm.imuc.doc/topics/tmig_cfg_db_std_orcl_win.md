# Creating Oracle databases and validating database connections

## Procedure

For each deployment environment that
you are creating, complete the following steps:

1 Create required databases. If you are migrating to a Standard deployment environment : If you are migrating to an Advanced deployment environment : For each database, make any required changes and run the followingscript:install\_root \BPM\dbscripts\Oracle\Create\createUser.sql
    - Create a messaging engine database if you want to use a single messaging engine bus in the new
environment (recommended). If you want to use multiple buses, you can reuse the previous messaging
engine database and schema.
    - Create a Business Process Choreographer database.
    - Create a messaging engine database if you want to use a single messaging engine bus in the new
environment (recommended). If you want to use multiple buses, you can reuse the previous messaging
engine database and schema.

```
install\_root\BPM\dbscripts\Oracle\Create\createUser.sql
```

2 For case management, you must create three additional users, one forIBM ContentNavigator (ICN), one for the design object store (DOS), and one for the target object store (TOS).

1. Find the files to create the databases in
install\_root\BPM\dbscripts\Oracle\Create.
2 To create the IBM ContentNavigator database,replace the parameters in the following files: createUser.sqlcreateTablespace\_ICN.sql where:

```
createUser.sql
createTablespace\_ICN.sql
```

    - @DB\_NAME@ is the Oracle instance name, for example, orcl.
    - @DB\_DIR@ is the directory, which you must create before running the SQL files. The DB\_DIR
directory is the data directory of your database.
    - @ECMClient\_TBLSPACE@ is the table space used by IBM Content Navigator (ICN). The default value
is WFICNTS.
    - @ECMClient\_SCHEMA@ is the schema used by ICN.
    - @DB\_USER@ is the ICN user name, for example, icnuser. The schema name and user name are usually
the same.
    - @DB\_PASSWD@ is the password for the user.
3. Run the files to create the IBM Content
Navigator
database.

createUser.sql
createTablespace\_ICN.sql
4 To create the users and table spaces for IBM Enterprise Content Management, using the embeddedContent Platform Engine , find thefollowing database creation SQL file and make a copy of it. createUserTablespace\_ECM.sql Replace the following parameters:

```
createUserTablespace\_ECM.sql
```

- Use the backslash ("\") to replace the forward slash as the file separator.
- @ECM\_DATA\_TS@ is the data table space used by DOS or TOS. The default value for DOS is
WFDOSDATATS. The default value for TOS is WFTOSDATATS. You can set these values in the SQL
file.
- @DB\_NAME@ is the Oracle instance name, for example, orcl.
- @DB\_DIR@ is the data directory of your database.Important: Make sure that the
@DB\_DIR@\@DB\_NAME@ path already exists on your database computer. You will use this value when you
update the properties file later.
- @DB\_USER@ is the DOS user name or TOS user name. for example, dosuser or tosuser.
- @DB\_PASSWD@ is the password for the user.
5. Run the file to create the Enterprise Content Management users and table spaces.

createUserTablespace\_ECM.sql
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