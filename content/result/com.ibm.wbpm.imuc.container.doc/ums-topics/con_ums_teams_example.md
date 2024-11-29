# Examples: Using the User Management Service Teams REST
API

- Creating a new team
- Creating a new team that includes an existing team
- Retrieving a team
- Incrementally updating a team
- Replacing a team
- Retrieving a list of teams that you are a member of
- Deleting a team

## Creating a new team

```
POST /teamserver/rest/teams
```

To add users and groups as member of the new team, you must provide their distinguished names
from the connected LDAP repository. To include another team, you must specify its internal ID
(uuid).

```
{
  "distinguishedName": "cn=Authors,ou=bpm,dc=example,dc=com",
  "displayName": "Authors",
  "description": "This team writes the technical documentation.",
  "users": [
    "cn=John Doe,ou=User,dc=example,dc=com",
    "cn=Joe Bloggs,ou=User,dc=example,dc=com"
  ],
  "groups": [
    "cn=Department 4711,ou=Group,dc=example,dc=com"
  ]
}
```

```
{
  "description": "This team writes the technical documentation.",
  "displayName": "Authors",
  "distinguishedName": "cn=authors,ou=bpm,dc=example,dc=com",
  "groups": [
    "cn=Department 4711,ou=Group,dc=example,dc=com"
  ],
  "metadata": {
    "created": "2020-02-18T14:28:33.040Z",
    "lastModified": "2020-02-18T14:28:33.040Z"
  },
  "teams": [],
  "users": [
    "cn=Joe Bloggs,ou=User,dc=example,dc=com",
    "cn=John Doe,ou=User,dc=example,dc=com"
  ],
  "uuid": "e60d02c1-7e55-4534-81f8-b3c079e83ee3"
}
```

## Creating a new team that includes an existing team

```
{
  "distinguishedName": "cn=Reviewers,ou=bpm,dc=example,dc=com",
  "displayName": "Reviewers",
  "description": "This team is responsible for reviewing the documentation.",
  "teams": [
    "e60d02c1-7e55-4534-81f8-b3c079e83ee3"
  ]
}
```

## Retrieving a team

```
GET /teamserver/rest/teams/{uuid}
```

```
GET /teamserver/rest/teams/e60d02c1-7e55-4534-81f8-b3c079e83ee3
```

```
{
  "description": "This team writes the technical documentation.",
  "displayName": "Authors",
  "distinguishedName": "cn=authors,ou=bpm,dc=example,dc=com",
  "groups": [
    "cn=Department 4711,ou=Group,dc=example,dc=com"
  ],
  "metadata": {
    "created": "2020-02-18T14:28:33.040Z",
    "lastModified": "2020-02-18T14:28:33.040Z"
  },
  "teams": [],
  "users": [
    "cn=Joe Bloggs,ou=User,dc=example,dc=com",
    "cn=John Doe,ou=User,dc=example,dc=com"
  ],
  "uuid": "e60d02c1-7e55-4534-81f8-b3c079e83ee3"
}
```

## Incrementally updating a team

```
PATCH /teamserver/rest/teams/{uuid}
```

```
PATCH /teamserver/rest/teams/e60d02c1-7e55-4534-81f8-b3c079e83ee3
```

```
{
  "operations": [
    {
      "op": "replace",
      "path": "description",
      "value": "This team is responsible for the product documentation."
    }
  ]
}
```

## Replacing a team

```
PUT /teamserver/rest/teams/{uuid}
```

```
PUT /teamserver/rest/teams/e60d02c1-7e55-4534-81f8-b3c079e83ee3
```

```
{
  "distinguishedName": "cn=Authors,ou=bpm,dc=example,dc=com",
  "displayName": "Authors",
  "description": "This team is responsible for the product documentation.",
  "users": [
    "cn=Joe Bloggs,ou=User,dc=example,dc=com"
  ],
  "groups": [
    "cn=Department 4711,ou=Group,dc=example,dc=com"
  ]
}
```

## Retrieving a list of teams that you are a member of

```
GET /teamserver/rest/teams?my\_teams=true
```

```
GET /teamserver/rest/teams?my\_teams=true&filter=displayName SW "Aut"
```

```
{
  "items": [
    {
      "description": "This team is responsible for the product documentation.",
      "displayName": "Authors",
      "distinguishedName": "cn=authors,ou=bpm,dc=example,dc=com",
      "groups": [
        "cn=Department 4711,ou=Group,dc=example,dc=com"
      ],
      "metadata": {
        "created": "2020-02-18T14:28:33.040Z",
        "lastModified": "2020-02-18T14:33:57.688Z"
      },
      "teams": [],
      "users": [
        "cn=Joe Bloggs,ou=User,dc=example,dc=com"
      ],
      "uuid": "e60d02c1-7e55-4534-81f8-b3c079e83ee3"
    }
  ],
  "metadata": {
    "startIndex": 1,
    "totalSize": 1
  }
}
```

## Deleting a team

```
DELETE /teamserver/rest/teams/{uuid}
```

The delete request removes the corresponding team from the database and also removes all
references from other teams to that team.

```
DELETE /teamserver/rest/teams/e60d02c1-7e55-4534-81f8-b3c079e83ee3
```