# BPMGroupMembershipFullUpdateTask command

The BPMGroupMembershipFullUpdateTask
command is run using the AdminTask object of the wsadmin scripting client.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
BPMGroupMembershipFullUpdateTask
-dynamicGroupUpdate default|never|always
```

## Parameters

## Example

```
wsadmin -conntype SOAP -port 8880 -host PC1.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMGroupMembershipFullUpdateTask('[-dynamicGroupUpdate always]')
```