<!-- image -->

# Managing test data

## About this task

- Adding variables

In the Test Data Table view of the test suite editor, you can add new variables to the test data in the test data table.
- Specifying variable values

In the test data table of the test suite editor, variables are automatically set to their default values. However, you can specify a wide variety of alternate values for the variables.
- Specifying variable values for exports

If an export has a binding type that is supported by the test suite editor, the test data table will be populated with values that are based on the binding type and you can invoke and test the export directly through its binding in the integration test client. Currently, the test suite editor and test client support web services binding types and SCA binding types. If you have an export that does not have a supported binding type or does not have any binding at all, you can still test the export in the test client. However, the test client will invoke the component that is wired to the export rather than invoking the export directly through a binding.
- Specifying values for web services exports with SOAP messages

In the test suite editor, you can edit test cases to send a sample SOAP message without attachments as input to a web services export and then compare the results to an expected sample SOAP message that does not contain attachments.
- Referencing environment variables in the test suite editor

In the Test Data Table view of the test suite editor, you can reference environment variables in the test data table.
- Java expressions

In the test data table of the test suite editor, you can set the format of variable values to Java expressions. The type of the expressions must be compatible with the type of the variables. The Java context is the variables themselves and any imports defined in the Imports page of the Test Data Table view.