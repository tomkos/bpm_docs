# createDiscretionaryTaskInCurrentCaseWithWorkflowParams operation

| Parameter                      | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId                         | String   | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| discretionaryTaskName          | String   | The symbolic name of the discretionary activity. The name format must be PREFIX\_ActivityName.This parameter is also used as the default activity name. For an IBM® FileNet® P8 activity, F\_Subject is used as the activity name instead (truncated to 64 characters) if F\_Subject is specified.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| workflowParameterAuthoredNames | String[] | An array of parameter authored names to add to the launched workflow for the discretionary activity. If no properties must be set, specify a null string {""} as an empty set. For FileNet P8 activities, F\_Subject and F\_Comment can be included.For a discretionary activity backed by a local process or external process, these parameters should be a 0-sized array. The method ignores these parameters for this type of activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| workflowParameterValues        | String[] | A String array of parameter values, if any, to add to the launched workflow for the discretionary activity. Time values are expressed in the form MM/dd/yyyy HH:mm:ss. Multivalue properties are expressed in a string representation of arrays. The parameters in the inner array should be surrounded by single quotes ('), not double quotes ("). The following example shows a possible entry in IBM FileNet Process Designer for this argument: { "123", "auto",  "{ 'one', 'two',  'three' }",  "medical" }Process Engine-specific objects, such as Attachments or participants, can be passed into this argument, as they will be converted into a string automatically. If no properties need to be set, specify a null string {""} as an empty set. To specify an empty attachment, specify "||0|0||" for a single attachment and "{ "||0|0||" }" for an attachment array.  For a discretionary activity backed by a local process or external process, these parameters should be a 0-sized array. The method ignores these parameters for this type of activity. |
| return\_value                   | String   | The GUID of the new activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |