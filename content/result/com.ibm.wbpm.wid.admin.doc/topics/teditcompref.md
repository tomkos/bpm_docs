<!-- image -->

# Editing emulator definition steps for components and references

## About this task

To
edit emulator definition steps for components and references:

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
    2. In the Component field, select
the component that you want to use for the emulator definition step.
    3. If you selected a Define reference emulator step
in the Test Cases area, select the reference that you want to use
for the emulator definition step in the Reference field.
    4. In the Interface field, select
the interface that you want to use for the emulator definition step.
    5. In the Operation field, select
the operation that you want to use for the emulator definition step.
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