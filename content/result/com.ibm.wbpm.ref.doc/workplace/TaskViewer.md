### Methods

### Parent

### Helpers

<!-- image -->

| Set task:                  | Set the task that you want to display in the task viewer.        | ANY      |
|----------------------------|------------------------------------------------------------------|----------|
| Customize system data:     | Set the system data that you want to display in the task viewer. | String   |
| Set task actions:          | Specify the list of actions that can be performed on the task.   | String[] |
| Show on task closed:       | Show the task viewer when the task is closed.                    | Boolean  |
| Show the breadcrumb trail: | Show the navigation path to the current page in the task viewer. | Boolean  |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name         | Type      | Default   | Description                                                               |
|--------------|-----------|-----------|---------------------------------------------------------------------------|
| collapseFlag | {boolean} |           | Set to true to collapse the view (equivalent to a view setting of "NONE") |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name    | Type   | Default   | Description                                 |
|---------|--------|-----------|---------------------------------------------|
| service | {ANY}  |           | The data to be set on the Task Viewer view. |

| Name         | Type   | Default   | Description                        |
|--------------|--------|-----------|------------------------------------|
| task         | {ANY}  |           | The data to be set on Task Viewer. |
| businessData | {ANY}  |           | The data to be set on Task Viewer. |
| systemData   | {ANY}  |           | The data to be set on Task Viewer. |

| Name                | Type      | Default   | Description                                                                            |
|---------------------|-----------|-----------|----------------------------------------------------------------------------------------|
| data                | {Object}  |           | Value of bound data. The type of this parameter must match the type of the bound data. |
| createPseudoBinding | {boolean} |           | If set to true, creates a pseudo binding if there is no current binding.               |

| Name     | Type      | Default   | Description                                                             |
|----------|-----------|-----------|-------------------------------------------------------------------------|
| visible  | {boolean} |           | Visibility flag (true to show view, false to hide)                      |
| collapse | {boolean} |           | Set to true to collapse the control space when visible is set to false. |

| MyView.setVisible(false, false); //Equivalent to MyView.hide()   |
|------------------------------------------------------------------|
| MyView.setVisible(false, true); // Sets visibility to "None"     |