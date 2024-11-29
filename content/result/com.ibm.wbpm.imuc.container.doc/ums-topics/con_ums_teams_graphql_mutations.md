# User Management Service Teams GraphQL example
mutations

- Creating a new team
- Replacing a team
- Deleting a team

## Creating a new team

```
{
    "query" : "mutation { createTeam(team: { displayName: \"ABC\", distinguishedName: \"cn=abc,ou=bpm,dc=example,dc=com\", description: ...   }) { uuid displayName distinguishedName description ... } } " 
}
```

```
mutation {
    createTeam(
        team: {
            displayName: "ABC",
            distinguishedName: "cn=abc,ou=bpm,dc=example,dc=com",
            description: "Desc",
            users: [
                "U1"
            ],
            teams: [
                "5183d3c6-d25e-4fe7-847e-8b2bd5a0e1d0"
            ]
        }
    ) {
        uuid
        displayName
        distinguishedName
        description
        users
        groups
        teams {
            uuid
        }
    }
}
```

```
{
    "data": {
        "createTeam": {
            "uuid": "9b62c908-b356-4de2-b784-527a782649dd",
            "displayName": "ABC",
            "distinguishedName": "cn=abc,ou=bpm,dc=example,dc=com",
            "description": "Desc",
            "groups": [],
            "teams": [
                {
                    "uuid": "5183d3c6-d25e-4fe7-847e-8b2bd5a0e1d0"
                }
            ],
            "users": [
                "U1"
            ]
        }
    }
}
```

## Replacing a team

```
mutation {
    replaceTeam(
        uuid: "9b62c908-b356-4de2-b784-527a782649dd",
        team: {
            displayName: "DEF",
            distinguishedName: "cn=def,ou=bpm,dc=example,dc=com",
            users: [
                "U2", "U3"
            ],
            teams: [
                "936783c6-d24e-41f1-217e-1a3cd4a1e201"
            ]
        }
    ) {
         uuid
        displayName
        distinguishedName
        description
        users
        groups
        teams {
            uuid
            displayName
            description
            teams {
                uuid
                teams {
                    uuid
                    teams {
                        uuid
                        teams {
                            uuid
                            teams {
                                uuid
                                teams {
                                    uuid
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
```

## Deleting a team

```
mutation {
    deleteTeam(
        uuid: "9b62c908-b356-4de2-b784-527a782649dd"
    )
}
```

```
{
    "data": {
        "deleteTeam": "9b62c908-b356-4de2-b784-527a782649dd"
    }
}
```