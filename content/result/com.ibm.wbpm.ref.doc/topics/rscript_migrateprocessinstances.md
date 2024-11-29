<!-- image -->

# migrateProcessInstances.py administrative script

Use the migrateProcessInstances.py script
to migrate instances of a specific process template version to the
latest version, or a specified version. Instances that are in an end
state (finished, terminated, compensated, or failed) are not migrated.
Only instances of the specified template with the same version as
the specified valid from value are migrated. If you prefer
to write a script to migrate instances, an MBean interface is available.

## Prerequisites

- Run the script in the connected mode, that is,
do not use the wsadmin -conntype none option.
- At least one cluster member must be running.
- Include the wsadmin -user and -password options
to specify a user ID that has administrator authority.
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
-f migrateProcessInstances.py
        -cluster cluster\_name
       ( -templateName template\_name) 
       (-sourceValidFromUTC timestamp ) 
       [(-targetValidFromUTC timestamp )]
       [(-slice slice\_size
```

## Parameters

The timestamp string
specifies the date from which the template is valid, in Coordinated
Universal Time (UTC), and must have the following format: yyyy-mm-ddThh:mm:ss (year,
month, day, T, hours, minutes, seconds). For example, 2009-01-31T13:40:50.
In the administrative console this date is displayed in local time
of the server, so make sure that you take the server time zone into
account.