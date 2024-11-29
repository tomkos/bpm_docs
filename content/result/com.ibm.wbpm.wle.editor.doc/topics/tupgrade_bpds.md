# Upgrading BPDs from IBM Business Process Manager V8.5.5 and earlier (deprecated)

## About this task

In IBM Business Process Manager V8.5.5 and later versions, client-side human services for
instance UIs contain a data change event handler. This event handler manages both the local and
remote changes to data in the UI. You can include this function in BPDs from earlier releases.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open the BPD that you want to upgrade.
3. Open the client-side human service for the instance UI.
4. In the Diagram view, add an event handler  to the diagram.
By default, the event handler is an Error Event handler.
5. Change the default Error Event handler to a data change event handler by renaming the
Error node to Data Change and, in the
Implementation properties, under Event Trigger, select
Data Change Event.

Tip: The data change event handler is available only for client-side human services that
run in the context of a process. A client-side human service can have only one data change event
handler. Human services for processes automatically contain an implemented data change event
handler.
6 Implement the data change event handler.
    1. Optional: 
Specify the boundary events that can trigger the data change event handler.
By default, the event handler checks the server at regular intervals for updated data. To
specify the boundary events, in the Behavior implementation properties,
select the coach boundary events in the current client-side human service that trigger the event
handler. For example, you can add a Refresh Button to the UI so that users can manually refresh the
data. In the data change event handler properties, add the boundary events for the Refresh Button to
trigger the refresh. 
If the current
service contains nested client-side human services that have Trigger the root data change
event handler selected, the nested services are also shown in the
Behavior list.
    2. Add the logic for reacting to data changes by double-clicking
the Data change node.  Several tw.system.coachUtils and tw.system.dataChangeUtils JavaScript
APIs are available for detecting data changes on the server and applying
them to the client. For more information, see JavaScript API for client-side human service development.
7 To test the interaction between the user interface andthe process, complete the following steps:

1. In the Process Designer desktop
editor, open the BPD and click Run Process  in the toolbar.
2. Switch to the Inspector when prompted.
3. In the Inspector, select the process instance and click
the Runs the Details UI for the selected BPD Instance in
the toolbar.