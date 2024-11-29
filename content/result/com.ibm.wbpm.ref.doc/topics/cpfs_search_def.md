# The advanced search query definition

## Main structure

- where to perform the search (datasource field)
- whose data should be searched (population field)
- what additional conditions the source entries must match to be returned by
						the search (filters field)
- how to format and to present the results (output
						field)

## datasource

- datatype (string) defines the type of data to retrieve:
							TASKS or INSTANCES.
							TASKS is the default value.
- systemTypes (array of strings) defines the type of systems where the data is to be retrieved from: Process , BPEL , Case . The default value depends on the type of data:
    - Process and BPEL for tasks
    - Process and Case for
								instances
- systemFilter (object) defines a list of systems to include
						or not when searching. This is an object with two fields (arrays of
						strings), includes and excludes to
						respectively list IDs of systems to include or exclude for the search.

```
"datasource": {
    "datatype": "TASKS",
    "systemTypes": ["Process", "BPEL"],
    "systemFilter": {
        "excludes": ["4a8a5317-808e-48fe-964e-ff489ed356ce"]
    }
}
```

```
"datasource": {
    "datatype": "INSTANCES",
    "systemTypes": ["Case"]
}
```

## population

- target (string): SELF (searching your own tasks and
						instances)

```
"population": {
    "target": "SELF"
}
```

## filters

- interaction (string) leverages private fields to allow easy filtering bystate. It is the equivalent of the interaction field of Saved Searches and supportsthe same values: The default value is all .
    - claimed: tasks that have been claimed and are not yet completed (not valid for
instances search)
    - available: tasks that have not yet been claimed and are not yet completed (not
valid for instances search)
    - claimed\_and\_available: tasks that are not yet completed (not valid for instance
search)
    - completed: tasks or instances that are completed
    - active: instances that are not yet completed (not valid for task search)
    - failed: instances that have failed (not valid for task search)
    - all: all tasks and instances whatever their current state.
- caseScope (string) is the scope of the search for case instances. Possiblevalues are: The default value is Assigned .

- Allowed: all case instances that the population is allowed to see
- Assigned: only case instances that are assigned to the population
- v1\_conditions : Saved Search conditions (array of conditions which must
all match)
- v1\_queryFilter (string): SQL-like syntax, same as the
							queryFilter parameter of GET
							/v1/tasks and PUT /v1/instances REST
						API.
- v1\_searchFilter (string): full text search syntax, same as
						the searchFilter parameter of the GET
							/v1/tasks REST API.
- json\_query (object): new JSON syntax that supports AND, OR
						and NOT combination of conditions. The json\_query filter is
						a JSON Object (tree). The fields are Saved Search conditions
							(field, operator,
							value) that can be combined with
							and, or, and
							not.The following example illustrates a query
							in JSON syntax: 
"json\_query": {
    ”not": {
        ”or": [{
            "field": "taskPriority",
            "operator": "GreaterThan",
            "value": 100
        },
        {
            ”and": [{
                "field": "customer",
                "operator": "Equals",
                "value": ”ACME corp."
            },
            {
                "field": "product",
                "operator": "Equals",
                "value": "CP4BA"
            }]
        }]
    }
}

```
"filters": {
  "interaction": "claimed",
  "json\_query": {
    "field": "taskPriority",
    "operator": "GreaterThan",
    "value": 100
  },
  "v1\_searchFilter": "ACME"
}
```

## output

- fields (array of strings): list of fields to return for
						each task or instance.
- includeAllBusinessData (boolean): return all business data
						fields at once.false is the default value.
- usersFullName (boolean): specifies how to format user's
						information in the results (full name or user ID). true is
						the default value.
- aliases (array of objects): list of aliases (same as Saved
						Search aliases field)
- sort (array of objects): specifies how to sort the results. Each object in
the array has two fields, field (string) is the name of a fields to sort the
results on, and order (string), either ASC or
DESC (default to ASC) depending on whether the results should be
respectively sorted by ascending or descending field value.
- alphabeticalSort (string): sort by alphabetical versus lexicographical
order (for string fields referenced in the sort field).
- size (integer): maximum number of results in the response (the default
number is 25).
- stats (object): statistics to return with the results. There is currently
a single type of statistics that can be returned (same than when executing a Saved Search with the
calcStats parameter set to true), specified by setting the
type (string) parameter of the stats object to
Basic

```
"output": {
    "fields": ["taskNarrative", "taskId", "instanceId", "taskAtRiskTime"],
    "includeAllBusinessData": true,
    "sort": [{
        "field": "taskAtRiskTime",
        "order": "ASC"
    }],
    "size": 50,
    "stats": {
        "type": "Basic"
    }
}
```

## Reusable search queries metadata

Similarly to Saved Searches, advanced search queries definitions can be stored and shared with
team, using the Reusable search queries REST API.

## metadata

- name (string): a mandatory unique name for the reusable search query;
- description (string): an optional description for the reusable search
query;
- sharing (object): optional information about the reusable search query isshared. It includes the following fields:
    - shared (boolean): true to share with other users,
false (default value) otherwise
    - teams (array of objects): list of process teams to share the search query with.
If null, undefined or empty while shared is
true, then the search query is shared with everybody. To share with a specific
process team that you are a member or manager of, define this team in the array (note that a single
value is currently supported) by using an object with field teamId for the process
team identifier.
- owner (object): information about the user that owns the reusable search
query
- creator (object): information about the user that created the reusable search
query
- lastUpdater (object): information about the user that last updated the reusable
search query
- creationDate (string): ISO8601 timestamp of when the reusable search query was
created
- lastUpdateDate (string): ISO8601 timestamp of when the reusable search query
was last updated

```
"metadata": {
    "name": "my tasks list",
    "description": "a search query that retrieves my task list",
    "sharing": {
        "shared": true,
        "teams": [{
            "teamId": "24.6615a4b0-fd38-4ea5-8bc0-69d2f107369e",
            "teamName": "Human Resources",
            "processAppName": "Hiring Sample"
        }],
    },
    "owner": {
        "id": "jane.doe@acme.com",
        "fullName": "Jane Doe"
    },
    "creator": {
        "id": "admin@acme.com",
        "fullName": "Administrator"
    },
    "lastUpdater": {
        "id": "user.name@ibm.com",
        "fullName": "User Name"
    },
    "creationDate": "2024-01-31T12:34:42.183Z",
    "lastUpdateDate": "2024-02-01T16:03:12.874Z"
}
```