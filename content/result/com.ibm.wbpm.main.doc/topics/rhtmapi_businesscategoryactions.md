# Actions for business category

There are actions that roles can take for any given business
category.

Access to the HumanTaskManager interface does not guarantee that
the caller can perform all of the actions on a business category.
The caller must be logged on to the client application with a role
that is authorized to perform the action

The following table shows the actions on a business category that
a specific role can take.

| Action                        | Caller’s principal roleReader    | TaskSystemAdministrator / BusinessCategorySystemAdministrator   |
|-------------------------------|----------------------------------|-----------------------------------------------------------------|
| CREATEBUSINESSCATEGORY        | No                               | Yes                                                             |
| DELETEBUSINESSCATEGORY        | No                               | Yes                                                             |
| GETBUSINESSCATEGORY           | Yes                              | Yes                                                             |
| GETBUSINESSCATEGORYDEFINITION | No                               | Yes                                                             |
| GETROLEINFO                   | Yes                              | Yes                                                             |
| UPDATE                        | No                               | Yes                                                             |