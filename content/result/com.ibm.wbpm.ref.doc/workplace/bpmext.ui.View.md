### Methods

### Parent

### Helpers

| Name    | Type      | Default   | Description                                                                    |
|---------|-----------|-----------|--------------------------------------------------------------------------------|
| literal | {boolean} |           | Return the literal parent (which may be a visual-only section) of this control |

| Name      | Type     | Default   | Description                                      |
|-----------|----------|-----------|--------------------------------------------------|
| eventName | {string} |           | Name of event for which to test the subscription |

| alert("Index of this control: " + me.ui.getIndex()); // this example does not work for views within a paginated table                                                                                                                                                                                                                                                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| // the following example can be used to get the correct index when a button view is used within a paginated table    // Note: To use this example within a custom function, it needs to be defined with the parameter "me". For instance, function(me) {...}    var tableView = me.ui.getParent(me);    var row = tableView.getRow(me);    var record = row.getData();    var recordIndex = tableView.getRecordIndex(record);    console.log("I clicked the button with index: ",recordIndex); |

| Name    | Type      | Default   | Description                                                                           |
|---------|-----------|-----------|---------------------------------------------------------------------------------------|
| name    | {string}  |           | Return a control in the ancestor chain of this control matching the name specified    |
| literal | {boolean} |           | Searches the literal ancestor(s) (which may be a visual-only section) of this control |

| Name   | Type      | Default   | Description                                                          |
|--------|-----------|-----------|----------------------------------------------------------------------|
| name   | {string}  |           | Name of a control that is an immediate literal child of this control |
| index  | {integer} |           | Index of child control (if the child control is repeating)           |

| Name         | Type     | Default   | Description                                                |
|--------------|----------|-----------|------------------------------------------------------------|
| functionName | {string} |           | Name of the function to invoke                             |
| args         | {...ANY} |           | 0 or more arguments passed to the function (up to 9 total) |

| Name       | Type     | Default   | Description                                                     |
|------------|----------|-----------|-----------------------------------------------------------------|
| optionName | {string} |           | The name of the configuration option for the view               |
| defVal     | {ANY}    |           | (Optional) The default value to return if the option is not set |

| Name      | Type     | Default   | Description                         |
|-----------|----------|-----------|-------------------------------------|
| eventName | {string} |           | Name of event previously registered |

| Name   | Type     | Default   | Description               |
|--------|----------|-----------|---------------------------|
| path   | {string} |           | Relative path to the view |

| Name   | Type     | Default   | Description                                                   |
|--------|----------|-----------|---------------------------------------------------------------|
| name   | {string} |           | Return a control on the same addressing level as this control |

| Name             | Type       | Default   | Description                                         |
|------------------|------------|-----------|-----------------------------------------------------|
| eventName        | {string}   |           | Name of event associated with the callback function |
| callbackFunction | {function} |           | Reference to the callback function                  |

| Name      | Type     | Default   | Description                                             |
|-----------|----------|-----------|---------------------------------------------------------|
| eventName | {string} |           | Name of event to be published                           |
| payload   | {Object} |           | Additional (optional) data to send to event subscribers |

| Name   | Type     | Default   | Description                                                     |
|--------|----------|-----------|-----------------------------------------------------------------|
| path   | {string} |           | Path to the view (start path with / for absolute addressing)    |
| index  | {number} |           | Index of the child view if the path refers to an array of views |

| Name   | Type     | Default   | Description                                                        |
|--------|----------|-----------|--------------------------------------------------------------------|
| path   | {string} |           | Path to the view array (start path with / for absolute addressing) |