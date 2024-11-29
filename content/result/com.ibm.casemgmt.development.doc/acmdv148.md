# GET method for Case stage

## URI

/CaseManager/CASEREST/v1/case/{CaseInstanceId}/stages

The URI for the GET method includes the following path element:

| Name             | Type   | Description                                                                             |
|------------------|--------|-----------------------------------------------------------------------------------------|
| {CaseInstanceId} | String | The ID that identifies the root folder of the case that is used to retrieve all stages. |

| Name              | Type   | Required?   | Description                                                                   |
|-------------------|--------|-------------|-------------------------------------------------------------------------------|
| TargetObjectStore | String | Yes         | This is a symbolic name of the object store that contains the case instances. |
| Operation         | String | Yes         | Operations:  retrieveAllStages retrieveCurrentStage                           |

## GET method request

This sample code requests a
list of case stages for the case with the ID ending in EE55D8BCF2ED.

## #Request to get the list of case stages for the given case instance

```
/CaseManager/CASEREST/v1/case/9E45A997-0E42-406E-AAC4-EE55D8BCF2ED/stages?TargetObjectStore=MyTOS&Operation=retrieveAllStages
```

## GET method response

```
{
	"stages": [ {
		"Status": "COMPLETED",
		"Description": null,
		"expectedDurationUnitType": 0,
		"timeSpent": 0.0,
		"displayName": "FirstStage",
		"estimatedStartDate": null,
		"dueDate": null,
		"startedDate": "2021-03-11T05:05:15Z",
		"SymbolicName": "FirstStage",
		"completedDate": "2021-03-11T05:05:39Z",
		"RestartCount": 0,
		"isOverdue": false,
		"expectedDurationUnitCount": 0,
		"overdueTime": 0.0,
		"estimatedCompleteDate": null
	}, {
		"Status": "WORKING",
		"Description": null,
		"expectedDurationUnitType": 0,
		"timeSpent": 1788.0,
		"displayName": "SecondStage",
		"estimatedStartDate": null,
		"dueDate": null,
		"startedDate": "2021-03-11T05:05:55Z",
		"SymbolicName": "SecondStage",
		"completedDate": "2021-03-12T10:54:10Z",
		"RestartCount": 1,
		"isOverdue": false,
		"expectedDurationUnitCount": 0,
		"overdueTime": 0.0,
		"estimatedCompleteDate": null
	},{
		....
	}]
}
```