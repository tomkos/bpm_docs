<!-- image -->

# Editing Verify Event steps for fine-grained traces

## About this task

## Procedure

1. In the Business Integration view, expand your component
test project and expand the Test Suites folder.
2. Right-click your test suite and select Open.
The test suite opens in the test suite editor.
3. Click the Test Cases tab. The Test
Cases page opens.
4. In the Test Cases area, select a Verify event:
Fine-Grained Trace step.
5 In the Detailed Properties area,complete the following steps:
    1. In the Business process, Business
state machine, or Mediation flow field,
select the business process, business state machine, or mediation
flow that you want to use for the Verify event: Fine-Grained Trace
step. (If you need additional information about these properties or
any other properties, position your cursor in a property and press F1 to
open the context-sensitive help information.)
    2. In the Activity, State,
or Primitive field, select the business process
activity, business state machine state, or mediation primitive that
you want to use for the Verify event: Fine-Grained Trace step.
    3. In the Wait maximum list, specify
a wait time (in milliseconds) before the verification happens. This
is useful for verifying events for asynchronous calls because these
call do not happen immediately.
    4. In the Event occurrence field,
specify whether the event being verified ever occurs in the test case.
The event position text box allows you to specify the position of
the event to distinguish between identical events. For example, there
may be two request events reported for the same wire and the event
position is used to distinguish which event should be verified.
    5. In the After event field, specify
whether the event being verified in this step must occur after another
event seen in the test client trace. The drop-down list box displays
a list of Verify Event steps that have already been created in the
test case.
    6. In the Variables section, create
a new variable for each parameter. (Information about adding variables
is found in the topic "Adding variables.")
6. In the test suite editor, press Ctrl-S to
save your changes.