# relateCurrentCase operation

| Parameter            | Type    | Description                                                                                                                                                                                                                                                             |
|----------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId               | String  | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window.                                                                                                            |
| relateTargetId       | String  | For this value, use the returned value of the createCase operation that you used.                                                                                                                                                                                       |
| relateDescription    | String  | The description of this relationship.                                                                                                                                                                                                                                   |
| relationshipCategory | String  | The relationship category.Optional. For related relationship types only. Relationship categories are user-defined. A category provides additional information to identify the nature of the relationship and to facilitate searches for certain types of relationships. |
| twoWayRelationship   | Boolean | A Boolean field that indicates whether the relationship is two-way.                                                                                                                                                                                                     |
| return\_value         | String  | The identifier of the new relationship.                                                                                                                                                                                                                                 |