# Alerts

The Alerts view is a listener and the alerts are sent using the
bpmext.ui.alert() method. An alert automatically closes based on the
Default auto close delay configuration option, which means that you don't
need to manually close the alert. However, you can choose to close the alert manually at any
time.

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                | Data type       |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Default alert color style           | Specifies an alert color style to use when no color is specified. The colors correspond to variables in the specified theme. The default alert color style is Info (blue). | AlertColorStyle |
| Dark style                          | Specifies that a darker color is used for alerts. By default, this property is selected.                                                                                   | Boolean         |
| No vertical spacing                 | Specifies that no vertical spacing is shown between alerts. By default, this property is not selected.                                                                     | Boolean         |
| Show alert icon                     | Displays the alert icon. This option is available only for the Carbon theme.                                                                                               | Boolean         |

| Behavior configuration property   | Description                                                                                                                                                                                                                                                                                                                           | Data type    |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Alert topic                       | Specifies the topics that the view should listen for. Use the wild card asterisk character (*) to listen for alerts with unspecified topics. This is the default setting. When no topics are specified, the alert will listen for all unspecified topics, which is the same as specifying the wild card character as the alert topic. | String(List) |
| Default auto close delay          | Specifies the number of milliseconds each alert is displayed before closing. By default, no value is specified. If a value of 0 is specified, the alert will not close.                                                                                                                                                               | Integer      |

## Events

- On alert Click: Activated when an alert is clicked. For
example:${WarningNavigationEvent}.fire()
- On alert close: Activated when an alert is closed. For
example:me.ui.invoke("addNotif", item)
- On alert expired: Activated when the time duration specified for the
Default auto close delay property expires. For
example:me.ui.invoke("addNotif", item)

Depending on the specific event, you can use JavaScript logic to modify the effects of the
view. More information on using events with views is found in the topic
User-defined events.

## Methods

For detailed information on the available methods for Alerts, see the Alerts JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.