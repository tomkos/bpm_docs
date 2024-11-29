### Methods

### Parent

### Helpers

| Name      | Type                          | Default   | Description                                          |
|-----------|-------------------------------|-----------|------------------------------------------------------|
| view      | {com.ibm.bpm.coach.CoachView} |           | Reference.                                           |
| eventName | {string}                      |           | Name of the event handling function to be retrieved. |

| Name   | Type                          | Default   | Description   |
|--------|-------------------------------|-----------|---------------|
|        | {com.ibm.bpm.coach.CoachView} |           | view          |

| Name                          | Type                          | Default   | Description                                                                                                 |
|-------------------------------|-------------------------------|-----------|-------------------------------------------------------------------------------------------------------------|
| onlyEmpty                     | {boolean}                     |           | return only views that are required (visibility = REQUIRED) AND whose binding data is empty.                |
| fromView                      | {com.ibm.bpm.coach.CoachView} |           | view to start the query from. Defaults to the page root.                                                    |
| includeDefaultVisibilityViews | {boolean}                     |           | include views whose visibility is the "Same as parent". Adjusts based on the visibility of the parent view. |

| var viewList = bpmext.ui.getRequiredViews(); //checks all views on the page and returns any whose visibility is REQUIRED                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| var viewList = bpmext.ui.getRequiredViews(true); //checks all views on the page and returns any whose visibility is REQUIRED and whose binding data is empty |

| Name         | Type                          | Default   | Description                                                           |
|--------------|-------------------------------|-----------|-----------------------------------------------------------------------|
| functionName | {string}                      |           | Name of the function to locate.                                       |
| fromView     | {com.ibm.bpm.coach.CoachView} |           | Reference to an SPARK    view/control from which to start the search. |

| Name   | Type                          | Default   | Description                                                         |
|--------|-------------------------------|-----------|---------------------------------------------------------------------|
| view   | {com.ibm.bpm.coach.CoachView} |           | A reference to an SPARK section (not a regular non-containing view) |

| Name         | Type                          | Default   | Description                                                     |
|--------------|-------------------------------|-----------|-----------------------------------------------------------------|
| view         | {com.ibm.bpm.coach.CoachView} |           | Reference to a SPARK view/control                               |
| optionName   | {string}                      |           | The name of the configuration option for the view               |
| defaultValue | {ANY}                         |           | (Optional) The default value to return if the option is not set |

| Name      | Type                          | Default   | Description                      |
|-----------|-------------------------------|-----------|----------------------------------|
| eventName | {string}                      |           | Name of the event to be checked. |
| view      | {com.ibm.bpm.coach.CoachView} |           | Reference to the view to check.  |

| Name      | Type                          | Default   | Description                                                        |
|-----------|-------------------------------|-----------|--------------------------------------------------------------------|
| view      | {com.ibm.bpm.coach.CoachView} |           | Reference.                                                         |
| eventName | {string}                      |           | Name of the event handling function to be executed.                |
| argument  | {...object}                   |           | Up to 9 arguments in addition to the view to pass to the function. |

| Name   | Type                          | Default   | Description                                                       |
|--------|-------------------------------|-----------|-------------------------------------------------------------------|
| view   | {com.ibm.bpm.coach.CoachView} |           | A reference to a repeating SPARK view/control                     |
| [deep  | {boolean}                     |           | = false] an indication of whether to drill down into nested views |

| Name               | Type                          | Default   | Description                                                                     |
|--------------------|-------------------------------|-----------|---------------------------------------------------------------------------------|
| view               | {com.ibm.bpm.coach.CoachView} |           | View instance of the view where this method is executed.                        |
| childViewControlId | {string}                      |           | Control ID of direct design time child view on which the event is to be preset. |
| configOptionName   | {string}                      |           | Name of configuration option to be preset.                                      |
| configOptionValue  | {string}                      |           | Value which is to be preset to the configuration option.                        |

| Name   | Type            | Default   | Description            |
|--------|-----------------|-----------|------------------------|
| prefix | {string|number} |           | Optional prefix for ID |

| Name   | Type                          | Default   | Description                              |
|--------|-------------------------------|-----------|------------------------------------------|
| view   | {com.ibm.bpm.coach.CoachView} |           | The view who's errors are to be returned |

| Name                 | Type      | Default   | Description                                                                                                                                         |
|----------------------|-----------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| title                | {string}  |           | The title of the alert                                                                                                                              |
| text                 | {string}  |           | The text of the alert                                                                                                                               |
| style                | {string}  |           | The style to use for this alert. Used to generate the event name for the alert.                                                                     |
| topic                | {string}  | ""        | The topic of the alert. Used to generate the event name for the alert.                                                                              |
| timeout              | {int}     |           | The timeout value in milliseconds.  Time before the alert is removed.                                                                               |
| id                   | {string}  |           | The id of the alert.                                                                                                                                |
| data                 | {object}  |           | The payload data for the alert.                                                                                                                     |
| iconSetting.showIcon | {boolean} |           | True indicates that showing the alert icon, false means not showing icons, undefined indicates remain the default setting (carbon theme restricted) |
| iconSetting.iconName | {String}  |           | Name of a carbon icon, applying only on one alert instance. If the value is not defined, then default value will be applied (carbon icon only)      |

