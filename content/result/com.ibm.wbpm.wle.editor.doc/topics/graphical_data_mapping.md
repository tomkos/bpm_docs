# Mapping input and output data for an activity in processes

To pass variables to an activity, you must set the input and output data
mapping.

- Procedure
- Example

## Before you begin

## About this task

The following procedure describes how to map both input and output data for an activity.
Depending on the logic of your process, an activity may require only input or output data and not
both.

## Procedure

1. Open the process.
2. Click the activity in the diagram, and go to the General tab in
the properties. Click Open. Alternatively, you can open the Data
Mapping dialog from the Data Mapping tab. The
Data Mapping dialog displays the input and output variables that are available
in the activity in two different tabs.
3. In the Input Mapping and Output Mapping
tabs, complete the fields with the variables you want to map.
4. Click OK.

## Example

- To use the parent object to map every field it contains, complete the parent
field.
- To map some or every subfield in a parent object individually, complete their
fields.
- To switch from mapping the parent object to map each subfield in a parent object individually,
click the question mark icon in the subfield, and then click
Yes.
- To map objects with JavaScript, click the JS button next to the field you
want to complete.
- To autofill the fields, click Insert suggestions in the dialog box.
Automapping fills the fields with intelligent guesses based on previously used
values.

- Initializing parent objects for data mapping

Ensure that all the parent objects of a property exist to prevent an error from occurring at run time.