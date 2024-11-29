# Creating DB2 for z/OS databases and validating database connections

## Procedure

For each deployment environment that
you are creating, complete the following steps:

```
target\_install\_root/bin/BPMConfig -validate -db configuration\_properties\_file
```

- configuration\_properties\_file is the full path
and name of the properties file that you copied over to the target
environment after you migrated the configuration using the BPMConfig
-migrate command. The BPMConfig -validate -db command
uses the database properties and the database-related authentication
alias properties (including passwords) from the configuration properties
file. If necessary, you can update these database properties in the
file, such as adding the properties for any new databases that you
created.

```
A JDBC connection to the 'BusinessSpaceDb' (CMNDB.bpmadmin) has been successfully established.
```

## Results

After all connections are checked,
you see a message that the BPMConfig -validate command
completed successfully.

## Related information

- BPMConfig command-line utility