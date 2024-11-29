<!-- image -->

# Value and data pool editors

- The value editor and operations
- The value editor and event definitions
- The data pool editor
- Unicode escape sequences
- Business graphs
- Pop-up menu items
- Date and time values
- Maximum depth of expanded business objects
- Importing values from XML

## The value editor and operations

When you
invoke an operation in the integration test client, the test pauses
whenever it encounters an interactive event such as a manual Invoke
event or a manual Emulate event. During the pause, you can use the
value editor to specify input values for an operation or output values
for a manual emulator. For those events that are not interactive,
the value editor simply displays the values that were passed or returned
for the events. The value editor is shown in the following figure:

- 1 Parameters
- 2 Fields
- 3 Arrays
- 4 Elements
- 5 Fields

The Name column presents a hierarchical
view of the data. Fields of a complex element are nested below the
complex element. Similarly, elements of arrays are nested below the
arrays, and fields are nested below the elements. To add an element
to an array, right click the array and select Add Elements.

The Type column
shows the data type of each object.

The Value column
accepts and displays the values specified for each object.

If
you specify an invalid value in the Value column,
the row is flagged with the validation error symbol . Validation errors do not indicate that you have
errors in your workspace and they do not prevent you from continuing
your testing. You can hover your cursor over the validation error
symbol to obtain information about the validation error. Similarly,
if you select the row that contains the validation error, the status
area at the bottom of the value editor provides additional information
about the error.

Note that at the top of the value editor, you
can use the Go to Previous Error icon  and the Go to Next Error icon  to move to the previous error or the next error.

When
the value editor first opens for an event, the following values are
automatically assigned:

- Read-only fields are flagged with the read-only symbol .
- All other fields are populated with default values.

If you are working with large business objects that have many
fields and values, you can use the following features to work more
effectively with the objects in the value editor:

- A Maximize Editor icon  to maximize the size of the value editor.
- Keyboard navigation to navigate the value editor using common
keys such as Tab, Page Up/Down and
the arrow keys.
- Multiple field editing mechanisms.

Field editing mechanisms are discussed more fully in the topic
"Specifying operation values."

## The value editor and event definitions

In
the test client, you can use the value editor to specify values for
an event definition. The value editor is shown in the following figure:

- 1 Event definition
- 2 Property container
- 3 Properties
- 4 Extended data container
- 5 Extended data elements
- 6 Array elements

The Name column presents a hierarchical
view of the data. If an extended data element is an array, the elements
of the array are nested below the extended data element. To add an
element to an array, right click the array and select Add
element.

The Type column
shows the data types of the properties and extended data elements.
Properties are always a String data type. Extended data elements can
be any non-array or array primitive data type.

The Value column
accepts and displays the values specified for the properties and extended
data elements.

If you specify an invalid value in the Value column,
the row is flagged with the validation error symbol . Validation errors do not indicate that you have
errors in your workspace and they do not prevent you from continuing
your testing. You can hover your cursor over the validation error
symbol to obtain information about the validation error. Similarly,
if you select the row that contains the validation error, the status
area at the bottom of the value editor provides additional information
about the error.

Note that at the top of the value editor, you
can use the Go to Previous Error icon  and the Go to Next Error icon  to move to the previous error or the next error.

When
the value editor first opens for an Emit event, the following values
are automatically assigned:

- If any extended data element is an array and it does not yet have
any array elements, it is automatically defined as read-only and it
is flagged with the read-only symbol
- If other properties and non-array extended data elements do not
yet have values, they are automatically assigned the default values
that are associated with their data types.

## The data pool editor

In the value editor,
you can save values to a data pool, view and edit the values using
the data pool editor, and later reuse the values in the value editor.
Since the value editor and the data pool editor are both used to manage
the same kind of data, the two editors are similar in many respects.

You
can use the data pool editor to modify or reorder values in a data
pool that resides in the workspace. You can copy values or entire
rows between data pools.

## Unicode escape sequences

In both the value
editor and the data pool editor, you can type values directly into
the Value column for any attribute with a primitive data type, such
as a string or integer. These values can be either Unicode or Unicode
escape sequences.

