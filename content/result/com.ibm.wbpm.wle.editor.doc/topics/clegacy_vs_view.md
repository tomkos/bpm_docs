# Difference between coaches and heritage coaches (deprecated)

The primary difference between coaches and the heritage coaches of previous versions is that
coaches consist of one or more views. Heritage coaches are deprecated. Views are reusable
collections of user interfaces that are frequently bound to a data type. This reusability means that
you can share common pieces of user interface between coaches. For example, you can create a coach
that has a view that contains a set of address fields. That is, the view is bound to an Address
business object and the individual fields are bound to parameters of that business object. If you
create a second coach that needs address fields, you can reuse the view. Conversely, with heritage
coaches you must re-create the address fields. You can now implement your own custom controls as
views and then reuse these custom controls in other views and coaches.

- Coaches introduce a client-side model to coaches to apply the Web 2.0 appearance and behavior.
The coach has data on the client, which is available to all the views. That is, fields in different
views that are bound to the same data object update without requiring a full-page refresh.
- Instead of the one-button mechanism of heritage coaches, views use named boundary events.
Programmers use boundary events for actions such as data updates with the server and flows to other
coaches or services. For example, a coach can have multiple buttons. In the human service diagram,
you can wire each button to a different event. Any view can declare and fire a boundary event. You
are not limited to using only buttons to do so although only the button view can fire a boundary
event. Furthermore, the programming for views consists entirely of client-side JavaScript. There is no need for server-side JavaScript.
- (Deprecated) Coaches support collaboration while heritage coaches do not. More than one person
can work on the same coach instance at the same time in their own browsers. For example, with
collaboration, users can call on colleagues to help them complete a coach instance. These users see
which controls their colleagues are editing and the values that they are setting in those controls.
Collaboration is available only if the service flow uses coaches for its user interface. If the
service flow contains one or more heritage coaches, collaboration is not available.
- The control ID of a coach is different from the control ID of a heritage coach. The control ID
of a heritage coach is the div node ID. This is not the case in coaches because
views are reusable and you can have multiple views in a coach. In coaches, the control ID is the
value of the data-viewid  attribute of a <div></div> tag. By
using the data-viewid attribute, developers can locate the nested view because
data-viewid is unique within its parent or enclosing view.

In Business Automation Workflow, services use coaches for the
user interface. A human service can use coaches only; heritage coaches are not supported by the
web-based human services. A heritage human service can mix coaches and heritage coaches so that one
type can flow into the other. However, a coach cannot contain heritage coach elements, and heritage
coaches cannot contain views. That is, a user interface for a heritage human service must be a coach
or a heritage coach, but not a mix of the two.

- The available tools include views that you can drop into the coach. Although some views and
other items have the same name in heritage coaches, these items are implemented differently.
- Tags are used to categorize the views that are available. You can use the filter to show or hide
the categories of views.
- The properties for views have different options from the properties for heritage coach views and
sections. However, many of the properties in heritage coach views have a corresponding property in
views. For example, the page that is named after the heritage coach view has properties such as
Label, Binding, and Control Id. In views, you can find corresponding general properties. Many of the
heritage coach presentation properties have a corresponding coach configuration option. Even when
heritage coach views and views have properties that have the same name, the implementation of those
properties can be different.