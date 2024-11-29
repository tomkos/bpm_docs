# POST method for Case stage

## URI

/CaseManager/CASEREST/v1/case/{CaseInstanceId}/stages

The URI for the POST method includes the following path element:

| Name             | Type   | Description                                                                             |
|------------------|--------|-----------------------------------------------------------------------------------------|
| {CaseInstanceId} | String | The ID that identifies the root folder of the case that is used to retrieve all stages. |

| Name              | Type   | Required?   | Description                                                                                              |
|-------------------|--------|-------------|----------------------------------------------------------------------------------------------------------|
| TargetObjectStore | String | Yes         | This is a symbolic name of the object store that contains the case instances.                            |
| Operation         | String | Yes         | Operations:  completeCurrentStage placeCurrentStageOnHold releaseCurrentOnHoldStage restartPreviousStage |

## POST method request

This sample code requests
to perform stage action for the case with the ID ending in EE55D8BCF2ED.

## Request to get the list of case stages for the given case instance

```
/CaseManager/CASEREST/v1/case/9E45A997-0E42-406E-AAC4-EE55D8BCF2ED/stages?TargetObjectStore=MyTOS&Operation=releaseCurrentOnHoldStage
```

## POST method response

```
{"removeStageOnHoldResult":true}
```