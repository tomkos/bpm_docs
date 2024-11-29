<!-- image -->

# dbUtility.py administrative script

## Prerequisites

- You cannot run the script on the deployment manager node.
- You must run the script on the node of a
cluster member that you specify.
- The cluster members must not be running.
- The script must be run in disconnected mode by including the -conntype NONE
option.

## Location

```
install\_root\ProcessChoreographer\admin
install\_root/ProcessChoreographer/admin
```

## Syntax

```
wsadmin -conntype NONE [-profileName profileName]  -f dbUtility.py
       -cluster clusterName
       [-dbUser userID] [-dbPassword password] 
       [-dbSchema schema]
       [-slice slice]
       (-testConnection | (-check (all | SharedWorkItems)) | (-repair (all | SharedWorkItems))]
```

## Parameters

## Example: Checking the shared work items

To run the script on the node of a member of the cluster my\_cluster, to check how many inconsistent elements there
are for the shared work item resource, using the current user ID to
connect to the database using the password secret.

<!-- image -->

<!-- image -->

```
wsadmin.sh -conntype none -f ../../ProcessChoreographer/admin/dbUtility.py -cluster my\_cluster -dbPassword secret -check SharedWorkItems
```

<!-- image -->

```
wsadmin.bat -conntype none -f ..\..\ProcessChoreographer\admin\dbUtility.py -cluster my\_cluster -dbPassword secret -check SharedWorkItems
```

```
dbUtility.py finished with the following results:
------------------------------------------------------------------------------------

SharedWorkItems:        2 elements need to be repaired.

************************************************************************************
NOTE: If the utility has found elements that need to be repaired, run anksthe script
again with the '-repair' option.
************************************************************************************
```

## Example: Repairing shared work items

Running
the script on the node of a member of the cluster my\_cluster, to repair all inconsistent elements for the shared work item resource,
using the current user ID to connect to the database using the password secret, and a transaction size of 100.

<!-- image -->

<!-- image -->

```
wsadmin.sh -conntype none -f ../../ProcessChoreographer/admin/dbUtility.py -cluster my\_cluster -dbPassword secret -repair SharedWorkItems -slice 100
```

<!-- image -->

```
wsadmin.bat -conntype none -f ..\..\ProcessChoreographer\admin\dbUtility.py -cluster my\_cluster -dbPassword secret -repair SharedWorkItems -slice 100
```

```
dbUtility.py finished with the following results:
------------------------------------------------------------------------------------

SharedWorkItems:        2 elements were repaired.

************************************************************************************
NOTE: The number of repaired elements can be higher than the number of elements
found using the '-check' option if dependant elements were also repaired.
************************************************************************************
```