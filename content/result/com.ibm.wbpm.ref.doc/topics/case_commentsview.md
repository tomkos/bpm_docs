# Case Comments

When Case Comments view is used in the context of the process user task page, the view configures
itself based on the parent case, without specifying the Case identifier and target object store name
in the view’s configuration.

## Configuration properties

| Property                    | Description                                                                                              | Data type   |
|-----------------------------|----------------------------------------------------------------------------------------------------------|-------------|
| Case Identifier             | The Case Identifier is a mandatory option that needs to be bound to the input variable caseId.           | String      |
| Target Object Store Name    | The target object store name is a mandatory option that needs to be bound to the input variable tosName. | String      |
| Edit title                  | Allows to edit the title of this view.                                                                   | Any         |
| Hide title                  | Allows to hide the title as an option.                                                                   | Any         |
| Get Repository Name Service | Service to retrieve the repository name that is associated to the case instance.                         | String      |