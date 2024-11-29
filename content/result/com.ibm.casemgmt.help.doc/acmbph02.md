# Adding an existing FileNet P8 process as an
activity

## Before you begin

## About this task

## Procedure

To add an existing workflow as an activity:

1. From the Activities page, click Add Activity > Activity with Existing FileNet P8
Process.
If Activity with Existing FileNet P8 Process is not
available, then no process is associated with the solution. Tip: If you want to add the
process as a subactivity inside a container activity, open the container activity first. Then, click Add Subactivity > Subactivity with Existing FileNet P8 Process.
2. In the General window, specify the name, unique identifier, a description
(optional), define how the activity starts, and assign the activities to a set (optional).
3. In the Preconditions window, define any preconditions that are required
before the activity can start.
4. In the Select Process window, select
the workflow to reuse.
5 In the Map Properties window, mapprocess data fields to solution properties:
    1. Select a process data field name from the reused workflow.
    2. Select a solution property name to map to the selected
process data field name.
Property names must match the
data type and number of values (single value or multivalue) of the
selected data field. After selecting a data field name, only valid
matching properties are displayed in the Case type property
name menu.
    3. To add the selected mapping to the property map, click
the plus (+) icon.
6. Optional: 
Click Finish or
proceed to the final step.
7. Optional: 
In the Design Comment window, add a design comment that explains the
reasons this activity was created, or what the imported process does, or how it works with the
solution, for example.
8. Click Finish.

## Results

- Importing an existing workflow into a solution

To reuse an existing  FileNet P8 process as a task, first import the existing workflow into the solution.
- Updating case property values in a reused process

You can update case property values as a workflow progresses.
- Removing a reused process from a solution

You can remove a reused process from a solution by using IBM FileNet Process Designer.