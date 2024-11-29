# The validate event handler

## Usage

The validate function contains the logic to display indicators or some other
notifier that there is a problem with the data. The framework starts with the
validate function in parent views before it calls the validate
function in their children views.

The validate event
handler is for when you want to provide custom error visualizations
and behavior. See the stock controls for examples of presentation
logic. For example, the Text stock control changes color and displays
an error icon when it contains non-valid data. The error icon has
hover help that displays the message that is associated with the error
condition.

## The event object

An error event can have two lists of error objects. One list
is named errors and the other is named errors\_subscription. Views
that are bound to a business object automatically receive errors for themselves. They also
automatically receive errors for all descendant views that are bound to the same business
object.

| Property       | Type         | Description                                                                                                                                           |
|----------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| binding        | String       | Contains the path to the data binding relative to the data binding of the current view.                                                               |
| message        | String       | Contains the localized message that describes the error.                                                                                              |
| view\_dom\_ids[] | String[List] | Contains the list of DOM IDs of the views that receive the same error message. The list can include the current view and any of its descendant views. |

| Property    | Type         | Description                                              |
|-------------|--------------|----------------------------------------------------------|
| messages    | String[List] | Contains a list of localized error messages              |
| view\_dom\_id | String       | Contains the DOM ID of the view with the non-valid data. |

```
type: "error",
errors: 
	[
		{
			binding: "birthday.year"
			message: "The year you entered, 2013, is after current year of 2012.",
			view\_dom\_ids: ["domId\_ProfileView", "domId\_yearView"]
		}
	]
errors\_subcription: 
	[
		{
			view\_dom\_id: "domId\_accountView",
			messages: ["Enter your account number."]
		}
	]
```

A
clear event object contains no properties. A view uses the clear
object to remove the error indicators for views that now have valid data.