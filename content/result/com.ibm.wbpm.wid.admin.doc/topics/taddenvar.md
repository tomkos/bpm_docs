<!-- image -->

# Referencing environment variables in the test suite editor

## Procedure

1. In the test suite editor, click the Test Data
Table tab. The Test Data Table view opens.
2. In the Test Data Table view, click the Default tab
(or the tab of another test variation) to display the test data table.
3. In the Name column of the test data
table, locate the name of the field for which you want to reference
an environment variable. The field must have a simple data type, such
as string or integer. The field must also have a literal format and
cannot be specified in a Java expression.
4. In the row that contains the field name, type the environment
variable that you want to reference in either the Set column
or the Expected column and then press Enter.
By default, the format is literal. Alternatively, you can right-click
the root (top level) of the environment variable in the Name column
and select Set Format > XML, then double-click
the XML string in the Set or Expected column
to open the XML editor and type the environment variable. Regardless
of which approach you use, you can reference one of the following
three types of environment variables:

Environment variable type
Description

Proprietary
These environment variables are referenced in the test suite
editor or the test client, but they are generally defined in the test
client, Component Test Explorer, or by using command-line invocation.
The syntax for these environment variables is:${proprietary\_variable\_name}
For
example:
${MY\_VAR}

WebSphere Application Server
These environment variables are defined in the server Administrative
Console and referenced in either the test data table or the test client.
The syntax for these environment variables is:$WAS{WAS\_variable\_name}
For
example:
$WAS{INSTALL\_ROOT}

JVM property
These environment variables are defined in the server Administrative
Console and referenced in either the test data table or the test client.
The syntax for these environment variables is:$JVM{JVM\_property\_name}
For
example:
$JVM{file.encoding}

If you want, you can concatenate different types of environment
variables using a forward slash (/) character. For example:$WAS{INSTALL\_ROOT}/${MY\_LOG\_DIR\_NAME}
5. If you are referencing an environment variable that will
not have a value defined at run time, you can specify a default value
for the environment variable in the test data table. For example:
${MY\_VAR, customer}
In the example, the default value customer is
specified. If the environment variable is not defined at run time,
it will be substituted by the string customer.
Note: If
your test data table contains environment variables and you plan to
export the data table to an XML file, you need to exercise caution.
Environment variables that are referenced in the test data table are
generally defined at run time rather than in the data table, which
means that they will be exported from the data table to the XML file
"as is" with only a name and without any defined value. However, if
you have specified a default value for the environment variable in
the data table, it will be exported to the XML file with the defined
value.
6. Save the test suite.

## What to do next

- Defining environment variable values in the test client
- Running test projects, suites, and cases in the Component Test
Explorer
- Defining environment variables for command-line invocation