# REST APIs for advanced searches support

- A federated version of the APIs, exposed by Process Federation Server, for which
detailed documentation is available in IBM Process Federation Server REST APIs.
- A non-federated version of the APIs, exposed by Business Automation Workflow Server, for which
detailed documentation is available in REST Interface for BPD-related Resources. The non-federated version of the REST
APIs for advanced searches requires data to be indexed into the federated data repository. See
Administering the federated data repository indexes.

## Metadata REST APIs

- lists of teams a search query can be shared with
- roles granted to the user for search queries (using, creating, sharing, managing)
- lists of fields and constants that are available to use in search queries

- Systems metadata: use this REST API to retrieve information about the systems which can be searched (see GET /v1/systems in the detailed documentation)
- Global Teams: use this REST API to retrieve a list of teams that a search query can be shared with (see GET /v1/globalTeams in the detailed documentation)
- Search actions: use this REST API to retrieve the list of search related roles that have been granted to the calling user (see GET /v1/searches/action in the detailed documentation)
- Tasks and instances metadata: use this REST API to retrieve lists of fields and values that can be used in search queries (see Process Federation Server's GET /v1/searches/meta/{type} and Business Automation Workflow Server's GET /v1/searches/tasks/meta/{type} in the detailed documentation)

## Reusable Search Queries REST APIs

- List: GET /v2/search/queries
- Create: POST /v2/search/queries
- Retrieve: GET /v2/search/queries/{id}
- Update: PUT /v2/search/queries/{id}
- Delete: DELETE /v2/search/queries/{id}

## Search REST API

The POST /v2/search REST API is the one to use to execute search queries. With
				this API, you can run both ad hoc and reusable search queries, and extend or refine
				a referenced reusable search query.

Three options are available to run a search query: provide the ID of a reusable search query as a
query parameter, submit a JSON search query in the request body, or combine both by extending a
reusable search query with additional details in a JSON search query within the request body.

- narrow down the results by running the query against a subset of the
						datasource (for example, only against BPD tasks)
- change the interaction (closed vs. claimed
							and available)
- add additional filter conditions (for example a due date)
- customize the output (sort the results differently, add or remove fields)

In the POST/v2/search API, you provide the extension in the same format as the
initial search query.

The following snippets show an example of how a search query can be extended:

```
{
  "datasource": {
    "datatype": "TASKS",
    "systemTypes": ["Process", "BPEL"]
  },
  "population": {
    "target": "SELF"
  },
  "filters": {
    "interaction": "claimed\_and\_available"
    "json\_query": {
      "field": "customer",
      "operator": "Equals",
      "value": "ACME corp."
    }
  },
  "output": {
    "includesAllBusinessData": true,
    "sort": [
      {"field": "taskDueDate", "order": "ASC" }, 
      {"field": "taskPriority", "order": "DESC" }, 
    ],
    "size": 25
  }
}
```

```
{
  "datasource": {
    "systemTypes": [”Process"]
  },
  "population": {
    "target": "MANAGED\_TEAMS"
  },
  "filters": {
    "interaction": "completed"
    "json\_query": {
      "field": "taskClosedDate",
      "operator": "GreaterThan",
      "value": "end\_of last\_month"
    }
  },
  "output": {
    "fields": ["taskOwner"],
    "usersFullName": false,
    "sort": [
      {"field": "taskOwner", "order": "ASC" }
    ],
    "size": 30
  }
}
```

```
{
  "datasource": {
    "datatype": "TASKS",
    "systemTypes": [”Process"]
  },
  "population": {
    "target": "MANAGED\_TEAMS"
  },
  "filters": {
    "interaction": "completed"
    "json\_query": {
      "and": [
         {"field": "customer", "operator": "Equals", …},
         {"field": "taskClosedDate", "operator": …}
      ]
    }
  },
  "output": {
    "fields": ["taskOwner"],
    "includesAllBusinessData": true,
    "usersFullName": false,
    "sort": [
      {"field": "taskOwner", "order": "ASC" }
    ],
    "size": 30
  }
}
```

```
{
	"datatype": "TASKS" | "INSTANCES",
	"systems": [{…}],
	"queryExecuteTime": "…",
	"requestedSize": 25,
	"responseSize": 25,
	"offset": 0,
	"totalCount": 150,
	"fieldsMetadata": [{
		"name": "…",
		"type": "…",
		"isArray": true | false,
		"isBusinessData": true | false,
		"source": "…"
	}],
	"results": [{…}],
	"stats": {…}
}
```

- The advanced search query definition

Advanced search capability is made available through a JSON schema that defines search queries.