| Name         | Type                          | Default   | Description                                                                                                                                                         |
|--------------|-------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| view         | {com.ibm.bpm.coach.CoachView} |           | A reference to an SPARK view/control                                                                                                                                |
| type         | {string}                      |           | (Optional) Specify "config" for a configuration object or "binding" for the bound object. Default is "binding" (if null is specified)                               |
| propertyName | {string}                      |           | When type is "config" specify the name of the configuration property, when type is "binding" specify the name of the "Business Data" variable (i.e. bound variable) |
| defVal       | {ANY}                         |           | (Optional)    (e.g. "selectedItem" for the Select control)                                                                                                          |

| Name              | Type                          | Default   | Description                                                     |
|-------------------|-------------------------------|-----------|-----------------------------------------------------------------|
| view              | {com.ibm.bpm.coach.CoachView} |           | A reference to an SPARK view/control                            |
| callback          | {function}                    |           | function to be executed for each identically named sibling view |
| includeContainers | {boolean}                     |           | an indication of whether to return sibling container views      |

| Name   | Type                          | Default   | Description                          |
|--------|-------------------------------|-----------|--------------------------------------|
| view   | {com.ibm.bpm.coach.CoachView} |           | A reference to an SPARK view/control |

| Name     | Type                          | Default   | Description                                                                                                                                   |
|----------|-------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| viewPath | {string}                      |           | Path is the format view/subview/subsubview/etc.    For arrays of view, use the [] notation. e.g. view/subview[0]/subsubview[5]/etc.           |
| fromView | {com.ibm.bpm.coach.CoachView} |           | Optional reference to an SPARK    view/control from which to start the search. If not specified, search starts from the top of the view tree. |

| Name      | Type                          | Default   | Description                                                        |
|-----------|-------------------------------|-----------|--------------------------------------------------------------------|
| view      | {com.ibm.bpm.coach.CoachView} |           | Reference to the view being processed.                             |
| eventName | {string}                      |           | Name of the event to be added.                                     |
| argument  | {...object}                   |           | Up to 9 arguments in addition to the view to pass to the function. |

| Name   | Type                          | Default   | Description                                               |
|--------|-------------------------------|-----------|-----------------------------------------------------------|
| view   | {com.ibm.bpm.coach.CoachView} |           | The view to be pushed into the validation container stack |

| Name               | Type                          | Default   | Description                                                                                                                                                           |
|--------------------|-------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| view               | {com.ibm.bpm.coach.CoachView} |           | View instance where this method is executed.    Note that property \_\_fn\_preset\_handler\_numericIndex (e.g. \_\_fn\_preset\_handler\_2) is set on the prototype of the view. |
| childViewControlId | {string}                      |           | Control ID of direct design time child view on which the event is to be preset.                                                                                       |
| eventName          | {string}                      |           | Name of the event to be preset.                                                                                                                                       |
| eventHandler       | {function}                    |           | Event handler function which is to be preset.                                                                                                                         |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required flag for control                                      |

| Name     | Type                          | Default   | Description                                                                                                                                   |
|----------|-------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| data     | {Object}                      |           | The data to set into the view's bound data                                                                                                    |
| viewPath | {string}                      |           | Path is the format view/subview/subsubview/etc.    For arrays of view, use the [] notation. e.g. view/subview[0]/subsubview[5]/etc.           |
| fromView | {com.ibm.bpm.coach.CoachView} |           | Optional reference to an SPARK    view/control from which to start the search. If not specified, search starts from the top of the view tree. |

| Name   | Type                          | Default   | Description                                       |
|--------|-------------------------------|-----------|---------------------------------------------------|
| view   | {com.ibm.bpm.coach.CoachView} |           | A reference to a section-style SPARK view/control |

| Name     | Type                          | Default   | Description                                                                                                                                   |
|----------|-------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| viewPath | {string}                      |           | Path is the format view/subview/subsubview/etc.    For arrays of view, use the [] notation. e.g. view/subview[0]/subsubview[5]/etc.           |
| fromView | {com.ibm.bpm.coach.CoachView} |           | Optional reference to an SPARK    view/control from which to start the search. If not specified, search starts from the top of the view tree. |

| Name      | Type                          | Default   | Description                                         |
|-----------|-------------------------------|-----------|-----------------------------------------------------|
| view      | {com.ibm.bpm.coach.CoachView} |           | Reference.                                          |
| eventName | {string}                      |           | Name of the event handling function to be executed. |

| Name         | Type                          | Default   | Description                          |
|--------------|-------------------------------|-----------|--------------------------------------|
| view         | {com.ibm.bpm.coach.CoachView} |           | A reference to an SPARK view/control |
| propertyName | {string}                      |           | (Optional)                           |
| defVal       | {ANY}                         |           | (Optional)                           |

| Name         | Type                          | Default   | Description                                                           |
|--------------|-------------------------------|-----------|-----------------------------------------------------------------------|
| functionName | {string}                      |           | Name of the function to locate.                                       |
| fromView     | {com.ibm.bpm.coach.CoachView} |           | Reference to an SPARK    view/control from which to start the search. |

