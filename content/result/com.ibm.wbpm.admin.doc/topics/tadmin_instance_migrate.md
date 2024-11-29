<!-- image -->

# Migrating BPEL process instances in bulk to a new version of
a process template

## Before you begin

- Run the script in the connected mode, that is,
do not use the wsadmin -conntype none option.
- At least one cluster member must be running.
- Include the wsadmin -user and -password options
to specify a user ID that has administrator authority.
- If you are not working with the default
profile, use the wsadmin -profileName profile option
to specify the profile.

## About this task

Use the migrateProcessInstances.py script
to migrate instances of a specific process template version to the
latest version, or a specified version. Instances that are in an end
state (finished, terminated, compensated, or failed) are not migrated.
Only instances of the specified template with the same version as
the specified valid from value are migrated. If you prefer
to write a script to migrate instances, an MBean interface is available.

## Procedure

1. Change to the Business Process Choreographer
subdirectory where the administrative script is located.  Enter the following
command:cd install\_root/ProcessChoreographer/admin
Enter the following command:cd install\_root\ProcessChoreographer\admin
2. Migrate the instances of process templates that are no
longer valid.  Enter the following
command:
install\_root/bin/wsadmin.sh -f migrateProcessInstances.py
        -cluster cluster\_name
       ( -templateName template\_name) 
       (-sourceValidFromUTC timestamp) 
       [(-targetValidFromUTC timestamp)]
       [(-slice slice\_sizeEnter the following command:
install\_root\bin\wsadmin -f migrateProcessInstances.py
       -cluster cluster\_name 
       (-templateName template\_name) 
       (-sourceValidFromUTC timestamp) 
       [(-targetValidFromUTC timestamp)]
       [(-slice slice\_sizeWhere:

-cluster clusterName
The name of the cluster where Business Process Choreographer is
configured. In a multicluster setup, you must specify the application
cluster because that is where Business Process Choreographer is configured.
-templateNametemplate\_name
The name of the process template to be migrated. 
-sourceValidFromUTCtimestamp
The timestamp specifies which version of the named template will
have its instances migrated. The timestamp string
specifies the date from which the template is valid, in Coordinated
Universal Time (UTC), and must have the following format: yyyy-mm-ddThh:mm:ss (year,
month, day, T, hours, minutes, seconds). For example, 2009-01-31T13:40:50.
In the administrative console this date is displayed in local time
of the server, so make sure that you take the server time zone into
account.

-targetValidFromUTCtimestamp
This optionally specifies which version of the named process template
the instances will be migrated to. If this parameter is not specified,
the latest available version of the template will be used. The timestamp string
has the same format as for the sourceValidFromUTC parameter.
-sliceslice\_size
This parameter is optional. The value slice\_size specifies
how many process instances are migrated in one transaction. The default
value is 10.
3. When the script runs, it outputs the name of the cluster
where the migration is running. Check the SystemOut.log file to see the progress information and whether the migration of
any instances caused any exceptions. For example, because instances
are not in a suitable state or because a problem occurred during migration.

## Results

<!-- image -->