# Data binding for views

To associate a business object and a view, you bind the view to the business object. When the
view definition declares a binding type, you must bind the view to data. Without the data that is
provided by the binding, the view might not function properly. When the view definition does not
declare a binding type, the data binding is optional.

When a business object is associated with a view, you can drop the parameters of the business
object onto the layout. These parameters are available as variables on the palette. If there is a
view that is associated with that data type of the variable, the layout displays that view. For
example, if you drop a string onto the layout, you can see a Text view that is bound to the string.
If the variable is a business object that has an associated view, you can see that view. If the
business object does not have an associated view, you can see a placeholder message.

- If the variable is a primitive data type, such as a string or one parameter business object, the
designer adds a Select view.
- If the variable is a business object with more than one parameter, the designer adds a Table
view with a column for each parameter. Each column contains the view that is associated with the
data type of the variable.
- If you drop a currentItem variable onto the layout, the designer adds a
vertical section that contains the view that is associated with data type of variable. At run time,
the content of the section repeats for each item in the list.
- If you drop a listSelected variable onto the layout, the designer adds the view
that is associated with the data type of the variable. At run time, the view contains the data for
the selected item in the list. For example, you have a Select view that is bound to
listBO[] and an Output Text view that is bound to
listBO.listSelected.myItem. At run time, the user selects the third item in the
Select view. The Output Text view displays the third myItem string.

When you have a view definition that contains a Content Box item and an instance of that view is
bound to a list, the contents in the content box repeats for each list item. The content box can
contain views that are also bound to lists or elements of lists. When you have this arrangement, the
list of the container (outer) view controls the repetition. The list of the contained (inner) view
provides the contents. For example, you have a section that is bound to a list of names. The content
box for the section contains a Text view that is bound to the currentItem of the
list of names. At run time, the section repeats for each name in the list. Each repeating section
contains a field. In the first section, the field contains the first name. The field in the second
section contains the second name, and so on.

You can bind the outer view and the inner views to different lists. However, if you bind an inner
view to the currentItem of a different list, the two lists must contain the same
number of items. If the two lists do not have the same number of items, users see a message. The
specific message depends on whether the inner list contains more or fewer items. If the outer list
has more items, the users see some highlighted views in the repeated content. They are highlighted
because they do not have data. For example, outerList[] has three items and
innerList[] has two items. The views that are bound to
innerList.currentItem repeat three times, but only the first two have data. If the
outer list has fewer items during run time, the user cannot see these excess items because
the inner list has nowhere to display them. For example, outerList[] has four items
and innerList[] has five items. The views that are bound to
innerList.currentitem repeat four times. The user cannot see the views for the
fifth innerList[] item.