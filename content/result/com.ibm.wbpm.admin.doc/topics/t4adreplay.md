<!-- image -->

# Querying and replaying failed messages, using administrative
scripts

## Before you begin

- Run the script in connected mode,
that is, do not use the wsadmin -conntype none option.
- At least one cluster member must be running.
- Include the wsadmin -user and -password options
to specify a user ID that has operator authority.
- If you are not working with the default
profile, use the wsadmin -profileName profile option
to specify the profile.

## About this task

## Procedure

1. Change to the Business Process Choreographer
subdirectory where the administrative script is located. 
Enter the following
command:cd install\_root/ProcessChoreographer/admin
Enter the following command:cd install\_root\ProcessChoreographer\admin
2. Query the number of failed messages on both the retention
and hold queues.  Enter the following
command:
install\_root/bin/wsadmin.sh -f queryNumberOfFailedMessages.py
           -cluster clusterName
           [ -bfm | -htm ]
Enter the following command:
install\_root\bin\wsadmin -f queryNumberOfFailedMessages.py
           -cluster clusterName
           [ -bfm | -htm ]
Where:

-cluster clusterName
The name of the cluster where Business Process Choreographer is
configured. In a multicluster setup, you must specify the application
cluster because that is where Business Process Choreographer is configured.
-bfm | -htm
These keywords are optional and mutually exclusive. The default,
if neither option is specified is to replay failed messages for both
BPEL processes and human tasks. If you want to only replay the messages
for BPEL processes, specify the -bfm option.  If
you want to only replay messages for human tasks, specify the -htm option.
3 Replay all failed messages on the hold queue, retentionqueue, or both queues. Enter the followingcommand: install\_root/bin/wsadmin.sh -f replayFailedMessages.py -cluster cluster\_name -queue replayQueue [ -bfm | -htm ] Enter the following command: install\_root\bin\wsadmin -f replayFailedMessages.py -cluster cluster\_name -queue replayQueue [ -bfm | -htm ] Where: -cluster clusterName The name of the cluster where Business Process Choreographer isconfigured. In a multicluster setup, you must specify the applicationcluster because that is where Business Process Choreographer is configured. -queue replayQueue Optionally specifies the queue to replay. replayQueue canhave one of the following values: -bfm | -htm These keywords are optional and mutually exclusive. The default,if neither option is specified is to replay failed messages for bothBPEL processes and human tasks. If you want to only replay the messagesfor BPEL processes, specify the -bfm option. Ifyou want to only replay messages for human tasks, specify the -htm option.

Enter the following
command:

```
install\_root/bin/wsadmin.sh -f replayFailedMessages.py
       -cluster cluster\_name
       -queue replayQueue
       [ -bfm | -htm ]
```

Enter the following command:

```
install\_root\bin\wsadmin -f replayFailedMessages.py
       -cluster cluster\_name
       -queue replayQueue
       [ -bfm | -htm ]
```

Where:

    - holdQueue (this is the default value)
    - retentionQueue (only valid when the -bfm option
is specified)
    - both (not valid when the -htm option
is specified)

<!-- image -->