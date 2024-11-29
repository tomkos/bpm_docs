# Database deadlock issue with large solution deployments

## Symptoms

You try to deploy a large solution and a database deadlock
error is generated in the IBM
FileNet P8 server
error log, such as the following error: 013-07-12T16:48:33.293
19F319F3 ENG FNRCE0019E - ERROR method name: throwEngineException
principal name: Administrator Global Transaction: true User Transaction:
false Exception Info: The operation could not be completed due to
a deadlock error. A retry might be appropriate. ObjectStore: "CMTOS",
SQL: ""ALTER TABLE CMTOS.Container ADD (u2586\_dub\_hvlointeger67 number(10)
NULL) "" com.filenet.api.exception.EngineRuntimeException: FNRCE0019E:
E\_DEADLOCK\_ERROR: The operation could not be completed due to a deadlock
error. A retry might be appropriate. ObjectStore: "CMTOS", SQL: ""ALTER
TABLE CMTOS.Container ADD (u2586\_dub\_hvlointeger67 number(10) NULL)
"" failedBatchItem=42  
at com.filenet.engine.dbpersist.DBOracleContext.throwEngineException(DBOracleContext.java:335)
 
at com.filenet.engine.dbpersist.DBExecutionElement.execute(DBExecutionElement.java:296)
 
at com.filenet.engine.dbpersist.DBExecutionContext.getNextResult(DBExecutionContext.java:106)
 
at com.filenet.engine.dbpersist.DBStatementList.executeStatements(DBStatementList.java:161)
 
at com.filenet.engine.dbpersist.DBStatementList.getNextResult(DBStatementList.java:601)
 
at com.filenet.engine.dbpersist.DBStatementAlter.process(DBStatementAlter.java:834)
 
at com.filenet.engine.dbpersist.DBStatementAlter.process(DBStatementAlter.java:778)

## Causes

## Resolving the problem

For large solution deployments, increase the value of
the keep-alive interval from 2 seconds to 30 seconds. The value is
specified in milliseconds: 30000 is 30 seconds.

To increase
the keep-alive interval to 30 seconds:

1. Set the following JVM parameter on the workflow
server:-Dcom.ibm.casemgmt.config.keep.alive.interval=30000
2. Restart the JVM for your changes to take effect.