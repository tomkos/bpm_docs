<!-- image -->

# Deleting audit log entries, using administrative scripts

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
2. Delete the entries in the audit log table. Enter the following
command:
install\_root/bin/wsadmin.sh -f deleteAuditLog.py 
       -cluster cluster\_name
       ( -all | -timeUTC timestamp | -timeLocal timestamp 
              | -processtimeUTC timestamp | -processtimeLocal timestamp )
       [-slice size]
Enter the following command:
install\_root\bin\wsadmin -f deleteAuditLog.py 
       -cluster cluster\_name
       ( -all | -timeUTC timestamp | -timeLocal timestamp 
              | -processtimeUTC timestamp | -processtimeLocal timestamp )
       [-slice size]
Where:
-cluster clusterName
The name of the cluster where Business Process Choreographer is
configured. In a multicluster setup, you must specify the application
cluster because that is where Business Process Choreographer is configured.
-all
Deletes all the audit log entries in the database. The deletion
is done in multiple transactions. Each transaction deletes the number
of entries that are specified in the slice parameter, or the default
number.
-timeLocal timestamp
Use this option to specify the deletion cutoff date and local
time on the server. Only audit log entries that are older than the
time you specify for timestamp are deleted. Its
format must be: YYYY-MM-DD['T'HH:MM:SS]. If you specify
only the year, month, and day, the hour, minutes, and seconds are
set to 00:00:00 local time on the server.
-timeUTC timestamp
Use this option to specify the deletion cutoff date and time in
Coordinated Universal Time (UTC). Only audit log entries that are
older than the time you specify for timestamp are
deleted. Its format must be: YYYY-MM-DD['T'HH:MM:SS].
If you specify only the year, month, and day, the hour, minutes, and
seconds are set to 00:00:00 UTC.
-processTimeLocal timestamp
Use this option to specify the deletion cutoff date and local
time on the server. Only audit log entries that belong to a process
that finished before the time you specify for timestamp are
deleted. Its format must be: YYYY-MM-DD['T'HH:MM:SS].
If you specify only the year, month, and day, the hour, minutes, and
seconds are set to 00:00:00 local time on the server.
-processTimeUTC timestamp
Use this option to specify the deletion cutoff date and time in
UTC. Only audit log entries that belong to a process that finished
before the time you specify for timestamp are deleted.
Its format must be: YYYY-MM-DD['T'HH:MM:SS]. If you
specify only the year, month, and day, the hour, minutes, and seconds
are set to 00:00:00 UTC.
-slice size 
Used with the -all parameter, size specifies
the number of entries included in each transaction. The optimum value
depends on the available log size for your database system. Higher
values require fewer transactions but you might exceed the database
log space. Lower values might cause the script to take longer to complete
the deletion. The default value for the slice parameter is 250.

The -timeLocal,
-timeUTC, -processTimeLocal,
and  -processTimeUTC options are mutually exclusive.
3. Optional: If the
script triggers long-running work, the script might fail if the connection
timeout is not long enough to complete the action. Check the SystemOut.log file
to see whether you need to restart the script. If the timeout happens
often, consider increasing the value of the timeout property for the
connector you are using, or adjusting the script parameters to reduce
the amount of work done.

<!-- image -->