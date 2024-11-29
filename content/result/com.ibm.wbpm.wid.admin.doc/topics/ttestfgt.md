<!-- image -->

# Running tests with fine-grained trace

## About this task

To run a test with
fine-grained trace:

## Procedure

1. Open the integration test client, as described in the topic
"Opening the integration test client."
2. In the Configurations page of the test client, add a fine-grained
trace for one or more components, as described in the topic "Adding
fine-grained traces."
3. In the Configurations page, select a fine-grained trace
and then select the variables that you want to track, as described
in the topic "Editing fine-grained traces". When you run a test and
then select fine-grained trace events in the Events area of the test
client, the values for the selected variables will be displayed in
the value editor. (Note that you can only select variables for business
processes and state machines. If you are testing a mediation flow,
there is nothing to select because the message is automatically tracked
and the values are automatically collected and displayed in the value
editor.)
4. In the Events page, ensure that the correct test configuration
is selected in the Configurations area.
5. In the Module field, ensure that
the correct module is selected.
6. In the Component field, select a
business process, state machine, or mediation flow component for which
you added a fine-grained trace.
7. In the Interface and Operation fields, ensure that the correct interface and
operation are selected.
8. In the value editor, specify values for the operation,
as shown in the following example: 
Information about using the value editor to specify values
is found in the test client topic "Value and data pool editors."
9. Click the Continue icon . (If the Deployment Location wizard opens,
select the server where you want to deploy your selected module, as
described in the test client topic "Deploying modules.") When the
invocation has finished, the results are returned and the Events area
is populated with both standard test client events and fine-grained
trace events, as shown in the following figure:
The fine-grained trace events are those that are nested under
the event named Fine-Grained Trace, as shown
in the figure.
10. In the Events area of the test client,
select a fine-grained trace event. If the associated component editor
is open beside the test client and if the test client still
has the focus, the corresponding element in the component editor will
automatically be selected and highlighted in a different color than
the rest of the execution path. For example, in the figure, the HumanTaskInBPEL event is selected in the Events area
of the test client. And in the open business process editor, the corresponding HumanTaskInBPEL activity is automatically selected and
highlighted, as shown in the following figure: You can set a preference to automatically open the appropriate
component editor in split-editor mode when you select a fine-grained
trace event in the Events area of the test client. Information about
setting the preference is found in the topic "Controlling split-editor
mode for fine-grained trace".

## Results