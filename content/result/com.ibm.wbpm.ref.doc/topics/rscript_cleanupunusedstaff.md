<!-- image -->

# cleanupUnusedStaffQueryInstances.py administrative
script

Business Process Choreographer maintains lists
of user names in the runtime database for people queries that have
been evaluated. Although the BPEL process instances and human tasks
that used the people queries have finished, the lists of user names
are maintained in the database until the corresponding process application
is undeployed.

If the size of the
database is affecting performance, you can remove the unused lists
of people that are cached in the database tables.

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

-f cleanupUnusedStaffQueryInstances.py 
  -cluster cluster\_name 
    [-cleanupSharedWorkItems]
```

## Parameters