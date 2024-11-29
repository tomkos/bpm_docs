# BPMSyncExistingUsersTask command

You can also synchronize existing users by using the
syncExistingUsers.[bat|sh] script, as described in Synchronizing users
or by calling the REST API that is described in Synchronizing
users between the BPM database and the user registry.

- Force the use of one VMM call per user by changing the threshold
value to reflect the actual number of users in the user registry.
- Contact your LDAP administrator to adjust the LDAP configuration
so that all users can be retrieved in one LDAP search call.

The output of the command contains the number
of synchronized users.

The BPMSyncExistingUsersTask command
is run using the AdminTask object of the wsadmin scripting client.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
BPMSyncExistingUsersTask
[-userState sync|any\_other\_value] [-userIds [username\_1 username\_2 ... username\_n]]
```

## Parameters

The command has no parameters
in Business Automation Workflow Version
8.5.7.0 Cumulative Fix 2016.06 and earlier versions.

- Users who were deleted from the user registry become inactive
in the Business Automation Workflow database.
- Users who are reactivated in the user registry become active in
the Business Automation Workflow database.

## Examples

```
wsadmin -conntype SOAP -port 8880 -host PC1.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMSyncExistingUsersTask('[-userState sync]')
```

```
wsadmin -conntype SOAP -port 8880 -host PC1.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMSyncExistingUsersTask('[-userState sync, -userIds [username\_1 username\_2]]')
```

## Configuration

- For 1000 or fewer available users, calls are sent for each user
(user-by-user).
- For more than 1000 users, one call for all users is sent.

- The value of the configurationProvider->maxSearchResults property
is appropriate for the value of the threshold property
- The configuration of the associated user repository, for example,
LDAP, doesn't limit the total number of returned search results.

```
<common merge="mergeChildren">
   <security>
      <threshold-for-existing-user-retrieval-mode merge="replace">1000</threshold-for-existing-user-retrieval-mode>
   </security>
</common>
```