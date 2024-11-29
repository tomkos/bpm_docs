# Handling data changes in client-side human services

## About this task

- At regular intervals that are based on the settings for the system timer. For more information, see Changing custom properties for Process Portal.
- Explicitly by a user if the data change event handler is bound to a view, for example, Refresh
Button.

When
the execution of the data event handler finishes, control is returned
to the coach that was running when the event handler was started.

Human services for process UIs automatically include a default data change handler. If you generated the client-side human service for the instance UI from the
Instance Details UI Service template, the service contains a data change handler with a reference
implementation. You can customize the reference implementation that is provided by the template, for
example, so that the instance UI refreshes when the user clicks a Refresh
button. For more information about the template, see Instance Details UI Service Template.

Human services for BPDs (deprecated) and case types

do not contain data change event handlers. You can upgrade the human services to handle data changes
by adding and implementing a data change event handler.

## Procedure

The following procedure describes how to add a data change
event handler to a human service. If one of the following situations
apply, follow all the steps in the procedure:
You are creating a new data change handler implementation, for example, because you didn't
generate the process instance UI from the template.
You are upgrading a client-side human service from an earlier product
version.

If you are customizing the reference implementation, go to step 4.

1. Open the client-side human service that you want to work
with.
2. In the Diagram view, add an event handler  to the diagram.
By default, the event handler is an Error Event handler.
3. Change the default Error Event handler to a data change event handler by renaming the
Error node to Data Change and, in the
Implementation properties, under Event Trigger, select
Data Change Event.

Tip: The data change event handler is available only for client-side human services that
run in the context of a process. A client-side human service can have only one data change event
handler. Human services for processes automatically contain an implemented data change event
handler.
4 Implement the data change event handler.
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