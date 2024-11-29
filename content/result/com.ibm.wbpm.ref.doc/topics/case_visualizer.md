# Case Visualizer

You can configure the Case Visualizer by using the configuration properties. When Case Visualizer
view is used in the context of the process user task page, the view configures itself based on the
parent case, without specifying the Case identifier and Target Object Store name in the view’s
configuration.

## Configuration properties

| Property                                           | Description                                                                                                                                         | Data type   |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Case Identifier                                    | The Case Identifier is a mandatory option that needs to be bound to the input variable caseId.                                                      | String      |
| Target Object Store Name                           | The Target Object Store Name is a mandatory option that needs to be bound to the input variable tosName.                                            | String      |
| Edit title                                         | Allows to edit the title of this view.                                                                                                              | Any         |
| Hide title                                         | Allows to hide the title as an option.                                                                                                              | Any         |
| Show only this number of tasks and workitems       | Allows to enter the maximum number of tasks and work items to be shown in the tasks list.                                                           | Integer     |
| Show hidden tasks                                  | Shows the number of tasks and work items.                                                                                                           | Boolean     |
| Default time range to display(in number of events) | Loads maximum number of events to determine the default time range to display when opening the view.                                                | Integer     |
| Set default height                                 | Sets the default height of the view to 300 px. When the view is placed above any other view, if default height is not set, the views would overlap. | Boolean     |