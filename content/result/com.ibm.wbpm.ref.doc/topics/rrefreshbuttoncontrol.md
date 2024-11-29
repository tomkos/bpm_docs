# Refresh Button

To automatically refresh the controls in the view, see Refresh Controller control.
To trigger the refresh of the controls in a view by using boundary
events, see Service Controller control.

## Restrictions and limitations

- This view does not use the visibility property.
- For performance reasons, the Refresh Controller control can be
disabled by the system administrator. To ensure that the contents
of the coach view can be refreshed, always include the Refresh Controller,
the Refresh Button, and the Service Controller controls in a coach
view.

- The control has a Refresh trigger configuration
property that is wired to the variable that is bound to the Refresh
Button control.
- The control responds to boundary events from the Service Controller
control.

## Data binding

Set the data binding for the view in the General properties
tab.

| Description                                                                                                                                                                                                                                                                  | Data type   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| A variable that enables the manual refresh of the contents of a coach view. When the user clicks the Refresh button, the Refresh Button control changes the value of the variable to true. Coach controls that are bound to the variable can respond to the refresh request. | Boolean     |

## Refresh behavior

When the button is clicked,
the control changes the value of the bound Boolean variable from false to true.
Other coach controls in the view must include a configuration property
that is wired to the variable that is used by the data binding so
that they can react to the refresh request. During the refresh, the
value of the bound variable is reset to false.