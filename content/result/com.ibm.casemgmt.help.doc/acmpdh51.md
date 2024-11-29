# addCaseRoleMembers operation

| Parameter   | Type            | Description                                                                                                                                                  |
|-------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId      | String          | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window. |
| roleName    | String          | The role to which case members are to be assigned for this case.                                                                                             |
| assigner    | VWParticipant   | A VWParticipant object that represent the name of the user who is assigning members to the specified role in this case.                                      |
| members     | VWParticipant[] | An array of VWParticipant objects that represent the names of the users who are to be assigned to the specified role in this case.                           |