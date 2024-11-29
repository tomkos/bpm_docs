# Importing saved searches from federated systems into Process Federation Server

## Before you begin

- This API is not supported for BPEL-related resources.
- You cannot import saved searches that are organized by instance.
- Only saved searches that were created in IBM® BPM V8.5.7 or later, or in Business Automation Workflow federated systems, can be exported. You cannot
export saved searches that appear in these product versions but were created in earlier
versions.

- Process Federation Server is installed.
- All federated systems are configured, and each of them contain saved searches definitions in
their respective database.

## About this task

You start by exporting the saved searches definitions from the federated systems databases, then
        you import those saved searches definitions into the Process Federation Server database.

As a guidance, the examples provided in each step of this procedure are based on a Process Federation Server configuration with two  systems.

## Procedure

1. Check that the federated systems are working by using the following REST API that lists the
federated systems currently available: GET
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/systems.

In the following example, the result of this query reports that two BPD-related systems with
respective id
bpm1 and bpm2 are federated and
available:{
  "federationResult": [
    {
      "restUrlPrefix": "https://bpm1Host.mycompany.com:9446/rest/bpm/wle",
      "systemID": "2ee12405-f15c-4482-85d0-e1ff7ec564b8",
      "displayName": "BPM1",
      "systemType": "SYSTEM\_TYPE\_WLE",
      "portalSupportUrlPrefix": "https://bpm1Host.mycompany.com:9446/portal",
      "id": "bpm1",
      "taskCompletionUrlPrefix": "https://bpm1Host.mycompany.com:9446/teamworks",
      "version": "8.5.7.201703",
      "indexRefreshInterval": 2000,
      "statusCode": "200"
    },
    {
      "restUrlPrefix": "https://bpm2Host:9443/rest/bpm/wle",
      "systemID": "7cf5b53b-6c76-487c-93e5-25361b46d01d",
      "displayName": "BPM2",
      "systemType": "SYSTEM\_TYPE\_WLE",
      "portalSupportUrlPrefix": "https://bpm2Host.mycompany.com:9443/portal",
      "id": "bpm2",
      "taskCompletionUrlPrefix": "https://bpm2Host.mycompany.com:9443/teamworks",
      "version": "8.5.7.0",
      "indexRefreshInterval": 2000,
      "statusCode": "200"
    }
  ],
  ...
}
2. Export the saved search definitions from the federated systems, for example
bpm1 and bpm2, by using the following REST API: GET
https://pfsHost.mycompany.com:9443/rest/bpm/federated/v1/searches/transfer/bpd/systems?renameDuplicates=true. 

You can optionally save this query result to a file by appending the parameter
outputFile to the query and specify the absolute path and file name of this file as
the value.
Each saved search must have a unique name. However, saved searches might exist with the same name
on different federated systems. To avoid duplicate saved search names in the export query results,
the renameDuplicates parameter with the value set to true is
appended to the query so that each exported saved search in the list gets a unique name that is used
later for import.

After the export has completed successfully, an ordered array of saved search definitions
that were exported from both BPD federated systems is returned in JSON format as shown in the
following
example.
{
  "results": [
    {
      "importName": "my\_bpm\_saved\_search\_1",
      "exportedFrom": {
        "systemId": "7cf5b53b-6c76-487c-93e5-25361b46d01d",
        "id": "bpm2"
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
          "taskDueDate"
        ],
        "conditions": []
      }
    },
    {
      "importName": "my\_bpm\_saved\_search\_3",
      "exportedFrom": {
        "systemId": "7cf5b53b-6c76-487c-93e5-25361b46d01d",
        "id": "bpm2"
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
        "name": "my\_bpm\_saved\_search\_3",
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
    },
    {
      "importName": "my\_bpm\_saved\_search\_50.bpm1",
      "exportedFrom": {
        "systemId": "2ee12405-f15c-4482-85d0-e1ff7ec564b8",
        "id": "bpm1"
      },
      "savedSearch": {
        "owner": "admin",
        "shared": false,
        "aliases": [
          {
            "field": "Location",
            "alias": "Location"
          }
        ],
        "teams": null,
        "size": 10000,
        "organization": "byTask",
        "name": "my\_bpm\_saved\_search\_50",
        "interaction": "all",
        "id": "1002",
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
          "instanceId",
          "Location@String"
        ],
        "conditions": []
      }
    },
    {
      "importName": "my\_bpm\_saved\_search\_50.bpm2",
      "exportedFrom": {
        "systemId": "7cf5b53b-6c76-487c-93e5-25361b46d01d",
        "id": "bpm2"
      },
      "savedSearch": {
        "owner": "admin",
        "shared": false,
        "teams": null,
        "size": 10000,
        "organization": "byTask",
        "name": "my\_bpm\_saved\_search\_50",
        "interaction": "all",
        "id": "1002",
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
          "instanceId",
          "taskDueDate",
          "Department@String",
          "GMApproval@Boolean",
        ],
        "conditions": []
      }
    }
  ],
  "status": 200
}Note: In
this example, a saved search name conflict for my\_bpm\_saved\_search\_50 was
automatically resolved by the renameDuplicates parameter being specified with the
value set to true in this GET query to preserve the
importName uniqueness.
3 Import the saved search definitions that were exported by using the following REST API: POST https://pfsHost.mycompany.com:9443 /rest/bpm/federated/v1/searches/transfer . It takes as input an array of exported saved search definitions corresponding to the results property of the JSON object returned by the GET query in step 2 . If you specified the ouptutFile , you can use the array of saved search definitions that was saved as the input.Note: When the saved search definitions can be successfully imported, a JSON objectsimilar to the following is returned.{ "imported": [ { "savedSearch": { "owner": "uid=admin,o=defaultWIMFileBasedRealm", "shared": false, "aliases": [ { "field": "Location", "alias": "Location" } ], "size": 10000, "organization": "byTask", "name": "my\_bpm\_saved\_search\_50.bpm1", "interaction": "all", "id": 508, "sort": [ { "field": "taskDueDate", "order": "ASC" } ], "conditions": [], "fields": [ "taskSubject", "instanceName", "taskStatus", "instanceId", "Location@String" ] }, "exportedFrom": "bpm1" }, { "savedSearch": { "owner": "uid=admin,o=defaultWIMFileBasedRealm", "shared": false, "aliases": [], "size": 10000, "organization": "byTask", "name": "my\_bpm\_saved\_search\_1", "interaction": "completed", "id": 509, "sort": [ { "field": "taskDueDate", "order": "ASC" } ], "conditions": [], "fields": [ "taskDueDate" ] }, "exportedFrom": "bpm2" }, { "savedSearch": { "owner": "uid=admin,o=defaultWIMFileBasedRealm", "shared": true, "aliases": [], "size": 10000, "organization": "byTask", "name": "my\_bpm\_saved\_search\_3", "interaction": "claimed\_and\_available", "id": 510, "sort": [ { "field": "taskDueDate", "order": "ASC" } ], "conditions": [], "fields": [ "taskSubject", "instanceName", "taskStatus", "taskPriority", "GMApproval@Boolean", "EmploymentStatus@String", "RequisitionNumber@String", "taskDueDate" ] }, "exportedFrom": "bpm2" }, { "savedSearch": { "owner": "uid=admin,o=defaultWIMFileBasedRealm", "shared": false, "aliases": [], "size": 10000, "organization": "byTask", "name": "my\_bpm\_saved\_search\_50.bpm2", "interaction": "all", "id": 511, "sort": [ { "field": "taskDueDate", "order": "ASC" } ], "conditions": [], "fields": [ "taskSubject", "instanceName", "taskStatus", "instanceId", "taskDueDate", "Department@String", "GMApproval@Boolean" ] }, "exportedFrom": "bpm2" } ], "failed": [], "malformed": [], "status": 201} Note: If some of the saved search definitions are not properly formed, or if they cannot beinternally validated by this POST REST API, no saved search is imported. In thatcase, you should find out the root cause that prevents the import operation to complete, make thenecessary modifications and perform this last step again.
    - If you try to import saved searches that contain fields that do not yet exist in
