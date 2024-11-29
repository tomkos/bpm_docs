<!-- image -->

# Deleting BPEL process instances

## Before you begin

- Run the script in connected mode,
that is, do not use the wsadmin -conntype none option.
- In the cluster where the Business Process Choreographer configuration
or Business Process Archive Manager where you want to delete instances
is configured, at least one cluster member must be running.
- Include the wsadmin -user and -password options
to specify a user ID that has operator authority.
- If you are not working with the default
profile, use the wsadmin -profileName profile option
to specify the profile.

## About this task

A
top-level process instance is considered completed if it is in one
of the following end states: finished, terminated, compensated,
or failed. You specify criteria to selectively
delete top-level process instances and all their associated data,
such as instance custom properties, and subprocess instances, from
the database.

## Procedure

1. Change to the Business Process Choreographer
subdirectory where the administrative script is located.  Enter the following
command:cd install\_root/ProcessChoreographer/admin
Enter the following command:cd install\_root\ProcessChoreographer\admin
2 Delete process instances from the database. where-cluster cluster\_name The name of the cluster where Business Process Choreographer configuration or Business ProcessArchive Manager isconfigured. -all | [-finished ] [-terminated ] [-failed ] Specifies which instances are to be deleted according to their state. The -all option means all end states: finished , terminated , andfailed . If you do not specify -all , you must specify one or moreof the end states. -templateName templateName Optionally, specifies the name of the process template whose instances will be deleted. If there are multiple process templates with the same name but with differentvalidFromUTC dates the instances for all process templates with that name aredeleted unless you use the validFromUTC parameter to specify a particularprocess template. -validFromUTC timestamp The date and time from which the template is valid in CoordinatedUniversal Time (UTC). The string must have the following format: yyyy-MM-ddThh:mm:ss (year,month, day, T, hours, minutes, seconds). For example, 2005-01-31T13:40:50 -startedBy userID Optionally, only deletes completed process instances that werestarted by the given User ID. -completedAfterLocal timestamp Optionally, specifies that only instances that completed afterthe given local time on the server are deleted. Theformat for the timestamp string is the same asfor -validFromUTC , except that the time part isoptional for this parameter. If you specify only a date, the timedefaults to 00:00:00 local time on the server. -completedAfterUTC timestamp Optionally, specifies that only instances that completed afterthe UTC time are deleted. Theformat for the timestamp string is the same asfor -validFromUTC , except that the time part isoptional for this parameter. If you specify only a date, the timedefaults to 00:00:00 local time on the server. -completedBeforeLocal timestamp Optionally, specifies that only instances that completed beforethe given local time on the server are deleted. Theformat for the timestamp string is the same asfor -validFromUTC , except that the time part isoptional for this parameter. If you specify only a date, the timedefaults to 00:00:00 local time on the server. -completedBeforeUTC timestamp Optionally, specifies that only instances that completed beforethe given UTC time are deleted. Theformat for the timestamp string is the same asfor -validFromUTC , except that the time part isoptional for this parameter. If you specify only a date, the timedefaults to 00:00:00 local time on the server. For example, to delete allof the process instances that are running on cluster myCluster that are in the state finished , and were startedby the user Anita : Enter the followingcommand: wsadmin.sh -f deleteCompletedProcessInstances.py -cluster myCluster -finished -startedBy Anita Enter the following command: wsadmin -f deleteCompletedProcessInstances.py -cluster myCluster -finished -startedBy Anita IfBusiness Process Choreographer is configured on the cluster, the processes will be deleted from theBusiness Process Choreographer runtime database. If Business Process Archive Manager is configuredon the cluster, the same command will delete the specified processes from the archive databaseassociated with the Business Process Archive Manager. Be careful not to delete any instances from aruntime database that should actually be moved to an archive.
    - Enter the following
command:
install\_root/bin/wsadmin.sh -f deleteCompletedProcessInstances.py 
  -cluster cluster\_name
  (-all | [-finished] [-terminated] [-failed])
  [-templateName templateName] 
  [-validFromUTC timestamp]
  [-startedBy userID]
  [(-completedAfterLocal timestamp)|(-completedAfterUTC timestamp)]
  [(-completedBeforeLocal timestamp)|(-completedBeforeUTC timestamp)]
    - Enter the following command:
install\_root\bin\wsadmin -f deleteCompletedProcessInstances.py 
  -cluster cluster\_name
  (-all | [-finished] [-terminated] [-failed] )
  [-templateName templateName] 
  [-validFromUTC timestamp]
  [-startedBy userID]
  [(-completedAfterLocal timestamp)|(-completedAfterUTC timestamp)]
  [(-completedBeforeLocal timestamp)|(-completedBeforeUTC timestamp)]

For example, to delete all
of the process instances that are running on cluster myCluster
that are in the state finished, and were started
by the user Anita:

Enter the following
command:

```
wsadmin.sh -f deleteCompletedProcessInstances.py 
        -cluster myCluster 
        -finished
        -startedBy Anita
```

Enter the following command:

```
wsadmin -f deleteCompletedProcessInstances.py 
        -cluster myCluster 
        -finished
        -startedBy Anita
```

3. Optional: If the
script triggers long-running work, the script might fail if the connection
timeout is not long enough to complete the action. Check the SystemOut.log file
to see whether you need to restart the script. If the timeout happens
often, consider increasing the value of the timeout property for the
connector you are using, or adjusting the script parameters to reduce
the amount of work done.

## Results

<!-- image -->