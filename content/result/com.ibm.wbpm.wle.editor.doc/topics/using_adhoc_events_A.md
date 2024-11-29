# Building a sample ad hoc action (deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

For the following example, you can use the Standard HR
Open New Position business process definition (BPD) included in the
Hiring Sample process application. (If you do not see the Hiring Sample
process application in your list of applications in Workflow Center,
ask your IBM Business Automation Workflow administrator
to give you access.) To do so, clone a snapshot of the Hiring Sample
process application so that your changes do not affect other users
of IBM Process
Designer.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a BPD in the Designer view and click the Diagram tab.
3. Drag a swimlane from the palette to the diagram.
4. Right-click the new lane and select Move Lane
Down until the new lane is the last lane in the BPD (below
the System lane).
5. Click the new lane in the diagram (named Untitled
1 by default) and in the Name field
in the properties, type Ad hoc event .
6. Drag a start event from the palette onto the BPD diagram
so that it is positioned in the new Ad hoc event lane.
7. In the text box that displays over the start event , type Show
Requisition Data for the event name.
8. Click the Implementation tab in the Properties view and
select Ad Hoc from the available start event
types. If you wanted to restrict the users who can perform
the action, you could also associate a specific team with the swimlane
and then in the Event Visibility section specify
that the event visibility is restricted by swimlane.
9. Drag an activity from the palette into the Ad hoc event
lane.
10. In the text box that displays over the user task,, type Show
Data for the user task name.
11. Drag an end event from the palette onto the BPD diagram
so that it is positioned after the Show Data activity
in the Ad hoc event lane and optionally name the
end event.
12. Using the Sequence Flow tool, connect the Show
Requisition Data start event, the Show Data activity,
and the end event on the BPD diagram.
13. Right-click the Show Data activity and
select Activity Wizard from the list of options.
14. In the Activity Wizard - Setup Activity window, make the
following selections: 
Table 1. Recommended selections
in the Activity Wizard - Setup Activity window

Option
Selection

Activity Type
User Task

Service Selection
Select the Create a New Service or Process option.

In the Name field,
type Show Data for the new service. (For this example,
name the new Human service the same as the corresponding activity
in the BPD.)
15. In the Activity Wizard - Setup Activity window, click Next.
16. In the Activity Wizard - Parameters window, choose the
process variables from the regular process to use as input and output
for the new service for the ad hoc process. For the
private variable named requisition, leave the Input field
set to true and change the Output field
to false. These settings reflect the fact that
our sample ad hoc event simply displays the requisition data and does
not pass back modified data. For other variables, click to change
the setting from true to false under the Input and Output field. Click Finish.
The
new service is created and attached to the activity. The new service
includes a single Coach.
17. Double-click the Show Data activity in
the Ad hoc event lane in the BPD. The new service opens
and you can see the service diagram.
18. Click the Coaches tab and then click
the listed Coach to see its controls. Because we used
the Activity Wizard, the Coach includes a form element for each of
the parameters in the requisition variable.
19. Save your work and then follow the instructions in Deprecated: Testing a sample ad hoc action.