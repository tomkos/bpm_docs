# User Management Service  Teams access control

- Global access permissions
- Team scoped access permissions

## Global access permissions

The following permissions provide access control for all teams.

- All members of the J2EE role teamserveradmin.
- All members of the global administrators team, which has the uuid
10000000-0000-0000-0000-000000000000.

- The user is member of the creators team, which has the uuid
20000000-0000-0000-0000-000000000000.
- The user is a global administrator.

- GET /teamserver/rest/groups
- GET /teamserver/rest/users

- The user is a global administrator.
- The user is member of the "creators" team, which has the uuid
20000000-0000-0000-0000-000000000000.
- The user is member of the "repository readers" team, which has the uuid
30000000-0000-0000-0000-000000000000.
- If the user passes the uuid of a team as context and has the permission to update that team.
When a user can update a team, the user  also has a reasonable need for obtaining the list of users
or groups from the user repository.

- PUT /teamserver/rest/teams/uuid
- PATCH /teamserver/rest/teams/uuid

```
PUT /teamserver/rest/teams/30000000-0000-0000-0000-000000000000
```

## Team scoped access permissions

## What the owner of a team can and can't do

The owner (or administrator) of team has the permission to choose which user should be the owner
of the team, or which team should be used as reader team, writer team, or administrator team. This
does however not imply any permissions on the chosen team.

```
{
  "uuid": "a1c81405-429a-4fc2-803e-b6e8cf03f7f1",
  "distinguishedName": "cn=exampleteam,ou=team,dc=example,dc=com",
  "displayName": "Example Team",
  "description": "This is a new team",
  "users": [
    "cn=John Doe,ou=User,dc=example,dc=com",
    "cn=Jane Doe,ou=User,dc=example,dc=com"
  ],
  "groups": [
    "cn=Example,ou=Group,dc=example,dc=com"
  ],
  "teams": [
    "a3c90404-419a-4fc5-804e-b7e9cf14f8f2"
  ],
  "admin": {
    "owner": "cn=John Doe,ou=User,dc=example,dc=com",
    "administratorTeam": "aabb0000-517a-44de-413e-a78ccef3f2f2",
    "writerTeam": "ccdd0101-517a-34de-112e-a7616273f343",
    "readerTeam": "eeff0202-732a-5a4f-ee12-b86211c79ff1",
  }
  "metadata": {
    "created": "2020-10-25T14:37:08.198Z",
    "lastModified": "2020-10-25T14:37:08.198Z"
  }
}
```