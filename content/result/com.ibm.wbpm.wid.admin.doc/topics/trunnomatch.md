<!-- image -->

# Running test suites with unmatched emulator definition steps

## About this task

## Procedure

1. In the Business Integration view, right-click a test
suite that contains two or more emulator definition steps for the
same component and then select Run Test. The
test client opens.
2. In the test client, click the Continue icon  to invoke the operation and run the test.
(If the Deployment Location wizard opens, select the server where
you want to deploy the test artifacts and then click Finish.)
3. If none of the emulator definitions match for the same
component, reference or human task and the test fails, select the Test
Variation event in the Events area and view the results
of the test in the Detailed Properties area. A verdict of FAILED is
displayed and the exception trace displays an exception message.
4. In the Events area, select the Emulate event
and view the test results in the Detailed Properties area. (If you
need additional information about a property, position your cursor
in the property and press F1 to open the context-sensitive
help information.)
5. Close the test client without saving the test trace.