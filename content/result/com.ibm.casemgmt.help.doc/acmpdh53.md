# removeCaseRoleMembers operation

| Parameter   | Type            | Description                                                                                                                                                  |
|-------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId      | String          | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window. |
| roleName    | String          | The role from which case members are to be removed for this case.                                                                                            |
| members     | VWParticipant[] | An array of VWParticipant objects that represent the names of the users who are to be removed from the specified role in this case.                          |