# Initializing parent objects for data mapping

## About this task

- Author the mapping by selecting variables or properties with graphical data mapping.
    - For the input mapping source, you can select a variable or a property in a variable. The runtime
maps the value as null if the property's parent variable is not initialized.
    - For the input mapping target, you can choose an input variable to map the data to. The runtime
automatically initializes the parent input object before it maps the value to a property.
    - For the output mapping source, you can choose an output variable to map the data from. The
runtime maps the value as null if the property's parent output is not returned from the call.
    - For the output mapping target, you can select a variable or a property in a variable. The
runtime automatically initializes the parent variable object before it maps the value to a
property.
- Convert the mapping from JavaScript to select the variable or properties by using graphical data mapping.

- Open the Data Mapping dialog and go to the existing mapping. Existing
mappings are specified using JavaScript mode display JS icon and a JavaScript
expression. If a JavaScript expression refers to a single local variable or a property, click
Select a variable to select a new value to replace the existing mapping.

- Define the default value for local variables that are used as a source or target of data mapping
that is specified with JavaScript.
- Assign an object that is returned from an earlier activity to a variable. Then, use that
variable or its properties as an input mapping source for a later activity.
- Add JavaScript before activity with input mapping.
    1. Define a variable of a complex type in the Variables tab.
    2. Place a script activity before the activity with the data mapping in the flow.
    3. In the script activity, write JavaScript to initialize the variable and set its properties.
    4. Use that variable or its properties as a source of input mapping for a later activity.
- Add JavaScript after activity with the output mapping.

1. Define a variable of a complex type using Variables tab.
2. In the data mapping, map the output to the variable.
3. Place a script activity after the activity with the data mapping in the flow.
4. In the script activity, write JavaScript to check that the variable exists and assign the
property values to other variables as required by the process logic.