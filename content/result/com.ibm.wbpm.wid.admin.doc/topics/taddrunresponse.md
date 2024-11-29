<!-- image -->

# Adding and running Verify Event steps for monitor responses

## Before you begin

## About this task

## Procedure

1 Add a Verify Event step for a monitor response by completingthe following steps:
    1. In the Business Integration view, expand your component
test project and expand the Test Suites folder.
    2. Right-click your test suite and select Open.
The test suite opens in the test suite editor.
    3. Click the Test Cases tab. The
Test Cases page opens.
    4. In the upper left corner of the Test Cases area, click
the down arrow beside the Add Test Case icon .
    5. From the menu list, select Verify Event Step
> Response. The Add Verify Response Event wizard opens.
    6. In the list box, expand the module, wire, and interface
and then select the operation that you want to use to verify the response
data that is returned from the target component of the wire.
    7. If you want to have variables automatically created
for the new Verify Response event, ensure that the Create
the variables for the new Verify Response events check
box is selected. (If the check box is not selected, you will need
to manually create the variables yourself in the test suite editor.)
    8. Click Finish. A new Verify
event: Response step is displayed under the associated
invocation in the Test Cases area.
2 Specify properties for the new Verify Event step by completingthe following steps:

1. In the Test Cases area, ensure that the new Verify
event: Response step is selected.
2. In the Detailed Properties area,
ensure that the Verify in invocation field
displays the invocation that you want to use for the Verify event:
Response step. (If you need additional information about this property
or any other property, position your cursor in the property and press F1 to
open the context-sensitive help information.)
3. In the Detailed Properties area,
ensure that the default selections for the remaining properties are
correct.
4. In the Verify Response section,
ensure that one or more output variables are specified. You can accept
the default values for the variables or you can specify new values
in the test data table. (If you chose to clear the Create
the variables for the new Verify Response events check
box in the Add Verify Response Event wizard, then you will need to
use the test data table to manually add one or more variables for
the Verify event: Response step. Information
about adding variables is found in the topic "Adding variables.")
5. In the test suite editor, press Ctrl-S to
save your changes.
3 Use the new Verify event: Response step to run a test bycompleting the following steps:

1. In the Business Integration view, right-click the test
suite and select Run Test. The test client
opens.
2. In the test client, click the Continue icon  to invoke the operation and run the test.
3. If the Deployment Location wizard opens, select the
server where you want to deploy the test artifacts and then click Finish.
4. When the test has completed, select the Verify
event: Response event in the Events area and view the
test results in the Detailed Properties area. (If you need additional
information about a property, position your cursor in the property
and press F1 to open the context-sensitive
help information.)