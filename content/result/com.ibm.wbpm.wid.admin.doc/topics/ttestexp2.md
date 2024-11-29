<!-- image -->

# Specifying variable values for exports

## About this task

To test
an export:

## Procedure

1. Open the test suite editor, as described in the topic "Opening
the test suite editor."
2. In the Test Cases area, select an
invocation for your export.
3. In the Module field, ensure that
the correct module is selected.
4. In the Component field, ensure that
the export is selected that you want to test. The test suite editor
will list all exports found in the selected module or in any libraries
or projects that are referenced by the module. If the test suite editor
supports the binding type used by the export, the Binding
type is supported check box is selected.
5. In the Interface and Operation fields, ensure that the correct interface and
operation are selected.
6. In the Request, Response, and Exception parameter sections, select
the variables that you want to use for the request, response, and
exception parameters (as described in the topic "Specifying request,
response, and exception variables"). The following figure shows the
Request parameters section and the variables that have been selected
for the serviceAddress and request parameters:
7. In the test data table, specify values for the variables
that you selected in the Request, Response, and Exception parameter
sections. Alternatively, you can accept the default values that already
exist for the variables. Note:  When you select a web services
binding export in the test suite editor, the test data table is populated
with a serviceAddress variable. This enables
you to change the service address used to invoke the web service and
allows you to route the invocation to a different monitoring tool,
such as the TCP/IP Monitor.Also, when you select a web services
binding export in the test suite editor, the test data table is populated
with the SOAP Security header. This enables
you to specify your web service security credentials in the SOAP message.

Information about using the test data table is found in
the topic "Test Data Table view."