# Dynamic configuration of view properties

## References to view instance data

When you
create views, it is a good practice to update the default Control
Id to reflect the purpose of the view. In the following
example, the default value for Control Id is
updated from Text1 to UserName.

<!-- image -->

- Option 1: ${Your Control Id}.method()
- Option 2: page.ui.get("Your Control Id").method();

- ${UserName}.method(), or
- page.ui.get("UserName").method();

Based on the view type, you can use different methods
to retrieve different types of data, from the bound data to the values
of different configuration options. For more information about the
methods that are available for each view, see the corresponding JavaScript
documentation.

## Dynamic text changes using ${ControlId}.method();

<!-- image -->

<!-- image -->

## Dynamic text changes using page.ui.get("ControlId").method();

For
debugging purposes, you can use this option if you need to change
data in the JavaScript logic in the console. The following example
uses JavaScript logic to change the text when the page loads.

To
retrieve information from the Text view by using page.ui.get("UserName"),
you can set the expression to a changeUserName variable.

<!-- image -->

To
call the function described earlier whenever the page loads, place
the text-changing logic in the On load event,
as follows:

<!-- image -->

## Self references

When a view must refer
to itself, use the me syntax. For example, me.setText("Hello
World");${ControlId}.method() is primarily used for communication
between views. Use the me syntax when you make
self-contained changes within one view.

<!-- image -->

This is the result when the page runs:

<!-- image -->