By specifying Unicode escape sequences in
the value editor or the data pool editor, you can pass extended ASCII
characters or control characters as values. For example, if you want
to use a null character in a CICS® program, you could type \u0000.
If you type Unicode escape sequences in the data pool editor or value
editor, they are displayed as the Unicode characters that they represent.
However, when you begin to edit them, they are displayed as Unicode
escape sequences. For example, if the Unicode escape sequence \u004a
is specified as part of a Unicode value, the character J would be
displayed, but when you begin to edit the value in the Value column,
the Unicode escape sequence \uoo4 would be displayed rather than the
character J.

You can specify Unicode escape sequences to represent
character strings in whole or in part. For example, you could type AB\u0043 to
specify the string ABC. You can also use the
backslash (\) escape character to prevent Unicode escape sequences
from being interpreted. For example, if you type \\u0043,
it is interpreted as \u0043 rather than as the letter C.

In
standard Unicode, escape sequences are specified using hex characters
and only valid values are interpreted. For example, the hex characters
\u004a are interpreted because they are valid and represent the letter J.
However, the hex characters \u004k are not interpreted because they
are not valid and they do not represent a valid character.

## Business graphs

If the operation
that you are testing has a business graph as its parameter, you can
view, specify, and test values for both the verb property and
the changeSummary property in the value editor of the test
client.

In the value editor, you can select a Show
Change Summary menu item to append a Change
Summary column to both the value editor and data pool
editor. The Change Summary column accepts values
that represent the original state of the business objects in the business
graph. The Value column, by comparison, accepts
values that represent the current state of the business objects in
the business graph. You can modify business object and attribute values
in both the Change Summary column and the Value column.

If
the Show Change Summary menu item is selected,
the test client passes the business graph to the target adapter or
component during the test and the business graph contains changeSummary
information.

If the Show Change Summary menu
item is selected and the Enable Logging menu
item is also selected, the test client passes the business graph to
the target adapter or component during the test and the business graph
contains changeSummary information. However, the changeSummary information
also includes a record of business object changes that have occurred
since the operation was last invoked. You can use this logging capability
to restore a business object to its original state.

If the Show
Change Summary menu item is not selected, the test
client still passes the business graph to the target adapter or component
during the test. However, the business graph does not contain any
changeSummary information at all.

In the Preferences window
of IBM® Integration
Designer,
you can set a preference to determine whether verb and changeSummary
properties are displayed in the value editor. This is described in
the test client topic "Selecting business graph properties to display."
However, you can use the Show Change Summary menu
item in the value editor to override any preference that you set in
the Preferences window for the changeSummary property.

## Pop-up menu items

In the value editor and
data pool editor, you can choose from numerous pop-up menu items to
help you manage the values that you pass to operations, manual emulations,
and event definitions. Although many of the same context menu items
are found in both of the editors, some of the pop-up menu items are
specific to one editor or the other.

Additionally, the pop-up
menu items that are available differ depending on whether you are
specifying values for operations, manual emulations, or event definitions.

The
pop-up menu items available for working with operations and manual
emulations are described in the following table:

