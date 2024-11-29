# BPMUsersFullSyncTask command

Traditional: 
Use the BPMUsersFullSyncTask command to import all the user
information from the WebSphere® Application
Server user registry into
the IBM® Business Automation
Workflow database. If the user registry
contains new users, these users are created in the Business Automation Workflow database.

You can also perform this task by using the usersFullSync.[bat|sh] script.
For more information, see Synchronizing users.

The output of the command contains the number of synchronized users.

The BPMUsersFullSyncTask command is run using the AdminTask object of the
wsadmin scripting client.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
BPMUsersFullSyncTask
```

## Parameters

The command has no parameters.

## Example

```
wsadmin -conntype SOAP -port 8880 -host PC1.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMUsersFullSyncTask()
```

## Configuration