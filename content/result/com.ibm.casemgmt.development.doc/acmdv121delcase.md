# POST method for deleting a case

## URI

```
/CASEREST/v1/deletecase
```

## Request content for deleting a case

The request for the POST method contains the following parameters in JSON in the body. One of the
casetype or caseid parameters must be passed.

```
{
    connectionpoint:"Name of the process engine connection point",
    casetype:"Symbolic name of the case type for which the cases are to be deleted. ",
     caseid : "The guid of the case instance which is to be deleted",
    tos:"Name of the target object store"
}
```

## Request parameters

| Name            | Type   | Required?   | Description                                                           |
|-----------------|--------|-------------|-----------------------------------------------------------------------|
| connectionpoint | String | Yes         | Name of the  FileNet®  process engine connection point.               |
| casetype        | String | Yes         | Symbolic name of the case type for which the cases are to be deleted. |
| caseid          | String | Yes         | The GUID of the case instance, which is to be deleted.                |
| tos             | String | Yes         | Name of the target object store that contains the case to be deleted. |

1. Use the Administration Console for Content Platform
Engine.
2. Go to
TargetObjectstore > Administrative > WorkflowSystem > Connection
Points.

- This case REST method deletes the case and all associated activity processes. Documents
associated with the case are not removed, only the references to the case folders are removed. If
the documents are not referenced in any other folders, then the documents end up in the 'Unfiled
Documents' folder in the object store.