<!-- image -->

# Business Process Choreographer Explorer components

The components consist of a set of JSF components and a set of
client model objects. The relationship of the components to Business
Process Choreographer, Business Process Choreographer Explorer, and
other custom clients is shown in the following figure.

<!-- image -->

## JSF components

- List componentThe List component
displays a list of application objects in a table, for example, tasks,
activities, process instances, process templates, work items, or escalations.
This component has an associated list handler.
- Details componentThe Details component
displays the properties of tasks, work items, activities, process
instances, and process templates. This component has an associated
details handler.
- CommandBar componentThe CommandBar component
displays a bar with buttons. These buttons represent commands that
operate on either the object in a details view or the selected objects
in a list. These objects are provided by a list handler or a details
handler.
- Message componentThe Message component
displays a message that can contain either a Service Data Object (SDO)
or a simple type.

## Client model objects

The client model objects
are used with the JSF components. The objects implement some of the
interfaces of the underlying Business Process Choreographer API and
wrap the original object. The client model objects provide national
language support for labels and converters for some properties.