| Name   | Type                          | Default   | Description                             |
|--------|-------------------------------|-----------|-----------------------------------------|
| view   | {com.ibm.bpm.coach.CoachView} |           | The view to be updated                  |
| id     | {string}                      |           | The element id of the item to be marked |

| Name     | Type                          | Default   | Description                                     |
|----------|-------------------------------|-----------|-------------------------------------------------|
|          | {com.ibm.bpm.coach.CoachView} |           | view                                            |
| function | {function}                    |           | The function to be called on update             |
| function | {function}                    |           | The function to be called to get default values |

| Name   | Type                          | Default   | Description                          |
|--------|-------------------------------|-----------|--------------------------------------|
| view   | {com.ibm.bpm.coach.CoachView} |           | A reference to an SPARK view/control |

| Name   | Type                          | Default   | Description                                                       |
|--------|-------------------------------|-----------|-------------------------------------------------------------------|
| view   | {com.ibm.bpm.coach.CoachView} |           | A reference to a repeating SPARK view/control                     |
| [deep  | {boolean}                     |           | = false] an indication of whether to drill down into nested views |

| Name      | Type                          | Default   | Description                                              |
|-----------|-------------------------------|-----------|----------------------------------------------------------|
| eventName | {string}                      |           | Name of the event to be removed.                         |
| view      | {com.ibm.bpm.coach.CoachView} |           | Reference to an SPARK view/control which is subscribing. |

| Name   | Type                          | Default   | Description                                       |
|--------|-------------------------------|-----------|---------------------------------------------------|
| view   | {com.ibm.bpm.coach.CoachView} |           | A reference to a section-style SPARK view/control |

| Name   | Type                          | Default   | Description                                              |
|--------|-------------------------------|-----------|----------------------------------------------------------|
| view   | {com.ibm.bpm.coach.CoachView} |           | The view to be updated                                   |
| id     | {string}                      |           | The id of the validation error                           |
| text   | {string}                      |           | Validation error text to show on the invalid-styled view |

| Name   | Type                          | Default   | Description                                              |
|--------|-------------------------------|-----------|----------------------------------------------------------|
| view   | {com.ibm.bpm.coach.CoachView} |           | view to start the check from. Defaults to the page root. |

| var invalidList = bpmext.ui.getInvalidViews(); //checks all views on the page and returns any marked as invalid     |
|---------------------------------------------------------------------------------------------------------------------|
| var invalidSection = bpmext.ui.getInvalidViews(${Horizontal\_Layout1}); //checks all views inside Horizontal\_Layout1 |

| Name       | Type                          | Default   | Description                                                      |
|------------|-------------------------------|-----------|------------------------------------------------------------------|
| eventName  | {string}                      |           | Name of the event to be subscribed to.                           |
| callback   | {function}                    |           | function to receive control when the event is published.         |
| view       | {com.ibm.bpm.coach.CoachView} |           | Reference to an SPARK view/control which is subscribing.         |
| persistent | {boolean}                     | false     | indicator of whether or not to make the subscription persistent. |

| Name       | Type      | Default   | Description                                                                   |
|------------|-----------|-----------|-------------------------------------------------------------------------------|
| eventName  | {string}  |           | Name of the event to be published.                                            |
| payload    | {object}  |           | to be passed to the registered callback function.                             |
| persistent | {boolean} | false     | indicator of whether or not to make the publish persistent.                   |
| async      | {boolean} | false     | indicator of whether the subscribers should be notified asynchronously or not |

| Name   | Type                          | Default   | Description                                       |
|--------|-------------------------------|-----------|---------------------------------------------------|
| view   | {com.ibm.bpm.coach.CoachView} |           | The view to be updated                            |
| event  | {object}                      |           | The event passed to the validation event handler. |

| Name   | Type                          | Default   | Description                          |
|--------|-------------------------------|-----------|--------------------------------------|
| view   | {com.ibm.bpm.coach.CoachView} |           | A reference to an SPARK view/control |

| Name   | Type                          | Default   | Description                                              |
|--------|-------------------------------|-----------|----------------------------------------------------------|
| view   | {com.ibm.bpm.coach.CoachView} |           | The view to be popped off the validation container stack |

| Name   | Type                          | Default   | Description                          |
|--------|-------------------------------|-----------|--------------------------------------|
| view   | {com.ibm.bpm.coach.CoachView} |           | A reference to an SPARK view/control |

| Name   | Type                          | Default   | Description                                          |
|--------|-------------------------------|-----------|------------------------------------------------------|
| view   | {com.ibm.bpm.coach.CoachView} |           | A reference to an SPARK view/control (not a section) |

| Name     | Type                          | Default   | Description                                                                                                                                   |
|----------|-------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| viewPath | {string}                      |           | Path is the format view/subview/subsubview/etc.    For arrays of view, use the [] notation. e.g. view/subview[0]/subsubview[5]/etc.           |
| fromView | {com.ibm.bpm.coach.CoachView} |           | Optional reference to an SPARK    view/control from which to start the search. If not specified, search starts from the top of the view tree. |