<!-- image -->

# Adding and running emulator definition steps for references

## About this task

To
add and run an emulator definition step for a reference:

## Procedure

1 Add an emulator definition step for a reference by completingthe following steps:
    1. In the Business Integration view, expand your component
test project and expand the Test Suites folder.
    2. Right-click your test suite and select Open.
The test suite opens in the test suite editor.
    3. Click the Test Cases tab. The
Test Cases page opens.
    4. In the upper left corner of the Test Cases area, click
the down arrow beside the Add Test Case icon .
    5. From the menu list, select Emulator Definition
Step > Reference. The Add Reference Emulator Definition
wizard opens.
    6. In the list box, expand the module, component, reference,
and interface and then select the operation for which you want to
emulate the response data that is returned from the reference.
    7. If you want to have variables automatically created
for the new emulator definition step, ensure that the Create
variables for the new emulator definitions check box is
selected. One variable will be automatically created in the test data
table for each operation parameter. (If the check box is not selected,
you will need to manually create the variables yourself in the test
suite editor.)
    8. Click Finish. A new Define
reference emulator step is displayed under the associated
invocation in the Test Cases area.
2 Specify properties for the new emulator definition stepby completing the following steps:

1. In the Test Cases area, ensure that the new Define
reference emulator step is selected.
2. Move the reference emulator definition step to a position
over the invocation step by clicking the Move Up icon . (Emulator definition steps
must be placed in a position that precedes the associated invocation
step.)
3. In the Detailed Properties area,
ensure that the fields display the correct module, component, reference,
interface, and operation for the selected emulator definition step.
(If you need additional information about these properties or any
other properties, position your cursor in a property and press F1 to
open the context-sensitive help information.)
4. Click the Output tab and then
select either Return response or Throw
exception, depending on the parameter type that you want
to return. If you choose Return response, select
a variable for the output parameter and then click the link on the
parameter name to open the test data table and specify a variable
value in the Set column. If you choose Throw
exception, select the exception that you want to throw
and then create a variable for it.
5. If you want to specify a variable value for the input
parameter, click the Input tab, then select
a variable for the input parameter and click the link on the parameter
name to open the test data table and specify a variable value in the Expected column.
The emulator rule will only apply if the actual input data values
match the values specified in the expected inputs of the emulator
definition. By default, the expected inputs are not set, which means
that the emulator rule is always applied.
6. Using the previous steps, create another new emulator
definition for the same reference and then specify some values for
the variables. This creates a series of emulator definition steps
for the same target.
7. In the test suite editor, press Ctrl-S to
save your changes.
3 Use the new emulator definition step to run a test by completingthe following steps:

1. In the Business Integration view, right-click the test
suite and select Run Test. The test client
opens.
2. In the test client, click the Continue icon  to invoke the operation and run the test.
(If the Deployment Location wizard opens, select the server where
you want to deploy the test artifacts and then click Finish.)
ADefine Reference Emulator event is displayed
in the Events area.
3. In the Events area, select the Emulate event
and view the test results in the Detailed Properties area. It shows
that the reference emulator definition has been applied. (If you need
additional information about a property, position your cursor in the
property and press F1 to open the context-sensitive
help information.)
4. Close the test client without saving the test trace.