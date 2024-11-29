<!-- image -->

# Business Process Choreographer data migration script for shared
work items

## Location

<!-- image -->

<!-- image -->

```
install\_root/ProcessChoreographer/admin/migrateWI.py
```

<!-- image -->

```
install\_root\ProcessChoreographer\admin\migrateWI.py
```

## Restrictions

- Run the script in disconnected mode to avoid connection timeout
problems.
- When you use the -setMode option, the cluster
that hosts the Business Process Choreographer configuration must be
stopped.
- You must run the database migration script on the node of a cluster
member, and not on the deployment manager.
- Depending on the quantity of data and the power of your database
server, the migration process can take several hours.

## Command syntax

```
-conntype NONE
 [-profileName profile] 
 [-tracefile trace\_file] 
  -f migrateWI.py 
 (-migrateToWISharing | -setMode WS\_SHARING\_ACTIVE\_MODE | -getMode)
 [-duration duration]
 [-slice slice\_size]
 -cluster clusterName
[[-dbUser userID] -dbPassword password]
 [-dbSchema schema]
```

Because wsadmin overwrites
its trace file, use the -tracefile option to specify
a file name and location for the trace file for the work item data
migration.

## Parameters

- For DB2® the implicit schema
is the user ID used to connect to the database, so if you specify
the -dbUser parameter, and you are using an implicit
schema based on a different user ID, then you must specify the -dbSchema parameter
to prevent the wrong user ID being used as the implicit schema.
- For Microsoft SQL
Server, the implicit schema is dbo.

<!-- image -->