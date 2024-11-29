<!-- image -->

# Creating transforms

## About this task

- Creating transforms using the graph view

You can create transforms using the graph view in a number of ways.
- Creating transforms using the table view

You can create transforms using the table view of the business object map editor.
- Creating transforms using arrays

Arrays in business object maps can be represented in two ways: zero base style dot notation (array.0) and one base style bracket notation (array[1]). A dot is a valid character in a field name and by default, the business object map editor interprets dots as part of the name and not as an array index.  Therefore, inputs and outputs to transforms will appear to be unresolved even though the map is valid and will still run.