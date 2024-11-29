# Tab section

## Configuration properties

Typically,
the height of the Tab section is the height of the currently displayed content.

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                              | Data type   |
|-------------------------------------|------------------------------------------------------------------------------------------|-------------|
| Color style                         | The color style for the view. The colors correspond to variables in the specified theme. | String      |
| Tab style                           | The appearance of the tabs. Available options are Default and Simple.                    | String      |
| Size                                | The size of the tabs.                                                                    | String      |

| Behavior configuration property   | Description                                                                                                                                                                                                                                                                                             | Data type   |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Default tab index                 | Specifies the default selection for the tabs. The selection indices start at 0, which places the default selection on the first tab in the view. If no value and no data binding are specified, the default index value is 0. If you do not want a default selection be specified, set the value to -1. | Integer     |

## Events

Set
or modify the event handlers for the view in the Events properties. You can set
events to be triggered programmatically or when a user interacts with the view. For information about how to define and code events, see User-defined events.

Tab section has the following types of event handlers:

- On load: Activated when the page loads. For example:
me.setCurrentPane(1)
- On tab changed: Activated when the tab is changed. For example:
if(oldTabIndex == 0){ ${ModalAlert}.setEnabled(true); }

## Methods

For detailed information on the available methods for Tab section, see the Tab section JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.