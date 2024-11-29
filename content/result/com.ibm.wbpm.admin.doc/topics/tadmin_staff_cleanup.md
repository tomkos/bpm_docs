<!-- image -->

# Removing unused people query results, using administrative
scripts

## Before you begin

- Run the script in the connected mode, that is,
do not use the wsadmin -conntype none option.
- At least one cluster member must be running.
- Include the wsadmin -user and -password options
to specify a user ID that has operator authority.
- If you are not working with the default
profile, use the wsadmin -profileName profile option
to specify the profile.

## About this task

Business Process Choreographer maintains lists
of user names in the runtime database for people queries that have
been evaluated. Although the BPEL process instances and human tasks
that used the people queries have finished, the lists of user names
are maintained in the database until the corresponding process application
is undeployed.

If the size of the
database is affecting performance, you can remove the unused lists
of people that are cached in the database tables.

## Procedure

1. Change to the Business Process Choreographer
subdirectory where the administrative script is located. 
Enter the following
command:cd install\_root/ProcessChoreographer/admin
Enter the following command:cd install\_root\ProcessChoreographer\admin
2. Remove the unused lists of people. Enter the following
command:
install\_root/bin/wsadmin.sh -f cleanupUnusedStaffQueryInstances.py 
  -cluster cluster\_name 
    [-cleanupSharedWorkItems]
Enter the following command:
install\_root\bin\wsadmin -f cleanupUnusedStaffQueryInstances.py 
  -cluster cluster\_name 
    [-cleanupSharedWorkItems]
Where:
-cluster clusterName
The name of the cluster where Business Process Choreographer is
configured. In a multicluster setup, you must specify the application
cluster because that is where Business Process Choreographer is configured.
-cleanupSharedWorkItems 
Specify this optional parameter if you also want the script to
delete unused shared work items.

## Results

<!-- image -->