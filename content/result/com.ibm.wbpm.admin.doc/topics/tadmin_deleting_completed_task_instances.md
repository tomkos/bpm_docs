<!-- image -->

# Deleting completed task instances

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

A top-level task instance is considered
completed if it is in one of the following end states: finished, terminated, expired,
or failed. You specify criteria to selectively
delete top-level task instances and all their associated data, such
as instance custom properties, escalation instances, subtask instances,
and follow-on task instances, from the database.

Sometimes
follow-on task instances form a chain of follow-on tasks; where all
but the last task instance are in the forwarded state
and the last task instance in the chain is in some other state. In
this case, a top-level task instance that is in the forwarded state
is considered to be completed if the last task instance in the chain
is in one of the following end states: finished, terminated, expired,
or failed.

Normally,
an inline task instance is not considered to be a top-level task instance,
and cannot be deleted using the deleteCompletedTaskInstances.py script
because the inline task instance belongs to a BPEL process, which
means you must use deleteCompletedProcessInstances.py to
delete the completed process instance that the inline task belongs
to. However, any inline invocation task instance that was created
using the Human Task Manager API or the Service Component Architecture
(SCA) API is treated as a top-level task instance, and can be deleted
using the deleteCompletedTaskInstances.py script.

## Procedure

1. Change to the Business Process Choreographer
subdirectory where the administrative script is located. 
Enter the following
command:cd install\_root/ProcessChoreographer/admin
Enter the following command:cd install\_root\ProcessChoreographer\admin
2 Delete task instances from the database. where-cluster clusterName The name of the cluster where Business Process Choreographer or Business Process Archive Manageris configured. -all | [-finished ][-terminated ] [-failed ] [-expired ] Specifies which task instances are to be deleted according totheir state. The -all option means all end states: finished , terminated , failed ,and expired . If you do not specify -all ,you must specify one or more of the end states. -templateName templateName Optionally, specifies the name of the task template whose instances will be deleted. Ifyou specify this option, you must also specify the nameSpace parameter. Ifthere are multiple task templates with the same name but with differentvalidFromUTC dates the instances for all task templates with that name are deletedunless you use the validFromUTC parameter to specify a particular template. -nameSpace nameSpace Optionally, specifies the namespace of the task template tobe deleted. If you specify this option, you must also specifythe templateName parameter. If there are multiple task templates withthe same name but with different validFromUTC datesthe instances for all task templates with that name are deleted unlessyou use the validFromUTC parameter to specify aparticular template. -validFromUTC timestamp The date and time from which the template is valid in CoordinatedUniversal Time (UTC). The string must have the following format: yyyy-MM-ddThh:mm:ss (year,month, day, T, hours, minutes, seconds). For example, 2005-01-31T13:40:50 -createdBy userID Optionally, deletes only completed task instances that were createdby the given User ID. -completedAfterLocal timestamp Optionally, specifies that only instances that completed afterthe given local time on the server are deleted. Theformat for the timestamp string is the same asfor -validFromUTC , except that the time part isoptional for this parameter. If you specify only a date, the timedefaults to 00:00:00 local time on the server. -completedAfterUTC timestamp Optionally, specifies that only instances that completed afterthe UTC time are deleted. Theformat for the timestamp string is the same asfor -validFromUTC , except that the time part isoptional for this parameter. If you specify only a date, the timedefaults to 00:00:00 local time on the server. -completedBeforeLocal timestamp Optionally, specifies that only instances that completed beforethe given local time on the server are deleted. Theformat for the timestamp string is the same asfor -validFromUTC , except that the time part isoptional for this parameter. If you specify only a date, the timedefaults to 00:00:00 local time on the server. -completedBeforeUTC timestamp Optionally, specifies that only instances that completed beforethe given UTC time are deleted. Theformat for the timestamp string is the same asfor -validFromUTC , except that the time part isoptional for this parameter. If you specify only a date, the timedefaults to 00:00:00 local time on the server. For example, to delete the task instanceson cluster myCluster that are in the finished state,and were created by the user Erich : Enter the followingcommand: wsadmin.sh -f deleteCompletedTaskInstances.py -cluster myCluster -finished -createdBy Erich Enter the following command: wsadmin -f deleteCompletedTaskInstances.py -cluster myCluster -finished -createdBy Erich If Business Process Choreographer is configuredon the cluster, the tasks will be deleted from the Business ProcessChoreographer runtime database. If Business Process Archive Manageris configured on the cluster, the same command will delete the specifiedtasks from the archive database associated with the Business ProcessArchive Manager. Be careful not to delete any instances from a runtimedatabase that should actually be moved to an archive.
    - Enter the following
command:
install\_root/bin/wsadmin.sh -f deleteCompletedTaskInstances.py 
     -cluster clusterName
     (-all | [-finished] [-terminated] [-failed] [-expired] )
     [-templateName templateName -nameSpace nameSpace] 
     [-validFromUTC timestamp]
     [-createdBy userID ]
     [(-completedAfterLocal timeStamp)|(-completedAfterUTC timeStamp)]
     [(-completedBeforeLocal timeStamp)|(-completedBeforeUTC timeStamp)]
    - Enter the following command:
install\_root\bin\wsadmin -f deleteCompletedTaskInstances.py 
    -cluster clusterName
    (-all | [-finished] [-terminated] [-failed] [-expired] )
    [-templateName templateName -nameSpace nameSpace] 
    [-validFromUTC timestamp]
    [-createdBy userID ]
    [(-completedAfterLocal timeStamp)|(-completedAfterUTC timeStamp)]
    [(-completedBeforeLocal timeStamp)|(-completedBeforeUTC timeStamp)]

For example, to delete the task instances
on cluster myCluster that are in the finished state,
and were created by the user Erich:

Enter the following
command:

```
wsadmin.sh -f deleteCompletedTaskInstances.py 
           -cluster myCluster 
           -finished
           -createdBy Erich
```

Enter the following command:

```
wsadmin -f deleteCompletedTaskInstances.py 
        -cluster myCluster 
        -finished
        -createdBy Erich
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