### Methods

### Parent

### Helpers

<!-- image -->

| Show Refresh button:   | Show the Refresh button, which you can use to manually refresh the instance list when the notification server is unavailable.   | Boolean   |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------|-----------|
| Show Start workflow:   | Show the Start workflow button.                                                                                                 | Boolean   |
| Hide status column:    | Hide the status column from the list.                                                                                           | Boolean   |
| Disable actions menu:  | Disable the menu that gives access to more actions for the task.                                                                | Boolean   |
| Show search filter:    | Show the search filter button.                                                                                                  | Boolean   |

| Filter by project:                            | Enter the project name to filter the instance list to only the instances for that project.                                                                                                 | String          |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Customize instance columns:                   | Specify the columns to display in the instance list.                                                                                                                                       | NameValuePair[] |
| Set persistent instance filters:              | Select the binding to persist the filters in the instance list.                                                                                                                            | SearchFilter[]  |
| Set instances per page:                       | Enter the number of instances to show per page.                                                                                                                                            | Integer         |
| Enable instance launch:                       | Enable the ability to open a workflow instance.                                                                                                                                            | Boolean         |
| Set persistent searches:                      | Select the binding to persist the recent searches in the search bar.                                                                                                                       | String[]        |
| Case scope:                                   | Choose what case instances are included in your list, either all the instances that you're authorized to see or just the instances that are directly assigned to you. {Allowed | Assigned} | CaseScope       |
| Set persistent column widths:                 | Select the binding to persist the column widths in the instance list.                                                                                                                      | NameValuePair[] |
| Set persistent instance sorting:              | Select the binding to persist the sorting of the instance list.                                                                                                                            | NameValuePair   |
| Open instance in new window:                  | Open an instance in a new window.                                                                                                                                                          | Boolean         |
| Show copy link:                               | Show the copy link action in the overflow menu.                                                                                                                                            | Boolean         |
| Set persistent instance advanced search text: | Select the binding to persist the advanced search text of the instance list.                                                                                                               | String          |
| Set persistent instance advanced search:      | Select the binding to persist the advanced search of the instance list.                                                                                                                    | String          |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name   | Type   | Default   | Description       |
|--------|--------|-----------|-------------------|
| data   | {Data} |           | The instance data |

| Name    | Type   | Default   | Description                                                    |
|---------|--------|-----------|----------------------------------------------------------------|
| theView | {View} |           | The current view                                               |
| cell    | {Cell} |           | The table cell where the status information will be displayed. |

| Name         | Type      | Default   | Description                                                               |
|--------------|-----------|-----------|---------------------------------------------------------------------------|
| collapseFlag | {boolean} |           | Set to true to collapse the view (equivalent to a view setting of "NONE") |

| Name   | Type   | Default   | Description            |
|--------|--------|-----------|------------------------|
| view   | {View} |           | The view to initialize |

| Name   | Type   | Default   | Description                                      |
|--------|--------|-----------|--------------------------------------------------|
| row    | {Row}  |           | The table row that contains the instance record. |

| Name                     | Type      | Default   | Description                                                 |
|--------------------------|-----------|-----------|-------------------------------------------------------------|
| actionsMenuView          | {View}    |           | The actions menu view                                       |
| actionsMenuTargetElement | {Element} |           | The action menu button that was clicked to invoke the menu. |

| Name   | Type     | Default   | Description                                                                                            |
|--------|----------|-----------|--------------------------------------------------------------------------------------------------------|
| data   | {Object} |           | An object containing the input string, interaction filter, json query, and sort of the advanced search |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name       | Type              | Default   | Description                    |
|------------|-------------------|-----------|--------------------------------|
| conditions | {NameValuePair[]} |           | The list of filter conditions. |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name       | Type              | Default   | Description                    |
|------------|-------------------|-----------|--------------------------------|
| conditions | {NameValuePair[]} |           | The list of filter conditions. |

| Name       | Type     | Default   | Description                                  |
|------------|----------|-----------|----------------------------------------------|
| searchTerm | {string} |           | The search term to filter the instance list. |

| Name    | Type              | Default   | Description                   |
|---------|-------------------|-----------|-------------------------------|
| columns | {NameValuePair[]} |           | The list of selected columns. |

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