<!-- image -->

# Troubleshooting the Business Process Choreographer database
and data source

Use this task to solve problems with the Business Process
Choreographer database and data source.

## About this task

## Procedure

- If the Business Process Choreographer database is getting biggerand slower over time, consider performing following:
    - To get a better idea of how many instances and activities arein the database and to verify their numbers you can use variationson the following example queries:
        - If your typical process models run an average of x activities,then the number of activity instances should not be more than x timeslarger than the number of process instances. Any large deviation fromthis ratio might indicate a problem and be worth investigating further.
            - To display the number of process instances that are in the database,
we count the number of rows in the process instance table using the
following query:select count(*) from process\_instance\_b\_t with urBy
specifying with UR, locking is avoided, which could
affect other users of the database.
            - To display the number of activity instances that are in the database,
we count the number of rows in the activity instance table using the
following query:select count(*) from activity\_instance\_b\_t with urNote: Only
activities that have the business relevance flag set are persisted
in the activity instance table
    - To see which process instances have the most activities, use the
following query:SELECT 
   PI.PIID, PT.NAME, PI.STATE, COUNT(AI.AIID) AS NUMBER\_OF\_ACTIVITIES
FROM 
   ACTIVITY\_INSTANCE\_B\_T AS AI,
   PROCESS\_INSTANCE\_B\_T AS PI,
   PROCESS\_TEMPLATE\_B\_T AS PT
WHERE 
   PI.PTID = PT.PTID AND 
   AI.PIID = PI.PIID
GROUP BY 
   PI.PIID, PT.NAME, PI.STATE
ORDER BY 
   NUMBER\_OF\_ACTIVITIES DESC
FETCH FIRST 20 ROWS ONLY
WITH URwhere PI.PIID is the process instance
ID from the process\_instance\_b\_t table and PT.NAME is
the name of the process template. This query might result in output
that is similar to the following example:PIID                                  NAME        STATE   NUMBER\_OF\_ACTIVITIES
-----------------------------------   ----------  ------  --------------------
x'9003011CE5DED75B3EFDEB538C02DAE4'   claimWork        6                147047
x'9003011E841DE9AF3EFDEB53045C4103'   claimWork        6                 96609
x'9003011E841DDEF13EFDEB53045C3DD9'   claimWork        6                 96462
...In this example, the claimWork process
template has the most activities in the database. For process instances,
the state, 6, indicates that they are in the state TERMINATED.
If the database is filling up with such instances, you should consider
setting the property for automatic deletion in the model, configuring
the cleanup service and cleanup jobs to periodically delete eligible
instances, or running a script to delete completed instances. These
and other techniques for reducing the size of the database are described
in Cleanup procedures for Business Process Choreographer.
    - If you are interested in process instances that are in a particular
state, use the following query:select count(*) from process\_instance\_b\_t where state = processState with urwhere processState is
one of the following integer values representing the state of the
process instance:0 = DELETED

1 = READY

2 = RUNNING

3 = FINISHED

4 = COMPENSATING

5 = FAILED

6 = TERMINATED

7 = COMPENSATED

8 = TERMINATING

9 = FAILING

10 = INDOUBT

11 = SUSPENDED

12 = COMPENSATION\_FAILED
    - If you are interested in activity instances that are in a particular
state, use the following query:select count(*) from activity\_instance\_b\_t where state = activityState with urwhere activityState is
one of the following integer values representing the state of the
activity instance:1 = INACTIVE

2 = READY

3 = RUNNING

4 = SKIPPED

5 = FINISHED

6 = FAILED

7 = TERMINATED

8 = CLAIMED

9 = TERMINATING

10 = FAILING

11 = WAITING

12 = EXPIRED

13 = STOPPED

14 = PROCESSING\_UNDO
Note: Only activities that have the business
relevance flag set are persisted in the activity instance table
- If you want to investigate the activity instances belonging to
a particular process instance ID, use a query that is similar to the
following example: SELECT
   AI.LAST\_STATE\_CHANGE, ATP.NAME, AI.STATE
FROM 
   ACTIVITY\_INSTANCE\_B\_T  AI, 
   ACTIVITY\_TEMPLATE\_B\_T  ATP
WHERE 
   AI.ATID = ATP.ATID and 
   AI.PIID = '9003011CE5DED75B3EFDEB538C02DAE4'
ORDER BY
   AI.LAST\_STATE\_CHANGE DESC
