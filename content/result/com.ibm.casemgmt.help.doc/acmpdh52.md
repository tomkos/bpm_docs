# addCaseOwners operation

| Parameter   | Type            | Description                                                                                                                                                  |
|-------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId      | String          | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window. |
| assigner    | VWParticipant   | A VWParticipant object that represent the name of the user who is assigning owners to this case.                                                             |
| owners      | VWParticipant[] | An array of VWParticipant objects that represent the names of the users who are to be assigned as owners of this case.                                       |