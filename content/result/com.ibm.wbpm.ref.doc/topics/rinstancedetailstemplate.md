# Default Instance Details template

- Responsive Document Explorer
- Instance Activities Section control
- Instance Summary Section control
- Instance Tasks Section control
- Refresh Button control

The Default Get Related ECM Folders Service is available as a configuration property on the
Default Instance Details template. This configuration property can be useful if you want to
customize the behavior on the instance details user interface. You can, for example, constrain the
number of returned folders to be the folders only appropriate to your application. See the example
in Adding references.

- Refresh Controller control
- Service Controller control

The template does not include a Data Section control.
Instead, it includes a content box that you can use to create a customized
data section. Alternatively, you can reproduce the ready-to-use instance
details page, by dropping a Data Section control into the content
box.

You can create a customized instance details page from
a copy of the template, and then add or remove coach views. You can
also customize each of the individual coach views, for example, by
updating the configuration properties for the control. For more information,
see the documentation for the individual coach controls.

## Restrictions and limitations

- The Responsive Document Explorer control is available only for
process instances.
- If you are migrating process applications created before Business Automation Workflow 8.5.7,
such as process applications created with the case editor in Business Automation Workflow 8.5.6,
you must add the Responsive Coaches toolkit to your process applications.

## Refresh behavior provided by the template

- The Refresh Controller control automatically triggers refreshes at regular intervals. It is
bound to the template's Automatic refresh trigger configuration
property.
- The Refresh Button control triggers a refresh when a user clicks the button. It is bound to the
template's Manual refresh trigger configuration property.
- Two Service Controller controls that send boundary events to refresh service variables when the
value of the bound variable changes. One of these controls is bound to the Automatic
refresh trigger configuration property and the other control is bound to the
Manual refresh trigger configuration property.

When a refresh
needs to happen, the notifying control changes the value of the bound
variable to true, which triggers the refresh of the
controls in the body of the view. When the refresh is complete, the
value of the bound variable is reset to false.