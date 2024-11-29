# Defining properties views

## About this task

Defining a view for the Properties widget is optional.
You can use a system-generated view instead. The system-generated
view provides an ordered list of all properties that are associated
with the case type.

As you design a view, consider the space
that is available in the user interface. If the Properties widget
is too wide or too high, you might see scroll bars that make editing
the properties awkward for the user. Use the different layout containers
such as the tabbed layout container or the titled layout container
to organize the content of the view efficiently.

## Procedure

To define a view for the Properties widget:

1. On the Views page for the case type, click Add
Layout on the Case Layouts tab.
2. Select the Properties View menu
item.
3. Enter a name and a unique identifier for the layout.
4. To make this view the default layout for the case type, select the Use as default
property view check box.
This view is then used for the Properties widget on all pages for this case type unless you
select a different layout for the widget on a specific page. If you do not select this check box, a
system-generated view is used as the default. Tip: To reduce the amount of
configuration, select the view that is used most frequently as the default view.
5. Click OK.
6. Click the Open Properties View Designer icon for the
view.
7. Drag one or more containers onto the canvas. Configure
the settings for the containers as needed.
Each container provides a different layout for the properties that it contains. For the layout
containers, you can add other containers and properties to a container. Note: In the solution designer, not everything in the canvas works in run time as it does
during design time. Use the canvas only as a tool for designing your layout, not to test runtime
behavior. 
While you drag a container, press the Ctrl key to copy the container instead of moving it. Press
the ESC key to cancel a drag operation.
Tip: To make working with the containers
easier, the design view displays extra space around the containers. Click the Show Extra
Padding icon to see an approximation of how the view will look in Case Client.
8. Select the category of properties to display
from the drop-down list in the       Properties palette.
Drag the properties into the appropriate      containers.
Use the Shift and Ctrl keys to select multiple properties. While you drag a property, press
the Ctrl key to copy the property instead of moving it. Press the ESC key to cancel a drag
operation. You can also drag properties from one container to another on the palette. 
The
categories of properties include case properties, runtime properties, and, if defined for the
solution, task properties. The runtime properties include workflow fields and external
properties.
To add workflow data fields or workgroups to the view, click Run time only > Workflow Field. Alternatively for some containers, you can select Data fields
or Workgroups from the Automatically include list to
include all the workflow data fields or workgroups that are exposed in a step to the container.
9. With the property selected, configure the settings for
that property.

You must configure a workflow field, workgroup, or external property so that
Case Client can discover the data field or workgroup at run
time.
When you add a property to a container, it initially uses the default control for editing the
property. For example, a Boolean property is displayed as a check box by default. You can change the
type of control that is used for a property. For example, you might change the control so that a
Boolean property displays as radio buttons or a drop-down list. You can also select
Static text to display the property value in read-only mode and configure the
appearance and behavior of some controls.
Important:  You can set a default value for the property in the view.
However, this value is applied only on the Add Case page, and only if the property value is null and
is not specified by another mechanism such as a JavaScript call or an external data service.
10. Save the view and close the designer.

- Containers

You use the containers in Properties View Designer to organize the content of the view. The three layout containers provide for the general layout of the view and can contain both properties and other containers. The two property containers provide specific layouts for properties.
- Adding workflow data fields and workgroups to the properties view

You can associate data fields and workgroups with the workflows that you     define for tasks by using either Case Builder or IBM® FileNet® Process Designer. You can add these data fields and workgroups to a     properties view in the same way that you add case properties.
- Adding external properties to the properties view

You can add properties to a properties view that are managed externally from your solution. For example, external properties can be from another object model or provided by an external data service.
- Property editor settings

When you add a property to a view in Properties View Designer, you can select the         type of editor that Case Client users use to enter or         select property values. For example, you might specify that an integer property is edited by         using either a number text box or a number spinner. You can also specify that the property         value is displayed as static text, which prevents users from editing the value.
- Properties

You can configure various property settings in Properties View Designer, such as the width of the property editors.