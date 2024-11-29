# SQL Error when starting multiple nodes in a cluster

```
0000007c E com.ibm.mm.server.persistence.rdbms.dao.ibatis.BaseDao readPathByPath BMWSD0429E: An SQLException was encountered while communicating with the database.
	Error code: 0, SQL State:  null, Message:  Error: executeQueryForObject returned too many results. 
	java.sql.SQLException: Error: executeQueryForObject returned too many results.
```

## Resolving the problem

1. Stop all servers and clusters
2. Delete all rows from the FILESTORE\_PATH table.
3. Using the command line, restart the nodes or node agents one at
a time letting each node complete its start before you go to the next
one. Each node may take several minutes to start and then import the
Business Space theme. To know whether the node has finished importing
the theme properly, check the profile\_root\BusinessSpace\cluster\_name\mm.runtime.prof\public\oobLoadedStatus.properties file. All the values for importTemplates.txt, importSpaces.txt and importThemes.txt are set to true after a successful import of the theme and other
artifacts.