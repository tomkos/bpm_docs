# Configuring a basic user registry for IBM® Process Federation
Server

## About this task

- The user registry realm name is the same in Process Federation Server and federated systems
- The user name in Process Federation Server basic
registry is a fully qualified name that has the following
format:uid=%user security name%, %base dn%For example,
uid=admin,o=defaultWIMFileBasedRealm.

## Procedure

```
<basicRegistry realm="defaultWIMFileBasedRealm" 
   <user name="uid=admin,o=defaultWIMFileBasedRealm" password="admin" />
   <user name="uid=johndoe,o=defaultWIMFileBasedRealm" password="password" />
 </basicRegistry>
```

- Use unique names for each user and group.
- Remove all trailing and leading spaces from the user and group names.
- If user IDs or passwords contain characters other than US-ASCII characters, save the file by
using UTF-8 character encoding.
- If you edit the server.xml file directly, you can use the
securityUtility encode command to encode the password for each user. The
securityUtility encode command-line tool is available in the
pfs\_install\_root/bin directory. For more information, see
Liberty profile: securityUtility command
- Log in to the federated system with the short user name, for example
admin or johndoe.
- Log in to Process Federation Server with the fully
qualified user name, for example, uid=admin,o=defaultWIMFileBasedRealm.