| Pop-up menu item        | Editor           | How to invoke                                                                                                                                                                                                                                                                                                                                                          | Function                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Copy Row                | Data pool        | In the Name column, select one or more objects and then right-click one of the selected objects and select Copy Row.                                                                                                                                                                                                                                                   | Copies the selected rows to the clipboard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Paste Row Before        | Data pool        | In the Name column, right-click an object and select Paste Row Before.                                                                                                                                                                                                                                                                                                 | Pastes the copied rows from the clipboard to a position immediately before the row that contains the object that you right-clicked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Paste Row After         | Data pool        | In the Name column, right-click an object and select Paste Row After.                                                                                                                                                                                                                                                                                                  | Pastes the copied rows from the clipboard to a position immediately after the row that contains the object that you right-clicked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Undo                    | Data pool        | In the Name column, select one or more editable fields, then click the down arrow icon and select Undo.                                                                                                                                                                                                                                                                | Undoes the last action that you have performed, such as adding new array elements or changing values in a value field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Redo                    | Data pool        | In the Name column, select one or more editable fields, then click the down arrow icon and select Redo.                                                                                                                                                                                                                                                                | Redoes the last action that you have undone, such as adding new array elements or changing values in a value field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Set To > Value          | Value, data pool | In the Name column, select one or more editable fields, then right-click a selected row and select Set To > Value.                                                                                                                                                                                                                                                     | Opens the Set Value window where you can specify a value for selected fields. Alternatively, you can also type a value directly into the Value column for an individual field. You can use this menu item in conjunction with the Select All menu item to open the Set Value window and specify a value for all fields. Set values are flagged with the Set symbol .                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Set To > Unset          | Value, data pool | In the Name column, select one or more editable fields, then right-click one of the selections and select Set To > Unset.                                                                                                                                                                                                                                              | Sets the value of the selected fields to the value Unset, as indicated by the Unset symbol . You can use this menu item in conjunction with the Select All menu item to set the value of all fields to the value Unset.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Set To > Null           | Value, data pool | In the Name column, select one or more editable fields, then right-click one of the selections and select Set To > Null.                                                                                                                                                                                                                                               | Sets the value of the selected fields to the value Null. You can use this menu item in conjunction with the Select All menu item to set the value of all fields to the value Null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Set To > Default        | Value, data pool | In the Name column, select one or more editable fields, then right-click one of the selections and select Set To > Default.                                                                                                                                                                                                                                            | Sets the value of the selected fields to their default values. For example, a boolean data type is set to a value of false and an integer value is set to a value of 0. You can use this menu item in conjunction with the Select All menu item to set the value of all fields to their default values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Add Elements            | Value, data pool | In the Name column, right-click an array and select Add Elements.                                                                                                                                                                                                                                                                                                      | Opens the Add Element window so that you can specify the number of elements that you want to add to the array.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Remove Elements         | Value, data pool | In the Name column, select one or more array, then right-click a selected row and select Remove Elements.                                                                                                                                                                                                                                                              | Removes all array elements from the selected arrays.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Show Change Summary     | Value            | If the operation that you are testing has a business graph as its parameter, right-click any cell in the Name column and then select the Show Change Summary menu item. A check mark symbol is displayed beside the menu item to show that it is selected.                                                                                                             | Appends a Change Summary column to the value editor and the data pool editor. The column accepts values that represent the original state of the business objects in the business graph.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Enable Logging          | Value            | If the operation that you are testing has a business graph as its parameter, right-click any cell in the Name column and then select the Enable Logging menu item. A check mark symbol is displayed beside the menu item to show that it is selected. Note that the Show Change Summary menu item must be selected before you can select the Enable Logging menu item. | Initiates the logging of business object changes that occur after the operation has been invoked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Copy Value              | Value, data pool | In the Name column, right-click a parameter, field, array, or element and select Copy Value.                                                                                                                                                                                                                                                                           | Copies the selected parameter, field, array, or element to the clipboard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Set Required to Default | Value, data pool | In the Name column, select one or more editable fields, then right-click one of the selections and select Set Required to Default.                                                                                                                                                                                                                                     | Sets the required fields to their default values. Sets any unrequired fields to unset. You can use this menu item in conjunction with the Select All menu item to set all required fields to their default values and set all unrequired fields to unset.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Use Previous Value      | Value            | In the Name column, right-click a parameter and select Use Previous Value.                                                                                                                                                                                                                                                                                             | Opens the Use Previous Value window where you can select one or more previous values that were automatically saved when the test client was closed. Information on setting a preference to specify the maximum number of previous values to save is found in the topic "Specifying the maximum number of previous input values to save."                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Add Value to Pool       | Value            | In the Name column, right-click a parameter, field, array, or element and select Add Value to Pool.                                                                                                                                                                                                                                                                    | Adds the selected parameter, field, array, or element to the data pool. Additional information about adding values to pools is found in the topic "Adding values to data pools."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Use Value from Pool     | Value            | In the Name column, select one or more objects and then right-click a selected row and select Use Value from Pool.                                                                                                                                                                                                                                                     | Opens the data pool editor, where you can select a value to use for a field, array element, or business object. Values of one business object in the data pool may be used for a business object with a different data type if the attribute names match. For example, if a business object in the data pool has attributes A, B, and C but the business object for which you are using the values has attributes B, A, and D, then attributes A and B will receive copied values but attribute D will not. If the data type of any fields copied from the data pool do not match, such as when you are using a boolean value in an integer field, an error icon is displayed in the cell. Additional information about using values from pools is found in the topic "Using values from data pools." |
| Import from XML File    | Value, data pool | In the Name column, select one or more objects and then right-click a selected row and select Import from XML.                                                                                                                                                                                                                                                         | Opens a file selection window where you can import the value of a field, array element, or business object from an XML file. Values of one business object may be copied to a business object with a different data type if the attribute names match. If a copied value is not correct for the data type of the field to which it is being imported, such as when you are importing a boolean value to an integer field, an error icon is displayed in the cell. For additional information and an example of an XML file, see the section below entitled "Importing values from XML files."                                                                                                                                                                                                         |
| Export to XML File      | Value, data pool | In the Name column, select one or more XSD elements or attributes and then right-click a selected row and select Export to XML File.                                                                                                                                                                                                                                   | Opens a New XML File window where you can save the selected XSD element or attribute to your workspace as either an XML or XSD file. If the value element is representing an XSD schema, then you should export the XSD element as an XSD (.xsd) file. Note that the XSD element or attribute that you chose to export will be exported as well as any nested objects, but the siblings of the object will not be exported.                                                                                                                                                                                                                                                                                                                                                                           |
| Use Derived Type        | Value, data pool | In the Name column, right-click a field, element, or attribute and select Use Derived Type.                                                                                                                                                                                                                                                                            | Opens a Data Type Selection window where you can select a concrete type for an xsd:anyType field. You can also select a different type that is derived from the original type that was specified in the editor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Select Element          | Value, data pool | In the Name column, right-click an element and choose Select Element.                                                                                                                                                                                                                                                                                                  | Opens a Select Element window where you can select a global XSD element (defined at the top level of the XSD schema) for an xsd:any element or select an XSD substitution group element for the selected element in the editor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Select Attribute        | Value, data pool | In the Name column, right-click an attribute and choose Select Attribute.                                                                                                                                                                                                                                                                                              | Opens a Select Attribute window where you can elect a global XSD attribute (defined at the top level of the XSD schema) for an xsd:anyAttribute attribute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Paste Value             | Value, data pool | In the Name column, select one or more objects and then right-click a selected row and select Paste Value.                                                                                                                                                                                                                                                             | Pastes the copied value of a field, array element, or business object from the clipboard. Values of one business object may be copied to a business object with a different data type if the attribute names match. For example, if a copied business object has attributes A, B, and C but the business object to which you are pasting has attributes B, A, and D, then attributes A and B will receive copied values but attribute D will not. If the data type of any copied fields do not match, such as when you are copying a boolean value to an integer field, an error icon is displayed in the cell.                                                                                                                                                                                       |
| Remove                  | Data pool        | In the Name column, select one or more top-level parameters, fields, arrays, or elements, then right-click a selected row and select Remove.                                                                                                                                                                                                                           | Removes the value of the parameters, fields, arrays, or elements that are selected at the top level in the data pool editor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Select All              | Value, data pool | In the Name column, right-click any object and select Select All.                                                                                                                                                                                                                                                                                                      | Selects all objects in the value editor or the data pool editor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

