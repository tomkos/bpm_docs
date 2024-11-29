<!-- image -->

# refreshStaffQuery.py administrative script

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
-f refreshStaffQuery.py 
       -cluster clusterName
       [-processTemplate templateName | 
       (-taskTemplate templateName [-nameSpace nameSpace]) | 
        -userlist username{,username}...]
```

## Parameters