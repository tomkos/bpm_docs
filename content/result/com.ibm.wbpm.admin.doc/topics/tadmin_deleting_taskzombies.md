<!-- image -->

# Deleting human task templates that are no longer valid

## Before you begin

You must know both the name of
the template and the ValidFromUTC value for the
template that you want to delete. If you do not have that information,
perform Listing information about process and task templates first.

- Run the script in the connected mode, that is,
do not use the wsadmin -conntype none option.
- You must have either operator or deployer
authority.
- At least one cluster member must be running.
- If you are not working with the default
profile, use the wsadmin -profileName profile option
to specify the profile.

## About this task

The deleteInvalidTaskTemplate.py script
removes from the database those templates, and all objects that belong
to them, that are not contained in any corresponding valid application
in the WebSphere® configuration
repository. This situation can occur if deploying an application was
canceled or the application was not stored in the configuration repository
by the user. These templates usually have no impact. They are not
shown in Business Process Choreographer Explorer.

You cannot use this script
to remove templates of valid applications from the database. This
condition is checked and a ConfigurationError exception is thrown
if the corresponding application is valid.

## Procedure

1. Change to the Business Process Choreographer
subdirectory where the administrative script is located. 
Enter the following
command:cd install\_root/ProcessChoreographer/admin
Enter the following command:cd install\_root\ProcessChoreographer\admin
2. Delete, from the database, human task templates that are
no longer valid. Enter the following
command:
install\_root/bin/wsadmin.sh -f deleteInvalidTaskTemplate.py
     -cluster cluster\_name
     -templateName templateName
     -validFromUTC timestamp
     -nameSpace nameSpaceEnter the following command:
install\_root\bin\wsadmin -f deleteInvalidTaskTemplate.py
    -cluster cluster\_name
     -templateName templateName
     -validFromUTC timestamp
     -nameSpace nameSpaceWhere:
-cluster clusterName
The name of the cluster where Business Process Choreographer is
configured. In a multicluster setup, you must specify the application
cluster because that is where Business Process Choreographer is configured.
-templateNametemplateName
The name of the template to be deleted.
-validFromUTCtimestamp
The date and time from which the template is valid in Coordinated
Universal Time (UTC). The string must have the following format: yyyy-MM-ddThh:mm:ss (year,
month, day, T, hours, minutes, seconds). For example, 2005-01-31T13:40:50
-nameSpacenameSpace 
The target namespace of the task template.
3. Optional: If the
script triggers long-running work, the script might fail if the connection
timeout is not long enough to complete the action. Check the SystemOut.log file
to see whether you need to restart the script. If the timeout happens
often, consider increasing the value of the timeout property for the
connector you are using, or adjusting the script parameters to reduce
the amount of work done.

<!-- image -->