The pop-up menu items available for working with event
definitions are described in the following table:

| Pop-up menu item        | Editor           | How to invoke                                                                                                                                        | Function                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Copy Row                | Data pool        | In the Name column, select one or more objects and then right-click one of the selected objects and select Copy Row.                                 | Copies the selected rows to the clipboard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Paste Row Before        | Data pool        | In the Name column, right-click an object and select Paste Row Before.                                                                               | Pastes the copied rows from the clipboard to a position immediately before the row that contains the object that you right-clicked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Paste Row After         | Data pool        | In the Name column, right-click an object and select Paste Row After.                                                                                | Pastes the copied rows from the clipboard to a position immediately after the row that contains the object that you right-clicked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Undo                    | Data pool        | In the Name column, select one or more editable fields, then click the down arrow icon and select Undo.                                              | Undoes the last action that you have performed, such as adding new array elements or changing values in a value field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Redo                    | Data pool        | In the Name column, select one or more editable fields, then click the down arrow icon and select Redo.                                              | Redoes the last action that you have undone, such as adding new array elements or changing values in a value field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Set To > Value          | Value, data pool | In the Name column, select one or more properties or extended data elements, then right-click a selected row and select Set To > Value.              | Opens the Set Value window where you can specify a value for all selected fields. Alternatively, you can also type a value directly into the Value column for an individual field. You can use this menu item in conjunction with the Select All menu item to open the Set Value window and specify a value for all fields. Set values are flagged with the Set symbol .                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Set To > Unset          | Value, data pool | In the Name column, select one or more properties and extended data elements and then right-click one of the selections and select Set To > Unset.   | Sets the value of the selected fields to the predefined value unset, as indicated by the Unset symbol . You can use this menu item in conjunction with the Select All menu item to set the value of all fields to the predefined value unset.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Set To > Null           | Value, data pool | In the Name column, select one or more properties and extended data elements and then right-click one of the selections and select Set To > Null.    | Sets the value of the selected fields to the predefined value null. You can use this menu item in conjunction with the Select All menu item to set the value of all fields to the predefined value null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Set To > Default        | Value, data pool | In the Name column, select one or more properties and extended data elements and then right-click one of the selections and select Set To > Default. | Sets the value of the selected fields to their default values. For example, a boolean data type is set to a value of false and an integer value is set to a value of 0. You can use this menu item in conjunction with the Select All menu item to set the value of all fields to their default values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Add Elements            | Value, data pool | In the Name column, right-click any extended data element that is an array and select Add elements.                                                  | In the value editor, this menu item opens the Add Element window where you can specify the number of elements that you want to add to the array.In the data pool editor, this menu item opens the Add Element window where you can specify the number of elements that you want to add to the array as well as the name of the module that defines the data type.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Remove Elements         | Value, data pool | In the Name column, select one or more arrays, then right-click a selected row and select Remove Elements.                                           | Removes all array elements from the selected arrays.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Copy Value              | Value, data pool | In the Name column, right-click any object and select Copy Value.                                                                                    | Copies the selected object to the clipboard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Set Required to Default | Value, data pool | In the Name column, select a property or an extended data element and then right-click the selection and select Set Required to Default.             | Sets the required fields to their default values. Sets any unrequired fields to unset. You can use this menu item in conjunction with the Select All menu item to set all required fields to their default values and set all unrequired fields to unset.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Add Value to Pool       | Value            | In the Name column, right-click any object and select Add Value to Pool.                                                                             | Adds the selected object to the data pool. Additional information about adding objects to pools is found in the topic "Adding values to data pools."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Use Value from Pool     | Value            | In the Name column, select one or more objects and then right-click a selected row and select Use Value from Pool.                                   | Opens the data pool editor, where you can select a value to use for an object, such as an event definition, property, or extended data element. Values of one object in the data pool may be used for an object with a different data type if the names match. For example, if an extended data element array has the elements A, B, and C but the extended data element array to which you are pasting has the elements B, A, and D, then elements A and B will receive copied values but element D will not. If the data type of any copied fields do not match, such as when you are copying a boolean value to an integer field, an error icon is displayed in the cell. Additional information about using objects from data pools is found in the topic "Using values from data pools." |
| Paste Value             | Value, data pool | In the Name column, select one or more objects and then right-click a selected row and select Paste Value.                                           | Pastes the copied value of an object (such as an event definition, property, or extended data element) from the clipboard. Values of one object may be copied to an object with a different data type if the names match. For example, if an extended data element array has the elements A, B, and C but the extended data element array to which you are pasting has the elements B, A, and D, then elements A and B will receive copied values but element D will not. If the data type of any copied fields do not match, such as when you are copying a boolean value to an integer field, an error icon is displayed in the cell.                                                                                                                                                       |
| Remove                  | Data pool        | In the Name column, right-click one or more properties or extended data elements and select Remove.                                                  | Removes the selected property or extended data element from the data pool.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Select All              | Value, data pool | In the Name column, right-click any object and select Select All.                                                                                    | Selects all objects in the value editor or the data pool editor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## Date and time values

