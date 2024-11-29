# Case History

When the Case History view is used in the context of the process user task page, it configures
itself based on the parent case, without specifying the case identifier and the target object store
name in the view’s configuration.

## Configuration properties

| Property                    | Description                                                                                              | Data type   |
|-----------------------------|----------------------------------------------------------------------------------------------------------|-------------|
| Case Identifier             | The case identifier is a mandatory option that needs to be bound to the input variable caseId.           | String      |
| Target Object Store Name    | The target object store name is a mandatory option that needs to be bound to the input variable tosName. | String      |
| Edit title                  | Allows to edit the title of this view.                                                                   | Any         |
| Hide title                  | Allows to hide the title as an option.                                                                   | Any         |
| Is Case Client              | The option set to indicate whether the view is used in the context of Case Client or Workplace.          | Boolean     |
| Get Repository Name Service | Service to retrieve the repository name that is associated to the case instance.                         | String      |
| Initial Size                | Initial number of table rows to display.                                                                 | Integer     |

The detailed state changes for case stages are not listed in the Case History view due to the
default filter set to “All”. To view the detailed case stage state changes, select the “Stages”
filter. The view also does not display the completed state of a case.