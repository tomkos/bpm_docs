# Configuration properties and configuration options

For example, the Radio Buttons view has the layout configuration option and a
Layout label. When you drop a Radio Button instance onto a view layout and then
select the instance, a list of configuration properties is displayed. One of these configuration
properties is Layout. You can choose Horizontal or Vertical for this configuration property. This
choice affects only this Radio Buttons instance.

- In the Label field, provide the display name of the configuration
property. If you do not provide a label, the view instance uses the name of the configuration option
as the display name.
- In the Documentation field, provide hover help text to help users decide
on the setting for that configuration property.
- To group several related configuration options, provide a group name. The view instance displays
the group name with a twistie. When users expand the twistie, they see all the configuration
properties that have the same group name. For example, you add config1 and
config2 to the Config group.When users click an instance of the view, they see the Config group. If
users expand the twistie, they see config1 and
config2.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

A view instance uses implicit default values for configuration properties if users do not set a
value for them. The implicit default value depends on the type. When you are defining a
Boolean-typed configuration option, you must account for its implicit default value, which is
false. This means that the designer displays Boolean-typed configuration options
set to false by default, such as check boxes being cleared.

<!-- image -->

<!-- image -->

When users are configuring the view instance and want to set a different value for each screen
size, they click the screen size icon next to the configuration option to specify that the value
applies to a large, medium, or small screen size. Then they can change the screen size setting to a
new size, and enter a new value for the configuration option. For information about responsive
settings for view instances, see the topic Responsive settings for views.

<!-- image -->

<!-- image -->

- You cannot statically bind to a business object that contains nested lists. Instead, you must
bind to it dynamically.
- If a dynamic value is set for a responsive configuration option instance, only one value can be
chosen. For example, you cannot bind a different variable for each screen size setting. One
exception to this restriction is configuration options that have a URL type. If these configuration
options are set to be responsive, they can accept values for different screen size settings provided
that those values are web files.
- Only configuration options that are object type can be marked as responsive. Responsive settings
are not supported for service-type configuration options.