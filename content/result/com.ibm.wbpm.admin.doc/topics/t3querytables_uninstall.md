<!-- image -->

# Undeploying composite and supplemental query tables

## Before you begin

- Run the script in connected mode,
that is, do not use the wsadmin -conntype none option.
- At least one cluster member must be running.
- Include the wsadmin -user and -password options
to specify a user ID that has administrator or deployer authority.
- If you are not working with the default
profile, use the wsadmin -profileName profile option
to specify the profile.
- Ensure that no applications are running that reference a query
table that is to be undeployed. If a supplemental query table is undeployed,
it must not be referenced, as attached query table, by any composite
query table.

## About this task

## Procedure

1 Change to the Business Process Choreographersubdirectory where the administrative script is located.
    - install\_root/ProcessChoreographer/admin
    - install\_root\ProcessChoreographer\admin
2. Undeploy the query table:  Enter the following
command:
install\_root/bin/wsadmin.sh -f manageQueryTable.py
       -cluster clusterName
       -undeploy queryTableName
Enter the following command:
install\_root\bin\wsadmin -f manageQueryTable.py
       -cluster clusterName) ]
       -undeploy queryTableName
Where: 
-cluster clusterName
The name of the cluster where Business Process Choreographer is
configured. In a multicluster setup, you must specify the application
cluster because that is where Business Process Choreographer is configured.
-undeploy queryTableName
The name of the query table. Use this option to undeploy a query
table.

## Example

Enter the following
command:

```
wsadmin.sh -f manageQueryTable.py -cluster myCluster -undeploy COMPANY.SAMPLE
```

Enter the following command:

```
wsadmin -f manageQueryTable.py -cluster myCluster -undeploy COMPANY.SAMPLE
```

<!-- image -->