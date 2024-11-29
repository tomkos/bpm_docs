<!-- image -->

# Retrieving a list of query tables

## Before you begin

- Run the script in connected mode,
that is, do not use the wsadmin -conntype none option.
- At least one cluster member must be running.
- Include the wsadmin -user and -password options
to specify a user ID that has administrator or deployer authority.
- If you are not working with the default
profile, use the wsadmin -profileName profile option
to specify the profile.

## About this task

## Procedure

1 Change to the Business Process Choreographersubdirectory where the administrative script is located.
    - install\_root/ProcessChoreographer/admin
    - install\_root\ProcessChoreographer\admin
2. To list query tables in the command prompt window: 
Enter the following
command:
install\_root/bin/wsadmin.sh -f manageQueryTable.py
       -cluster clusterName
       -query names 
       -kind (composite | predefined | supplemental)Enter the following command:
install\_root\bin\wsadmin -f manageQueryTable.py
       -cluster clusterName
       -query names 
       -kind (composite | predefined | supplemental)Where: 
-cluster clusterName
The name of the cluster where Business Process Choreographer is
configured. In a multicluster setup, you must specify the application
cluster because that is where Business Process Choreographer is configured.
-kind (composite | predefined | supplemental)
The type of the query table to be listed whether composite, predefined,
or supplemental. If there are no query tables of the selected kind, none is
returned.

## Example

Enter the following
command:

```
wsadmin.sh -f manageQueryTable.py -cluster myCluster 
           -query names -kind composite
```

Enter the following command:

```
wsadmin -f manageQueryTable.py -cluster myCluster 
        -query names -kind composite
```

<!-- image -->