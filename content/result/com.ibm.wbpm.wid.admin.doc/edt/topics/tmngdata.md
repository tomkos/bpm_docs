<!-- image -->

# Managing extended data elements in event definitions

In event definitions, extended data elements are used to
express business information and you can specify array or non-array
primitive types as values. You can use the event definition editor
to customize any existing extended data elements or you can add and
customize new extended data elements.

## About this task

- Adding extended data elements to event definitions

Extended data elements are used to express business information and you can specify array or non-array primitive types as values. An event definition can contain any number of extended data elements or no extended data elements at all. By default, an event definition inherits any extended data elements of its parent event definition. However, using the event definition editor, you can add one or more new extended data elements to an event definition that are independent of the extended data elements of the parent.
- Adding child extended data elements in event definitions

In event definitions, you can add extended data elements as nested children under existing extended data elements. This enables you to use extended data elements to convey business data that is stored in a hierarchal structure, such as typically found in a business object.
- Renaming extended data elements in event definitions

In the event definition editor, you can rename any of the extended data elements in an event definition. If you rename an extended data element and it has the same name and data type as an extended data element in the parent event definition (or in any higher-level parent in the same inheritance hierarchy), then the renamed extended data element will override the extended data element of the parent.
- Specifying data types of extended data elements

In the event definition editor, you can specify the data type of extended data elements in an event definition.
- Overriding extended data elements of parent event definitions

A child event definition automatically inherits the extended data elements of its parent event definition. However, in the event definition editor, you can choose to have your child event definition override one or more extended data elements of its immediate parent or any higher-level parents in the same inheritance hierarchy.
- Changing extended data element values in event definitions

In the event definition editor, the Properties view displays values associated with extended data elements. You can use the Properties view to set or change the values.
- Moving extended data elements up or down in event definitions

In the event definition editor, you can move extended data elements up or down in your event definitions without needing to directly modify the underlying source code.
- Moving extended data elements inside or outside of other extended data elements

In the event definition editor, you can move extended data elements inside or outside of other extended data elements without needing to directly modify the underlying source code. When you move an extended data element inside of another extended data element, the extended data element that you are moving becomes a child of the extended data element that you are moving it into. When you move an extended data element outside of another extended data element, the extended data element that you are moving becomes a peer of the extended data element that you are moving it out of.
- Deleting extended data elements in event definitions

In the event definition editor, you can delete one or more extended data elements in an event definition.