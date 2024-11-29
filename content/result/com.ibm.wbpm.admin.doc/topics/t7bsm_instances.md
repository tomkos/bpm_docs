<!-- image -->

# Creating customized views in Business Process Choreographer
Explorer or Business Process Archive Explorer for process instances
for state machines

## Before you begin

## About this task

## Procedure

1. Click Manage Views in the taskbar.
2. In the Manage Views page, select Search
For Process Instances And Define Customized Views.
3 Click Custom Property Filters > Custom Property Filter .
    1 Add a custom property with the following settings:
        - In the Property Name field, type generatedBy.
        - In the Property Value field, type BusinessStateMachine.
2. Click Add.
3. Add other custom properties as needed.
4 Click View Properties > List Columns .

1 In the List Columns for Query Properties, add the followingquery properties.
    - To add business state information to the view, type name in
the Property Name field, DisplayState in
the Variable Name field, and tns in
the Namespace field, where tns is
the target namespace of the business state machine suffixed by -process.
Also specify a display name for the column in the Display
Name field, and click Add.
    - To add correlation information to the view, provide the appropriate
information in the Property Name field, the Variable
Name field, and the Namespace field.
These values are derived from the definition of the state machine.
Also provide a display name for the column in the Display
Name field.
Property Name
The name of the correlation property that you defined for the
state machine.
Variable Name
If the correlation set is initiated by incoming parameters, the
variable name has the following format:operation\_name\_Input\_operation\_parameter\_name	where operation\_name is
the name of the operation for the transition out of the initial state.If
the correlation set is initiated by outgoing parameters, the variable
name has the following format:operation\_name\_Output\_operation\_parameter\_name	

Namespace
The namespace of the query property, where tns is
the target namespace of the state machine suffixed by -process.
2. Add other custom properties or query properties, or
add columns to or remove columns from the list of selected columns.
5. Type a name for the query in the View Name field,
and click Check and Save. The
search is run to check for errors. If it runs without errors, the
view is saved.

## Results

By default, a link to the new view is added to the Process
Instances group in the navigation pane. Your users see this view the
next time that they log in to the instance of the client that you
added the view to.

<!-- image -->