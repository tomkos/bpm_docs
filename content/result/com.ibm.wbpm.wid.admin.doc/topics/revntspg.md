<!-- image -->

# Events page of the integration test client

<!-- image -->

- 1 Status area
- 2 Control area
- 3 Events area
- 4 General Properties
- 5 Detailed Properties

## Status area

The status area
is located at the top of the Events page. It displays messages for
the event that is currently selected in the Events area. Typically,
these messages provide instructions about how to work with interactive
events, such as Invoke events and manual Emulate events. For example,
the status area in the figure indicates that for the Invoke
event selected in the Events area, you should choose the component,
interface, and the operation that you want to invoke and then click Continue to
invoke the operation.

## Control area

| Icon      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Invoke    | Generates an Invoke event in the Events area, which you can use to select an operation, specify values for the operation, and invoke and test the operation. Beside the Invoke icon, you can select the following menu items by clicking the down arrow icon : Attach, which generates an Attach event in the Events area and attaches the integration test client directly to a test configuration module. This is useful if you want to use your own invocation mechanism rather than that provided by the integration test client, such as a JMS message, web service, or JSP. Emit, which generates an Emit event in the Events area, which you can use to select a  6.0.2-format event definition, specify values for the event definition, and emit a common base event to test the event definition. Run Test, which generates a Run Test event in the Events area, which you can use to perform testing on test suites and associated test cases. |
| Data Pool | In the Detailed Properties area of the Events page, any values that you specify for an operation, manual emulation, or event definition in the value editor can be saved to the data pool. The Data Pool icon opens the data pool editor, which you can use to view, edit, select, and use the saved data pool values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Filters   | Opens the Event Filter window, from which you can choose an event filter that suppresses the display of selected event types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Continue  | Initiates the invocation. Depending on the current deployment state of your module, the Deployment Location wizard might open so that you can select a test server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Stop      | Detaches the integration test client from the server. All running operations that are waiting on user input from the test client are terminated. All other running applications will continue until they terminate, but no status will be reported in the test client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Save      | Opens the Save Test Trace window, with which you can save the test trace.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Events area

The
Events area displays a hierarchal test trace for the events that are
generated during a test. These events are typically grouped together
under a top-level event. For example, if you are testing an operation,
the events are nested together under the Invoke event that was used
in the invocation of the operation.

In the preceding figure,
the manual Invoke event at the top of the Events area is a client-side
event. All of the events nested below the manual Invoke event are
server-side events that collectively represent the complete lifecycle
of a single invocation. Similarly, if an Attach or Emit event appeared
at the top of the Events area rather than a manual Invoke event, the
Attach or Emit event would be a client-side event and all of the events
nested below the Attach or Emit event would be server-side events
that together represent the lifecycle of a single invocation.

If
an interactive event such as an Invoke event or a manual Emulate event
is encountered during your test, the invocation of the operation pauses
at the event so that you can specify values for the operation or emulation.

In
the Events area, the event trace can display multiple concurrent invocations
at the same time. For example, you could begin a new test while other
tests are still executing. The event trace is dynamic, which means
that it is continuously updated as events occur during a test. You
can save your test trace to a test trace file at any time by clicking
the Save Test Client icon.

- Running: Shows the Invoke events, Request events (two-way
that do not have a corresponding Return or Response event), and Fine-Grained
Trace events that are currently running.
- Waiting: Shows the Emulate and Claim events that are waiting
for user input.

If the test client
and the assembly editor are both open in the workbench and you organize
the views so that you can see both of them at the same time, you will
see that when you select an event in the Events area of the test client,
the corresponding entity is automatically selected in the assembly
editor. For example, if you select a manual Emulate event in the Events
area, the component or reference that is being emulated will automatically
be selected in the assembly editor. By clicking on one event after
another in the Events area, you can get a rudimentary animation in
the assembly editor that represents the flow of control during the
invocation.

## General Properties

The General
Properties area shows the time that an event selected in the Events
area was generated.

## Detailed Properties

The Detailed
Properties area displays the specific properties of any event that
is selected in the Events area. For some events, the specific properties
can include information about the resources associated with the selected
event, such as the name of the test configuration and module being
used in the test. If you are testing a module that is contained in
a process application or a toolkit, the name of the process application
or toolkit is added to the name of the module as a prefix.

For
other events, the specific properties might simply provide the name
of the event type. If a hyperlink appears on a resource name, you
can click the link to open the resource in the assembly editor.

For
example, the Detailed Properties area for an interactive Invoke event
provides fields you can use to select properties for your tests, such
as the test configuration, module, component, interface, and the operation
that you want to invoke. For those events that are not interactive,
the fields simply display the properties that are associated with
the events.

<!-- image -->

As shown in the figure, the Detailed Properties
area also provides a value editor. For an Invoke event or a manual
Emulate event, you use the value editor to specify, view, edit, and
pass values for the operation that you want to invoke. For an Emit
event, you use the value editor to specify, view, edit, and pass values
for the event definition that you want to emit as a common base event.
You can also use the value editor to save values to the data pool,
where you can view and edit them using the data pool editor. Both
the value editor and the data pool editor are described in the topic Value
and data pool editors.