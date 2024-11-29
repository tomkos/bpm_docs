# User Management Service Teams GraphQL error
handling

Most of the time, the two REST endpoints on teamserver/rest/graphql will return
the HTTP status OK (200), even when there is an error.

```
{
    "data": {
        "team": {
            "uuid": "ddc12371-b71a-4a9a-b819-6cb29713ff65",
            "displayName": "Team1"
        }
    },
    "errors": [
        {
            "locations": [
                {
                    "column": 33,
                    "line": 1
                }
            ],
            "message": "CWLUM1017E: Error in GraphQL query: ..."
        }
    ],
    "extensions": {}
}
```

- The data field represents the valid response data. It might or might not be
present, depending on whether an error stopped the entire processing, whether there is no error, or
an error is recoverable.
- The errors field contains the errors that occurred during the GraphQL
processing, for example, when the input query was syntactically wrong or if the caller is not
authorized to perform the request. When there are no errors, the errors field is
missing.
- The extensions field is usually missing. The extension field
might be filled with a GraphQL trace log if the server has logging and tracing enabled at the level
FINER.

There are cases when the two REST endpoints on teamserver/rest/graphql will
return an HTTP status code that is not the OK code (200). This happens if the error is outside the
GraphQL processing, for example, when the JSON input of the POST request cannot be parsed. In this
case, the response will not be in the GraphQL response format because the GraphQL processing was not
even started.