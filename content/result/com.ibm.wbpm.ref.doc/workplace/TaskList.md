### Methods

### Parent

### Helpers

<!-- image -->

| Show statistics:      | Show a summary of task statistics.                                                                                        | Boolean    |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------|------------|
| Show Refresh button:  | Show the Refresh button, which you can use to manually refresh the task list when the notification server is unavailable. | Boolean    |
| Hide status column:   | Hide the status column from the list.                                                                                     | Boolean    |
| Show Start workflow:  | Show the Start workflow button.                                                                                           | Boolean    |
| Disable actions menu: | Disable the menu that gives access to more actions for the task.                                                          | Boolean    |
| Hide search bar:      | Hide search bar                                                                                                           | Boolean    |
| Table style:          | The table style {Default | Condensed}                                                                                     | TableStyle |

| Customize columns:                   | Specify the columns to display in the task list.                                                                 | NameValuePair[]   |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------|-------------------|
| Set persistent filters:              | Select the binding to persist the filters in the task list.                                                      | SearchFilter[]    |
| Set tasks per page:                  | Enter the number of tasks to show per page.                                                                      | Integer           |
| Show saved searches:                 | Show a drop-down list of saved searches.                                                                         | Boolean           |
| Show search filter:                  | Show the search filter button.                                                                                   | Boolean           |
| Show view instance:                  | Enable the ability to open a task instance.                                                                      | Boolean           |
| Disable auto-refresh:                | Disable the auto-refresh of the list when filters are updated.                                                   | Boolean           |
| Filter by app:                       | Enter an app acronym to filter the list to show only tasks for that app.                                         | String            |
| Enable task prioritization:          | Activate Intelligent Task Prioritization that sorts the list, placing the best tasks to work on next at the top. | Boolean           |
| Set persistent searches:             | Select the binding to persist the recent searches in the search bar.                                             | String[]          |
| Use event to fetch tasks:            | Delegate the fetch tasks request to an event.                                                                    | Boolean           |
| Set event when tasks are launched:   | Enter the name of the event to fire when a task is opened.                                                       | String            |
| Check task ownership:                | Check whether the current user is authorized to open the task.                                                   | Boolean           |
| Disable opening of completed tasks:  | Disable opening of completed tasks                                                                               | Boolean           |
| Disable task claiming:               | Do not show the Claim task modal. The task is automatically claimed upon opening.                                | Boolean           |
| Set persistent saved searches:       | Select the binding to persist the saved searches in the task list                                                | String            |
| Enable batch modify:                 | Enable the modification of multiple selected tasks at once.                                                      | Boolean           |
| Set persistent column widths:        | Select the binding to persist the column widths in the task list.                                                | NameValuePair[]   |
| Set persistent sorting:              | Select the binding to persist the sorting of the task list.                                                      | NameValuePair     |
| Open task in new window:             | Open a task in a new window.                                                                                     | Boolean           |
| Enable task launch:                  | Enable the ability to open a task.                                                                               | Boolean           |
| Show copy link:                      | Show the copy link action in the overflow menu.                                                                  | Boolean           |
| Automatically claimed task:          | The task ID of the task that is automatically claimed when it appears in the task list.                          | String            |
| Set persistent advanced search:      | Select the binding to persist the advanced search of the task list.                                              | String            |
| Set persistent advanced search text: | Select the binding to persist the advanced search text of the task list.                                         | String            |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name    | Type   | Default   | Description                                                   |
|---------|--------|-----------|---------------------------------------------------------------|
| theView | {View} |           | The current view                                              |
| cell    | {Cell} |           | The table cell where the status information will be displayed |

| Name                | Type     | Default   | Description       |
|---------------------|----------|-----------|-------------------|
| row.td              | {object} |           | - task data       |
| row.data            | {object} |           | - task data       |
| row.data.TASK.TKIID | {string} |           | || row.data.tkiid |

| Name   | Type    | Default   | Description                  |
|--------|---------|-----------|------------------------------|
| event  | {event} |           | The actions menu click event |

| Name         | Type      | Default   | Description                                                               |
|--------------|-----------|-----------|---------------------------------------------------------------------------|
| collapseFlag | {boolean} |           | Set to true to collapse the view (equivalent to a view setting of "NONE") |

| Name   | Type   | Default   | Description                                         |
|--------|--------|-----------|-----------------------------------------------------|
| row    | {Row}  |           | The row of the table that contains the task record. |

| Name                     | Type      | Default   | Description                                                 |
|--------------------------|-----------|-----------|-------------------------------------------------------------|
| actionsMenuView          | {View}    |           | The actions menu view                                       |
| actionsMenuTargetElement | {Element} |           | The action menu button that was clicked to invoke the menu. |

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

| Name   | Type       | Default   | Description             |
|--------|------------|-----------|-------------------------|
| fields | {String[]} |           | The list of colum name. |

| Name       | Type              | Default   | Description                    |
|------------|-------------------|-----------|--------------------------------|
| conditions | {NameValuePair[]} |           | The list of filter conditions. |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name       | Type              | Default   | Description                    |
|------------|-------------------|-----------|--------------------------------|
| conditions | {NameValuePair[]} |           | The list of filter conditions. |

| Name       | Type              | Default   | Description                    |
|------------|-------------------|-----------|--------------------------------|
| conditions | {NameValuePair[]} |           | The list of filter conditions. |

| Name       | Type     | Default   | Description                                   |
|------------|----------|-----------|-----------------------------------------------|
| searchTerm | {string} |           | The search term used to filter the task list. |

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