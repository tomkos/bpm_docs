# View visibility properties

- When you set the Visibility property to Editable, users can see the view
and add or edit values in it or otherwise interact with it.
- When you set the visibility to Required, the view is editable and also
has a decorator that indicates to users that they must enter or set a value. Important: Setting the visibility to Required does not validate whether a user enters
or sets a value. You must provide code that does this checking by, for example, implementing a
validation service or script for the coach that contains the view.
- When you set the visibility to Read only, users can see the view but
cannot interact with the data in it. Read-only views are visually distinguishable from editable
views and the functionality for editing their data is disabled or removed.Important: The
Read-only setting only controls how the view renders. It is not meant to be a form of access
control. Since the data can be programmatically manipulated by using an API or a script, your
application must include server-side logic to protect the data on the server. For example, if an
application has a field customerID that must never be changed on the client, then the server-side
logic could compare that the customerID value that is sent from the client is the same as the
customerId value that is stored in a system-of-record database.
- When you set the visibility to Hidden, users see the view as disabled.
The generated HTML still contains the DOM node for the view. The Hidden value
is the visibility of the view on screen and not whether users can see it in the HTML source. If you
choose Hidden, the parent view reserves space in the layout as if the view is
visible. For example, you have a vertical section with three text fields. If you set the middle
field to Hidden visibility, the section displays empty space where the middle
field would be if it was visible.
- When you set the visibility to None, users cannot see the view, but the
view is listed in the Invisible Items
 pop-up window. To make the view visible again, select it in the pop-up list and click
Show invisible items. Similar to Hidden, the generated
HTML still contains the DOM node for the view. If you set the middle field to
None visibility, the section collapses the space between the upper and lower
fields. If the middle field becomes visible, the lower field moves down to make room for the middle
field.See the effects of setting a view to Same as parent,
Hidden, and None visibility in the following example:

Field 2 with editable visibility
Field 2 with hidden visibility
Field 2 with none visibility

## Setting visibility properties to respond to user screen
size

Visibility properties can also be set relative to a particular screen size. For example, you
might have two versions of a view, one more detailed and one that is pared down to the barest of
information for smaller screen environments. You can configure the visibility settings on the view
instances to hide the more detailed view instance in small screen size environments, and show a
simplified version instead.

To specify different visibility
settings for each screen size, select the view, click the screen size
icon to specify that the setting applies to a large, medium, or small
screen size, and then enter the visibility settings for that screen
size. Next, change the screen size setting to a new size, and enter
new visibility settings for that screen size setting.

For information about responsive settings for view instances see Responsive settings for views.