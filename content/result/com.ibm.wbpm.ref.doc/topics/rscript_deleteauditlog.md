<!-- image -->

# deleteAuditLog.py administrative script

## Prerequisites

- Run the script in connected mode,
that is, do not use the wsadmin -conntype none option.
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

-f deleteAuditLog.py 
       -cluster cluster\_name
       ( -all | -timeUTC timestamp | -timeLocal timestamp 
              | -processtimeUTC timestamp | -processtimeLocal timestamp )
       [-slice size]
```

## Parameters