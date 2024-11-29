# Traditional: 
Synchronizing
users between the Business Automation Workflow database and the user registry

You can also perform these tasks by using the AdminTask object
of the wsadmin scripting client. For more information, see BPMUsersSyncTask, BPMUsersFullSyncTask, and BPMSyncExistingUsersTask command.

| Command           | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| usersSync         | Updates the information for a set of specified users. You can also use this command to create specific users in the Business Automation Workflow database who are already available in the user registry. If you specify a user who is not available in the user registry, the user is skipped.                                                                                                                                                                                    |
| syncExistingUsers | Updates information for existing users in the Business Automation Workflow database but does not import new users from the user registry into the database. You can also use this command to synchronize the user state for users in the Business Automation Workflow database with the user availability in the user registry. For example, if users were deleted from the user registry, the command marks these users as inactive in the Business Automation Workflow database. |
| usersFullSync     | Imports all the user information from the user registry into the Business Automation Workflow database. If the user registry contains new users, these users are created in the Business Automation Workflow database.Attention: Use this command with care. Because all the users in the user registry are imported into the Business Automation Workflow database, the command might also import users who do not use Business Automation Workflow.                              |

- Force the use of one VMM call per user by changing the threshold
value to reflect the actual number of users in the user registry.
- Contact your LDAP administrator to adjust the LDAP configuration
so that all users can be retrieved in one LDAP search call.

The output of the commands contains the number of synchronized
users.

## Location

## usersSync syntax

```
usersSync.[bat|sh]
  -username|-u|-user user\_name
  -password|-p password
  [-host host\_name]
  [-port port]
  username\_1 username\_2 ... username\_n
```

## syncExistingUsers syntax

```
syncExistingUsers.[bat|sh]
  -username|-u|-user user\_name
  -password|-p password
  [-userState sync|any\_other\_value]
  [-host host\_name]
  [-port port]
  [username\_1 username\_2 ... username\_n]
```

## usersFullSync syntax

```
usersFullSync.[bat|sh]
  -username|-u|-user user\_name
  -password|-p password
  [-host host\_name]
  [-port port]
```

## Parameters

- Users who were deleted from the user registry become inactive
in the Business Automation Workflow database.
- Users who are reactivated in the user registry become active in
the Business Automation Workflow database.

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
    <vmm-options>                                                             
      <threshold-for-existing-user-retrieval-mode>1000</threshold-for-existing-user-retrieval-mode>                             
    </vmm-options>                                                            
  </security>                                                               
</common>
```