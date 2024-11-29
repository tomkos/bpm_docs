# BPMGroupMembershipUpdateTask command

If you pass a user ID that is not known to Business Automation Workflow, the user ID is synchronized from the WebSphere Application
Server user registry into the Business Automation Workflow database.

You can also perform this task by using the groupMembershipUpdate.[bat|sh]
script. For more information, see Synchronizing group membership by users.

The BPMGroupMembershipUpdateTask command is run using the AdminTask object of
the wsadmin scripting client.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
BPMGroupMembershipUpdateTask
-dynamicGroupUpdate default|never|always
-userIds [username\_1 username\_2... username\_n]
```

## Parameters

## Example

```
wsadmin -conntype SOAP -port 8880 -host PC1.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMGroupMembershipUpdateTask('[-dynamicGroupUpdate always, -userIds [username\_1 username\_2]]')
```