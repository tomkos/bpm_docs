# Restricting installation access to runtime servers

## About this task

- The user needs the following access to the process application depending on the type of target environment: For more information about providing permissions to users and groups, see Managing access to workflow projects .Note: To create a generic deployment package, you need read accessonly.
    - Administrative access to install to process servers in production environments
    - Write access to install to any non-production process server
    - Read access to install to process servers in development environments
- If the processCenterInstall group is enabled, the user must be a member of
the processCenterInstall group. The processCenterInstall group
must exist on Workflow Center
and you must be a part of this group in Workflow Center for the online
deployment to work.

- The user must be a member of tw\_admins or the BPMAuthor user and a member of tw\_authors. Important: If these internal groups, which are created when the deployment environment is
created, are deleted, you won't be able to deploy snapshots.
- If the offlineInstall group is enabled, the user must be a member of the
offlineInstall group to run offline deployment commands.

## Procedure

To enable a processCenterInstall or offlineInstall group,
perform the following steps on the Workflow Server deployment manager.

1. Start the wsadmin scripting tool. To start wsadmin using
the Jython language, run the following command from the bin directory of the
server profile: 

wsadmin -conntype NONE -lang jython
2. Extract the properties of the BPMProcessServer configuration object.

wsadmin> groups = AdminConfig.list('BPMServerSecurityGroups')
wsadmin> print AdminConfig.show(groups)
3. View the output and note the processCenterInstall or
offlineInstall value. For example, [processCenterInstall
Existing\_group\_name] or [offlineInstall Existing\_group\_name].

Note: If processCenterInstall or offlineInstall is missing,
the group is not enabled.
4. Update the processCenterInstall or offlineInstall
value.

wsadmin> AdminConfig.modify(groups, [['processCenterInstall', 'New-Group-Name']])
wsadmin> AdminConfig.modify(groups, [['offlineInstall', 'New-Group-Name']])
where the New\_group\_name variable represents the group of users you want to
grant access to. The group must exist in the user repository or be an internal group that is managed
in the Process Admin Console.
5. Verify your update. 

wsadmin> print AdminConfig.show(groups)
6. Save the changes and exit.

wsadmin> AdminConfig.save()
wsadmin> exit
7. When the changes have been synchronized to the nodes, restart the application cluster for the
changes to take effect.