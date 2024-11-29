<!-- image -->

# Editing event definitions

In the event definition editor, you can edit an event definition
and customize its properties and extended data elements.

## About this task

- Renaming or refactoring event definition names

You can rename or refactor an event definition name in the event definition editor. If you rename an event definition, the event definition name is changed but the new name is not refactored in any other event definitions that reference your event definition. By comparison, if you refactor an event definition, the name is changed and the new name is refactored in any other event definitions that reference your event definition.
- Specifying parents for child event definitions in the event definition editor

All event definitions inherit directly or indirectly from a root event definition named WBI.MonitoringEvent. When you create a new event definition in the event definition editor, it is automatically defined as a child of the root event definition. However, if you do not want the root event definition to be the parent of your new event definition, you can specify a different event definition as the parent.
- Opening parents from within child event definitions in the event definition editor

If you are editing an event definition, you can easily open the parent of the event definition from within the event definition editor. However, you cannot open the parent event definition if it is the WBI.MonitoringEvent root event definition.
- Managing properties in event definitions

In event definitions, properties are used to store system information and correlation data as string values. You can use the event definition editor to customize any existing properties or you can add and customize new properties.
- Managing extended data elements in event definitions

In event definitions, extended data elements are used to express business information and you can specify array or non-array primitive types as values. You can use the event definition editor to customize any existing extended data elements or you can add and customize new extended data elements.