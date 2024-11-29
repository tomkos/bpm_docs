<!-- image -->

# Undeploying BPEL process and human task applications, using
an administrative command

## Before you begin

- If the application is deployed on a stand-alone server,
the server must be running and have access to the Business Process
Choreographer database.
- If the application is deployed on a cluster, the deployment
manager and at least one cluster member must be running. The cluster
member must have access to the Business Process Choreographer database.
- If the application is deployed on a managed server, the
deployment manager and the managed server must be running. The server
must have access to the Business Process Choreographer database.
- Ensure that the server process to which the administrative client
connects is running. To ensure that the administrative client automatically
connects to the server process, do not use the -conntype NONE option as a command option.
- Include the wsadmin -user and -password options
to specify a user ID that has operator or administrator authority. The
-uninstall option requires operator authority and the -force
option requires administrator authority.
- One or more of the following is true:
    - There are no instances of BPEL process or human task templates
present in any state.
    - You intend to use the -force option.
    - You have a stand-alone server that is running
in development mode.
- If a process instance was migrated to a newer version of
the process but it is waiting for a service invocation to reply, the
application that contains the previous version cannot be undeployed
until the reply is received. In all other cases, instances that have
been migrated are considered to be instances of the new version, and
the application that contains the older version of the process can
be undeployed.
- Make sure that no other modules depend on
the services exported by the application that you want to undeploy.

## About this task

The following steps describe how to use the manageTemplates.py script to undeploy applications that
contain BPEL process templates or human task templates.

## Procedure

1 If there are still process instances or task instancesassociated with the templates in the application that you want toundeploy, perform one or both of the following actions:
    - Use the Business Process Choreographer Explorer to delete
the instances.
    - In cases where you are sure that no other BPEL processes depend
on the process templates that are defined in the application you want
to undeploy, you can use the -force option. CAUTION:If you use the script with this option, it deletes
any instances that are associated with the templates, all of the data
that is associated with any running instances, stops the templates,
and undeploys the application in one step. Use this option with extreme
care.
2. Change to the Business Process Choreographer
subdirectory where the administrative script is located.
 Enter the following
command:cd install\_root\ProcessChoreographer\admin
cd install\_root/ProcessChoreographer/admin
3. Stop the templates and undeploy the corresponding application. 
Enter the following
command:wsadmin -f manageTemplates.py -uninstall application\_name
wsadmin.sh -f manageTemplates.py -uninstall application\_namewhere 
-uninstall application\_name
This specifies the name of the application to be undeployed. Do
not use this option for applications that were deployed using Workflow Center.
-force
This option causes any running instances to be stopped and deleted before the application is
undeployed. Use this option with care because it also deletes all of the data that is associated
with the running instances.
-wait seconds
This option allows you to define a custom wait time in seconds so you can verify whether the
application disappeared from the installed application list after a successful uninstallation. If no
parameter is defined, the default wait time of 5 seconds is used.

## Results