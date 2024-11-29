# createObjectStoreForContent command

If you configured IBM® Business Automation
Workflow to use an external
Content Platform Engine, you do not need to run this command.

The createObjectStoreForContent command is run using the AdminTask object of
the wsadmin scripting client.

## Prerequisites

- Run the command on an application cluster member.
- One or more application cluster members must be running.
- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- You must connect to an application cluster member with a user ID that has the WebSphere® Application
Server operator or deployer role.  See Administrative roles for information about roles.

## Location

Start the wsadmin scripting client from the
install\_root/profiles/deployment\_manager\_profile/bin
directory on either Workflow Server or Workflow Center.

The createObjectStoreForContent command does not write to a log file, but the
wsadmin scripting client always writes a
profile\_root/logs/wsadmin.traceout log file where you will
find exception stack traces and other information.

## Syntax

```
createObjectStoreForContent
-clusterName cluster\_name
-PEWorkflowSystemAdminGroup group\_name
-creationUser user\_name
-password password
```

## Required Parameters

## Example

The examples are for illustrative purposes only. They include variable values and are not meant
to be reused as snippets of code.

```
wsadmin -user admin -password admin -host localhost -port 8881 -lang jython
```

```
wsadmin -lang jython -user deadmin -password deadmin -host localhost -port 8880
print AdminTask.createObjectStoreForContent(['-clusterName', 'AppCluster', '-PEWorkflowSystemAdminGroup', 'adminGroup2','-creationUser','deadmin','-password','deadmin\_pw'])
```

```
wsadmin -lang jython -user deadmin -password deadmin -host localhost -port 8880
print AdminTask.createObjectStoreForContent(['-clusterName', 'app', '-PEWorkflowSystemAdminGroup', 'managergroup1','-creationUser','managergroup1user1','-password','managergroup1user1\_pwd'])
```

After you run the command for VMM with LDAP, go to the WebSphere Application
Server administrative console and click Applications > Application Types > WebSphere enterprise applications >  IBM\_BPM\_DocStoreAdmin\_cluster name. Click Security role to user/group mapping, select
DOC\_STORE\_ADMIN\_USERS and click Map Groups. Search for
the LDAP group you used above (managergroup1 in the example), click the arrow to
put the group into the selected column, click OK, and save the changes.

## Rerunning the createObjectStoreForContent command