<!-- image -->

# deleteCompletedTaskInstances.py administrative
script

Sometimes
follow-on task instances form a chain of follow-on tasks; where all
but the last task instance are in the forwarded state
and the last task instance in the chain is in some other state. In
this case, a top-level task instance that is in the forwarded state
is considered to be completed if the last task instance in the chain
is in one of the following end states: finished, terminated, expired,
or failed.

Normally, an inline task instance
is not considered to be a top-level task instance, and cannot be deleted
using the deleteCompletedTaskInstances.py script
because the inline task instance belongs to a BPEL process, which
means you must use deleteCompletedProcessInstances.py to
delete the completed process instance that the inline task belongs
to. However, any inline invocation task instance that was created
using the Human Task Manager API or the Service Component Architecture
(SCA) API is treated as a top-level task instance, and can be deleted
using the deleteCompletedTaskInstances.py script.

## Prerequisites

- Run the script in the connected mode, that is,
do not use the wsadmin -conntype none option.
- At least one cluster member must be running.
- Include the wsadmin -user and -password options
to specify a user ID that has operator authority.
- If you are not working with the default
profile, use the wsadmin -profileName profile option
to specify the profile.

## Location

```
install\_root\ProcessChoreographer\admin
install\_root/ProcessChoreographer/admin
```

## Syntax

```
install\_root/bin/wsadmin.sh 
install\_root\bin\wsadmin

-f deleteCompletedTaskInstances.py 
     -cluster clusterName
     (-all | [-finished] [-terminated] [-failed] [-expired] )
     [-templateName templateName -nameSpace nameSpace 
     [-validFromUTC timestamp]]
     [-createdBy userID ]
     [(-completedAfterLocal timeStamp)|(-completedAfterUTC timeStamp)]
     [(-completedBeforeLocal timeStamp)|(-completedBeforeUTC timeStamp)]
```

## Parameters

## Example

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