<!-- image -->

# Refreshing people query results, using administrative scripts

## Before you begin

- Run the script in connected mode,
that is, do not use the wsadmin -conntype none option.
- At least one cluster member must be running.
- Include the wsadmin -user and -password options
to specify a user ID that has operator authority.
- If you are not working with the default
profile, use the wsadmin -profileName profile option
to specify the profile.

## About this task

Business
Process Choreographer caches the results of people queries, which
have been evaluated against a people directory, such as a Lightweight
Directory Access Protocol (LDAP) server, in the runtime database.
If the people directory changes, you can force the people assignments
to be evaluated again.

## Procedure

1. Change to the Business Process Choreographer
subdirectory where the administrative script is located. 
Enter the following
command:cd install\_root/ProcessChoreographer/admin
Enter the following command:cd install\_root\ProcessChoreographer\admin
2. Force the people assignment to be evaluated again. 
Enter the following
command:
install\_root/bin/wsadmin.sh -f refreshStaffQuery.py 
       -cluster clusterName
       [-processTemplate templateName | 
       (-taskTemplate templateName [-nameSpace nameSpace]) | 
        -userlist username{,username}...]
Enter the following command:
install\_root\bin\wsadmin -f refreshStaffQuery.py 
       -cluster clusterName
       [-processTemplate templateName | 
       (-taskTemplate templateName [-nameSpace nameSpace]) | 
        -userlist username{,username}...]
Where:

-cluster clusterName
The name of the cluster where Business Process Choreographer is
configured. In a multicluster setup, you must specify the application
cluster because that is where Business Process Choreographer is configured.
-processTemplatetemplateName
The name of the process template. People assignments that belong
to this process template are refreshed.
-taskTemplatetemplateName 
The name of the task template. People assignments that belong
to this task template are refreshed. The refresh is not performed
for the default user, but for the staff queries that model task roles.
If the refresh fails, then the queries for the fallback user are not
refreshed, for example, for the process administrators.
-nameSpacenameSpace 
The target namespace of the task template.
-userlistuserName
A comma-separated list of user names. People assignments that
contain the specified names are refreshed. The user list can be
surrounded by quotation marks. If the quotation marks are omitted
the user list must not contain blanks between the user names. 

Note: If you do not specify any templateName nor userlist,
all people queries that are stored in the database are refreshed.
You might want to avoid this for performance reasons.
3. Optional: If the
script triggers long-running work, the script might fail if the connection
timeout is not long enough to complete the action. Check the SystemOut.log file
to see whether you need to restart the script. If the timeout happens
often, consider increasing the value of the timeout property for the
connector you are using, or adjusting the script parameters to reduce
the amount of work done.  For
more information about this connection timeout, see Connection timeout when running a wsadmin script.

<!-- image -->