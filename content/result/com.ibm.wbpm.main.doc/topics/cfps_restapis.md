# The Process Federation Server REST
APIs

- Process Federation Server
REST APIs focus on a subset of APIs that are required for task worker scenarios.
- Process Federation Server
REST APIs are for aggregate sets of resources, such as the task list. The APIs query a distributed
index on the process federation server, instead of querying each of the federated systems
individually as is the case for the federated REST APIs. This query behavior improves performance
and offloads expensive queries from the federated systems.
- For working with individual resources, for example, claiming or working on an individual task,
client applications work directly against the system that hosts the task. In this way, existing
client code that interacts with a single system resource will continue to work as is.

To ease the transition of existing clients from the federated APIs to the Process Federation Server REST APIs, the
Process Federation Server REST
APIs use the same API signature as the federated REST APIs.

## REST APIs

<!-- image -->

```
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/launchableEntities
```

- Create a saved search: [POST][include saved search payload]
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/searches/tasks
- Retrieve a specific saved search: [GET]
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/searches/tasks/2
- Update specific saved search: [PUT][include saved search payload]
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/searches/tasks/My Saved Search
- Delete a saved search:
[DELETE]https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/searches/tasks/2
- Retrieve a list of searches available to the requesting user:
[GET]https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/searches/tasks
- Retrieve a list of saved search authorization roles for the requesting user: [GET]https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/searches/actions Dependingon the user's role, the appropriate actions are returned: For more information about authorizations for saved searches in federated systems, see Federated systems and authorization for saved searches .

```
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/searches/actions
```

    - Users with the ACTION\_ADMINISTER\_SHARED\_SAVED\_SEARCHES action role can create or update a
shared saved search definition to be owned by another user's ID.
    - Users with the ACTION\_CREATE\_SHARED\_SAVED\_SEARCH action role can create or update saved search
definitions to be shared.
    - Users with the ACTION\_RUN\_SAVED\_SEARCH action role cannot create or update saved search
definitions.
    - Users with no action role (the API returns an empty array) can create and update personal saved
searches.

```
{ "name": "My Saved Search",
  "shared": false,
  "conditions": [{"field": "applicationName", "value": "Process1", "operator": "Equals" }],
  "sort": [{"field": "taskDueDate","order": "ASC"}],
  "fields": ["taskDueDate","taskId","applicationName"],
  "interaction": "claimed",
  "size": 10 }
```

You can also restrict the rights to create and update
saved searches to a user or group of users. For more information, see Administering Process Portal searches and saved searches.

```
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/searches/meta/fields?searchType=INSTANCE\_SEARCH
```

```
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/searches/meta/fields
```

```
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/searches/meta/constraintFields
```

```
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/searches/meta/businessDataFields
```

```
{
   "result":[{
      "name":"customer\_name",
      "type":"String",
      "full\_text\_searchable":true
     },
     { 
      "name":"phone",
      "type":"Integer",
      "full\_text\_searchable":false
     }
     ]
}
```

By design, Process Federation Server returns all
business data fields that it detects as included in process instances. It does not detect business
data fields that are modeled but not included in any instances yet.

```
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/searches/meta/taskStatus
```

```
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/searches/meta/priority
```

```
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/globalTeams
```

```
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/systems
```

<!-- image -->

- Base task query URL: [GET]
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/tasks
- Base task query URL with saved search referenced by ID: [GET]
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/tasks?savedSearch=2
- Task query with interaction filter and specific task fields and sort fields:
[GET]https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/tasks?interaction=claimed\_and\_available&size=25&offset=0&fields=taskState,taskDueDate,taskPriority,instanceName,taskActivityName,assignedToUser,taskStatus&sort=taskDueDate,taskPriority
- Task query for the second page of search results: [PUT][include saved search payload]
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/tasks?size=10&offset=10

- Base process instance list query URL: [PUT] [include saved search
payload]https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/instances
- process instance list query for the second page of search results: [PUT] [include saved search
payload]https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/instances?size=10&offset=10

- Export a specific saved search:
[GET]https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/searches/transfer/bpd/system/federatedSystem1/search/MySavedSearch
- Export a list of saved searches from a federated system to the requesting user:
[GET]https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/searches/transfer/bpd/system/federatedSystem1
- Export a list of saved searches from all federated systems to the requesting user: [GET]
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/searches/transfer/bpd/systems
- Import one saved search or more: [POST][include list of saved searches
payload]https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/searches/transfer
- Export a list of saved searches recorded in the Process Federation Server database: [GET]
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/searches/transfer

```
[
    {
      "importName": "my\_pfs\_saved\_search\_1",
      "exportedFrom": {
        "id": "federatedSystem1"
      },
      "savedSearch": {
        "owner": "admin",
        "shared": false,
        "teams": null,
        "size": 10000,
        "organization": "byTask",
        "name": "my\_bpm\_saved\_search\_1",
        "interaction": "completed",
        "id": "1006",
        "sort": [
          {
            "field": "taskDueDate",
            "order": "ASC"
          }
        ],
        "fields": [
          "taskSubject",
          "instanceName",
          "taskStatus",
          "taskPriority",
          "rfc@String",
          "nombre@String",
          "GMApproval@Boolean",
          "orderID@String",
          "HiringManager@String",
          "taskDueDate"
        ],
        "conditions": []
      }
    },
    {
      "importName": "my\_pfs\_saved\_search\_2",
      "exportedFrom": {
        "id": "federatedSystem2"
      },
      "savedSearch": {
        "owner": "admin",
        "shared": true,
        "teams": [
          {
            "teamName": "Managers",
            "teamId": "24.581a472b-5016-479a-b5b5-0a9701c2c42c",
            "processAppName": "System Data"
          }
        ],
        "size": 10000,
        "organization": "byTask",
        "name": "my\_bpm\_saved\_search\_2",
        "interaction": "claimed\_and\_available",
        "id": "1004",
        "sort": [
          {
            "field": "taskDueDate",
            "order": "ASC"
          }
        ],
        "fields": [
          "taskSubject",
          "instanceName",
          "taskStatus",
          "taskPriority",
          "GMApproval@Boolean",
          "EmploymentStatus@String",
          "RequisitionNumber@String",
          "taskDueDate"
        ],
        "conditions": []
      }
    }
  ]
```

