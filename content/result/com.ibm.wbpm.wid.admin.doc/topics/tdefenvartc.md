<!-- image -->

# Defining environment variable values in the test client

## Procedure

1 If you are performing unit (ad hoc) testing in the testclient and you have referenced some proprietary environment variablesin the value editor that you now want to define, complete the followingsteps:
    1. In the Events page of the test client, ensure that the Invoke event
is selected in the Events area.
    2. In the Detailed Properties section, click the test
configuration link. The Configurations page opens.
    3. Beside the Environment variables table,
click the Add button. The Add Environment Variable
window opens.
    4. In the Name field, type the name
of an environment variable that you referenced in the value editor.
    5. In the Value field, type in a
value for the environment variable. This value will override any default
value that may have been defined in the value editor. If you do not
specify a value in the Value field, the value
will default to an empty string (" ").
    6. Click OK. The environment variable
name and value are displayed in the Environment variables table.
Note:  If you do not choose to define an environment variable
in the Environment variables table, the test
will use any default value that has been specified for the environment
variable in the value editor. If no default value was specified in
the value editor, the environment variable will be used "as is" for
the value. For example, the environment variable ${MYVAR} will have
a value of ${MYVAR}.The Environment variables table
always displays the names and the current values of environment
variables. The test trace does not record any environment variable
values that are used during a test run.
    7. Repeat the previous four steps for each environment
variable that you have referenced in the value editor.
    8. Click the Events tab. The Events
page opens.
    9. Click the Continue icon to run
the test.
2 If you want to perform component testing in the test clientand you have referenced some proprietary environment variables inthe test suite editor that you now want to define, complete the followingsteps:

1. In the Business Integration view, right-click your test
suite and select Run Test Cases. The test client
opens.
2. In the Events page of the test client, ensure that the Run
Test Cases event is selected in the Events area.
3. In the Detailed Properties section, click the test
configuration link. The Configurations page opens.
4. Beside the Environment variables table,
click the Add button. The Add Environment Variable
window opens.
5. In the Add Environment Variable window, select the
check boxes beside the proprietary environment variables that are
referenced in the test suite editor and then click OK.
The names of the environment variables are displayed in the Name column
of the Environment variables table and they
are all assigned an initial value of empty string (" ").
6. In the Value column of the Environment
variables table, type in a value for each environment
variable that you do not want to have assigned a value of empty string
during the test. Note: If you defined a default value for
an environment variable in the test suite editor and you want to use
the default value in the test, you must ensure that the environment
variable does not appear in the Environment variables table.
If it appears in the table, you can remove it by clicking Remove.
7. Click the Events tab. The Events
page opens.
8. Click the Continue icon to run
the test.

## Example

- If a value is specified for an environment variable that has been
added to the Environment variables table, this
is the value that will be used for the test.
- If a value is not specified for an environment variable that has
been added to the Environment variables table,
an empty string (" ") value will be used for the test.
- If an environment variable has not been added to the Environment
variables table but a default value has been specified
for the referenced environment variable in the value editor or test
suite editor, the default value will be used for the test.
- If an environment variable has not been added to the Environment
variables table and no default value has been specified
for the referenced environment variable in the value editor or test
suite editor, the environment variable will be used "as is" for the
value in the test. For example, the environment variable ${VAR} will
have a value of ${VAR}.