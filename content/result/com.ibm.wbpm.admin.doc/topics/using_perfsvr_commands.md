# Using the Performance Data Warehouse command-line tool (perfDWTool)

## Accessing perfDWTool

The perfDWTool must be run from an active node in the support cluster.

```
C:\IBM\WebSphere\AppServer\profiles\Node1Profile\bin
```

## perfDWTool syntax

<!-- image -->

<!-- image -->

```
perfDWTool.sh -u user\_name -p password -nodeName node\_name 
-serverName server\_name command-name -command-arg
```

<!-- image -->

```
perfDWTool.bat -u user\_name -p password -nodeName node\_name 
-serverName server\_name command-name -command-arg
```

The
following table lists all the options available with perfDWTool.

| Option                    | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Required or Optional                                      |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| -?, -help                 | Displays information about the options, commands, and arguments available with this command-line tool.                                                                                                                                                                                                                                                                                                                                                                                                                             | Optional                                                  |
| -u, user\_name             | Specifies the user name for connecting to the Performance Data Warehouse. You must include this option each time you invoke the tool.Important: The user name must be defined as an administrator in WebSphere Application Server.                                                                                                                                                                                                                                                                                                 | Required                                                  |
| -p, password              | Specifies the password for connecting to the Performance Data Warehouse. You must include this option each time you invoke the tool.You can provide the password in plain text or in encrypted form. To encrypt the password, use the following command: java -cp utility.jar com.lombardisoftware.utility.WsEncryptPassword <BPM\_install\_dir> "<password>". The utility.jar file is located in directory <BPM\_install\_dir>/BPM/Lombardi/lib. Note: If you use an encrypted password, you must always enclose it in double quotes. | Required                                                  |
| -nodeName node\_name       | Specifies the node name to use if the Performance Data Warehouse is installed in a network deployment environment.                                                                                                                                                                                                                                                                                                                                                                                                                 | Required in a clustered environment; optional, otherwise. |
| -serverName server\_name   | Specifies the server name to use if the Performance Data Warehouse is installed in a network deployment environment.                                                                                                                                                                                                                                                                                                                                                                                                               | Optional                                                  |
| command-name -command-arg | Specifies the command to run with perfDWTool.The commands and command arguments are listed in Table 2.                                                                                                                                                                                                                                                                                                                                                                                                                             | Required                                                  |

## Commands available with perfDWTool

The tool
includes the following commands:

| Command   | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| prune     | Purges data from the Performance Data Warehouse database. With the prune command you can remove data that is older than the number of days specified by the -daysOld parameter or remove only the system tasks by specifying the -systemTasks parameter. The -cancel parameter stops the current prune operation or prevents the next prune operation from running if it has not yet started. You can use the -showStatus parameter to determine if a prune action is currently queued, processing, or not processing, without requesting an actual prune operation. You can use the -systemTasks parameter to prune only the system tasks. The -daysOld parameter must not be specified, all the system tasks are pruned regardless of their creation date. |
| archive   | Archives the snapshots that you specify and marks all the metadata in those snapshots with an ARCHIVED time stamp. IBM® Business Automation Workflow does not use archived metadata when it generates Performance Data Warehouse schema and views. To specify snapshots, use the ID for each snapshot from the SNAPSHOTS view in the performance database.                                                                                                                                                                                                                                                                                                                                                                                                   |
| restore   | Restores the snapshots that you specify. The restore command nulls out the ARCHIVED time stamp and allows the metadata of the snapshot to contribute to the Performance Data Warehouse physical schema and views. To specify snapshots, use the ID for each snapshot from the SNAPSHOTS view in the performance database.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| pending   | Identifies failed definition records and resolves their pending state. You can also use the pending command to review and then commit pending schema changes from the archive and restore commands.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

- Pruning data from the Performance Data Warehouse database

 Traditional: 
Use the prune command to remove data that you no longer need from the Performance Data Warehouse database. The prune command removes data that is older than the number of days old specified by the -daysOld parameter.
- Archiving and restoring data in the Performance Data Warehouse database

 Traditional: 
You use the archive command to mark records in the Performance Data Warehouse with an ARCHIVED time stamp. You use the restore command to null out the ARCHIVED time stamp. Both commands leave the database in a pending state, and you use the pending command to complete the archive or restore operation.