<!-- image -->

# Managing properties in event definitions

In event definitions, properties are used to store system
information and correlation data as string values. You can use the
event definition editor to customize any existing properties or you
can add and customize new properties.

## About this task

- Adding properties to event definitions

Properties are used to store system information and correlation data as string values. An event definition can contain any number of properties or no properties at all. By default, an event definition inherits any properties of its parent event definition. However, using the event definition editor, you can add one or more new properties to an event definition that are independent of the properties of the parent.
- Renaming properties in event definitions

In the event definition editor, you can rename any of the properties in an event definition. If you rename a property and it has the same name and path as a property in the parent event definition or in any higher-level parent in the same inheritance hierarchy, then the renamed property will override the property of the parent.
- Overriding properties of parent event definitions

A child event definition automatically inherits any properties of its parent event definition. However, in the event definition editor, you can choose to have your child event definition override one or more properties of its immediate parent or any higher-level parents in the same inheritance hierarchy.
- Changing property values in event definitions

In the event definition editor, all values associated with event definition properties are displayed in the Properties view. You can use the Properties view to set or change the values of properties.
- Moving properties up or down in event definitions

In the event definition editor, you can move properties up or down in your event definitions without needing to directly modify the underlying source code.
- Deleting properties in event definitions

In the event definition editor, you can delete one or more properties from an event definition.