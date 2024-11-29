<!-- image -->

# Event definition editor

In IBM® Integration
Designer,
the event definition editor is the designated tool for creating and
editing custom event definitions. The event definition editor features
a simple user interface that enables you to easily add and manage
event definitions.

You open the event definition editor from within the Business Integration perspective. The event
definition editor is shown in the following figure:

- 1 Event Definition area
- 2 Properties view

All of the tasks that you can perform in the event definition
editor are either initiated or performed in the Event Definition area
or the Properties view, which are described in the following sections.

## Event Definition area

The Event Definition
area contains all of the controls for working with your event definitions
and it enables you to perform numerous actions, such as selecting
a parent event definition and adding, editing, and removing properties
and extended data elements in your event definitions. The Event Definition
area is shown in the following figure:

- 1 Event definition name
- 2 Event definition parent
- 3 Properties and controls
- 4 Extended data elements and controls

## Properties view

The Properties view enables
you to set or change values for properties and extended data elements
that you have selected in the Event Definition area, as described
in the following two subsections:

- The Properties view and properties
- The Properties view and extended data elements

If you select a property in the Event
Definition area, the Properties view displays a General page and a
Details page.

The General page provides a
read-only display of the name of the property and the XPath location path of the property. In the
following figure, the name of the property is MyProperty1 and the XPath shows that
MyProperty1 derives from the contextDataElements parent property:

The
Details page enables you to specify values for the selected property, such as
whether the property is required, the default value, and the minimum and maximum values or
permitted values.

If
you select an extended data element in the Event Definition area,
the Properties view displays a Details page
that enables you to edit values for the extended data element. The
Details page differs depending on whether you are editing values for
a non-array data type, or an array data type, or a noValue data type.

If
you select an extended data element with a non-array data type, the
Details page enable you to specify a default value for the extended
data element.

By comparison, if you select an
extended data element with an array data type, the Details page will
also enable you to add or remove array elements.

Finally,
if you select an extended data element with a noValue data type, the
Details page will only enable to you specify the minimum and maximum
number of occurrences.

- Icons and symbols

In the event definition editor, icons are images that are used to invoke actions. Symbols, by comparison, are images that simply represent workbench elements and they are not used to invoke actions.
- Keyboard shortcuts for the event definition editor

In the event definition editor, you can perform many of the available actions by using keyboard shortcuts.