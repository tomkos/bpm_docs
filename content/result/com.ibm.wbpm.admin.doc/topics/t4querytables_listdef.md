<!-- image -->

# Retrieving the XML definitions of query tables

## Before you begin

- Run the script in connected mode,
that is, do not use the wsadmin -conntype none option.
- At least one cluster member must be running.
- Include the
wsadmin -user and -password options
to specify a user ID that has operator, administrator, or deployer
authority.
- If you are not working with the default
profile, use the wsadmin -profileName profile option
to specify the profile.

## About this task

Complete
the following steps to retrieve the XML definition of composite and
supplemental query tables.

## Procedure

1 Change to the Business Process Choreographersubdirectory where the administrative script is located.
    - install\_root/ProcessChoreographer/admin
    - install\_root\ProcessChoreographer\admin
2. To list the XML definition of a query table in the command
prompt window.  Enter the following
command:
install\_root/bin/wsadmin.sh -f manageQueryTable.py
       -cluster clusterName
       -query definition 
       -name queryTableNameEnter the following command:
install\_root\bin\wsadmin -f manageQueryTable.py
       -cluster clusterName
       -query definition 
       -name queryTableNameWhere: 
-cluster clusterName
The name of the cluster where Business Process Choreographer is
configured. In a multicluster setup, you must specify the application
cluster because that is where Business Process Choreographer is configured.
-name queryTableName
The name of the query table, in uppercase, whose XML definition
is to be listed.

## Example

Enter the following
command:

```
wsadmin.sh -f manageQueryTable.py -cluster myCluster 
           -query definition -name COMPANY.SAMPLE
```

Enter the following command:

```
wsadmin -f manageQueryTable.py -cluster myCluster 
        -query definition -name COMPANY.SAMPLE
```

<!-- image -->