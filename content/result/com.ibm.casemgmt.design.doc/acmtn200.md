# Tuning case management

## About this task

During redeployment of a solution, some system configuration information might be overwritten and
might need to be specified again. However, most configuration steps do not need to be repeated.

- Tuning transmission protocols
- Tuning the object request broker (ORB)
- Indexing Content Platform Engine databases to improve Business Automation Workflow performance
- Setting the log size for Oracle case history databases
- Tuning the in-basket property synchronization settings
- Tuning the maximum pool size for business rules

For JVM troubleshooting information, see Best practices for JVM memory issuesBest practices for JVM memory issues.

## Tuning transmission protocols

Adjusting the following transmission protocols can improve Business Automation Workflow performance.

### About this task

- IBM®
FileNet® P8
Content Platform Engine - If secured
transmissions (such as FIPS) are not required, using the default IIOP protocol with IBM
FileNet P8
Content Platform Engine HTTP Tunneling
increases both CPU usage and response time.
- TCP/IP buffer size - Consider increasing the system TCP/IP buffer size from the default
value. For example, on AIX® use no -o
tcp\_sendspace=524176 and no -o tcp\_recvspace=524176 to set the buffer size
to 512 KB.
- HTTP server - If an HTTP server is used as a load balancer for an application server
cluster, increase the number of threads (or processes) accordingly for a high concurrency
workload.

## Tuning the object request broker (ORB)

Under moderate workloads, the default object request broker (ORB) settings work well..

### About this task

Adjusting the following property values can improve performance during heavy workloads.

- com.ibm.CORBA.ConnectionMultiplicity - Consider increasing the
com.ibm.CORBA.ConnectionMultiplicity property value from its default setting of
1 to a value from 5 to 10.
- com.ibm.CORBA.FragmentSize - Consider setting the
com.ibm.CORBA.FragmentSize property value to 0. Increase this value as needed.
- Web container thread pool - Monitor the web container thread pool and increase its size
accordingly.

## Indexing Content Platform Engine databases to improve Business Automation Workflow
performance

Depending on your solution and workload, you may find it beneficial to add indexes to the
target object store database to improve the Business Automation Workflow performance. See the
following examples of such indexes and the circumstances when they may be helpful.

### About this task

## Setting the log size for Oracle case history databases

You might see a very high disk write queue length when using an Oracle database for case
history. You can increase each redo.log file size to improve the disk write
queue length.

### Procedure

To increase the redo.log file size:

1. If the redo log group associated with the log file has a status of CURRENT,
you need to first switch it with another group:

alter system switch logfile;
2. Deactivate the redo log group you want to drop:

alter system checkpoint;
3. Drop the redo log group from the database.

alter database drop logfile group group\_number
Restriction: If you only have two redo log groups active on the Oracle database, you
cannot drop the group, since Oracle databases require a minimum of two active redo log groups at all
times. If this is the case, create a third temporary redo log group before dropping either of the
other two groups. For example:
alter database add logfile group 3 '/app01/oratest/oradata/BOTI/BOTI/redo03.log' size 100M;
4. Delete the redo.log file associated with the redo log group you just
dropped.
5. Add the group back to the database with a larger specified size.
For example, if you want to create the redo log group with a size of 100 MB:
alter database add logfile group 2 '/app01/oratest/oradata/BOTI/BOTI/redo02.log' size 100M;Repeat
for all other redo log groups, making sure to make them inactive before dropping them.
6. Activate the last redo log group that you added:

alter system switch logfile;
Remember: If you originally had two redo log groups and you created a third temporary
group to be able to drop the other two, you can delete this third group now.

## Tuning the in-basket property synchronization settings

When a property value is updated in a case, the change is synchronized in all views of
the case. You might experience performance issues if all property updates are set to synchronize
automatically. To improve performance, you can disable the automatic synchronization for certain
properties.

### About this task

At design time, you use Process Designer to save the
event update settings as part of the solution. For solutions that are already deployed, you use
Process Configuration Console to change the settings.

### Procedure

To tune property synchronization settings:

1 Start the Process Configuration Console:
    1. Expand Object Stores.
    2. Expand your target object store.
    3. Select Workflow System.
    4. From the Actions menu, click Configure Workflow
Settings.
2. Expand the tree view for the Connection Point that is associated with the solution that you are
updating.
3. Right click the work queue that you are editing, and select Queue
Properties.
4. On the Data Fields tab, clear the checkbox in the Event Update column for
all properties that you want to disable synchronization for.
5. Commit your changes.

## Tuning the maximum pool size for business rules

You may want to adjust the maximum pool size for business rules, depending on how many
rules can be run in parallel by Content Platform Engine. You can tune the maximum
pool size using the -DrulesMaxPoolSize parameter in the WebSphere Application
Server profile for Content Platform Engine.

### About this task

### Procedure

To change the maximum pool size parameter value:

1. Add the following argument to the WebSphere Application
Server profile for Content Platform Engine:

-DrulesMaxPoolSize=NNNwhere NNN is the new value for the
parameter.
2. Restart Content Platform Engine.