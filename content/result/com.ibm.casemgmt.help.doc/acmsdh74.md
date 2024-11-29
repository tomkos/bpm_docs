# Designing views for to-do tasks

## About this task

Defining a view for a to-do task is optional. You can use the default view instead. The
    default view provides a list of all task properties that are associated with the to-do task.

In some cases, you might want to customize the view for a to-do task. For example, you might
    want to display only a subset of the associated task properties, change the order in which the
    properties are displayed, or include case properties. You can also customize the layout of the
    view.

As you design a view, consider the space that is available in the user interface. If the
    widget is too wide or too high, you might see scroll bars that make editing the properties
    awkward for the user. Use the different layout containers such as the tabbed layout container or
    the titled layout container to organize the content of the view efficiently.

## Procedure

To customize the view for a to-do task:

1. On the Activites page for the case type, click the Open To-do
View Designer icon for the to-do task.
2. Drag one or more containers onto the canvas.
Each container provides a different layout for the properties that it contains. For the
     layout containers, you can add other containers and properties to a container. 
Tip: To make working with the containers easier, the design view displays extra space around the
      containers. Click the Hide Extra Padding icon see an approximation of
      how the view will look in Case Client.
3. Select a container and configure the settings for that container.
The tabbed layout container and the multiple column container consist of a set of layout
     containers that are arranged in either tabbed pages or columns. You can configure settings for
     the entire container and for the individual layout containers.
4 Drag the properties into the appropriate containers. The Properties palette includes all the properties that you added to the task and the case type.Tips:
    - Multiple selections are supported by using the Shift and Ctrl keys.
    - Properties are added to the new container in the order in which they were selected.
    - Properties can be dragged between the containers in the view.
    - Properties cannot be dragged into the child containers of a view.
    - After you start a drag operation, press the Ctrl key to copy the objects instead of
        moving the objects. Press the ESC key to cancel a drag operation.
    - The graphic changes to indicate whether an object or group of objects can be dropped into
        the container.
5. Select a property and configure the settings for that property.

When you add a property to a container, it initially uses the default control for editing
      the property. For example, a Boolean property is displayed as a check box by default. You can
      change the type of control that is used for a property. For example, you might change the
      control so that a Boolean property displays as radio buttons or a drop-down list. You can also
      select Static text to display the property value in read-only mode and
      configure the appearance and behavior of some controls.
Important:  You can set a default value for each property in the view. However,
      this value is applied only if the default value in the property is null and is not specified
      by another mechanism such as a JavaScript call or an external data service.
6. Save the view and close the designer.

## What to do next

To display the to-do task view in your solution, add a To-do List widget to a page. Then, edit
    the To-Do List widget settings to select the to-do tasks to display.