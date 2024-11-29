# Upgrading case types: Adding data change management to details UIs

## Procedure

1. Convert the case type to a process.
2. Open the client-side human service for the details UI.
3. In the Diagram view, add an event handler  to the diagram.
By default, the event handler is an Error Event handler.
4. Change the default Error Event handler to a data change event handler by renaming the
Error node to Data Change and, in the
Implementation properties, under Event Trigger, select
Data Change Event.

Tip: The data change event handler is available only for client-side human services that
run in the context of a process. A client-side human service can have only one data change event
handler. Human services for processes automatically contain an implemented data change event
handler.
5 Implement the data change event handler.
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
6. Click Save or Finish Editing.
7 To test the interaction between the user interface and the process:

1. Run the process.
2. In the Inspector, select the process instance and click Open instance Details UI
 in the toolbar.