- yyyy is a four-digit year
- MM is a two-digit month
- dd is a two-digit day of the month
- T  is a literal indicating the beginning
of a time element
- HH is a two-digit hour
- mm is a two-digit minute
- ss is a two-digit second
- Z is an optional time zone designation

For example, 2007-01-18T04:00:00 EST.

The exact
format of a date and time value is dependent on the associated XML
schema type. The following table lists the XML schema types and their
corresponding date and time formats.

| XML Schema Type   | Format                | Example                 |
|-------------------|-----------------------|-------------------------|
| xs:dateTime       | yyyy-MM-ddTHH:mm:ss Z | 2007-01-18T04:00:00 EST |
| xs:date           | yyyy-MM-dd Z          | 2007-01-18 EST          |
| xs:time           | HH:mm:ss              | 04:00:00                |
| xs:gYearMonth     | yyyy-MM Z             | 2007-01 EST             |
| xs:gMonthDay      | MM-dd                 | 01-18                   |
| xs:gMonth         | MM                    | 01                      |
| xs:gDay           | dd                    | 18                      |

Specifying a time zone is optional for those XML schema
types that can accept a time zone designation. If you do not specify
a time zone, the time zone will default to Greenwich Mean Time (GMT) unless you
have specified local time as the default time zone. If you do specify
a time zone, you can specify it by using one of several standard time
zone offsets, as shown in the bold text in the following list:

