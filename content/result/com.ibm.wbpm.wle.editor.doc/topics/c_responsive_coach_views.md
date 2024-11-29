# Responsive settings for views

You can build interfaces that are responsive to the user's runtime environment by specifying the
responsive view settings. You can configure these settings separately for different screen sizes so
that you can design one interface that changes in appearance and behavior based on the user's screen
size.

<!-- image -->

| Screen size setting   | Icon   | Width                 |
|-----------------------|--------|-----------------------|
| Small                 |        | 640 pixels or less    |
| Medium                |        | 641 - 1024 pixels     |
| Large (default)       |        | More than 1024 pixels |

When you build your coach or view, you can configure the responsive settings for all the view
instances in your coach or view by using one screen size. You can then configure the same settings
using different values for another screen size. At run time, the pixel count of the viewport width
determines which screen-size setting the device browser uses to display the coach and the views that
it contains. Typically, the device browser uses the same screen-size setting regardless of the
device orientation. If a device has an unusual size, however, the browser could have one screen size
for the portrait orientation and a different screen size for the landscape orientation, depending on
the widths of the two orientations.

Note that the viewport pixel counts for a web browser on a device do not necessarily match the
advertised pixel counts of the device screen. The web browser viewport is often smaller.

The large screen size is the default. If you do not provide different values for a responsive
setting that is available for a view instance, all three screen sizes use the same value for the
setting and the view instance appears the same in all user environments. For example, if you set
values for the view instance margins for the large screen size, and do not provide values for the
medium or small screen sizes, then the large screen values apply in all user environments.

If you set the responsive settings for a view instance for the medium screen size, but do not
provide values for the small screen size, the medium screen size values apply in small screen size
environments.

## Responsive settings for view instances

You
can configure the following types of properties for different screen
sizes: positioning properties, configuration options, and visibility
properties.

Positioning properties enable you to configure the placement and spacing of a view instance. You
can set positioning properties for each screen size, for example, so that coach content can be
spaced more closely together when the interface is displayed on smaller devices. For information
about how to set responsive positioning properties, see Positioning options for view instances.

Configuration options, when they are marked as responsive, can change the presentation or even
the contents of a view instance, depending on the device. You can also add responsive configuration
options to your own views.

For example, you might create a view with a configuration option that determines whether
selection widgets on an instance of that view are rendered as check boxes, radio buttons, or slider
widgets. If this configuration option is marked as responsive, it can have three different settings
corresponding to three different screen size settings. For information about how to set
configuration properties as responsive, see Configuration properties and configuration options.

Visibility properties, which determine whether a view is hidden, visible, editable, and so on,
can also be set relative to a particular device size. For example, to pare down the user interface
in the smallest screen-size environments, you might hide a more detailed view instance in small
screen size environments and show a simplified version instead. For information about how to set
responsive visibility properties, see View visibility properties.