Process Federation Server, consider adding the
fieldValidationBypass parameter and setting the value to true
to this POST REST API.
    - When trying to import shared saved searches, you must have either
                    createSharedSavedSearch or
                    adminSharedSavedSearch privilege.

```
{
  "imported": [
    {
      "savedSearch": {
        "owner": "uid=admin,o=defaultWIMFileBasedRealm",
        "shared": false,
        "aliases": [
          {
            "field": "Location",
            "alias": "Location"
          }
        ],
        "size": 10000,
        "organization": "byTask",
        "name": "my\_bpm\_saved\_search\_50.bpm1",
        "interaction": "all",
        "id": 508,
        "sort": [
          {
            "field": "taskDueDate",
            "order": "ASC"
          }
        ],
        "conditions": [],
        "fields": [
          "taskSubject",
          "instanceName",
          "taskStatus",
          "instanceId",
          "Location@String"
        ]
      },
      "exportedFrom": "bpm1"
    },
    {
      "savedSearch": {
        "owner": "uid=admin,o=defaultWIMFileBasedRealm",
        "shared": false,
        "aliases": [],
        "size": 10000,
        "organization": "byTask",
        "name": "my\_bpm\_saved\_search\_1",
        "interaction": "completed",
        "id": 509,
        "sort": [
          {
            "field": "taskDueDate",
            "order": "ASC"
          }
        ],
        "conditions": [],
        "fields": [
          "taskDueDate"
        ]
      },
      "exportedFrom": "bpm2"
    },
    {
      "savedSearch": {
        "owner": "uid=admin,o=defaultWIMFileBasedRealm",
        "shared": true,
        "aliases": [],
        "size": 10000,
        "organization": "byTask",
        "name": "my\_bpm\_saved\_search\_3",
        "interaction": "claimed\_and\_available",
        "id": 510,
        "sort": [
          {
            "field": "taskDueDate",
            "order": "ASC"
          }
        ],
        "conditions": [],
        "fields": [
          "taskSubject",
          "instanceName",
          "taskStatus",
          "taskPriority",
          "GMApproval@Boolean",
          "EmploymentStatus@String",
          "RequisitionNumber@String",
          "taskDueDate"
        ]
      },
      "exportedFrom": "bpm2"
    },
    {
      "savedSearch": {
        "owner": "uid=admin,o=defaultWIMFileBasedRealm",
        "shared": false,
        "aliases": [],
        "size": 10000,
        "organization": "byTask",
        "name": "my\_bpm\_saved\_search\_50.bpm2",
        "interaction": "all",
        "id": 511,
        "sort": [
          {
            "field": "taskDueDate",
            "order": "ASC"
          }
        ],
        "conditions": [],
        "fields": [
          "taskSubject",
          "instanceName",
          "taskStatus",
          "instanceId",
          "taskDueDate",
          "Department@String",
          "GMApproval@Boolean"
        ]
      },
      "exportedFrom": "bpm2"
    }
  ],
  "failed": [],
  "malformed": [],
  "status": 201
}
```