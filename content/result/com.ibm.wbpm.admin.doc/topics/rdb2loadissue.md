# Resolving a DB2 process load issue

```
CWLLG2068E: An unexpected exception occurred during an attempt to generate the next primary key.   
Error: org.springframework.jdbc.UncategorizedSQLException: PreparedStatementCallback; uncategorized SQLException for SQL [update lsw\_pri\_key set high\_key = ? where table\_id = ?]; SQL state [57011]; error code [-964]; DB2 SQL Error: SQLCODE=-964, SQLSTATE=57011, SQLERRMC=null, DRIVER=3.61.65; nested exception is com.ibm.db2.jcc.am.SqlException: DB2 SQL Error: SQLCODE=-964, SQLSTATE=57011, SQLERRMC=null, DRIVER=3.61.65
```

- db2 get database config for BPMDB
- db2 get database config for PDWDB

To increase the LOGFILSIZ, use the following command,
where xxxx is the new value for the LOGFILSIZ: 
db2 update database config for BPMDB using LOGFILSIZ xxxx

- db2 update database config for BPMDB using LOGPRIMARY
yy
- db2 update database config for BPMDB using LOGSECOND zz

Increasing the LOGPRIMARY value also increases the disk requirements
for the log files because the primary log files are preallocated during
the very first connection to the database. Each log file has a size
that is equal to LOGFILSIZ. You can use the database system monitor
to help size the primary log files. See the IBM DB2 documentation
for more information about these values and how to monitor them. The
correct value for these parameters is specific to your environment.
When you increase these values, increase them in small increments
from their current settings until the problem is resolved.