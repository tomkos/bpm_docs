<!-- image -->

# deleteCompletedProcessInstances.py administrative
script

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

-f deleteCompletedProcessInstances.py 
  -cluster cluster\_name
  (-all | [-finished] [-terminated] [-failed] )
  [-templateName templateName 
  [-validFromUTC timestamp]]
  [-startedBy userID]
  [(-completedAfterLocal timestamp)|(-completedAfterUTC timestamp)]
  [(-completedBeforeLocal timestamp)|(-completedBeforeUTC timestamp)]
```

## Parameters

## Examples

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