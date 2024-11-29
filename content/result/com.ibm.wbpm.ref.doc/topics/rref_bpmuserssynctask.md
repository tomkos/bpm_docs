# BPMUsersSyncTask command

You can also perform this task by using the usersSync.[bat|sh] script. For
more information, see Synchronizing users.

In the case of
usersSync, one VMM call per user is used.

The output of the command contains the number of synchronized users.

The BPMUsersSyncTask command is run using the AdminTask object of the wsadmin
scripting client.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
BPMUsersSyncTask
-userIds [username\_1 username\_2 ... username\_n]
```

## Parameters

## Example

```
wsadmin -conntype SOAP -port 8880 -host PC1.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMUsersSyncTask('[-userIds [username\_1 username\_2]]')
```

## Configuration