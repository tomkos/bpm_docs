# Error message when server first starts

```
com.ibm.mm.server.persistence.rdbms.dao.ibatis.BaseDaoreadPathByPath BMWSD0429E: An SQLException was encountered while communicating with the database.  Error code: 0, SQL State:  null, Message:  Error: executeQueryForObject returned too many results.
```

```
Line 62310: [7/5/17 14:50:10:916 PDT] 00000073 SQLServerExce 1
*** SQLException: com.microsoft.sqlserver.jdbc.SQLServerException:Invalid object name 'FNGCD'.
Msg 208, Level 16, State 1, Invalid objectname 'FNGCD'.
Line 62724: [7/5/17 14:50:10:948 PDT] 00000073 SQLServerExce 1
*** SQLException: com.microsoft.sqlserver.jdbc.SQLServerException:Invalid object name 'FNGCD\_ADDON'. 
Msg 208, Level 16, State 1, Invalidobject name 'FNGCD\_ADDON'.
[7/3/17 15:51:17:172 PDT] 00000072 WSJdbcPrepare <  execute Exitcom.microsoft.sqlserver.jdbc.SQLServerException: 
Distributedtransaction completed. Either enlist this session in a new transaction
or the NULL transaction.atcom.microsoft.sqlserver.jdbc.SQLServerException.makeFromDatabaseError(SQLServerException.java:216)
```