FETCH FIRST 40 ROWS ONLY
WITH URThis query might result in output that is similar
to the following example:LAST\_STATE\_CHANGE           NAME	            STATE
-----------------------    	-------------	 -------
2011-03-22-16.24.17.964333  Activity\_17           7
2011-03-22-16.23.55.925757  Activity\_14           5
2011-03-22-16.23.32.528576  Activity\_14           5
2011-03-22-16.23.11.976875  Activity\_14           5
2011-03-22-16.22.49.582347  Activity\_14           5
2011-03-22-16.22.24.257894  Activity\_14           5
2011-03-22-16.22.01.723894  Activity\_14           5
...In this example, multiple instances of activity 14
are changing to the state FINISHED per second. Comparing
this information with your knowledge about the process and how you
expect it to behave, this might indicate an unintended loop that needs
to be corrected in the model.
- If you are using DB2®:

- If you use the DB2 Universal JDBC driver type 4and get DB2 internal errors such as "com.ibm.db2.jcc.a.re:XAER\_RMERR : The DDM parameter value is not supported. DDM parametercode point having unsupported value : 0x113f DB2ConnectionCorrelator:NF000001.PA0C.051117223022" when you test the connectionon the Business Process Choreographer data source or when the serverstarts up, perform the following actions:
    1. Check the class path settings for the data source. In a default
setup the WebSphere® variable ${DB2UNIVERSAL\_JDBC\_DRIVER\_PATH} can
point to the embedded DB2 Universal JDBC driver which
is found in the universalDriver\_wbi directory.
    2. The version of the driver might not be compatible with your DB2 server
version. Make sure that you use the original db2jcc.jar files from
your database installation, and not the embedded DB2 Universal
JDBC driver. If required, changed the value of the WebSphere variable ${DB2UNIVERSAL\_JDBC\_DRIVER\_PATH} to
point to your original db2jcc.jar file.
    3. Restart the server.
- If the db2diag.log file of your DB2 instance
contains messages, such as ADM5503E:2004-06-25-15.53.42.078000   Instance:DB2   Node:000
PID:2352(db2syscs.exe)   TID:4360   Appid:*LOCAL.DB2.027785142343
data management  sqldEscalateLocks Probe:4   Database:BPEDB

ADM5503E  The escalation of "10" locks on table "GRAALFS .ACTIVITY\_INSTANCE\_T"
          to lock intent "X" has failed.  The SQLCODE is "-911"Increase
the LOCKLIST value. For example to set the value
to 500, enter the following DB2 command: db2 UPDATE DB CFG FOR BPEDB USING LOCKLIST 500This
can improve performance significantly.
- To avoid deadlocks, make sure your database system is configured
to use sufficient memory, especially for the buffer pool. For DB2,
use the DB2 Configuration Advisor to determine reasonable
values for your configuration.
- If you get errors mentioning the data source implementation class COM.ibm.db2.jdbc.DB2XADataSource :

- Check that the class path definition for your JDBC provider is
correct.
- Check that the component-managed authentication alias is set to BPCDB\_nodeName.serverName\_Auth\_Alias if
Business Process Choreographer is configured on a server, and BPCDB\_clusterName\_Auth\_Alias if
Business Process Choreographer is configured on a cluster.
- If you get a database error when deploying an enterprise
application that contains a BPEL process or human task, make sure
that the database system used by the process container is running
and accessible. When an enterprise application is deployed,
any process templates and task templates are written into the Business
Process Choreographer database.
- If you have problems using national characters. Make
sure that your database was created with support for Unicode character
sets.
- If tables and views cannot be found in the database andthe create schema option is not enabled, check the following settings:

- If a database schema qualifier is configured, check the followingsettings:
    - The schema qualifier must match the schema in the database. It
must be the same schema as used in the scripts.
    - The user must be granted the privileges to work with the database
tables and views.
- If no schema qualifier is configured, ensure that:

- The authentication alias of the user must be the same user ID
as the one that is used to run the scripts, or must match the schema
qualifier that is used in the scripts.
- The user must be granted the privileges to work with the database
tables and views.
- If the create schema option is enabled, and the databasetable and views cannot be found, the database tables and objects willbe created automatically using the following terms:

- If a schema qualifier is configured, the tables and views will
be created using the schema qualifier.
- If no schema qualifier is configured,  the tables and views will
be created using the user ID.
- If you get the error message com.ibm.bpe.util.Assert.assertion(Assert.java:66)
Assertion violation ! (pWifl != null) in method >> com.ibm.bpe.database.Tom.augmentSharedWorkItem(Tom.java:9815),
there is a problem with shared work items in the database, run the
dbUtility.py script to check for and repair any database consistency
problems. For details about using the utility refer to dbUtility.py administrative script.