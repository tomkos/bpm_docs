<!-- image -->

# Testing exports

## Before you begin

Testing an export is similar in many respects to testing
an interface operation. If you have not worked with the test client
before, you should read "Testing interface operations" and its subtopics
before testing an export.

## About this task

To test
an export:

## Procedure

1. Open the integration test client, as described in the topic
"Opening the integration test client."
2. In the Configuration field, ensure
that the correct test configuration is selected. A default test configuration
is automatically created whenever you open the integration test client.
If you did not open the integration test client by loading a test
configuration that you saved earlier, the default test configuration
will already be selected in the Configuration field.
3. In the Module field, ensure that
the correct module is selected.
4. In the Component field, select the
export that you want to test. The test client will list all exports
found in the selected module or in any libraries or projects that
are referenced by the module. If the test client supports the binding
type used by the export, the Binding type is supported check box is selected.
5. In the Interface and Operation fields, ensure that the correct interface and
operation are selected.
6. In the value editor, specify values for the export. 
Note:  When you invoke a web services binding export in the
test client, the value editor is populated with a serviceAddress variable. This enables you to change the service address used to
invoke the web service and allows you to route the invocation to a
different monitoring tool, such as the TCP/IP Monitor.Also, when
you invoke a web services binding export in the test client, the value
editor is populated with the SOAP Security header.
This enables you to specify your web service security credentials
in the SOAP message.

Information about using the value
editor and data pool editor to specify values for exports is found
in the test client topic "Value and data pool editors."
7. Click the Continue icon . If the Deployment Location wizard opens,
select the server where you want to deploy your selected module, as
described in the test client topic "Deploying modules." The value
editor returns the results of your test.