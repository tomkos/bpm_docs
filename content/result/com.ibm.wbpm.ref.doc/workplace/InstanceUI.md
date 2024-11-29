### Methods

### Parent

### Helpers

<!-- image -->

| Optimize for processes:    | Optimize the view to display process information                                  | Boolean   |
|----------------------------|-----------------------------------------------------------------------------------|-----------|
| Show the breadcrumb trail: | Show the navigation path to the current page in the task viewer.                  | Boolean   |
| Disable task claiming:     | Do not show the Claim task modal. The task is automatically claimed upon opening. | Boolean   |
| Embeded View:              | Hides the close button for embedding in another view.                             | Boolean   |

| Name   | Type   | Default   | Description                           |
|--------|--------|-----------|---------------------------------------|
| event  | {view} |           | The single select activity state view |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name   | Type   | Default   | Description      |
|--------|--------|-----------|------------------|
| event  | {view} |           | Instance UI view |

| Name      | Type     | Default   | Description                     |
|-----------|----------|-----------|---------------------------------|
| eventName | {String} |           | The event name                  |
| eventData | {Object} |           | A new workstream object binding |

| Name   | Type   | Default   | Description      |
|--------|--------|-----------|------------------|
| event  | {view} |           | Instance UI view |

| Name   | Type   | Default   | Description           |
|--------|--------|-----------|-----------------------|
| event  | {view} |           | The close button view |

| Name    | Type   | Default   | Description                                                    |
|---------|--------|-----------|----------------------------------------------------------------|
| theView | {View} |           | The current view                                               |
| cell    | {Cell} |           | The table cell where the status information will be displayed. |

| Name         | Type      | Default   | Description                                                               |
|--------------|-----------|-----------|---------------------------------------------------------------------------|
| collapseFlag | {boolean} |           | Set to true to collapse the view (equivalent to a view setting of "NONE") |

| Name   | Type   | Default   | Description      |
|--------|--------|-----------|------------------|
| event  | {view} |           | Instance UI view |

| Name   | Type   | Default   | Description                                      |
|--------|--------|-----------|--------------------------------------------------|
| task   | {Task} |           | The table row that contains the instance record. |

| Name   | Type   | Default   | Description                   |
|--------|--------|-----------|-------------------------------|
| target | {view} |           | The comment card wrapper view |

| Name   | Type   | Default   | Description                 |
|--------|--------|-----------|-----------------------------|
| view   | {view} |           | All the activity card views |
| target | {view} |           | A single activity card view |

| Name          | Type      | Default   | Description                                                                    |
|---------------|-----------|-----------|--------------------------------------------------------------------------------|
| target        | {view}    |           | The comment card wrapper view                                                  |
| isForActivity | {boolean} |           | Returns true if it is a Workstream activity and not an instance-level activity |

| Name   | Type   | Default   | Description                |
|--------|--------|-----------|----------------------------|
| target | {view} |           | The data card wrapper view |

| Name   | Type   | Default   | Description                    |
|--------|--------|-----------|--------------------------------|
| target | {view} |           | The document card wrapper view |

| Name   | Type   | Default   | Description                              |
|--------|--------|-----------|------------------------------------------|
| target | {view} |           | The activity startable card wrapper view |

| Name   | Type     | Default   | Description    |
|--------|----------|-----------|----------------|
| event  | {string} |           | The event name |

| Name                     | Type      | Default   | Description                                                    |
|--------------------------|-----------|-----------|----------------------------------------------------------------|
| actionsMenuView          | {View}    |           | The actions menu view                                          |
| actionsMenuTargetElement | {Element} |           | In the instance list, the button you click to invoke the menu. |

| Name                     | Type      | Default   | Description                                                    |
|--------------------------|-----------|-----------|----------------------------------------------------------------|
| actionsMenuView          | {View}    |           | The actions menu view                                          |
| actionsMenuTargetElement | {Element} |           | In the instance list, the button you click to invoke the menu. |

| Name        | Type     | Default   | Description        |
|-------------|----------|-----------|--------------------|
| event       | {view}   |           | Instance UI view   |
| oldTabIndex | {Number} |           | previous tab index |
| tabIndex    | {Number} |           | current tab index  |

| Name   | Type   | Default   | Description                          |
|--------|--------|-----------|--------------------------------------|
| event  | {view} |           | The instance action menu button view |

| Name   | Type   | Default   | Description      |
|--------|--------|-----------|------------------|
| event  | {view} |           | Instance UI view |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name   | Type   | Default   | Description                     |
|--------|--------|-----------|---------------------------------|
| event  | {view} |           | The reload instance button view |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name     | Type     | Default   | Description       |
|----------|----------|-----------|-------------------|
| instance | {Object} |           | The instance data |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

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

| Name   | Type   | Default   | Description                      |
|--------|--------|-----------|----------------------------------|
| target | {view} |           | The activity startable icon view |

| Name      | Type     | Default   | Description                     |
|-----------|----------|-----------|---------------------------------|
| eventName | {String} |           | The event name                  |
| eventData | {Object} |           | A new workstream object binding |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |