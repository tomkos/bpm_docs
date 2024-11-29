# Associating process variables to a tracking group

## Before you begin

## About this task

## Procedure

1. Open the process.
2 To add a Pre Tracking Point or a Post TrackingPoint to an activity, gateway, or event in the process editor, follow these steps:
    1. In the Definition view, select an activity, gateway, or event.
    2. In the Properties view, open the Tracking tab.
    3. Select either Pre Tracking Point or Post Tracking
Point, which corresponds to a point before the activity starts or after the diagram node
finishes. You can set a tracking point in either one or both. A tracking point is the point in a
process where data from process variables is sent to a tracking group.
    4. For the Tracking Group field, click Select and
select the tracking group that you want to use. The tracking group fields are added in the Pr
section you are working with. You can also create a new tracking group. For each tracked field
defined in the tracking group, you must ensure that there is no other tracked field with the same
name but with a different type defined in any other tracking group, either in the same process or in
different processes or toolkits. Likewise, you must not change a tracked field type within the same
tracking group.
    5. (Optional) Sort the tracked fields by selecting a sort order from the
Sort tracked fields by list. Sorting can be helpful when you work with many
tracked fields.
    6. Bind a process variable to each tracked field you want to use by
clicking the selection icon (). Your process variable must be a simple type. You can also assign expressions and literal
values to tracking group fields.
3. Click  or
Finish Editing.
4. Click Update Tracking Definitions in the
Process Application Settings page to send the tracking information to the
Business Performance Data Warehouse.

## Results