- 2007-01-01T07:00:00 GMT-05:00
- 2007-01-01T17:00:00 +05:00
- 2007-01-01T23:00:00 +1200
- 2007-01-01T04:00:00 EST
- 2007-01-01T06:00:00 Central Standard Time
- 2007-01-01T07:00:00 America/New\_York

Note that for Java interfaces that use java.util.Date, both
the time and the time zone are optional.

## Maximum depth of expanded business objects

In
the Preferences window of IBM Integration
Designer,
you can set preferences to change the maximum depth to which you want
to automatically expand your nested business objects in the value
editor and data pool editor. This is described in the topic "Specifying
the maximum depth of expanded business objects." However, if you have
business objects that are nested many levels deep and you choose to
automatically expand the nested business objects to a great depth,
it can adversely impact the usability of the editor. They may take
a long time to display all of the nested business objects and it may
take you even longer to specify values for all of them. Conversely,
if you find that you are continually expanding nested business objects
manually, you may choose to specify a greater maximum depth. By default,
nested business objects are automatically expanded to a maximum depth
of five levels for the value editor and zero levels for the data pool
editor.

## Importing values from XML

Values of one business object in the XML can be imported into
a business object with a different data type in the value editor if the
attribute names match. (The one exception to this rule is that if
the top-level root element name in the XML differs from the top-level
parameter name in the value editor, the top-level root name in the
XML will be ignored. And if the XML resides in a SOAP message file,
the SOAP envelope and body elements are also ignored.)

The following
list contains other considerations for importing values from XML:

- If a value that you want to import from the XML is not the correct
data type for a corresponding field in the value editor, such as when
you are importing a boolean value from the XML into an integer field
in the value editor, an error icon is displayed.
- If no matching attribute name is found in the XML for an attribute
in the value editor, the attribute field in the value editor is automatically
set to unset.

To better illustrate how importing values from XML works,
assume that the value editor is populated with the following elements:

| Name   | Type          | Value   |
|--------|---------------|---------|
| order  | PurchaseOrder |         |
| id     | string        |         |
| items  | Item[]        |         |

```
<?xml version="1.0" encoding="UTF-8"?>
<bo:po xmlns:bo="http://OrderEntry/bos"
       xmlns:bo1="http://OrderEntry"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://OrderEntry/bos PurchaseOrder.xsd http:
              //OrderEntry xsd-includes/http.OrderEntry.xsd ">
       <id>id1</id>
       <items>
              <id>item1 id</id>
              <quan>5</quan>
       </items>
       <items>
              <id>item2 id</id>
              <desc>def</desc>
              <quan>6</quan>
       </items>
</bo:po>
```

| Name     | Type          | Value    |
|----------|---------------|----------|
| order    | PurchaseOrder |          |
| id       | string        | id1      |
| items    | Item[]        |          |
| items[0] | Item          |          |
| id       | string        | item1 id |
| desc     | string        | unset    |
| quan     | int           | 5        |
| items[1] | Item          |          |
| id       | string        | item2 id |
| desc     | string        | def      |
| quan     | int           | 6        |