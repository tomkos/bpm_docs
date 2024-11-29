<!-- image -->

# Editing emulator definition steps for human tasks

## About this task

To
edit emulator definition steps for human tasks:

## Procedure

1. In the Business Integration view, expand your component
test project and expand the Test Suites folder.
2. Right-click your test suite and select Open.
The test suite opens in the test suite editor.
3. Click the Test Cases tab. The Test
Cases page opens.
4. In the Test Cases area, select a Define component
emulator step or a Define reference emulator step.
5 In the Detailed Properties area,complete the following steps:
    1. In the Module field, select the
module that you want to use for the emulator definition step. (If
you need additional information about this property or any other property,
position your cursor in the property and press F1 to
open the context-sensitive help information.)
    2. If you selected a Define human task emulator step
in the Test Cases area for an inline human task, select the
business process that you want to use for the emulator definition
step in the Business process field.
    3. If you selected a Define human task emulator step
in the Test Cases area for a stand-alone human task, select
the component that you want to use for the emulator definition step
in the Component field.
    4. In the Claim radio button group,
select Immediately to claim the human task
right away or select After (ms) to claim the
human task after a number of milliseconds that you specify in the
associated field.
    5. In the Potential owner field group, specify the user ID and password
that you want to use to claim the human task. If a user ID and password are not specified, the user
ID and password for the potential owner will default to the user ID and password that are used to
log in to the server in the test client.
    6. Click the Output tab and then
select either Return response or Throw
exception, depending on the parameter type that you want
to return. If you choose Return response, select
a variable for the output parameter and then click the link on the
parameter name to open the test data table and specify a variable
value in the Set column. If you choose Throw
exception, select the exception that you want to throw.
    7. If you want to specify a variable value for the input
parameter, click the Input tab, then select
a variable for the input parameter and click the link on the parameter
name to open the test data table and specify a variable value in the Expected column.
The emulator rule will only apply if the actual input data values
match the values specified in the expected inputs of the emulator
definition. By default, the expected inputs are not set, which means
that the emulator rule is always applied.
6. In the test suite editor, press Ctrl-S to
save your changes.