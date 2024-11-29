# User-defined events

Views communicate with other views by using data bindings. However, you can also use events to
interact with other views. To illustrate the concepts in this topic, three related views named
Revenue, Expenses, and Profit have been added to a client-side human service. These views all use
events to interact with each other and they are all of the Decimal view type. The remainder of this
topic describes some of the key features in the event framework for views.

A Control ID is an identifier that you can specify in JavaScript code to refer to a
view. Control IDs can be referenced by other views to enable them to interact with each other using
events. For example, in the General properties, you can specify a control ID for a view in the
Control ID field.

All the user-defined event handlers for a view are displayed in the Events properties. Each event
handler has an expandable JavaScript editor for adding the business logic and has content assist
that you can invoke by pressing Ctrl-Space. The On Load and On change event
handlers are shown in the following image:

To define user-defined events, use the Event built-in type that has been added to
supplement the Object and Service build-in types. Under Variable Declarations, add one or more
configuration options. Under Data, change one or more configuration options to events by selecting
the Event radio button and specifying a name and label. In the following
figure, the eventON\_LOAD user-defined event is selected under Variable
Declarations and the corresponding name, label, and documentation for this user-defined event are
shown under Data:

The eventON\_LOAD user-defined event is a special
event handler. If you define an event configuration option with the
name eventON\_LOAD, it will be automatically run
in the load event handler.

To register a user-defined event after it has been defined, select an event handler
in the Behavior properties and then use the JavaScript editor under Code to optionally add
registration logic. If you have additional variables that you would like to pass to the event
handler, you can call the function registerEventHandlingFunction. However, if
you do not call explicitly call the registration function, the event handler will be registered with
no additional variables.

To designate when a user-defined event should fire, select an event handler in the
Behavior properties and then use the JavaScript editor under Code to add the required logic. In the
logic, you need to call the function executeEventHandlingFunction to execute
the event logic. In the following figure, the valueChange event is executed in
the change event handler. The content assist was invoked on the
this. statement by selecting Ctrl-Space to find and
select the function executeEventHandlingFunction:

The user-defined event handlers for the view are displayed in the Events properties.
Each event handler has an expandable JavaScript editor for adding the business logic and has content
assist that you can invoke by pressing Ctrl-Space. Using the JavaScript
editor, you can input custom code into an event handler. This enables your view to interact with
other views and perform tasks like setting values and checking validations. In the following figure,
the content assist is invoked in the JavaScript editor for the On change user-defined event handler
and the ${VIEW\_ID} variable is about to be
selected:

If you add the ${VIEW\_ID} variable to the JavaScript editor of a
user-defined event handler, you need to replace the token VIEW\_ID with the control ID of another
view, which provides your user-defined event handler with complete access to that view. For example,
you could replace the ${VIEW\_ID} variable with
${Revenue} (which is the control ID for the Revenue view). You could then
call a function like ${Revenue}.getData() to obtain the current bound
value for the Revenue view.

page.ui.get(VIEW\_ID)