# Refresh Controller

To manually refresh the controls in the view, see Refresh Button control. To trigger the refresh of the controls in a view by using
boundary events, see Service Controller control. To
ensure that the contents of the view can be refreshed, always include the Refresh Controller, the
Refresh Button, and the Service Controller controls in a view.

## Restrictions and limitations

- For performance reasons, the Refresh Controller control can be disabled by the system
administrator. For custom instance details pages, always include the Refresh Controller, the Refresh
Button, and the Service Controller control in the view to provide a refresh mechanism for the other
pages in the view.
- This view does not use the visibility property.

- The control has a Refresh trigger configuration property that is wired to
the variable that is bound to the Refresh Controller control.
- The control responds to boundary events from the Service Controller control.

## Data binding

| Description                                                                                                                                                                                                                      | Data type   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| A variable that enables the automatic refresh of the contents of a view. When the Refresh Controller control changes the value of the variable to true, views that are bound to the variable can respond to the refresh request. | Boolean     |

## Configuration properties

| Configuration property   | Property variable         | Description                                                                                                    |
|--------------------------|---------------------------|----------------------------------------------------------------------------------------------------------------|
| Time between refreshes   | refreshInterval (Integer) | The time in seconds between refresh events that are triggered by the control. The default value is 60 seconds. |

## Refresh behavior