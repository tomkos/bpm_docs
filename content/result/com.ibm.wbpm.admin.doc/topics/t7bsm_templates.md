<!-- image -->

# Creating customized views in Business Process Choreographer
Explorer or Business Process Archive Explorer for process templates
for state machines

## Before you begin

## About this task

## Procedure

1. Click Manage Views in the taskbar.
2. In the Manage Views page, select Search
For Process Templates And Define Customized Views.
3 Click Property Filters > Custom Property Filters .
    1 Add a custom property with the following settings:
        - In the Property Name field, type generatedBy.
        - In the Property Value field, type BusinessStateMachine.
2. Click Add.
3. Add other custom properties as needed.
4 Click View Properties > List Columns .

1 In the List Columns for Custom Properties, add a customproperty with the following settings:
    - In the Property Name field, type generatedBy.
    - In the Display Name field, type a display
name for the column, and click Add.
2. Add other columns to or remove columns from the list
of selected columns.
5. Type a display name for the query in the View
Name field, and click Check and Save.
The search is run to check for errors. If it runs without
errors, the view is saved.

## Results

By default, a link to the new view is added to the Process
Templates group in the navigation pane. Your users see this view the
next time that they log in to the instance of the client that you
added the view to.

<!-- image -->