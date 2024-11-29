# User Management Service Teams GraphQL example
queries

- GET API
- POST API
- Using GET to request the display name of a specific team
- Using POST to request the display name of a specific team
- Requesting more details for a specific team
- Using variables in queries
- Operation names
- Requesting a list of teams
- Requesting a list of teams with a filter
- Requesting information about the current user
- Checking if the current user is a member of any of the provided teams
- Checking the permissions of the current user:

## GET API

```
GET https://host:port/teamserver/rest/graphql?query=someQuery&variables=someVariableMap&operation\_name=opName
```

- query - The query string in GraphQL format.
- variables - A variable map in JSON format.
- operation\_name - A name selecting a named query if the query string contains multiple
named queries.

## POST API

```
POST https://{host}:{port}/teamserver/rest/graphql
```

```
{
    "query" : "{ team(uuid:\"72d8e3b6-d4a3-4d0f-a5a7-2e63cea03460\") { displayName }}"
}
```

```
{
    "query" : "....",
    "variables" : {
        "variable1" : "Test",
        "variable2" : 123
    },
    "operationName" : "TestOp"
}
```

## Using GET to request the display name of a specific team

```
{ team(uuid:"72d8e3b6-d4a3-4d0f-a5a7-2e63cea03460") { displayName }}
```

```
curl -i -k -H "Authorization: Bearer oauthtoken" -H "Accept: application/json" -H "Content-Type: application/json" -X POST https://host:port/teamserver/rest/graphql -d '{ "query" : "{ team(uuid:\"72d8e3b6-d4a3-4d0f-a5a7-2e63cea03460\") { displayName }}" }'
Reply
```

```
{
    "data": {
        "team": {
            "displayName": "Team3"
        }
    }
}
```

## Using POST to request the display name of a specific team

```
{
    "query" : "{ team(uuid:\"72d8e3b6-d4a3-4d0f-a5a7-2e63cea03460\") { displayName }}"
}
```

```
curl -i -k -H "Authorization: Bearer oauthtoken" -H "Accept: application/json" -H "Content-Type: application/json" -X POST https://localhost:9443/teamserver/rest/graphql -d '{ "query" : "{ team(uuid:\"72d8e3b6-d4a3-4d0f-a5a7-2e63cea03460\") { displayName }}" }'
```

## Requesting more details for a specific team

```
{
    team(uuid:"66c0fffd-402f-4062-9280-9cbcc6df5da2", membership:deep) { 
        uuid
        displayName
        description
        teams {
            uuid
            displayName 
        }
    }
}
```

```
{
    "data": {
        "team": {
            "uuid": "66c0fffd-402f-4062-9280-9cbcc6df5da2",
            "displayName": "Team3",
            "description": "This is a third test team",
            "teams": [
                {
                    "uuid": "4eadae15-85e2-434a-924a-81e2f840f485",
                    "displayName": "Team1"
                },
                {
                    "uuid": "9aeb2195-c96a-452a-859f-14f1e740d661",
                    "displayName": "Team2"
                }
            ]
        }
    }
}
```

## Using variables in queries

```
query TestOp($muuid: String!) {
    team(uuid:$muuid) {
        uuid
        displayName
        description
        teams {
            uuid
            displayName
        }
        metadata {
            created
            lastModified
        }
    }
}
```

```
{
    "muuid" : "9aeb2195-c96a-452a-859f-14f1e740d661"
}
```

## Operation names

Because the query in the previous example is named, you could pass the string
TestOp as the operation\_name parameter. Operation names are
optional for unique queries and are only needed when the query string contains multiple named
queries, for example, when an application always passes a query string with all possible queries and
wants to select which query from the possible ones should be executed.

## Requesting a list of teams

```
{
    teams(maxCount:2, startIndex:3, sortOrder:descending) {
        items {
            uuid 
            displayName 
            teams { 
                uuid 
                displayName
            }
        }
        metadata {
            startIndex
            totalSize
            pageIndex
            pageSize
        }
    }
}
```

```
{
    "data": {
        "teams": {
            "items": [
                {
                    "displayName": "Team2",
                    "teams": [
                        {
                            "displayName": "Team1",
                            "uuid": "6c009429-5240-4a29-b13a-36344e6a5504"
                        }
                    ],
                    "uuid": "21172f8a-c242-406d-9b64-e84911d2862e"
                },
                {
                    "displayName": "Team1",
                    "teams": [],
                    "uuid": "6c009429-5240-4a29-b13a-36344e6a5504"
                }
            ],
            "metadata": {
                "pageIndex": 2,
                "pageSize": 7,
                "startIndex": 3,
                "totalSize": 13
            }
        }
    }
}
```

## Requesting a list of teams with a filter

```
{
    teams(filter: "displayName EQ \"Team1\"", membership:shallow) {
        items {
            displayName
        }
    }
}
```

## Requesting information about the current user

```
{
  userInfo {
      principalName
      distinguishedName
      realm
      groups
  }
}
```

```
{
   "data": {
      "userInfo": {
         "principalName": "John.Doe@example.com",
         "distinguishedName": "cn=John Doe,ou=User,dc=example,dc=com",
         "realm": "PrimaryRealm",
         "groups": [ "cn=Example,ou=Group,dc=example,dc=com" ]
      }
   }
}
```

## Checking if the current user is a member of any of the provided teams

```
{
    userMemberOfAnyTeam(teamIds:"47c48aea-54ba-4007-9886-ba9cd81c67c0") {
        memberOfAnyTeam
    }
}
```

```
{
    "data": {
        "userMemberOfAnyTeam": {
            "memberOfAnyTeam": true
        }
    }
}
```

## Checking the permissions of the current user:

```
{
  userPermission {
      canCreateTeam
      canDeleteTeam
      canListAllTeams
      canListMyTeams
      canModifyTeam
      canReplaceTeam
      canViewTeamDetails
  }
}
```

```
{
   "data": {
      "userPermission": {
         "canCreateTeam": false,
         "canDeleteTeam": false,
         "canListAllTeams": false,
         "canListMyTeams": true,
         "canModifyTeam": false,
         "canReplaceTeam": false,
         "canViewTeamDetails": false
      }
   }
}
```