# Binding data and configuration options

## context.binding

The binding object, if defined, provides access to data
that is bound to a view. There is at most one data binding declared for each view.

You can
access data that is bound to a view by using the construct:
this.context.binding.get("value"), where value is a special
property name that returns the data binding. For example, if a view is bound to local.phoneBook.title, then the view can get the phone book's
title as follows:

```
if (!! this.context.binding){
var title = this.context.binding.get("value")
}
```

## Binding to simple and complex data types

For simple data types such as strings and numbers, the view framework detects data changes and
automatically notifies the view of the change. For example, when a view is bound to the simple
string type local.phoneBook.title, the view's change() function is
called with a change event that specifies that the title changed and its new value. All the views
that are bound to local.phoneBook.title are notified.

For the callback signature, see the function(event) topic.

```
var binding = this.context.binding.get("value");  //this is a complex object
   this.property2Handle = binding.bind("property1.property2", function(e) {some code}, this);
   this.property3Handle = binding.get("property3").bindAll(this.myBindAllChangeHandler, this);
   ......
   this.mybindAllChangeHandler(event) { .....};
```

## Binding to a list type

When you bind to a list, the view is automatically notified when the entire List object changes.
For example, consider that the view is bound to the list local.phoneBook.person[].
If a new person list is created and set to the view's binding, for example using the server script
syntax tw.local.phoneBook.person = new tw.object.listOf.person(); the framework
automatically notifies the view of the change.

## Binding to list updates

```
var binding = this.context.binding.get("value"); //this is a List object
this.bindAllHandle = binding.bindAll(this.listUpdated, this);
```

## Binding to list properties

| Property               | Type    | Description                                                                                                                                                                                                                                     |
|------------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| listAllSelectedIndices | Array   | The indexes of the list elements that are selected by a user. There can be more than one selected index. When you set listAllSelectedIndices, you pass in the indexes in an array. Use listAllSelectedIndices when updating the list selection. |
| listAllSelected        | Array   | An array of all the elements that a user has selected. Use listAllSelected to subscribe to a change to this property. This property is read-only.                                                                                               |
| listSelectedIndex      | Integer | The index of the selected element. This value corresponds to the value of the index 0 element of the listAllSelectedIndices array. Use listSelectedIndex to subscribe to a change to this property. This property is read-only.                 |
| listSelected           | Object  | The selected element. This value corresponds to the value of the index 0 element of the listAllSelected array. Use listSelected to subscribe to a change to this property. This property is read-only.                                          |

```
var binding = this.context.binding.get("value"); //this is a list
this.selectedIndicesHandle = binding.bind("listAllSelectedIndices", this.indicesChanged, this);
```

## Accessing list elements

- Use get("value") to get the list object. For example: list =
this.context.binding.get("value")
- Use get(index) to obtain the indexed element. For example:
list.get(0) to obtain the first element.
- Use get(property)  to obtain the value of the property. For example:
list.get("listSelected") to obtain the value of the listSelected
property. Use similar syntax to obtain the values of all other properties.
- Use items to get an array that represents the underlying elements of the list.
For example, list.items. The data returned by items should not be
modified.

## List operations

- To add an object, use list.add(item). For example,
this.context.binding.get("value").add(item)
- To remove an object, use list.remove(index), For example,
this.context.binding.get("value").remove(0)
- To replace an object, use list.put(index, item). For example,
this.context.binding.get("value").put(0, item)
- To get the length of a list, use list.length().
- To get an indexed element or property of the list, use list.get(index |
property). See Accessing list elements earlier.
- To programmatically update the selected property in the list, use
list.set(property). For example,
this.context.binding.get("value").set("listAllSelectedIndices", [1, 2,
3]);

## Cleaning up bound resources

```
if (event.type != "config"){
var binding = this.context.binding.get("value"); //this is a list
	// assumes that this.selectedIndicesHandle was initialized in the load function
  this.selectedIndicesHandle.unbind();
this.selectedIndicesHandle = binding.bind("listAllSelectedIndices", this.indicesChanged, this);
	// assumes that this.selectedIndicesHandle was initialized in the load function
this.bindAllHandle.unbind();
this.bindAllHandle = binding.bindAll(this.listUpdated, this);

}
```

## Configuration options

| Option          | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| label           | String | The label value of the view, if one exists                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| visibility      | String | The visibility settings for the view. Valid values are: "DEFAULT" | "EDITABLE" | "REQUIRED" | "READONLY" | "NONE" | "HIDDEN". See The coach view context object.See . DEFAULT is the code equivalent to Same as parent that users see on screen in a Visibility list.Important: Tables have a Disable click-to-edit configuration property. The default value is false, which means that views contained within that table use the visibility settings of the table. That is, the views in a given cell are READONLY until the user clicks in the cell. The views are then EDITABLE until the user clicks anywhere outside of the cell. The views revert to being READONLY. When Disable click-to-edit is true, these views use their own visibility settings. Important: Setting the visibility to REQUIRED does not validate whether a user has entered or set a value. You must provide code that does this checking by, for example, implementing a validation service for the coach that contains the view. |
| labelVisibility | String | The visibility settings for the label. Valid values are "SHOW" | "HIDE".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| helpText        | String | The view can use this property as hover text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| className       | String | The CSS class name(s) specified. Normally a view does not need to use this as the CSS class names are inserted into the view's DOM attribute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| htmlOverrides   | Map    | A name-value pair map that represents the HTML attribute specified. These name-value pairs are inserted into the view's DOM attribute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

- To get a view's predefined options, use this.context.options.\_metadata.*. For
example, to get a view's visibility option, use
this.context.options.\_metadata.visibility.get("value");
- To set a view's predefined options, use this.context.options.\_metadata.*. For
example, to set a view's visibility option, use
this.context.options.\_metadata.visibility.set("value", newValue);
- To get a user defined configuration option, use
this.context.options.myOption.get("value");, where myOption is the
option name.
- To set a user defined configuration option, use
this.context.options.myOption.set("value", newValue);, where
myOption is the option name.

To serialize the data binding object to a
JSON string, you can call the toJson() function on the data binding object. To get
a basic JavaScript object that represents the data binding, you can call
toJSObject().