For more information about how to use this Saved Search
Transfer REST API, see Importing saved searches into Process Federation Server.

Process Portal is an
example of the types of client application that you can build by using the Process Federation Server REST APIs.

## REST APIs for the Team Performance Dashboard

These REST APIs allow BPD Team managers to gather key performance indicators for their teams.
They can be leveraged to create a federated Team Performance Dashboard, similar to the nonfederated
Team Performance Dashboard that is available in Process Portal.

- team id
- team name
- team description
- id of the BPD process application that defines the team
- name of the BPD process application that defines the team
- number of open tasks for this team
- number of on track tasks for this team
- number of tasks that are at risk for this team
- number of overdue tasks for this team
- number of tasks completed today for this team

```
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v2/dashboards/teamsummary
```

```
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v2/dashboards/teamsummary/24.d0d5eaa0-8b7e-4e8c-85e7-5676d3e9d574
```

- the number of tasks created for this team
- the number of tasks completed for this team

```
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v2/dashboards/teamtasktrend/24.d0d5eaa0-8b7e-4e8c-85e7-5676d3e9d574?units=HOUR&numPeriods=48
```

```
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v2/dashboards/teamtasktrend/24.d0d5eaa0-8b7e-4e8c-85e7-5676d3e9d574?units=DAY&numPeriods=31
```

- name
- full name
- job title
- phone number
- email address
- number of tasks assigned
- number of tasks completed today

```
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v2/dashboards/teammember/24.d0d5eaa0-8b7e-4e8c-85e7-5676d3e9d574
```

- number of tasks completed today
- email address
- phone number
- number of tasks that are overdue
- job title
- name
- full name
- number of tasks that are at risk
- number of open tasks
- number of tasks that are on track

```
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v2/dashboards/teammember/24.d0d5eaa0-8b7e-4e8c-85e7-5676d3e9d57/fdadmin
```

```
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v2/dashboards/teamtasks/24.d0d5eaa0-8b7e-4e8c-85e7-5676d3e9d57
```

## Response data

| Attribute               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| indexRefreshInterval    | Task list queries are based on the Process Federation Server index. The indexRefreshInterval attribute indicates how often the index is updated, so that you can understand how fresh the returned data is. For example, if you modify a task and then immediately query the task list again, you might not see your update. Take this lapse time into consideration when you develop custom applications that are based on the REST service. Consider caching updates locally until the data is refreshed. The value, in milliseconds, is based on the value of the indexRefreshIntervalForClients property in the ibmPfs\_federatedSystem element in the server.xml configuration file. By default, the index is cached for 2 seconds, so you might not see status changes immediately. For more information about the configuration property, see Configuration properties for the Process Federation Server index. |
| statusCode              | Indicates the status of the federated system. The value of the attribute depends on whether the system can be queried by the process federation server.Attribute values. 200 The federated system is running normally. 408 The REST request cannot access the federated system because the request timed out. 503 The REST request cannot be processed because the federated system is unavailable.    By default, the system status is cached for 300 seconds, so you might not see status changes immediately. You can change the cache time by updating the ibmPfs\_restConfig cacheRefreshTime property in the server.xml configuration file, for example: cacheRefreshTime="200s"                                                                                                                                                                                                                                 |
| taskCompletionUrlPrefix | Indicates the root URL for completing tasks from a federated system, for example, https://bpmHost.mycompany.com:9443/teamworks. To complete a task from a specific system, use the taskCompletionUrlPrefix attribute to go directly to it. The value is based on the value for the ibmPfs\_federationSystem taskCompletionUrlPrefix property in the server.xml configuration file. If the system uses an HTTP server or reverse proxy server, use the URL of the HTTP server or reverse proxy server in front of the federated system as the value in the server.xml file.                                                                                                                                                                                                                                                                                                                                             |
| restUrlPrefix           | Indicates the root URL for REST requests on a federated system, for example, https://bpmHost.mycompany.com:9443/rest/bpm/wle. To make REST requests to a system (for example, to modify a task on this system), use the restUrlPrefix attribute to go directly to it. The value is based on the value that is configured for the ibmPfs\_federationSystem restUrlPrefix property in the server.xml configuration file. If the system uses an HTTP server or reverse proxy server, use the URL of the HTTP server or reverse proxy server in front of the system as the value in the server.xml file.                                                                                                                                                                                                                                                                                                                   |
| systemType              | Indicates the federated system type, for example: SYSTEM\_TYPE\_WLE for BPD systems SYSTEM\_TYPE\_WPS for BPEL systems SYSTEM\_TYPE\_CASE for Case systems                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| displayName             | The name that is used for Process Federation Server in user interfaces and messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| systemID                | Indicates the unique identifier of the federated system, for example, "a85ce736-a156-49cc-a41f-1a8ed9693357". The systemID attribute is included in every federated resource so that you can associate the resource to a system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| version                 | Indicates the version of the federated system, for example, "8.5.7.0"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## REST APIs for advanced searches support

Business Automation Workflow provides
three sets of APIs to support advanced searches. For more information about those APIs, see REST APIs for advanced searches support.