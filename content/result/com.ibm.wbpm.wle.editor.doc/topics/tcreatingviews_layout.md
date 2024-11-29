# Defining the contents of views

## Procedure

1. Switch to the Layout page to add views and other items to the view.
 The views that you can add to the layout are views from the UI
toolkit. For more information on the available UI views, see UI toolkit.
2. If your view has multiple areas of information, use the
toolbar slider and select Grid, then build
the appropriate grid pattern. Use the insertion points to add grid
cells or containers to specify the location of those areas. For
information on how to use the grid layout, see Laying out a coach or view using the grid layoutFor example, if your
view has an area in which the user selects something and another area
that displays information about the selection, use the grid to create
a cell for the selection area and another cell for the information
area.   Remember: Also consider whether your view will be nested inside other views and how
that impacts your layout. For example, say you create a view that has a cell that is 4 units wide
and another cell that is 8 units wide. If you place that view into a cell in a page that is 3 units
wide, the contents in that view have only 3 units of width available and uses 1 for the first cell
and 2 for the second cell.
3. To add content to your view, select Content from the toolbar
slider. On the canvas, click Add Content to display the pop-up window that
lists all the views that you can add to your layout. If you're not using grid cells, use
horizontal and vertical layouts to group related views or to arrange views, if needed. For
information about the data binding that occurs, see Data binding for views.  For an example of how you can create your own views, see
Example: creating a jQuery button view
When you add a view to the layout, it is automatically selected and its properties are shown.
Remember: Consider the effect of the various browsers when you are defining the layout
and what you must do to handle their differences. For example, the Safari browser does not have
scroll bars. Without scroll bars, it might not be obvious when, for example, table cells contain
more content than their frame can hold.
4 For each view that you add to the layout, define its properties. When you select a view on the layout, pop-up icons are displayed, enabling you to change thelabel, cut, or copy the view. When you hover over the view, insertion points are displayed on itssides. Click an insertion point to display a pop-up window that presents for selection all the viewsthat you can add beside, above or below the selected view. Note that each item that you add to the layout is a separate instance and changing itsproperties does not affect the properties of other instances. For example, you drop two instances ofa Text view. Changing the name of one does not affect the other. However, if you double-click a viewinstance in the layout, the view opens in the editor. If you then edit the view, you change itsdefinition. These changes affect all existing and future instances of that view.

<!-- image -->

    1 Define the general properties of the view instance, including setting the followingproperties: For information about these properties, see View general properties .
        - Change its label to the appropriate text.
        - Bind it to data such as a business object or one of its parameters by selecting the data from
the list. The list contains the variables that you defined in the Variables
page that have the same type as the type of the data binding that is defined for the view. If the
type of your selection and the type of view data binding do not match, a warning occurs.
        - Change the definition that the view instance uses. If you choose to select an existing view
definition, the list contains the view definitions with a data type that matches the type that is
defined for the data binding.
2. Configure the view instance by selecting or typing a value for each option, or by
assigning a variable if that choice is available. 
To set a configuration property to a variable, click . Click Select and then select the
variable from the list. The list contains the variables with a data type that matches the type that
is defined for the configuration option. Tip:  Alternatively, you can click  to create a unique configuration option that matches the data type of the
configuration property, and automatically bind to it.
Important: The designer handles strings that are directly set in a configuration property
differently from strings that are set through a variable. If you are setting the string by entering
it directly into a configuration property, do not surround the string with quotation marks. If you
are setting the string through a variable, surround the string with quotation marks and use escape
characters where necessary. For example, you have a Text view that you want to contain only five
numbers. The Text view has the Validation field. In this field, you enter, as
a string, the regular expression to use to evaluate the contents of the Text view. If you enter the
validation string, type \d{5}. If you assign the validation to a variable,
the variable is a string with a value of "\\d{5}".

 As an
alternative, you can expose certain configuration properties to the views or pages that contain your
view. For example, in your view, you add a check box as a set of radio buttons and expose its True
Label and False Label configuration properties. Pages or views that contain your view can then set
these labels to something appropriate for that page or view. Exposing the configuration property
automatically creates a configuration option as a variable in the current view. The configuration
option has data binding that matches what is defined in the selected view. To expose a configuration
property, click .
3. Set the height and width of the view instance and set how much padding you want around
it by setting its style properties.
For information, see Positioning options for view instances
4. Set how the parent page or view displays the view instance.
For information, see Setting the visibility of views. For information about the
visibility values, see View general properties.
5. Optional: To override existing styles on the instance, add HTML attributes
and classes to it. For information and an example of adding a class to change the
position of a text box label, see HTML attributes.
5. Click Save or Finish Editing.

- Adding bidirectional language support

Support is provided for languages that are written from left to right and from right to left.
- Setting the visibility of views

To allow or prevent users from seeing or editing a view, set its visibility property.