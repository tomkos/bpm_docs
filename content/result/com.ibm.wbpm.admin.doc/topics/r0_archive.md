<!-- image -->

# Archiving completed BPEL process and task instances

## Location

- install\_root/ProcessChoreographer/admin
- install\_root\ProcessChoreographer\admin

## Running the script

- The script must be run in connected mode to your
Business Process Choreographer configuration. The source and destination
clusters and the deployment manager must be running.
- Include the wsadmin -user and -password options
to specify a user ID that has WebSphere system administrator authority.
- If you are not working with the default
profile, use the wsadmin -profileName profile option
to specify the profile.
- If the script is already running, further invocations will be
serialized.

<!-- image -->

<!-- image -->

```
install\_root/bin/wsadmin.sh -f archive.py parameters
```

<!-- image -->

```
install\_root\bin\wsadmin -f archive.py parameters
```

## Parameters

```
-fromCluster fromClusterName
-toCluster   toClusterName
(-tasks | -processes)
(-all | [-finished] | [-terminated] | [-failed] | [-expired])
[(-templateName templateName [-nameSpace namespace] [ -validFromUTC timestamp ])]
[-kind ( todo | invocation | collaboration ) ]
[-completedAfterUTC  timestamp | -completedAfterLocal  timestamp ]
[-completedBeforeUTC timestamp | -completedBeforeLocal timestamp ]
[-startedBy userId | -createdBy userId]
[-slice numberOfEntities]
[-limit numberOfEntities]
```

The
set of instances to be archived can be restricted further by specifying
further parameters.

## Results

```
The archive operation is running on server 'runtimeClusterMember1' 
on node 'runtimeNode01'. Check the log files of the server to get 
information about the progress and results of the archiving operation.
```

```
archive.py finished.
```

- Top-level instances archived: 15
- WARNING: The selection criterion returned no results. 
No instances archived.

## Troubleshooting and recovery

Because the
archiving script must be run connected to the Business Process Choreographer
configuration that the data will be archived from, that is where the
API event handlers are called, and where events and audit log entries
are generated.

- If you get the error java.net.SocketTimeoutException:
Read timed out or ADMC0009E: The system failed to
make the SOAP RPC call: invoke, it probably means that a
SOAP connection timeout happened before the archiving finished. In
this case, the archiving continues, and you must check the log file
of the cluster member where the workload manager ran the script, to
see if it completed successfully. You can ignore these timeout errors,
but to prevent them you must increase the timeout values, as described
in Connection timeout when running a wsadmin script.
- If the archiving operation takes a long time, it is normal for
warnings like ThreadMonitor W WSVR0605W: Thread "SoapConnectorThreadPool
: 0" (00000032) has been active for 611322 milliseconds and may be
hung. There is/are 1 thread(s) in total in the server that may be
hung. to be written to the SystemOut.log file of the runtime deployment target. If the archiving operation
completes, you will see another message like ThreadMonitor
W WSVR0606W: Thread "SoapConnectorThreadPool : 0" (0000002d) was previously
reported to be hung but has completed. It was active for approximately
3958253 milliseconds. There is/are 0 thread(s) in total in the server
that still may be hung.
- If you get the error CWWBB0665E: Archiving
error with Oracle error ORA-01795, reduce
the size of the slice parameter.

If archiving fails for any reason, for example, because
the server is restarted during archiving, any unfinished archiving
is not automatically completed. You will have to invoke the script
again.

Because the script works in two phases; first copying
the selected instances to the target archive database, and then deleting
the instances from the source database, if the script fails during
archiving, it is possible that either the copying was not completed
or the deleting was not completed. This can mean that the same instances
exist and are visible in both databases.

- If the copying phase did not complete, the script will delete
the duplicate instances from the destination archive database.
- If the copying phase completed, but the deletion phase did not
complete, the script will continue deleting the duplicate instances
from the source database.

- You cannot transfer objects from an archive database back to a
Business Process Choreographer database, nor to another archive.
- The first time that you archive instances to a new archive database,
the identity of the Business Process Choreographer configuration is
written to the database, and in future, only instances from that configuration
can be archived to that archive database.
- When instances are successfully moved to the archive, they are
deleted from the Business Process Choreographer database, which generates
a deletion event for the common event infrastructure (CEI) and the
audit log. But it is not possible to identify that the deletion event
was caused by an archiving action rather than by some other delete
action, for example, cleanup service, user initiated delete action,
delete script, or automatic deletion after successful completion.
- You cannot archive to different archives at the same time. Parallel
invocations of the archive.py script are serialized.
- You cannot archive a process instance that has the same process
name as any other process instance in the archiving database.
- You cannot archive a process instance that has the same values
for its correlation set as another process instance in the archiving
database.
- If you archive instances of a process template, then undeploy
and redeploy the identical process template with the valid from date
unchanged, you cannot archive any new instances of that process template
to the same archive database. This is not an issue for normal process
template versioning, where a different valid from date is used.

## Example invocation

To move up to 500 finished
and terminated BPEL process instances from the database for the Business
Process Choreographer configuration on cluster ProcessCluster that completed before the year 2010 to the archive database for
the Business Process Archive Manager configured on cluster SupportCluster, perform the following action.

<!-- image -->

<!-- image -->

```
install\_root/bin/wsadmin.sh 
    -f install\_root/ProcessChoreographer/admin/archive.py 
    -fromCluster ProcessCluster -toCluster SupportCluster 
    -completedBeforeLocal 2010-01-01T00:00:00
    -processes
    -finished -terminated -limit 500
```

<!-- image -->

```
install\_root\bin\wsadmin 
    -f install\_root\ProcessChoreographer\admin\archive.py 
    -fromCluster ProcessCluster -toCluster SupportCluster 
    -completedBeforeLocal 2010-01-01T00:00:00
    -processes
    -finished -terminated -limit 500
```

<!-- image -->