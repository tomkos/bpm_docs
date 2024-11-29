# Solution export fails with an Apache Derby SQL exception

## Symptoms

```
The solution could not be exported because of the following error: EXPORT failed. 
0 items processed: 0 succeeded, 0 failed. Apache Derby experienced a sql exception.
Create table tablename. A lock could not be obtained within
 the time requested. FNRAM9042
```

```
The solution could not be exported because of the following error: EXPORT failed. 
0 items processed: 0 succeeded, 0 failed. Apache Derby experienced a sql exception. 
Create table tablename(hashcode int, mapkey varchar(76), 
mapdata varchar(32672)) Table/View 'TABLENAME' already exists 
in Schema 'APP'.  FNRAM9042
```

```
The solution could not be exported because of the following error: EXPORT failed. 
42 items processed: 42 succeeded, 0 failed. An unexpected exception occurred. The 
unexpected exception is chained to this exception. A lock could not be obtained 
within the time requested  FNRAM9042
```

## Causes

- When you export a solution, you might encounter Derby or SQL errors if another user tries to
export a solution on the same system at the same time.
- (For WebSphere® Application
Server on AIX or
Linux only) You might be unable to export a solution if two users previously attempted to export two
solutions at the same time. When a solution export fails, the Apache Derby database that is used
by the workflow Case administration client to export that solution is left behind. The database is
not removed when a solution export fails because the database is retained for diagnostic purposes.
When another solution is exported, the database that was left from an earlier solution export is
reused, which causes the Apache Derby SQL exception.

## Resolving the problem

- If you are exporting a solution while someone else is also exporting a solution, wait until the
other solution is exported and try the operation again.
- If you can't export a solution because of a previous simultaneous export attempt, clean up theWebSphere temp and Export temp folders. Then, try theexport again.To clean up the WebSphere temp and Exporttemp folders:
    - Stop the WAS server. If there are multiple nodes, then all the WAS nodes with Business
Automation Workflow or Content Navigator must be shut down.
    - Delete the folder exportstaging on the Business Automation Workflow Case
Network Shared Directory.
    - Delete <WebSphere install location>/derby/P8DerbyTmpDB .
    - Restart the WAS server nodes for Business Automation Workflow and Content Navigator.