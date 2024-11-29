# Adding variables to views

## Procedure

Define the variables that the view uses to store its association with business data and
how users can configure the view under Variables.Tip:  Alternatively, you
can create a view directly from an existing business object. The business data of the new view is
bound to the business object it originated from. See Developing reusable views.

- To associate the view with data, add data such as a business object.
A view can have only one associated data object. A data association is not mandatory. The
views that this view contains can bind to the associated data object or one of its parameters if it
is a business object.Restriction: To avoid errors with binding a map to a view instance, use a list (array) of
NameValuePair instead of a business data variable with the map type. This ensures
that the variable and its properties are all typed, and can be understood by the
server.
- To provide users with ways to customize view instances, add configuration options.
Pages and views that contain your view display these options as configuration properties when
users select your view in the layout. The users can then configure the instance by using the options
that you provided.
For example, the Button view has the allowMultipleClicks configuration option.
If you put a Button instance into a view, you can see Allow multiple clicks
when you display its properties.

For service
types, you must specify a default service to identify the signature of the service.
For event types, you can define variables that identify the user-defined event handlers. For more
information, see the topic User-defined events.
- To provide translations for the text of your view, add resource bundles by adding localization
resources.
For information, see Localizing user interfaces.